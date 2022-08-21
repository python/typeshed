#!/usr/bin/env python3

# For security (and simplicity) reasons, only a limited kind of files can be
# present in /stdlib and /stubs directories, see README for detail. Here we
# verify these constraints.
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import tomli
from packaging.requirements import Requirement
from packaging.version import Version

metadata_keys = {"version", "requires", "extra_description", "obsolete_since", "no_longer_updated", "tool"}
tool_keys = {"stubtest": {"skip", "apt_dependencies", "extras", "ignore_missing_stub"}}


def assert_stubs_only(directory: Path, allowed: set[str]) -> None:
    """Check that given directory contains only valid stub files."""
    allowed_paths = {Path(f) for f in allowed}
    contents = list(directory.iterdir())
    while contents:
        entry = contents.pop()
        if entry.relative_to(directory) in allowed_paths:
            # Note if a subdirectory is allowed, we will not check its contents
            continue
        if entry.is_file():
            assert entry.stem.isidentifier(), f"Files must be valid modules, got: {entry}"
            assert entry.suffix == ".pyi", f"Only stub files allowed, got: {entry}"
        else:
            assert entry.name.isidentifier(), f"Directories must be valid packages, got: {entry}"
            contents.extend(entry.iterdir())


def check_stdlib() -> None:
    assert_stubs_only(Path("stdlib"), allowed={"_typeshed/README.md", "VERSIONS"})


def check_stubs() -> None:
    for dist in Path("stubs").iterdir():
        assert dist.is_dir(), f"Only directories allowed in stubs, got {dist}"

        valid_dist_name = "^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$"  # courtesy of PEP 426
        assert re.fullmatch(
            valid_dist_name, dist.name, re.IGNORECASE
        ), f"Directory name must have valid distribution name: {dist}"
        assert not dist.name.startswith("types-"), f"Directory name not allowed to start with 'types-': {dist}"

        allowed = {"METADATA.toml", "README", "README.md", "README.rst", "@tests"}
        assert_stubs_only(dist, allowed)


def check_same_files() -> None:
    files = [os.path.join(root, file) for root, _, files in os.walk(".") for file in files]
    no_symlink = "You cannot use symlinks in typeshed, please copy {} to its link."
    for file in files:
        _, ext = os.path.splitext(file)
        if ext == ".pyi" and os.path.islink(file):
            raise ValueError(no_symlink.format(file))


_VERSIONS_RE = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_.]*): [23]\.\d{1,2}-(?:[23]\.\d{1,2})?$")


def check_versions() -> None:
    versions = set()
    with open("stdlib/VERSIONS") as f:
        data = f.read().splitlines()
    for line in data:
        line = line.split("#")[0].strip()
        if line == "":
            continue
        m = _VERSIONS_RE.match(line)
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
    modules = set()
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
    for distribution in os.listdir("stubs"):
        with open(os.path.join("stubs", distribution, "METADATA.toml")) as f:
            data = tomli.loads(f.read())
        assert "version" in data, f"Missing version for {distribution}"
        version = data["version"]
        msg = f"Unsupported version {repr(version)}"
        assert isinstance(version, str), msg
        # Check that the version parses
        Version(version.removesuffix(".*"))
        for key in data:
            assert key in metadata_keys, f"Unexpected key {key} for {distribution}"
        assert isinstance(data.get("requires", []), list), f"Invalid requires value for {distribution}"
        for dep in data.get("requires", []):
            assert isinstance(dep, str), f"Invalid requirement {repr(dep)} for {distribution}"
            for space in " \t\n":
                assert space not in dep, f"For consistency, requirement should not have whitespace: {dep}"
            # Check that the requirement parses
            Requirement(dep)

        assert set(data.get("tool", [])).issubset(tool_keys.keys()), f"Unrecognised tool for {distribution}"
        for tool, tk in tool_keys.items():
            for key in data.get("tool", {}).get(tool, {}):
                assert key in tk, f"Unrecognised {tool} key {key} for {distribution}"


if __name__ == "__main__":
    assert sys.version_info >= (3, 9), "Python 3.9+ is required to run this test"
    check_stdlib()
    check_versions()
    check_stubs()
    check_metadata()
    check_same_files()
