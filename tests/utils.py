"""Utilities that are imported by multiple scripts in the tests directory."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import venv
from collections.abc import Iterable
from functools import lru_cache
from pathlib import Path
from typing import NamedTuple
from typing_extensions import Annotated

import pathspec

try:
    from termcolor import colored as colored
except ImportError:

    def colored(text: str, color: str | None = None, on_color: str | None = None, attrs: Iterable[str] | None = None) -> str:
        return text


# A backport of functools.cache for Python <3.9
# This module is imported by mypy_test.py, which needs to run on 3.7 in CI
cache = lru_cache(None)


def strip_comments(text: str) -> str:
    return text.split("#")[0].strip()


def print_error(error: str, end: str = "\n", fix_path: tuple[str, str] = ("", "")) -> None:
    error_split = error.split("\n")
    old, new = fix_path
    for line in error_split[:-1]:
        print(colored(line.replace(old, new), "red"))
    print(colored(error_split[-1], "red"), end=end)


def print_success_msg() -> None:
    print(colored("success", "green"))


# ====================================================================
# Dynamic venv creation
# ====================================================================


class VenvInfo(NamedTuple):
    pip_exe: Annotated[str, "A path to the venv's pip executable"]
    python_exe: Annotated[str, "A path to the venv's python executable"]

    @staticmethod
    def of_existing_venv(venv_dir: Path) -> VenvInfo:
        if sys.platform == "win32":
            pip = venv_dir / "Scripts" / "pip.exe"
            python = venv_dir / "Scripts" / "python.exe"
        else:
            pip = venv_dir / "bin" / "pip"
            python = venv_dir / "bin" / "python"

        return VenvInfo(str(pip), str(python))


def make_venv(venv_dir: Path) -> VenvInfo:
    try:
        venv.create(venv_dir, with_pip=True, clear=True)
    except subprocess.CalledProcessError as e:
        if "ensurepip" in e.cmd and b"KeyboardInterrupt" not in e.stdout.splitlines():
            print_error(
                "stubtest requires a Python installation with ensurepip. "
                "If on Linux, you may need to install the python3-venv package."
            )
        raise

    return VenvInfo.of_existing_venv(venv_dir)


@cache
def get_mypy_req() -> str:
    with open("requirements-tests.txt", encoding="UTF-8") as requirements_file:
        return next(strip_comments(line) for line in requirements_file if "mypy" in line)


# ====================================================================
# Parsing the stdlib/VERSIONS file
# ====================================================================


VERSIONS_RE = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_.]*): ([23]\.\d{1,2})-([23]\.\d{1,2})?$")


# ====================================================================
# Getting test-case directories from package names
# ====================================================================


class PackageInfo(NamedTuple):
    name: str
    test_case_directory: Path

    @property
    def is_stdlib(self) -> bool:
        return self.name == "stdlib"


def testcase_dir_from_package_name(package_name: str) -> Path:
    return Path("stubs", package_name, "@tests/test_cases")


def get_all_testcase_directories() -> list[PackageInfo]:
    testcase_directories = [PackageInfo("stdlib", Path("test_cases"))]
    for package_name in os.listdir("stubs"):
        potential_testcase_dir = testcase_dir_from_package_name(package_name)
        if potential_testcase_dir.is_dir():
            testcase_directories.append(PackageInfo(package_name, potential_testcase_dir))
    return sorted(testcase_directories)


# ====================================================================
# Parsing .gitignore
# ====================================================================


@cache
def get_gitignore_spec() -> pathspec.PathSpec:
    with open(".gitignore", encoding="UTF-8") as f:
        return pathspec.PathSpec.from_lines("gitwildmatch", f.readlines())


def spec_matches_path(spec: pathspec.PathSpec, path: Path) -> bool:
    normalized_path = path.as_posix()
    if path.is_dir():
        normalized_path += "/"
    # pathspec.PathSpec.match_file has partially Unknown file parameter
    # https://github.com/cpburnz/python-pathspec/pull/75
    return spec.match_file(normalized_path)  # pyright: ignore[reportUnknownMemberType]
