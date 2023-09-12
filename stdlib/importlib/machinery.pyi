import importlib.abc
import sys
import types
from _typeshed import ReadableBuffer
from collections.abc import Callable, Iterable, Sequence
from typing import Any

if sys.version_info >= (3, 8):
    from importlib.metadata import DistributionFinder, PathDistribution

class ModuleSpec:
    def __init__(
        self,
        name: str,
        loader: importlib.abc.Loader | None,
        *,
        origin: str | None = None,
        loader_state: Any = None,
        is_package: bool | None = None,
    ) -> None: ...
    name: str
    loader: importlib.abc.Loader | None
    origin: str | None
    submodule_search_locations: list[str] | None
    loader_state: Any
    cached: str | None
    @property
    def parent(self) -> str | None: ...
    has_location: bool
    def __eq__(self, other: object) -> bool: ...

class BuiltinImporter(importlib.abc.MetaPathFinder, importlib.abc.InspectLoader):
    # MetaPathFinder
    if sys.version_info < (3, 12):
        @classmethod
        def find_module(cls, fullname: str, path: Sequence[str] | None = None) -> importlib.abc.Loader | None: ...

    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[str] | None = None, target: types.ModuleType | None = None
    ) -> ModuleSpec | None: ...
    # InspectLoader
    @classmethod
    def is_package(cls, fullname: str) -> bool: ...
    @classmethod
    def load_module(cls, fullname: str) -> types.ModuleType: ...
    @classmethod
    def get_code(cls, fullname: str) -> None: ...
    @classmethod
    def get_source(cls, fullname: str) -> None: ...
    # Loader
    if sys.version_info < (3, 12):
        @staticmethod
        def module_repr(module: types.ModuleType) -> str: ...
    if sys.version_info >= (3, 10):
        @staticmethod
        def create_module(spec: ModuleSpec) -> types.ModuleType | None: ...
        @staticmethod
        def exec_module(module: types.ModuleType) -> None: ...
    else:
        @classmethod
        def create_module(cls, spec: ModuleSpec) -> types.ModuleType | None: ...
        @classmethod
        def exec_module(cls, module: types.ModuleType) -> None: ...

class FrozenImporter(importlib.abc.MetaPathFinder, importlib.abc.InspectLoader):
    # MetaPathFinder
    if sys.version_info < (3, 12):
        @classmethod
        def find_module(cls, fullname: str, path: Sequence[str] | None = None) -> importlib.abc.Loader | None: ...

    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[str] | None = None, target: types.ModuleType | None = None
    ) -> ModuleSpec | None: ...
    # InspectLoader
    @classmethod
    def is_package(cls, fullname: str) -> bool: ...
    @classmethod
    def load_module(cls, fullname: str) -> types.ModuleType: ...
    @classmethod
    def get_code(cls, fullname: str) -> None: ...
    @classmethod
    def get_source(cls, fullname: str) -> None: ...
    # Loader
    if sys.version_info < (3, 12):
        @staticmethod
        def module_repr(m: types.ModuleType) -> str: ...
    if sys.version_info >= (3, 10):
        @staticmethod
        def create_module(spec: ModuleSpec) -> types.ModuleType | None: ...
    else:
        @classmethod
        def create_module(cls, spec: ModuleSpec) -> types.ModuleType | None: ...

    @staticmethod
    def exec_module(module: types.ModuleType) -> None: ...

class WindowsRegistryFinder(importlib.abc.MetaPathFinder):
    if sys.version_info < (3, 12):
        @classmethod
        def find_module(cls, fullname: str, path: Sequence[str] | None = None) -> importlib.abc.Loader | None: ...

    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[str] | None = None, target: types.ModuleType | None = None
    ) -> ModuleSpec | None: ...

class PathFinder:
    if sys.version_info >= (3, 10):
        @staticmethod
        def invalidate_caches() -> None: ...
    else:
        @classmethod
        def invalidate_caches(cls) -> None: ...
    if sys.version_info >= (3, 10):
        @staticmethod
        def find_distributions(context: DistributionFinder.Context = ...) -> Iterable[PathDistribution]: ...
    elif sys.version_info >= (3, 8):
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

def all_suffixes() -> list[str]: ...

class FileFinder(importlib.abc.PathEntryFinder):
    path: str
    def __init__(self, path: str, *loader_details: tuple[type[importlib.abc.Loader], list[str]]) -> None: ...
    @classmethod
    def path_hook(
        cls, *loader_details: tuple[type[importlib.abc.Loader], list[str]]
    ) -> Callable[[str], importlib.abc.PathEntryFinder]: ...

class SourceFileLoader(importlib.abc.FileLoader, importlib.abc.SourceLoader):
    def set_data(self, path: str, data: ReadableBuffer, *, _mode: int = 0o666) -> None: ...

class SourcelessFileLoader(importlib.abc.FileLoader, importlib.abc.SourceLoader): ...

class ExtensionFileLoader(importlib.abc.ExecutionLoader):
    def __init__(self, name: str, path: str) -> None: ...
    def get_filename(self, name: str | None = None) -> str: ...
    def get_source(self, fullname: str) -> None: ...
    def create_module(self, spec: ModuleSpec) -> types.ModuleType: ...
    def exec_module(self, module: types.ModuleType) -> None: ...
    def get_code(self, fullname: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
