import importlib.abc
import types
from typing import Any, Callable, List, Optional, Sequence, Tuple, Union

# TODO: the loaders seem a bit backwards, attribute is protocol but __init__ arg isn't?
class ModuleSpec:
    def __init__(
        self,
        name: str,
        loader: importlib.abc.Loader | None,
        *,
        origin: str | None = ...,
        loader_state: Any = ...,
        is_package: bool | None = ...,
    ) -> None: ...
    name: str
    loader: importlib.abc._LoaderProtocol | None
    origin: str | None
    submodule_search_locations: List[str] | None
    loader_state: Any
    cached: str | None
    parent: str | None
    has_location: bool

class BuiltinImporter(importlib.abc.MetaPathFinder, importlib.abc.InspectLoader):
    # MetaPathFinder
    @classmethod
    def find_module(cls, fullname: str, path: Sequence[importlib.abc._Path] | None = ...) -> importlib.abc.Loader | None: ...
    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[importlib.abc._Path] | None = ..., target: types.ModuleType | None = ...
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
    @staticmethod
    def module_repr(module: types.ModuleType) -> str: ...
    @classmethod
    def create_module(cls, spec: ModuleSpec) -> types.ModuleType | None: ...
    @classmethod
    def exec_module(cls, module: types.ModuleType) -> None: ...

class FrozenImporter(importlib.abc.MetaPathFinder, importlib.abc.InspectLoader):
    # MetaPathFinder
    @classmethod
    def find_module(cls, fullname: str, path: Sequence[importlib.abc._Path] | None = ...) -> importlib.abc.Loader | None: ...
    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[importlib.abc._Path] | None = ..., target: types.ModuleType | None = ...
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
    @staticmethod
    def module_repr(m: types.ModuleType) -> str: ...
    @classmethod
    def create_module(cls, spec: ModuleSpec) -> types.ModuleType | None: ...
    @staticmethod
    def exec_module(module: types.ModuleType) -> None: ...

class WindowsRegistryFinder(importlib.abc.MetaPathFinder):
    @classmethod
    def find_module(cls, fullname: str, path: Sequence[importlib.abc._Path] | None = ...) -> importlib.abc.Loader | None: ...
    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[importlib.abc._Path] | None = ..., target: types.ModuleType | None = ...
    ) -> ModuleSpec | None: ...

class PathFinder:
    @classmethod
    def invalidate_caches(cls) -> None: ...
    @classmethod
    def find_spec(
        cls, fullname: str, path: Sequence[bytes | str] | None = ..., target: types.ModuleType | None = ...
    ) -> ModuleSpec | None: ...
    @classmethod
    def find_module(cls, fullname: str, path: Sequence[bytes | str] | None = ...) -> importlib.abc.Loader | None: ...

SOURCE_SUFFIXES: List[str]
DEBUG_BYTECODE_SUFFIXES: List[str]
OPTIMIZED_BYTECODE_SUFFIXES: List[str]
BYTECODE_SUFFIXES: List[str]
EXTENSION_SUFFIXES: List[str]

def all_suffixes() -> List[str]: ...

class FileFinder(importlib.abc.PathEntryFinder):
    path: str
    def __init__(self, path: str, *loader_details: Tuple[importlib.abc.Loader, List[str]]) -> None: ...
    @classmethod
    def path_hook(
        cls, *loader_details: Tuple[importlib.abc.Loader, List[str]]
    ) -> Callable[[str], importlib.abc.PathEntryFinder]: ...

class SourceFileLoader(importlib.abc.FileLoader, importlib.abc.SourceLoader):
    def set_data(self, path: importlib.abc._Path, data: bytes, *, _mode: int = ...) -> None: ...

class SourcelessFileLoader(importlib.abc.FileLoader, importlib.abc.SourceLoader): ...

class ExtensionFileLoader(importlib.abc.ExecutionLoader):
    def __init__(self, name: str, path: importlib.abc._Path) -> None: ...
    def get_filename(self, name: str | None = ...) -> importlib.abc._Path: ...
    def get_source(self, fullname: str) -> None: ...
