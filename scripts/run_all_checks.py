import json
import re
import subprocess
import sys
from pathlib import Path

try:
    from termcolor import colored
except ImportError:

    def colored(text: str, color: str = "") -> str:
        return text


# Popular Flake8 extensions not used in Typeshed that cause errors
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
    stubtest_result = None
    pytype_result = None

    # Run formatters first. Order matters.
    subprocess.run(["python3", "-m", "pycln", path, "--all"])
    subprocess.run(["python3", "-m", "isort", path])
    subprocess.run(["python3", "-m", "black", path])

    flake8_result = subprocess.run(["python3", "-m", "flake8", path])

    check_consistent_result = subprocess.run(["python3", "tests/check_consistent.py"])
    check_new_syntax_result = subprocess.run(["python3", "tests/check_new_syntax.py"])

    pyright_result = subprocess.run(["python3", "tests/pyright_test.py", path] + _get_strict_params(path), stderr=subprocess.PIPE)
    print(pyright_result.stderr.decode())
    if b"error running npx" in pyright_result.stderr:
        pyright_returncode = 0
        pyright_skipped = True
    else:
        pyright_returncode = pyright_result.returncode
        pyright_skipped = False

    mypy_result = subprocess.run(["python3", "tests/mypy_test.py", path])
    # If mypy failed, stubtest will fail without any helpful error
    if mypy_result.returncode == 0:
        if folder == "stdlib":
            stubtest_result = subprocess.run(["python3", "tests/stubtest_stdlib.py", stub])
        else:
            stubtest_result = subprocess.run(["python3", "tests/stubtest_third_party.py", stub])

    # TODO: Run in WSL if available
    if sys.platform != "win32":
        pytype_result = subprocess.run(["python3", "tests/pytype_test.py", path])

    if folder == "stdlib":
        regr_test_result = subprocess.run(["python3", "tests/regr_test.py", "stdlib"], stderr=subprocess.PIPE)
    else:
        regr_test_result = subprocess.run(["python3", "tests/regr_test.py", stub], stderr=subprocess.PIPE)
    print(regr_test_result.stderr.decode())
    # No test means they all ran successfully (0 out of 0). Very few 3rd part stub have regression tests.
    regr_test_returncode = 0 if b"No test cases found" in regr_test_result.stderr else regr_test_result.returncode

    any_failure = (
        flake8_result.returncode
        + check_consistent_result.returncode
        + check_new_syntax_result.returncode
        + pyright_returncode
        + mypy_result.returncode
        + (stubtest_result.returncode if stubtest_result else 0)
        + (pytype_result.returncode if pytype_result else 0)
        + regr_test_returncode
        > 0
    )

    if any_failure:
        print("One or more tests failed. See above for details.")
    else:
        print("All tests passed!")
    print("flake8:", _SUCCESS if flake8_result.returncode == 0 else _FAILED)
    print("Check consistent:", _SUCCESS if check_consistent_result.returncode == 0 else _FAILED)
    print("Check new syntax:", _SUCCESS if check_new_syntax_result.returncode == 0 else _FAILED)
    if pyright_skipped:
        print("pyright:", _SKIPPED)
    else:
        print("pyright:", _SUCCESS if pyright_returncode == 0 else _FAILED)
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
