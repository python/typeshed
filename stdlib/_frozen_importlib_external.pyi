import _ast
import _io
import importlib.abc
import importlib.machinery
import sys
import types
from _typeshed import Incomplete, ReadableBuffer, StrOrBytesPath, StrPath
from _typeshed.importlib import LoaderProtocol
from collections.abc import Callable, Iterable, Iterator, Mapping, MutableSequence, Sequence
from importlib.machinery import ModuleSpec
from importlib.metadata import DistributionFinder, PathDistribution
from typing import Any, Literal
from typing_extensions import Self, deprecated

if sys.version_info >= (3, 10):
    import importlib.readers

path_separators: Incomplete
path_sep: Incomplete
path_sep_tuple: Incomplete

MAGIC_NUMBER: bytes

def cache_from_source(path: str, debug_override: bool | None = None, *, optimization: Any | None = None) -> str: ...
def source_from_cache(path: str) -> str: ...
def decode_source(source_bytes: ReadableBuffer) -> str: ...
def spec_from_file_location(
    name: str,
    location: StrOrBytesPath | None = None,
    *,
    loader: LoaderProtocol | None = None,
    submodule_search_locations: list[str] | None = ...,
) -> importlib.machinery.ModuleSpec | None: ...

class WindowsRegistryFinder(importlib.abc.MetaPathFinder):
    if sys.version_info < (3, 12):
        @classmethod
        def find_module(cls, fullname: str, path: Sequence[str] | None = None) -> importlib.abc.Loader | None: ...

    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[str] | None = None, target: types.ModuleType | None = None
    ) -> ModuleSpec | None: ...

class PathFinder(importlib.abc.MetaPathFinder):
    if sys.version_info >= (3, 10):
        @staticmethod
        def invalidate_caches() -> None: ...
    else:
        @classmethod
        def invalidate_caches(cls) -> None: ...
    if sys.version_info >= (3, 10):
        @staticmethod
        def find_distributions(context: DistributionFinder.Context = ...) -> Iterable[PathDistribution]: ...
    else:
        @classmethod
        def find_distributions(cls, context: DistributionFinder.Context = ...) -> Iterable[PathDistribution]: ...

    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[str] | None = None, target: types.ModuleType | None = None
    ) -> ModuleSpec | None: ...
    if sys.version_info < (3, 12):
        @classmethod
        def find_module(cls, fullname: str, path: Sequence[str] | None = None) -> importlib.abc.Loader | None: ...

SOURCE_SUFFIXES: list[str]
DEBUG_BYTECODE_SUFFIXES: list[str]
OPTIMIZED_BYTECODE_SUFFIXES: list[str]
BYTECODE_SUFFIXES: list[str]
EXTENSION_SUFFIXES: list[str]

class FileFinder(importlib.abc.PathEntryFinder):
    path: str
    def __init__(self, path: str, *loader_details: tuple[type[importlib.abc.Loader], list[str]]) -> None: ...
    @classmethod
    def path_hook(
        cls, *loader_details: tuple[type[importlib.abc.Loader], list[str]]
    ) -> Callable[[str], importlib.abc.PathEntryFinder]: ...

class _LoaderBasics:
    def is_package(self, fullname: str) -> bool: ...
    def create_module(self, spec: ModuleSpec) -> types.ModuleType | None: ...
    def exec_module(self, module: types.ModuleType) -> None: ...
    def load_module(self, fullname: str) -> types.ModuleType: ...

class SourceLoader(_LoaderBasics):
    def path_mtime(self, path: str) -> float: ...
    def set_data(self, path: str, data: bytes) -> None: ...
    def get_source(self, fullname: str) -> str | None: ...
    def path_stats(self, path: str) -> Mapping[str, Any]: ...
    def source_to_code(
        self, data: ReadableBuffer | str | _ast.Module | _ast.Expression | _ast.Interactive, path: ReadableBuffer | StrPath
    ) -> types.CodeType: ...
    def get_code(self, fullname: str) -> types.CodeType | None: ...

class FileLoader:
    name: str
    path: str
    def __init__(self, fullname: str, path: str) -> None: ...
    def get_data(self, path: str) -> bytes: ...
    def get_filename(self, fullname: str | None = None) -> str: ...
    def load_module(self, fullname: str | None = None) -> types.ModuleType: ...
    if sys.version_info >= (3, 10):
        def get_resource_reader(self, module: types.ModuleType) -> importlib.readers.FileReader: ...
    else:
        def get_resource_reader(self, module: types.ModuleType) -> Self | None: ...
        def open_resource(self, resource: str) -> _io.FileIO: ...
        def resource_path(self, resource: str) -> str: ...
        def is_resource(self, name: str) -> bool: ...
        def contents(self) -> Iterator[str]: ...

class SourceFileLoader(importlib.abc.FileLoader, FileLoader, importlib.abc.SourceLoader, SourceLoader):  # type: ignore[misc]  # incompatible method arguments in base classes
    def set_data(self, path: str, data: ReadableBuffer, *, _mode: int = 0o666) -> None: ...
    def path_stats(self, path: str) -> Mapping[str, Any]: ...

class SourcelessFileLoader(importlib.abc.FileLoader, FileLoader, _LoaderBasics):
    def get_code(self, fullname: str) -> types.CodeType | None: ...
    def get_source(self, fullname: str) -> None: ...

class ExtensionFileLoader(FileLoader, _LoaderBasics, importlib.abc.ExecutionLoader):
    def __init__(self, name: str, path: str) -> None: ...
    def get_filename(self, name: str | None = None) -> str: ...
    def get_source(self, fullname: str) -> None: ...
    def create_module(self, spec: ModuleSpec) -> types.ModuleType: ...
    def exec_module(self, module: types.ModuleType) -> None: ...
    def get_code(self, fullname: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

if sys.version_info >= (3, 11):
    class NamespaceLoader(importlib.abc.InspectLoader):
        def __init__(
            self, name: str, path: MutableSequence[str], path_finder: Callable[[str, tuple[str, ...]], ModuleSpec]
        ) -> None: ...
        def is_package(self, fullname: str) -> Literal[True]: ...
        def get_source(self, fullname: str) -> Literal[""]: ...
        def get_code(self, fullname: str) -> types.CodeType: ...
        def create_module(self, spec: ModuleSpec) -> None: ...
        def exec_module(self, module: types.ModuleType) -> None: ...
        @deprecated("load_module() is deprecated; use exec_module() instead")
        def load_module(self, fullname: str) -> types.ModuleType: ...
        def get_resource_reader(self, module: types.ModuleType) -> importlib.readers.NamespaceReader: ...
        if sys.version_info < (3, 12):
            @staticmethod
            @deprecated("module_repr() is deprecated, and has been removed in Python 3.12")
            def module_repr(module: types.ModuleType) -> str: ...

    _NamespaceLoader = NamespaceLoader
else:
    class _NamespaceLoader(importlib.abc.InspectLoader):
        def __init__(
            self, name: str, path: MutableSequence[str], path_finder: Callable[[str, tuple[str, ...]], ModuleSpec]
        ) -> None: ...
        def is_package(self, fullname: str) -> Literal[True]: ...
        def get_source(self, fullname: str) -> Literal[""]: ...
        def get_code(self, fullname: str) -> types.CodeType: ...
        def create_module(self, spec: ModuleSpec) -> None: ...
        def exec_module(self, module: types.ModuleType) -> None: ...
        @deprecated("load_module() is deprecated; use exec_module() instead")
        def load_module(self, fullname: str) -> types.ModuleType: ...
        @staticmethod
        @deprecated("module_repr() is deprecated, and has been removed in Python 3.12")
        def module_repr(module: types.ModuleType) -> str: ...

if sys.version_info >= (3, 13):
    class AppleFrameworkLoader(ExtensionFileLoader, importlib.abc.ExecutionLoader): ...
