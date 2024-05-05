#!/usr/bin/env python3

"""
Check that the typeshed repository contains the correct files in the
correct places, and that various configuration files are correct.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from parse_metadata import read_metadata
from utils import (
    REQS_FILE,
    TEST_CASES_DIR,
    TESTS_DIR,
    VERSIONS_RE,
    get_all_testcase_directories,
    get_gitignore_spec,
    parse_requirements,
    spec_matches_path,
    strip_comments,
    tests_path,
)

extension_descriptions = {".pyi": "stub", ".py": ".py"}

# These type checkers and linters must have exact versions in the requirements file to ensure
# consistent CI runs.
linters = {"black", "flake8", "flake8-noqa", "flake8-pyi", "mypy", "pyright", "pytype", "ruff"}


def assert_consistent_filetypes(
    directory: Path, *, kind: str, allowed: set[str], allow_nonidentifier_filenames: bool = False
) -> None:
    """Check that given directory contains only valid Python files of a certain kind."""
    allowed_paths = {Path(f) for f in allowed}
    contents = list(directory.iterdir())
    gitignore_spec = get_gitignore_spec()
    while contents:
        entry = contents.pop()
        if spec_matches_path(gitignore_spec, entry):
            continue
        if entry.relative_to(directory) in allowed_paths:
            # Note if a subdirectory is allowed, we will not check its contents
            continue
        if entry.is_file():
            if not allow_nonidentifier_filenames:
                assert entry.stem.isidentifier(), f'Files must be valid modules, got: "{entry}"'
            bad_filetype = f'Only {extension_descriptions[kind]!r} files allowed in the "{directory}" directory; got: {entry}'
            assert entry.suffix == kind, bad_filetype
        else:
            assert entry.name.isidentifier(), f"Directories must be valid packages, got: {entry}"
            contents.extend(entry.iterdir())


def check_stdlib() -> None:
    """Check that the stdlib directory contains only the correct files."""
    assert_consistent_filetypes(Path("stdlib"), kind=".pyi", allowed={"_typeshed/README.md", "VERSIONS"})


def check_stubs() -> None:
    """Check that the stubs directory contains only the correct files."""
    gitignore_spec = get_gitignore_spec()
    for dist in Path("stubs").iterdir():
        if spec_matches_path(gitignore_spec, dist):
            continue
        assert dist.is_dir(), f"Only directories allowed in stubs, got {dist}"

        valid_dist_name = "^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$"  # courtesy of PEP 426
        assert re.fullmatch(
            valid_dist_name, dist.name, re.IGNORECASE
        ), f"Directory name must be a valid distribution name: {dist}"
        assert not dist.name.startswith("types-"), f"Directory name not allowed to start with 'types-': {dist}"

        allowed = {"METADATA.toml", "README", "README.md", "README.rst", TESTS_DIR}
        assert_consistent_filetypes(dist, kind=".pyi", allowed=allowed)

        tests_dir = tests_path(dist.name)
        if tests_dir.exists() and tests_dir.is_dir():
            py_files_present = any(file.suffix == ".py" for file in tests_dir.iterdir())
            error_message = (
                f"Test-case files must be in an `{TESTS_DIR}/{TEST_CASES_DIR}` directory, not in the `{TESTS_DIR}` directory"
            )
            assert not py_files_present, error_message


def check_distutils() -> None:
    """Check whether all setuptools._distutils files are re-exported from distutils."""

    def all_relative_paths_in_directory(path: Path) -> set[Path]:
        return {pyi.relative_to(path) for pyi in path.rglob("*.pyi")}

    all_setuptools_files = all_relative_paths_in_directory(Path("stubs", "setuptools", "setuptools", "_distutils"))
    all_distutils_files = all_relative_paths_in_directory(Path("stubs", "setuptools", "distutils"))
    assert all_setuptools_files and all_distutils_files, "Looks like this test might be out of date!"
    extra_files = all_setuptools_files - all_distutils_files
    joined = "\n".join(f"  * {f}" for f in extra_files)
    assert not extra_files, f"Files missing from distutils:\n{joined}"


def check_test_cases() -> None:
    """Check that the test_cases directory contains only the correct files."""
    for _, testcase_dir in get_all_testcase_directories():
        assert_consistent_filetypes(testcase_dir, kind=".py", allowed={"README.md"}, allow_nonidentifier_filenames=True)
        bad_test_case_filename = f'Files in a `{TEST_CASES_DIR}` directory must have names starting with "check_"; got "{{}}"'
        for file in testcase_dir.rglob("*.py"):
            assert file.stem.startswith("check_"), bad_test_case_filename.format(file)


def check_no_symlinks() -> None:
    """Check that there are no symlinks in the typeshed repository."""
    files = [os.path.join(root, file) for root, _, files in os.walk(".") for file in files]
    no_symlink = "You cannot use symlinks in typeshed, please copy {} to its link."
    for file in files:
        _, ext = os.path.splitext(file)
        if ext == ".pyi" and os.path.islink(file):
            raise ValueError(no_symlink.format(file))


def check_versions_file() -> None:
    """Check that the stdlib/VERSIONS file has the correct format."""
    versions = set[str]()
    with open("stdlib/VERSIONS", encoding="UTF-8") as f:
        data = f.read().splitlines()
    for line in data:
        line = strip_comments(line)
        if line == "":
            continue
        m = VERSIONS_RE.match(line)
        if not m:
            raise AssertionError(f"Bad line in VERSIONS: {line}")
        module = m.group(1)
        assert module not in versions, f"Duplicate module {module} in VERSIONS"
        versions.add(module)
    modules = _find_stdlib_modules()
    # Sub-modules don't need to be listed in VERSIONS.
    extra = {m.split(".")[0] for m in modules} - versions
    assert not extra, f"Modules not in versions: {extra}"
    extra = versions - modules
    assert not extra, f"Versions not in modules: {extra}"


def _find_stdlib_modules() -> set[str]:
    modules = set[str]()
    for path, _, files in os.walk("stdlib"):
        for filename in files:
            base_module = ".".join(os.path.normpath(path).split(os.sep)[1:])
            if filename == "__init__.pyi":
                modules.add(base_module)
            elif filename.endswith(".pyi"):
                mod, _ = os.path.splitext(filename)
                modules.add(f"{base_module}.{mod}" if base_module else mod)
    return modules


def check_metadata() -> None:
    """Check that all METADATA.toml files are valid."""
    for distribution in os.listdir("stubs"):
        # This function does various sanity checks for METADATA.toml files
        read_metadata(distribution)


def check_requirement_pins() -> None:
    """Check that type checkers and linters are pinned to an exact version."""
    requirements = parse_requirements()
    for package in linters:
        assert package in requirements, f"type checker/linter '{package}' not found in {REQS_FILE}"
        spec = requirements[package].specifier
        assert len(spec) == 1, f"type checker/linter '{package}' has complex specifier in {REQS_FILE}"
        msg = f"type checker/linter '{package}' is not pinned to an exact version in {REQS_FILE}"
        assert str(spec).startswith("=="), msg


if __name__ == "__main__":
    assert sys.version_info >= (3, 9), "Python 3.9+ is required to run this test"
    check_versions_file()
    check_metadata()
    check_requirement_pins()
    check_no_symlinks()
    check_stdlib()
    check_stubs()
    check_distutils()
    check_test_cases()
