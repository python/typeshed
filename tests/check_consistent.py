#!/usr/bin/env python3

# For security (and simplicity) reasons, only a limited kind of files can be
# present in /stdlib and /stubs directories, see README for detail. Here we
# verify these constraints.

# In addition, for various reasons we need the contents of certain files to be
# duplicated in two places, for example stdlib/@python2/builtins.pyi and
# stdlib/@python2/__builtin__.pyi must be identical.  In the past we used
# symlinks but that doesn't always work on Windows, so now you must
# manually update both files, and this test verifies that they are
# identical.  The list below indicates which sets of files must match.

from __future__ import annotations

import filecmp
import os
import sys
from pathlib import Path

typeshed_path = Path(__file__).parent.parent
sys.path.append(str(typeshed_path / "src"))

from typeshed_utils import (  # noqa: E402
    PY2_PATH,
    all_stdlib_modules,
    distribution_path,
    read_metadata,
    stdlib_path,
    stdlib_versions,
    stubs_path,
    third_party_distributions,
)

consistent_files = [
    {"stdlib/@python2/builtins.pyi", "stdlib/@python2/__builtin__.pyi"},
    {"stdlib/threading.pyi", "stdlib/_dummy_threading.pyi"},
]
metadata_keys = {"version", "python2", "requires", "extra_description", "obsolete_since"}
allowed_files = {"README.md"}


def assert_stubs_only(directory: Path) -> None:
    """Check that given directory contains only valid stub files."""
    assert directory.name.isidentifier(), f"Bad directory name: {directory.name}"
    for _, dirs, files in os.walk(directory):
        for file in files:
            if file in allowed_files:
                continue
            name, ext = os.path.splitext(file)
            assert name.isidentifier(), f"Files must be valid modules, got: {name}"
            assert ext == ".pyi", f"Only stub flies allowed. Got: {file} in {directory.name}"
        for subdir in dirs:
            assert subdir.isidentifier(), f"Directories must be valid packages, got: {subdir}"


def check_stdlib() -> None:
    for entry in stdlib_path(typeshed_path).iterdir():
        if entry.is_file():
            if entry.suffix != ".pyi":
                assert entry.name == "VERSIONS", f"Unexpected file in stdlib root: {entry.name}"
            assert entry.stem.isidentifier(), "Bad file name in stdlib"
        else:
            if entry.name == PY2_PATH:
                continue
            assert_stubs_only(entry)
    for entry in stdlib_path(typeshed_path, py2=True).iterdir():
        if entry.is_file():
            assert entry.stem.isidentifier(), "Bad file name in stdlib"
            assert entry.suffix == ".pyi", "Unexpected file in stdlib/@python2 root"
        else:
            assert_stubs_only(entry)


def check_stubs() -> None:
    for entry in stubs_path(typeshed_path).iterdir():
        assert entry.is_dir(), f"Only directories allowed in stubs, got {entry.name}"
    for distribution in third_party_distributions(typeshed_path):
        path = distribution_path(typeshed_path, distribution)
        py2_path = distribution_path(typeshed_path, distribution, py2=True)
        for entry in path.iterdir():
            if entry.is_file():
                if entry.suffix != ".pyi":
                    assert entry.name in {"METADATA.toml", "README", "README.md", "README.rst"}, entry.name
                else:
                    assert entry.stem.isidentifier(), f"Bad file name '{entry.stem}' in stubs"
            else:
                if entry.name in (PY2_PATH, "@tests"):
                    continue
                assert_stubs_only(entry)
        if py2_path.is_dir():
            for entry in py2_path.iterdir():
                if entry.is_file():
                    assert entry.stem.isidentifier(), f"Bad file name '{entry.stem}' in stubs"
                    assert entry.suffix == ".pyi", f"Unexpected file {entry.name} in @python2 stubs"
                else:
                    assert_stubs_only(entry)


def check_no_links() -> None:
    files = [os.path.join(root, file) for root, _, files in os.walk(".") for file in files]
    no_symlink = "You cannot use symlinks in typeshed, please copy {} to its link."
    for file in files:
        _, ext = os.path.splitext(file)
        if ext == ".pyi" and os.path.islink(file):
            raise ValueError(no_symlink.format(file))


def check_same_files() -> None:
    for file1, *others in consistent_files:
        f1 = os.path.join(os.getcwd(), file1)
        for file2 in others:
            f2 = os.path.join(os.getcwd(), file2)
            if not filecmp.cmp(f1, f2):
                raise ValueError(
                    "File {f1} does not match file {f2}. Please copy it to {f2}\n"
                    "Run either:\ncp {f1} {f2}\nOr:\ncp {f2} {f1}".format(f1=file1, f2=file2)
                )


def check_versions() -> None:
    versions = stdlib_versions(typeshed_path).py3_modules
    modules = set(all_stdlib_modules(typeshed_path))
    # Sub-modules don't need to be listed in VERSIONS.
    extra = {m.split(".")[0] for m in modules} - versions
    assert not extra, f"Modules not in versions: {extra}"
    extra = versions - modules
    assert not extra, f"Versions not in modules: {extra}"


def _verify_dependency(dependency: str) -> None:
    for space in " \t\n":
        assert space not in dependency, f"For consistency dependency should not have whitespace: {dependency}"
    assert ";" not in dependency, f"Semicolons in dependencies are not supported, got {dependency}"
    relation = _strip_dep_version(dependency)
    if relation:
        assert relation in {"==", ">", ">=", "<", "<="}, f"Bad version in dependency {dependency}"


def _strip_dep_version(dependency: str) -> str:
    dep_version_pos = len(dependency)
    for pos, c in enumerate(dependency):
        if c in "=<>":
            dep_version_pos = pos
            break
    rest = dependency[dep_version_pos:]
    if not rest:
        return ""
    number_pos = 0
    for pos, c in enumerate(rest):
        if c not in "=<>":
            number_pos = pos
            break
    relation = rest[:number_pos]
    return relation


def check_metadata():
    for distribution in third_party_distributions(typeshed_path):
        data = read_metadata(typeshed_path, distribution)
        for dep in data.requires:
            _verify_dependency(dep)


if __name__ == "__main__":
    check_stdlib()
    check_versions()
    check_stubs()
    check_metadata()
    check_no_links()
    check_same_files()
