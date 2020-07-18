#!/usr/bin/env python3
"""Script to run mypy against its own code base."""

from pathlib import Path
import subprocess
import sys
import tempfile

MYPY_VERSION = "0.782"


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tempdir:
        dirpath = Path(tempdir)
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", f"v{MYPY_VERSION}", "git://github.com/python/mypy", str(dirpath)],
            check=True,
        )
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", f"mypy=={MYPY_VERSION}"], check=True)
            subprocess.run(
                [
                    "mypy",
                    "--config-file",
                    dirpath / "mypy_self_check.ini",
                    "--custom-typeshed-dir",
                    ".",
                    dirpath / "mypy",
                    dirpath / "mypyc",
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print("mypy self test failed", file=sys.stderr)
            sys.exit(e.returncode)
        else:
            print("mypy self test succeeded", file=sys.stderr)
            sys.exit(0)
