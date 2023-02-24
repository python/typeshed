#!/usr/bin/env python3
"""Test typeshed's stdlib using stubtest

stubtest is a script in the mypy project that compares stubs to the actual objects at runtime.
Note that therefore the output of stubtest depends on which Python version it is run with.
In typeshed CI, we run stubtest with each currently supported Python minor version.

"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from utils import get_mypy_req, make_venv, print_error


def run_stubtest(typeshed_dir: Path) -> int:
    allowlist_dir = typeshed_dir / "tests" / "stubtest_allowlists"
    version_allowlist = f"py{sys.version_info.major}{sys.version_info.minor}.txt"
    platform_allowlist = f"{sys.platform}.txt"
    combined_allowlist = f"{sys.platform}-py{sys.version_info.major}{sys.version_info.minor}.txt"
    with tempfile.TemporaryDirectory() as tmp:
        venv_dir = Path(tmp)
        print("Setting up an isolated virtual environment...", file=sys.stderr)
        try:
            pip_exe, python_exe = make_venv(venv_dir)
        except Exception:
            print_error("fail")
            raise

        # Install the same mypy version as in "requirements-tests.txt"
        try:
            install_command = [pip_exe, "install", get_mypy_req()]
            subprocess.run(install_command, check=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(e.stderr, file=sys.stderr)
            raise

        # Uninstall setuptools from the venv so we can test stdlib's distutils
        try:
            uninstall_command = [pip_exe, "uninstall", "-y", "setuptools"]
            subprocess.run(uninstall_command, check=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(e.stderr, file=sys.stderr)
            raise

        cmd = [
            python_exe,
            "-m",
            "mypy.stubtest",
            "--check-typeshed",
            "--custom-typeshed-dir",
            str(typeshed_dir),
            "--allowlist",
            str(allowlist_dir / "py3_common.txt"),
            "--allowlist",
            str(allowlist_dir / version_allowlist),
        ]
        if (allowlist_dir / platform_allowlist).exists():
            cmd += ["--allowlist", str(allowlist_dir / platform_allowlist)]
        if (allowlist_dir / combined_allowlist).exists():
            cmd += ["--allowlist", str(allowlist_dir / combined_allowlist)]
        if sys.version_info < (3, 10):
            # As discussed in https://github.com/python/typeshed/issues/3693, we only aim for
            # positional-only arg accuracy for python 3.10 and above.
            cmd += ["--ignore-positional-only"]
        print(" ".join(cmd), file=sys.stderr)
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(
                "\nNB: stubtest output depends on the Python version (and system) it is run with. "
                + "See README.md for more details.\n"
                + "NB: We only check positional-only arg accuracy for Python 3.10.\n"
                + f"\nCommand run was: {' '.join(cmd)}\n",
                file=sys.stderr,
            )
            print("\n\n", file=sys.stderr)
            print(f'To fix "unused allowlist" errors, remove the corresponding entries from {allowlist_dir}', file=sys.stderr)
            return e.returncode
        else:
            print("stubtest succeeded", file=sys.stderr)
            return 0


if __name__ == "__main__":
    sys.exit(run_stubtest(typeshed_dir=Path(".")))
