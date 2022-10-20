#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

try:
    from termcolor import colored
except ImportError:

    def colored(text: str, color: str = "") -> str:  # type: ignore[misc]
        return text


_STRICTER_CONFIG_FILE = "pyrightconfig.stricter.json"
_SUCCESS = colored("Success", "green")
_SKIPPED = colored("Skipped", "yellow")
_FAILED = colored("Failed", "red")
# We're using the oldest supported version because it's the most likely to produce errors
# due to unsupported syntax, feature, or bug in a tool.
_PYTHON_VERSION = "3.7"


def _parse_jsonc(json_text: str) -> str:
    # strip comments from the file
    lines = [line for line in json_text.split("\n") if not line.strip().startswith("//")]
    # strip trailing commas from the file
    valid_json = re.sub(r",(\s*?[\}\]])", r"\1", "\n".join(lines))
    return valid_json


def _get_strict_params(stub_path: str) -> list[str]:
    with open(_STRICTER_CONFIG_FILE, encoding="UTF-8") as file:
        data = json.loads(_parse_jsonc(file.read()))
    lower_stub_path = stub_path.lower()
    if any(lower_stub_path == stub.lower() for stub in data["exclude"]):
        return []
    return ["-p", _STRICTER_CONFIG_FILE]


def main() -> None:
    try:
        path = sys.argv[1]
    except IndexError:
        print("Missing path argument in format <folder>/<stub>", file=sys.stderr)
        sys.exit(1)
    assert os.path.exists(path), rf"Path {path} does not exist."
    path_tokens = Path(path).parts
    assert len(path_tokens) == 2, "Path argument should be in format <folder>/<stub>."
    folder, stub = path_tokens
    assert folder in {"stdlib", "stubs"}, "Only the 'stdlib' and 'stubs' folders are supported."
    stubtest_result: subprocess.CompletedProcess[bytes] | None = None
    pytype_result: subprocess.CompletedProcess[bytes] | None = None

    # Run formatters first. Order matters.
    print("\nRunning pycln...")
    subprocess.run([sys.executable, "-m", "pycln", path, "--all"])
    print("\nRunning isort...")
    subprocess.run([sys.executable, "-m", "isort", path])
    print("\nRunning Black...")
    black_result = subprocess.run([sys.executable, "-m", "black", path])
    if black_result.returncode == 123:
        print("Could not run tests due to an internal error with Black. See above for details.", file=sys.stderr)
        sys.exit(black_result.returncode)

    print("\nRunning Flake8...")
    flake8_result = subprocess.run([sys.executable, "-m", "flake8", path])

    print("\nRunning check_consistent.py...")
    check_consistent_result = subprocess.run([sys.executable, "tests/check_consistent.py"])
    print("\nRunning check_new_syntax.py...")
    check_new_syntax_result = subprocess.run([sys.executable, "tests/check_new_syntax.py"])

    print(f"\nRunning Pyright on Python {_PYTHON_VERSION}...")
    pyright_result = subprocess.run(
        [sys.executable, "tests/pyright_test.py", path, "--pythonversion", _PYTHON_VERSION] + _get_strict_params(path),
        stderr=subprocess.PIPE,
        text=True,
    )
    if re.match(r"error (runn|find)ing npx", pyright_result.stderr):
        print(colored("\nSkipping Pyright tests: npx is not installed or can't be run!", "yellow"))
        pyright_returncode = 0
        pyright_skipped = True
    else:
        print(pyright_result.stderr)
        pyright_returncode = pyright_result.returncode
        pyright_skipped = False

    print(f"\nRunning mypy for Python {_PYTHON_VERSION}...")
    mypy_result = subprocess.run([sys.executable, "tests/mypy_test.py", path, "--python-version", _PYTHON_VERSION])
    # If mypy failed, stubtest will fail without any helpful error
    if mypy_result.returncode == 0:
        if folder == "stdlib":
            print("\nRunning stubtest...")
            stubtest_result = subprocess.run([sys.executable, "tests/stubtest_stdlib.py", stub])
        else:
            run_stubtest_query = (
                f"\nRun stubtest for {stub!r} (Y/N)?\n\n"
                "NOTE: Running third-party stubtest involves downloading and executing arbitrary code from PyPI.\n"
                f"Only run stubtest if you trust the {stub!r} package.\n"
            )
            run_stubtest_answer = input(colored(run_stubtest_query, "yellow")).lower()
            while run_stubtest_answer not in {"yes", "no", "y", "n"}:
                run_stubtest_answer = input(colored("Invalid response; please try again.\n", "red")).lower()
            if run_stubtest_answer in {"yes", "y"}:
                print("\nRunning stubtest.")
                stubtest_result = subprocess.run([sys.executable, "tests/stubtest_third_party.py", stub])
            else:
                print(colored(f"\nSkipping stubtest for {stub!r}...", "yellow"))
    else:
        print(colored("\nSkipping stubtest since mypy failed.", "yellow"))

    if sys.platform == "win32":
        print(colored("\nSkipping pytype on Windows. You can run the test with WSL.", "yellow"))
    else:
        print("\nRunning pytype...")
        pytype_result = subprocess.run([sys.executable, "tests/pytype_test.py", path])

    print(f"\nRunning regression tests for Python {_PYTHON_VERSION}...")
    regr_test_result = subprocess.run(
        [sys.executable, "tests/regr_test.py", "stdlib" if folder == "stdlib" else stub, "--python-version", _PYTHON_VERSION],
        stderr=subprocess.PIPE,
        text=True,
    )
    # No test means they all ran successfully (0 out of 0). Not all 3rd-party stubs have regression tests.
    if "No test cases found" in regr_test_result.stderr:
        regr_test_returncode = 0
        print(colored(f"\nNo test cases found for {stub!r}!", "green"))
    else:
        regr_test_returncode = regr_test_result.returncode
        print(regr_test_result.stderr)

    any_failure = any(
        [
            flake8_result.returncode,
            check_consistent_result.returncode,
            check_new_syntax_result.returncode,
            pyright_returncode,
            mypy_result.returncode,
            getattr(stubtest_result, "returncode", 0),
            getattr(pytype_result, "returncode", 0),
            regr_test_returncode,
        ]
    )

    if any_failure:
        print(colored("\n\n--- TEST SUMMARY: One or more tests failed. See above for details. ---\n", "red"))
    else:
        print(colored("\n\n--- TEST SUMMARY: All tests passed! ---\n", "green"))
    print("Flake8:", _SUCCESS if flake8_result.returncode == 0 else _FAILED)
    print("Check consistent:", _SUCCESS if check_consistent_result.returncode == 0 else _FAILED)
    print("Check new syntax:", _SUCCESS if check_new_syntax_result.returncode == 0 else _FAILED)
    if pyright_skipped:
        print("Pyright:", _SKIPPED)
    else:
        print("Pyright:", _SUCCESS if pyright_returncode == 0 else _FAILED)
    print("mypy:", _SUCCESS if mypy_result.returncode == 0 else _FAILED)
    if stubtest_result is None:
        print("stubtest:", _SKIPPED)
    else:
        print("stubtest:", _SUCCESS if stubtest_result.returncode == 0 else _FAILED)
    if pytype_result is None:
        print("pytype:", _SKIPPED)
    else:
        print("pytype:", _SUCCESS if pytype_result.returncode == 0 else _FAILED)
    print("Regression test:", _SUCCESS if regr_test_returncode == 0 else _FAILED)

    sys.exit(int(any_failure))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\nTests aborted due to KeyboardInterrupt!\n", "red"))
        sys.exit(1)
