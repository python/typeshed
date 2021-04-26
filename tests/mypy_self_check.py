#!/usr/bin/env python3
"""Script to run mypy against its own code base."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tempdir:
        dirpath = Path(tempdir)
        subprocess.run(
            ["git", "clone", "--depth", "1", "git://github.com/python/mypy", dirpath],
            check=True,
        )
        os.environ["MYPYPATH"] = str(dirpath)
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements-tests-py3.txt"], check=True)
            subprocess.run(
                [
                    "mypy",
                    "--config-file",
                    dirpath / "mypy_self_check.ini",
                    "--custom-typeshed-dir",
                    ".",
                    "-p",
                    "mypy",
                    "-p",
                    "mypyc",
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print("mypy self test failed", file=sys.stderr)
            sys.exit(e.returncode)
        else:
            print("mypy self test succeeded", file=sys.stderr)
            sys.exit(0)
