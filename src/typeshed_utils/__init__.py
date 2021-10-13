from __future__ import annotations

import os
import re
from os import PathLike
from pathlib import Path
from typing import Iterable

import tomli

PY2_PATH = "@python2"

_STDLIB_VERSIONS_RE = re.compile(r"([a-zA-Z_][a-zA-Z0-9_.]*): ([23]\.\d{1,2})-([23]\.\d{1,2})?")
_STUB_VERSION_RE = re.compile(r"\d+(\.\d+)+|\d+(\.\d+)*\.\*")


class FormatError(Exception):
    pass


def stdlib_path(typeshed_path: str | PathLike[str], *, py2: bool = False) -> Path:
    path = Path(typeshed_path) / "stdlib"
    if py2:
        path /= PY2_PATH
    return path


def stubs_path(typeshed_path: str | PathLike[str]) -> Path:
    return Path(typeshed_path) / "stubs"


def distribution_path(typeshed_path: str | PathLike[str], distribution: str, *, py2: bool = False) -> Path:
    path = stubs_path(typeshed_path) / distribution
    if py2:
        path /= PY2_PATH
    return path


class VersionInfo:
    def __init__(self, versions: dict[str, tuple[str, str | None]]) -> None:
        self._versions = versions

    @property
    def modules(self) -> set[str]:
        return set(self._versions.keys())


def stdlib_versions(typeshed_path: str | PathLike[str]) -> VersionInfo:
    """Return Python versions supported by standard library modules.

    The returned dict has all standard library modules as keys. The values
    are 2-tuples with first/last Python version that contained the module.
    If Python 2.7 or earlier added the module, the first version will be
    "2.7". If the module is still supported by the latest Python version, the
    last version will be None.

    If a submodule has a lifetime that differs from the top module, it will
    be listed separately.
    """

    versions: dict[str, tuple[str, str | None]] = {}
    with open(stdlib_path(typeshed_path) / "VERSIONS") as f:
        data = f.read().splitlines()
    for line in data:
        line = line.split("#")[0].strip()
        if line == "":
            continue
        m = _STDLIB_VERSIONS_RE.fullmatch(line)
        if m is None:
            raise FormatError(f"Bad line in VERSIONS: {line}")
        module = m.group(1)
        assert module not in versions, f"Duplicate module {module} in VERSIONS"
        versions[module] = m.group(2), m.group(3)
    return VersionInfo(versions)


def all_stdlib_modules(typeshed_path: str | PathLike[str]) -> list[str]:
    """Return a list of all standard library modules and sub-modules."""
    stdlib_p = stdlib_path(typeshed_path).absolute()
    prefix_len = len(str(stdlib_p))
    modules: set[str] = set()
    for p, _, files in os.walk(stdlib_p):
        path = p[prefix_len + 1 :]
        if path.startswith(PY2_PATH):
            continue
        for filename in files:
            base_module = ".".join(path.split(os.sep))
            if filename == "__init__.pyi":
                modules.add(base_module)
            elif filename.endswith(".pyi"):
                mod, _ = os.path.splitext(filename)
                modules.add(f"{base_module}.{mod}" if base_module else mod)
    return sorted(modules)


def third_party_distributions(typeshed_path: str | PathLike[str]) -> list[str]:
    return [e.name for e in stubs_path(typeshed_path).iterdir()]


class MetaData:
    def __init__(
        self,
        distribution: str,
        version: str,
        requires: Iterable[str] = [],
        *,
        extra_description: str | None = None,
        obsolete_since: str | None = None,
        python2: bool = False,
    ) -> None:  # noqa: B006
        if not _STUB_VERSION_RE.fullmatch(version):
            raise FormatError(f"Invalid version {version} for {distribution}")
        self.distribution = distribution
        self.version = version
        self.requires = list(requires)
        self.extra_description = extra_description
        self.obsolete_since = obsolete_since
        self.python2 = python2

    @property
    def base_version(self) -> str:
        if self.version.endswith(".*"):
            return self.version[:-2]
        else:
            return self.version


_metadata_keys = {"version": str, "python2": bool, "requires": list, "extra_description": str, "obsolete_since": str}


def read_metadata(typeshed_path: str | PathLike[str], distribution: str) -> MetaData:
    with open(distribution_path(typeshed_path, distribution) / "METADATA.toml") as f:
        data = tomli.loads(f.read())
    if "version" not in data:
        raise FormatError(f"Missing version for {distribution}")
    for key, expected_type in _metadata_keys.items():
        if key in data and not isinstance(data[key], expected_type):
            raise FormatError(f"Invalid {key} value for {distribution}")
    for key in data:
        if key not in _metadata_keys:
            raise FormatError(f"Unexpected key {key} for {distribution}")
    version: str = data["version"]
    requires: list[str] = data.get("requires", [])
    extra_description: str | None = data.get("extra_description")
    obsolete_since: str | None = data.get("obsolete_since")
    python2: bool = data.get("python2", False)
    for dep in requires:
        if not isinstance(dep, str):
            raise FormatError(f"Invalid dependency {dep} for {distribution}")
    return MetaData(
        distribution, version, requires, extra_description=extra_description, obsolete_since=obsolete_since, python2=python2
    )
