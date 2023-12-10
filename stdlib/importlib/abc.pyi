import _ast
import sys
import types
from _typeshed import ReadableBuffer, StrPath
from abc import ABCMeta, abstractmethod
from collections.abc import Iterator, Mapping, Sequence
from importlib.machinery import ModuleSpec
from io import BufferedReader
from typing import IO, Any, Protocol, overload, runtime_checkable
from typing_extensions import Literal

if sys.version_info >= (3, 11):
    __all__ = [
        "Loader",
        "MetaPathFinder",
        "PathEntryFinder",
        "ResourceLoader",
        "InspectLoader",
        "ExecutionLoader",
        "FileLoader",
        "SourceLoader",
    ]

    if sys.version_info < (3, 12):
        __all__ += ["Finder", "ResourceReader", "Traversable", "TraversableResources"]

if sys.version_info < (3, 12):
    class Finder(metaclass=ABCMeta): ...

class Loader(metaclass=ABCMeta):
    def load_module(self, fullname: str) -> types.ModuleType: ...
    if sys.version_info < (3, 12):
        def module_repr(self, module: types.ModuleType) -> str: ...

    def create_module(self, spec: ModuleSpec) -> types.ModuleType | None: ...
    # Not defined on the actual class for backwards-compatibility reasons,
    # but expected in new code.
    def exec_module(self, module: types.ModuleType) -> None: ...

class ResourceLoader(Loader):
    @abstractmethod
    def get_data(self, path: str) -> bytes: ...

class InspectLoader(Loader):
    def is_package(self, fullname: str) -> bool: ...
    def get_code(self, fullname: str) -> types.CodeType | None: ...
    @abstractmethod
    def get_source(self, fullname: str) -> str | None: ...
    def exec_module(self, module: types.ModuleType) -> None: ...
    @staticmethod
    def source_to_code(
        data: ReadableBuffer | str | _ast.Module | _ast.Expression | _ast.Interactive, path: ReadableBuffer | StrPath = "<string>"
    ) -> types.CodeType: ...

class ExecutionLoader(InspectLoader):
    @abstractmethod
    def get_filename(self, fullname: str) -> str: ...

class SourceLoader(ResourceLoader, ExecutionLoader, metaclass=ABCMeta):
    def path_mtime(self, path: str) -> float: ...
    def set_data(self, path: str, data: bytes) -> None: ...
    def get_source(self, fullname: str) -> str | None: ...
    def path_stats(self, path: str) -> Mapping[str, Any]: ...

# The base classes differ starting in 3.10:
if sys.version_info >= (3, 10):
    # Please keep in sync with sys._MetaPathFinder
    class MetaPathFinder(metaclass=ABCMeta):
        if sys.version_info < (3, 12):
            def find_module(self, fullname: str, path: Sequence[str] | None) -> Loader | None: ...

        def invalidate_caches(self) -> None: ...
        # Not defined on the actual class, but expected to exist.
        def find_spec(
            self, __fullname: str, __path: Sequence[str] | None, __target: types.ModuleType | None = ...
        ) -> ModuleSpec | None: ...

    class PathEntryFinder(metaclass=ABCMeta):
        if sys.version_info < (3, 12):
            def find_module(self, fullname: str) -> Loader | None: ...
            def find_loader(self, fullname: str) -> tuple[Loader | None, Sequence[str]]: ...

        def invalidate_caches(self) -> None: ...
        # Not defined on the actual class, but expected to exist.
        def find_spec(self, fullname: str, target: types.ModuleType | None = ...) -> ModuleSpec | None: ...

else:
    # Please keep in sync with sys._MetaPathFinder
    class MetaPathFinder(Finder):
        def find_module(self, fullname: str, path: Sequence[str] | None) -> Loader | None: ...
        def invalidate_caches(self) -> None: ...
        # Not defined on the actual class, but expected to exist.
        def find_spec(
            self, __fullname: str, __path: Sequence[str] | None, __target: types.ModuleType | None = ...
        ) -> ModuleSpec | None: ...

    class PathEntryFinder(Finder):
        def find_module(self, fullname: str) -> Loader | None: ...
        def find_loader(self, fullname: str) -> tuple[Loader | None, Sequence[str]]: ...
        def invalidate_caches(self) -> None: ...
        # Not defined on the actual class, but expected to exist.
        def find_spec(self, fullname: str, target: types.ModuleType | None = ...) -> ModuleSpec | None: ...

class FileLoader(ResourceLoader, ExecutionLoader, metaclass=ABCMeta):
    name: str
    path: str
    def __init__(self, fullname: str, path: str) -> None: ...
    def get_data(self, path: str) -> bytes: ...
    def get_filename(self, name: str | None = None) -> str: ...
    def load_module(self, name: str | None = None) -> types.ModuleType: ...

class ResourceReader(metaclass=ABCMeta):
    @abstractmethod
    def open_resource(self, resource: str) -> IO[bytes]: ...
    @abstractmethod
    def resource_path(self, resource: str) -> str: ...
    if sys.version_info >= (3, 10):
        @abstractmethod
        def is_resource(self, path: str) -> bool: ...
    else:
        @abstractmethod
        def is_resource(self, name: str) -> bool: ...

    @abstractmethod
    def contents(self) -> Iterator[str]: ...

if sys.version_info >= (3, 9):
    @runtime_checkable
    class Traversable(Protocol):
        @abstractmethod
        def is_dir(self) -> bool: ...
        @abstractmethod
        def is_file(self) -> bool: ...
        @abstractmethod
        def iterdir(self) -> Iterator[Traversable]: ...
        if sys.version_info >= (3, 11):
            @abstractmethod
            def joinpath(self, *descendants: str) -> Traversable: ...
        else:
            @abstractmethod
            def joinpath(self, __child: str) -> Traversable: ...

        # The documentation and runtime protocol allows *args, **kwargs arguments,
        # but this would mean that all implementers would have to support them,
        # which is not the case.
        @overload
        @abstractmethod
        def open(self, __mode: Literal["r", "w"] = "r", *, encoding: str | None = None, errors: str | None = None) -> IO[str]: ...
        @overload
        @abstractmethod
        def open(self, __mode: Literal["rb", "wb"]) -> IO[bytes]: ...
        @property
        @abstractmethod
        def name(self) -> str: ...
        if sys.version_info >= (3, 10):
            def __truediv__(self, __child: str) -> Traversable: ...
        else:
            @abstractmethod
            def __truediv__(self, __child: str) -> Traversable: ...

        @abstractmethod
        def read_bytes(self) -> bytes: ...
        @abstractmethod
        def read_text(self, encoding: str | None = None) -> str: ...

    class TraversableResources(ResourceReader):
        @abstractmethod
        def files(self) -> Traversable: ...
        def open_resource(self, resource: str) -> BufferedReader: ...
        def resource_path(self, resource: Any) -> str: ...
        def is_resource(self, path: str) -> bool: ...
        def contents(self) -> Iterator[str]: ...
