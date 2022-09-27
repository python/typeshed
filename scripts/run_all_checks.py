import json
import re
import subprocess
import sys

# Popular Flake8 extensions not used in Typeshed that cause errors
_extend_ignore = "CCE,N8,Q"

_STRICTER_CONFIG_FILE = "pyrightconfig.stricter.json"


def _parse_jsonc(json_text: str) -> str:
    # strip comments from the file
    lines = [line for line in text.split('\n') if not line.strip().startswith('//')]
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
        print("Missing path argument in format <folder>/<stub>")
        sys.exit(1)
    path_tokens = Path(path).parts
    assert len(path_tokens) == 2, "Path argument should be in format <folder>/<stub>"
    folder, stub = path_tokens
    assert folder in {"stdlib", "stubs"}, "Only the 'stdlib' and 'stubs' folders are supported"

    subprocess.run(["python3", "-m", "pycln", path, "--all"])
    subprocess.run(["python3", "-m", "isort", path])
    subprocess.run(["python3", "-m", "black", path])
    subprocess.run(["python3", "-m", "flake8", path, "--extend-ignore", _extend_ignore])

    subprocess.run(["python3", "tests/check_consistent.py"])
    subprocess.run(["python3", "tests/check_new_syntax.py"])

    subprocess.run(["python3", "tests/pyright_test.py", path] + _get_strict_params(path))

    mypy_result = subprocess.run(["python3", "tests/mypy_test.py", path])

    # TODO: Run in WSL if available
    if sys.platform != "win32":
        subprocess.run(["python3", "tests/pytype_test.py", path])

    if folder == "stdlib":
        subprocess.run(["python3", "tests/regr_test.py", "stdlib"])
    else:
        subprocess.run(["python3", "tests/regr_test.py", stub])

    # If mypy failed, this will fail without any helpful error
    if mypy_result.returncode == 0:
        if folder == "stdlib":
            subprocess.run(["python3", "tests/stubtest_stdlib.py", stub])
        else:
            subprocess.run(["python3", "tests/stubtest_third_party.py", stub])
