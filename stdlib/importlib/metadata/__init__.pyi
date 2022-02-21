import abc
import pathlib
import sys
from _typeshed import Self, StrPath
from collections.abc import Mapping
from email.message import Message
from importlib.abc import MetaPathFinder
from os import PathLike
from pathlib import Path
from typing import Any, ClassVar, Iterable, NamedTuple, Pattern, overload

if sys.version_info >= (3, 10):
    __all__ = [
        "Distribution",
        "DistributionFinder",
        "PackageMetadata",
        "PackageNotFoundError",
        "distribution",
        "distributions",
        "entry_points",
        "files",
        "metadata",
        "packages_distributions",
        "requires",
        "version",
    ]
else:
    __all__ = [
        "Distribution",
        "DistributionFinder",
        "PackageNotFoundError",
        "distribution",
        "distributions",
        "entry_points",
        "files",
        "metadata",
        "requires",
        "version",
    ]

if sys.version_info >= (3, 10):
    from importlib.metadata._meta import PackageMetadata as PackageMetadata
    def packages_distributions() -> Mapping[str, list[str]]: ...

class PackageNotFoundError(ModuleNotFoundError): ...

class _EntryPointBase(NamedTuple):
    name: str
    value: str
    group: str

class EntryPoint(_EntryPointBase):
    pattern: ClassVar[Pattern[str]]
    def load(self) -> Any: ...  # Callable[[], Any] or an importable module
    @property
    def extras(self) -> list[str]: ...
    if sys.version_info >= (3, 9):
        @property
        def module(self) -> str: ...
        @property
        def attr(self) -> str: ...
    if sys.version_info >= (3, 10):
        dist: ClassVar[Distribution | None]
        def matches(self, **params: Any) -> bool: ...  # undocumented

if sys.version_info >= (3, 10):
    class EntryPoints(list[EntryPoint]):  # use as list is deprecated since 3.10
        def select(self, **params: Any) -> EntryPoints: ...
        @property
        def names(self) -> set[str]: ...
        @property
        def groups(self) -> set[str]: ...

    class SelectableGroups(dict[str, EntryPoints]):  # use as dict is deprecated since 3.10
        @classmethod
        def load(cls: type[Self], eps: Iterable[EntryPoint]) -> Self: ...
        @property
        def groups(self) -> set[str]: ...
        @property
        def names(self) -> set[str]: ...
        def select(self, **params: Any) -> SelectableGroups: ...

class PackagePath(pathlib.PurePosixPath):
    def read_text(self, encoding: str = ...) -> str: ...
    def read_binary(self) -> bytes: ...
    def locate(self) -> PathLike[str]: ...
    # The following attributes are not defined on PackagePath, but are dynamically added by Distribution.files:
    hash: FileHash | None
    size: int | None
    dist: Distribution

class FileHash:
    mode: str
    value: str
    def __init__(self, spec: str) -> None: ...

class Distribution:
    @abc.abstractmethod
    def read_text(self, filename: str) -> str | None: ...
    @abc.abstractmethod
    def locate_file(self, path: StrPath) -> PathLike[str]: ...
    @classmethod
    def from_name(cls, name: str) -> Distribution: ...
    @overload
    @classmethod
    def discover(cls, *, context: DistributionFinder.Context) -> Iterable[Distribution]: ...
    @overload
    @classmethod
    def discover(
        cls, *, context: None = ..., name: str | None = ..., path: list[str] = ..., **kwargs: Any
    ) -> Iterable[Distribution]: ...
    @staticmethod
    def at(path: StrPath) -> PathDistribution: ...

    if sys.version_info >= (3, 10):
        @property
        def metadata(self) -> PackageMetadata: ...
        @property
        def entry_points(self) -> EntryPoints: ...
    else:
        @property
        def metadata(self) -> Message: ...
        @property
        def entry_points(self) -> list[EntryPoint]: ...

    @property
    def version(self) -> str: ...
    @property
    def files(self) -> list[PackagePath] | None: ...
    if sys.version_info >= (3, 10):
        @property
        def name(self) -> str: ...

class DistributionFinder(MetaPathFinder):
    class Context:
        name: str | None
        def __init__(self, *, name: str | None = ..., path: list[str] = ..., **kwargs: Any) -> None: ...
        @property
        def path(self) -> list[str]: ...

    @abc.abstractmethod
    def find_distributions(self, context: DistributionFinder.Context = ...) -> Iterable[Distribution]: ...

class MetadataPathFinder(DistributionFinder):
    @classmethod
    def find_distributions(cls, context: DistributionFinder.Context = ...) -> Iterable[PathDistribution]: ...
    if sys.version_info >= (3, 10):
        # Yes, this is an instance method that has argumend named "cls"
        def invalidate_caches(cls) -> None: ...  # type: ignore

class PathDistribution(Distribution):
    def __init__(self, path: Path) -> None: ...
    def read_text(self, filename: StrPath) -> str: ...
    def locate_file(self, path: StrPath) -> PathLike[str]: ...

def distribution(distribution_name: str) -> Distribution: ...
@overload
def distributions(*, context: DistributionFinder.Context) -> Iterable[Distribution]: ...
@overload
def distributions(
    *, context: None = ..., name: str | None = ..., path: list[str] = ..., **kwargs: Any
) -> Iterable[Distribution]: ...

if sys.version_info >= (3, 10):
    def metadata(distribution_name: str) -> PackageMetadata: ...
    @overload
    def entry_points() -> SelectableGroups: ...
    @overload
    def entry_points(**params: Any) -> EntryPoints: ...

else:
    def metadata(distribution_name: str) -> Message: ...
    def entry_points() -> dict[str, list[EntryPoint]]: ...

def version(distribution_name: str) -> str: ...
def files(distribution_name: str) -> list[PackagePath] | None: ...
def requires(distribution_name: str) -> list[str] | None: ...
