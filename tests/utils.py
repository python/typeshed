"""Utilities that are imported by multiple scripts in the tests directory."""

from __future__ import annotations

import os
import re
from functools import cache
from itertools import filterfalse
from pathlib import Path
from typing import NamedTuple

import pathspec  # type: ignore[import]
import tomli


def strip_comments(text: str) -> str:
    return text.split("#")[0].strip()


try:
    from termcolor import colored as colored
except ImportError:

    def colored(s: str, _: str) -> str:  # type: ignore[misc]
        return s


def print_error(error: str, end: str = "\n", fix_path: tuple[str, str] = ("", "")) -> None:
    error_split = error.split("\n")
    old, new = fix_path
    for line in error_split[:-1]:
        print(colored(line.replace(old, new), "red"))
    print(colored(error_split[-1], "red"), end=end)


def print_success_msg() -> None:
    print(colored("success", "green"))


# ====================================================================
# Reading dependencies from METADATA.toml files
# ====================================================================


@cache
def read_dependencies(distribution: str) -> tuple[str, ...]:
    with Path("stubs", distribution, "METADATA.toml").open("rb") as f:
        data = tomli.load(f)
    requires = data.get("requires", [])
    assert isinstance(requires, list)
    dependencies = []
    for dependency in requires:
        assert isinstance(dependency, str)
        assert dependency.startswith("types-"), f"unrecognized dependency {dependency!r}"
        dependencies.append(dependency[6:].split("<")[0])
    return tuple(dependencies)


def get_recursive_requirements(package_name: str, seen: set[str] | None = None) -> list[str]:
    seen = seen if seen is not None else {package_name}
    for dependency in filterfalse(seen.__contains__, read_dependencies(package_name)):
        seen.update(get_recursive_requirements(dependency, seen))
    return sorted(seen | {package_name})


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
    return spec.match_file(normalized_path)  # type: ignore[no-any-return]
