from functools import cached_property
from pathlib import Path

from ts_utils.paths import STDLIB_PATH, STUBS_PATH, TESTS_DIR, distribution_path
from ts_utils.utils import parse_stdlib_versions_file


class StubFile:
    """A stdlib stub file."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def __fspath__(self) -> str:
        return self.path.__fspath__()

    def __str__(self) -> str:
        return str(self.path)

    @cached_property
    def module_name(self) -> str:
        return ".".join(self.module_parts)

    @cached_property
    def module_parts(self) -> tuple[str, ...]:
        raise NotImplementedError


class StdlibStubFile(StubFile):
    @cached_property
    def module_parts(self) -> tuple[str, ...]:
        relative = self.path.relative_to(STDLIB_PATH)
        parts = list(relative.parts[:-1])
        if relative.name != "__init__.pyi":
            parts.append(relative.stem)
        return tuple(parts)


class ThirdPartyStubFile(StubFile):
    @cached_property
    def upstream_distribution(self) -> str:
        return self.path.relative_to(STUBS_PATH).parts[0]

    @cached_property
    def module_parts(self) -> tuple[str, ...]:
        relative = self.path.relative_to(STUBS_PATH)
        parts = list(relative.parts[1:-1])
        print(parts)
        if relative.name != "__init__.pyi":
            parts.append(relative.stem)
        return tuple(parts)


def stdlib_stubs(version: str) -> list[StdlibStubFile]:
    """Return the stdlib stubs available in the requested Python version."""
    module_versions = parse_stdlib_versions_file()
    stubs: list[StdlibStubFile] = []

    for path in sorted(STDLIB_PATH.rglob("*.pyi")):
        if TESTS_DIR in path.parts:
            continue
        stub = StdlibStubFile(path)
        if module_versions.is_supported(stub.module_name, version):
            stubs.append(stub)

    return stubs


def third_party_stubs(distribution: str | None = None) -> list[ThirdPartyStubFile]:
    stubs: list[ThirdPartyStubFile] = []

    stub_path = distribution_path(distribution) if distribution else STUBS_PATH

    for path in sorted(stub_path.rglob("*.pyi")):
        if TESTS_DIR in path.parts:
            continue
        stubs.append(ThirdPartyStubFile(path))

    return stubs


def path_stubs(path: Path) -> list[Path]:
    """Return all stubs in a certain path."""
    if path.is_file():
        return [path] if path.suffix == ".pyi" and TESTS_DIR not in path.parts else []
    return sorted(p for p in path.rglob("*.pyi") if TESTS_DIR not in p.parts)
