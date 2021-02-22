#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List


_WELL_KNOWN_FILE = Path("tests", "pyright_test.py")
_PYRIGHT_COMMAND = ["npx", "-p", "pyright@1.1.113", "pyright"]


def main() -> None:
    assert_npm_is_installed()
    files = find_stubs()
    ret = run_pyright(files)
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


def find_stubs() -> List[str]:
    files: List[str] = []
    for top in ["stdlib", "stubs"]:
        for dirpath, dirnames, filenames in os.walk(top):
            for fn in filenames:
                if fn.endswith(".pyi"):
                    files.append(os.path.join(dirpath, fn))
            try:
                dirnames.remove("@python2")
            except ValueError:
                pass
    return files


def run_pyright(files: Iterable[str]) -> int:
    full_args = _PYRIGHT_COMMAND + list(files)
    return subprocess.run(full_args).returncode


if __name__ == "__main__":
    main()
