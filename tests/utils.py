"""Utilities that are imported by multiple scripts in the tests directory."""

from __future__ import annotations

import os
import re
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any, Final, NamedTuple

import pathspec

try:
    from termcolor import colored as colored  # pyright: ignore[reportAssignmentType]
except ImportError:

    def colored(text: str, color: str | None = None, **kwargs: Any) -> str:  # type: ignore[misc]
        return text


PYTHON_VERSION: Final = f"{sys.version_info.major}.{sys.version_info.minor}"


# A backport of functools.cache for Python <3.9
# This module is imported by mypy_test.py, which needs to run on 3.8 in CI
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


@cache
def venv_python(venv_dir: Path) -> Path:
    if sys.platform == "win32":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


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
    testcase_directories: list[PackageInfo] = []
    for package_name in os.listdir("stubs"):
        potential_testcase_dir = testcase_dir_from_package_name(package_name)
        if potential_testcase_dir.is_dir():
            testcase_directories.append(PackageInfo(package_name, potential_testcase_dir))
    return [PackageInfo("stdlib", Path("test_cases")), *sorted(testcase_directories)]


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
    return spec.match_file(normalized_path)
