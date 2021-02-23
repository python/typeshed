#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


_WELL_KNOWN_FILE = Path("tests", "pyright_test.py")
_PYRIGHT_COMMAND = ["npx", "-p", "pyright@1.1.114", "pyright"]


def main() -> None:
    assert_npm_is_installed()
    ret = subprocess.run(_PYRIGHT_COMMAND).returncode
    sys.exit(ret)


def assert_npm_is_installed() -> None:
    if not _WELL_KNOWN_FILE.exists():
        print("pyright_test.py must be run from the typeshed root directory", file=sys.stderr)
        sys.exit(1)
    try:
        subprocess.run(["npx", "--version"])
    except OSError:
        print("error running npx; is Node.js installed?", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
