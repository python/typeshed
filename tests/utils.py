"""Utilities that are imported by multiple scripts in the tests directory."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import venv
from functools import cache
from pathlib import Path
from typing import NamedTuple
from typing_extensions import Annotated

import pathspec  # type: ignore[import]
import tomli
from packaging.requirements import Requirement

# Used to install system-wide packages for different OS types:
METADATA_MAPPING = {"linux": "apt_dependencies", "darwin": "brew_dependencies", "win32": "choco_dependencies"}


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


class PackageDependencies(NamedTuple):
    typeshed_pkgs: tuple[str, ...]
    external_pkgs: tuple[str, ...]


@cache
def read_dependencies(distribution: str) -> PackageDependencies:
    with Path("stubs", distribution, "METADATA.toml").open("rb") as f:
        data = tomli.load(f)
    dependencies = data.get("requires", [])
    assert isinstance(dependencies, list)
    typeshed, external = [], []
    for dependency in dependencies:
        if dependency.startswith("types-"):
            maybe_typeshed_dependency = Requirement(dependency).name.removeprefix("types-")
            if maybe_typeshed_dependency in os.listdir("stubs"):
                typeshed.append(maybe_typeshed_dependency)
            else:
                external.append(dependency)
        else:
            external.append(dependency)
    return PackageDependencies(tuple(typeshed), tuple(external))


def get_recursive_requirements(package_name: str, seen: set[str] | None = None) -> PackageDependencies:
    typeshed: set[str] = set()
    external: set[str] = set()
    seen = seen if seen is not None else {package_name}
    non_recursive_requirements = read_dependencies(package_name)
    typeshed.update(non_recursive_requirements.typeshed_pkgs)
    external.update(non_recursive_requirements.external_pkgs)
    for pkg in non_recursive_requirements.typeshed_pkgs:
        if pkg in seen:
            continue
        reqs = get_recursive_requirements(pkg)
        typeshed.update(reqs.typeshed_pkgs)
        external.update(reqs.external_pkgs)
        seen.add(pkg)
    return PackageDependencies(tuple(sorted(typeshed)), tuple(sorted(external)))


# ====================================================================
# Dynamic venv creation
# ====================================================================


class VenvInfo(NamedTuple):
    pip_exe: Annotated[str, "A path to the venv's pip executable"]
    python_exe: Annotated[str, "A path to the venv's python executable"]


def make_venv(venv_dir: Path) -> VenvInfo:
    try:
        venv.create(venv_dir, with_pip=True, clear=True)
    except subprocess.CalledProcessError as e:
        if "ensurepip" in e.cmd:
            print_error(
                "stubtest requires a Python installation with ensurepip. "
                "If on Linux, you may need to install the python3-venv package."
            )
        raise

    if sys.platform == "win32":
        pip = venv_dir / "Scripts" / "pip.exe"
        python = venv_dir / "Scripts" / "python.exe"
    else:
        pip = venv_dir / "bin" / "pip"
        python = venv_dir / "bin" / "python"

    return VenvInfo(str(pip), str(python))


@cache
def get_mypy_req() -> str:
    with open("requirements-tests.txt", encoding="UTF-8") as f:
        return next(line.strip() for line in f if "mypy" in line)


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
    return spec.match_file(normalized_path)  # type: ignore[no-any-return]
