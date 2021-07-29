import sys
import types
from _typeshed import (
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
    StrOrBytesPath,
    StrPath,
)
from abc import ABCMeta, abstractmethod
from importlib.machinery import ModuleSpec
from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOWrapper
from typing import IO, Any, BinaryIO, Generator, Iterator, Mapping, Optional, Protocol, Sequence, Tuple, TypeVar, Union, overload
from typing_extensions import Literal, runtime_checkable

_Path = Union[bytes, str]

class Finder(metaclass=ABCMeta): ...

class ResourceLoader(Loader):
    @abstractmethod
    def get_data(self, path: _Path) -> bytes: ...

class InspectLoader(Loader):
    def is_package(self, fullname: str) -> bool: ...
    def get_code(self, fullname: str) -> Optional[types.CodeType]: ...
    def load_module(self, fullname: str) -> types.ModuleType: ...
    @abstractmethod
    def get_source(self, fullname: str) -> Optional[str]: ...
    def exec_module(self, module: types.ModuleType) -> None: ...
    @staticmethod
    def source_to_code(data: Union[bytes, str], path: str = ...) -> types.CodeType: ...

class ExecutionLoader(InspectLoader):
    @abstractmethod
    def get_filename(self, fullname: str) -> _Path: ...
    def get_code(self, fullname: str) -> Optional[types.CodeType]: ...

class SourceLoader(ResourceLoader, ExecutionLoader, metaclass=ABCMeta):
    def path_mtime(self, path: _Path) -> float: ...
    def set_data(self, path: _Path, data: bytes) -> None: ...
    def get_source(self, fullname: str) -> Optional[str]: ...
    def path_stats(self, path: _Path) -> Mapping[str, Any]: ...

# Please keep in sync with sys._MetaPathFinder
class MetaPathFinder(Finder):
    def find_module(self, fullname: str, path: Optional[Sequence[_Path]]) -> Optional[Loader]: ...
    def invalidate_caches(self) -> None: ...
    # Not defined on the actual class, but expected to exist.
    def find_spec(
        self, fullname: str, path: Optional[Sequence[_Path]], target: Optional[types.ModuleType] = ...
    ) -> Optional[ModuleSpec]: ...

class PathEntryFinder(Finder):
    def find_module(self, fullname: str) -> Optional[Loader]: ...
    def find_loader(self, fullname: str) -> Tuple[Optional[Loader], Sequence[_Path]]: ...
    def invalidate_caches(self) -> None: ...
    # Not defined on the actual class, but expected to exist.
    def find_spec(self, fullname: str, target: Optional[types.ModuleType] = ...) -> Optional[ModuleSpec]: ...

class Loader(metaclass=ABCMeta):
    def load_module(self, fullname: str) -> types.ModuleType: ...
    def module_repr(self, module: types.ModuleType) -> str: ...
    def create_module(self, spec: ModuleSpec) -> Optional[types.ModuleType]: ...
    # Not defined on the actual class for backwards-compatibility reasons,
    # but expected in new code.
    def exec_module(self, module: types.ModuleType) -> None: ...

class _LoaderProtocol(Protocol):
    def load_module(self, fullname: str) -> types.ModuleType: ...

class FileLoader(ResourceLoader, ExecutionLoader, metaclass=ABCMeta):
    name: str
    path: _Path
    def __init__(self, fullname: str, path: _Path) -> None: ...
    def get_data(self, path: _Path) -> bytes: ...
    def get_filename(self, name: Optional[str] = ...) -> _Path: ...
    def load_module(self, name: Optional[str] = ...) -> types.ModuleType: ...

if sys.version_info >= (3, 7):
    class ResourceReader(metaclass=ABCMeta):
        @abstractmethod
        def open_resource(self, resource: StrOrBytesPath) -> IO[bytes]: ...
        @abstractmethod
        def resource_path(self, resource: StrOrBytesPath) -> str: ...
        @abstractmethod
        def is_resource(self, name: str) -> bool: ...
        @abstractmethod
        def contents(self) -> Iterator[str]: ...

if sys.version_info >= (3, 9):
    _P = TypeVar("_P", bound=Traversable)
    @runtime_checkable
    class Traversable(Protocol):
        @abstractmethod
        def is_dir(self) -> bool: ...
        @abstractmethod
        def is_file(self) -> bool: ...
        @abstractmethod
        def iterdir(self: _P) -> Generator[_P, None, None]: ...
        @overload
        @abstractmethod
        def joinpath(self: _P, child: StrPath) -> _P: ...
        @overload
        @abstractmethod
        def joinpath(self: _P, *other: StrPath) -> _P: ...
        # Adapted from builtins.open
        # Text mode: always returns a TextIOWrapper
        @overload
        @abstractmethod
        def open(
            self,
            mode: OpenTextMode = ...,
            buffering: int = ...,
            encoding: Optional[str] = ...,
            errors: Optional[str] = ...,
            newline: Optional[str] = ...,
        ) -> TextIOWrapper: ...
        # Unbuffered binary mode: returns a FileIO
        @overload
        @abstractmethod
        def open(
            self, mode: OpenBinaryMode, buffering: Literal[0], encoding: None = ..., errors: None = ..., newline: None = ...
        ) -> FileIO: ...
        # Buffering is on: return BufferedRandom, BufferedReader, or BufferedWriter
        @overload
        @abstractmethod
        def open(
            self,
            mode: OpenBinaryModeUpdating,
            buffering: Literal[-1, 1] = ...,
            encoding: None = ...,
            errors: None = ...,
            newline: None = ...,
        ) -> BufferedRandom: ...
        @overload
        @abstractmethod
        def open(
            self,
            mode: OpenBinaryModeWriting,
            buffering: Literal[-1, 1] = ...,
            encoding: None = ...,
            errors: None = ...,
            newline: None = ...,
        ) -> BufferedWriter: ...
        @overload
        @abstractmethod
        def open(
            self,
            mode: OpenBinaryModeReading,
            buffering: Literal[-1, 1] = ...,
            encoding: None = ...,
            errors: None = ...,
            newline: None = ...,
        ) -> BufferedReader: ...
        # Buffering cannot be determined: fall back to BinaryIO
        @overload
        @abstractmethod
        def open(
            self, mode: OpenBinaryMode, buffering: int, encoding: None = ..., errors: None = ..., newline: None = ...
        ) -> BinaryIO: ...
        # Fallback if mode is not specified
        @overload
        @abstractmethod
        def open(
            self,
            mode: str,
            buffering: int = ...,
            encoding: Optional[str] = ...,
            errors: Optional[str] = ...,
            newline: Optional[str] = ...,
        ) -> IO[Any]: ...
        name: str
        @abstractmethod
        def __truediv__(self: _P, key: StrPath) -> _P: ...
        @abstractmethod
        def read_bytes(self) -> bytes: ...
        @overload
        @abstractmethod
        def read_text(self, encoding: Optional[str] = ...) -> str: ...
        @overload
        @abstractmethod
        def read_text(self, encoding: Optional[str] = ..., errors: Optional[str] = ...) -> str: ...
