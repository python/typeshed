#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys
from pathlib import Path

_WELL_KNOWN_FILE = Path("tests", "pyright_test.py")


def main() -> None:
    if not _WELL_KNOWN_FILE.exists():
        print("pyright_test.py must be run from the typeshed root directory", file=sys.stderr)
        sys.exit(1)

    # subprocess.run on Windows does not look in PATH.
    npx = shutil.which("npx")

    if npx is None:
        print("error finding npx; is Node.js installed?", file=sys.stderr)
        sys.exit(1)

    try:
        subprocess.run([npx, "--version"])
    except OSError:
        print("error running npx; is Node.js installed?", file=sys.stderr)
        sys.exit(1)

    with open("tests/PYRIGHT_VERSION.txt", "r") as file:
        PYRIGHT_VERSION = file.readline()

    os.environ["PYRIGHT_PYTHON_FORCE_VERSION"] = PYRIGHT_VERSION
    command = [npx, f"pyright@{PYRIGHT_VERSION}"] + sys.argv[1:]
    print("Running:", " ".join(command))

    ret = subprocess.run(command).returncode
    sys.exit(ret)


if __name__ == "__main__":
    main()
