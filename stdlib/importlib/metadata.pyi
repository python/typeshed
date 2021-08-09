import abc
import pathlib
import sys
from _typeshed import StrPath
from collections.abc import Mapping
from email.message import Message
from importlib.abc import MetaPathFinder
from os import PathLike
from pathlib import Path
from typing import Any, Dict, Iterable, List, NamedTuple, Tuple, overload

if sys.version_info >= (3, 10):
    def packages_distributions() -> Mapping[str, List[str]]: ...

if sys.version_info >= (3, 8):
    class PackageNotFoundError(ModuleNotFoundError): ...
    class _EntryPointBase(NamedTuple):
        name: str
        value: str
        group: str
    class EntryPoint(_EntryPointBase):
        def load(self) -> Any: ...  # Callable[[], Any] or an importable module
        @property
        def extras(self) -> List[str]: ...
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
            cls, *, context: None = ..., name: str | None = ..., path: List[str] = ..., **kwargs: Any
        ) -> Iterable[Distribution]: ...
        @staticmethod
        def at(path: StrPath) -> PathDistribution: ...
        @property
        def metadata(self) -> Message: ...
        @property
        def version(self) -> str: ...
        @property
        def entry_points(self) -> List[EntryPoint]: ...
        @property
        def files(self) -> List[PackagePath] | None: ...
        @property
        def requires(self) -> List[str] | None: ...
    class DistributionFinder(MetaPathFinder):
        class Context:
            name: str | None
            def __init__(self, *, name: str | None = ..., path: List[str] = ..., **kwargs: Any) -> None: ...
            @property
            def path(self) -> List[str]: ...
        @abc.abstractmethod
        def find_distributions(self, context: DistributionFinder.Context = ...) -> Iterable[Distribution]: ...
    class MetadataPathFinder(DistributionFinder):
        @classmethod
        def find_distributions(cls, context: DistributionFinder.Context = ...) -> Iterable[PathDistribution]: ...
    class PathDistribution(Distribution):
        def __init__(self, path: Path) -> None: ...
        def read_text(self, filename: StrPath) -> str: ...
        def locate_file(self, path: StrPath) -> PathLike[str]: ...
    def distribution(distribution_name: str) -> Distribution: ...
    @overload
    def distributions(*, context: DistributionFinder.Context) -> Iterable[Distribution]: ...
    @overload
    def distributions(
        *, context: None = ..., name: str | None = ..., path: List[str] = ..., **kwargs: Any
    ) -> Iterable[Distribution]: ...
    def metadata(distribution_name: str) -> Message: ...
    def version(distribution_name: str) -> str: ...
    def entry_points() -> Dict[str, Tuple[EntryPoint, ...]]: ...
    def files(distribution_name: str) -> List[PackagePath] | None: ...
    def requires(distribution_name: str) -> List[str] | None: ...
