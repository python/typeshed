#!/usr/bin/env python3
from __future__ import annotations

import json
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


def _parse_jsonc(json_text: str) -> str:
    # strip comments from the file
    lines = [line for line in json_text.split("\n") if not line.strip().startswith("//")]
    # strip trailing commas from the file
    valid_json = re.sub(r",(\s*?[\}\]])", r"\1", "\n".join(lines))
    return valid_json


def _get_strict_params(stub_path: str) -> list[str]:
    with open(_STRICTER_CONFIG_FILE) as file:
        data = json.loads(_parse_jsonc(file.read()))
    if stub_path in data["exclude"]:
        return []
    return ["-p", _STRICTER_CONFIG_FILE]


if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        print("Missing path argument in format <folder>/<stub>", file=sys.stderr)
        sys.exit(1)
    path_tokens = Path(path).parts
    assert len(path_tokens) == 2, "Path argument should be in format <folder>/<stub>"
    folder, stub = path_tokens
    assert folder in {"stdlib", "stubs"}, "Only the 'stdlib' and 'stubs' folders are supported"
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

    print("\nRunning Pyright...")
    pyright_result = subprocess.run(
        [sys.executable, "tests/pyright_test.py", path] + _get_strict_params(path), stderr=subprocess.PIPE, text=True
    )
    print(pyright_result.stderr)
    if re.match(r"error (runn|find)ing npx", pyright_result.stderr):
        pyright_returncode = 0
        pyright_skipped = True
    else:
        pyright_returncode = pyright_result.returncode
        pyright_skipped = False

    print("\nRunning mypy...")
    mypy_result = subprocess.run([sys.executable, "tests/mypy_test.py", path])
    # If mypy failed, stubtest will fail without any helpful error
    if mypy_result.returncode == 0:
        print("\nRunning stubtest...")
        if folder == "stdlib":
            stubtest_result = subprocess.run([sys.executable, "tests/stubtest_stdlib.py", stub])
        else:
            stubtest_result = subprocess.run([sys.executable, "tests/stubtest_third_party.py", stub])
    else:
        print("Skipping stubtest since mypy failed.")

    if sys.platform == "win32":
        print("Skipping pytype on Windows. You can run the test with WSL.")
    else:
        print("\nRunning pytype...")
        pytype_result = subprocess.run([sys.executable, "tests/pytype_test.py", path])

    print("\nRunning regression tests...")
    regr_test_result = subprocess.run(
        [sys.executable, "tests/regr_test.py", "stdlib" if folder == "stdlib" else stub], stderr=subprocess.PIPE, text=True
    )
    # No test means they all ran successfully (0 out of 0). Not all 3rd-party stubs have regression tests.
    if "No test cases found" in regr_test_result.stderr:
        regr_test_returncode = 0
        print(f"No test cases found for '{stub}'!")
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
        print("\nOne or more tests failed. See above for details.")
    else:
        print("\nAll tests passed!")
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
