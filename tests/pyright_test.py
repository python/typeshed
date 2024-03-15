#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path

from utils import parse_requirements, print_command

_WELL_KNOWN_FILE = Path("tests", "pyright_test.py")


def main() -> None:
    if not _WELL_KNOWN_FILE.exists():
        print("pyright_test.py must be run from the typeshed root directory", file=sys.stderr)
        sys.exit(1)

    req = parse_requirements()["pyright"]
    assert len(req.specifier) == 1
    spec = str(req.specifier)
    assert spec.startswith("=="), f"pyright version must be pinned in requirements-tests.txt: {req}"
    os.environ["PYRIGHT_PYTHON_FORCE_VERSION"] = spec[2:]

    print_command("pyright --version")
    subprocess.run(["pyright", "--version"], check=True)
    print()

    command = ["pyright"] + sys.argv[1:]
    print_command(command)
    ret = subprocess.run(command).returncode
    sys.exit(ret)


if __name__ == "__main__":
    main()
