import importlib.abc
import importlib.machinery
import sys
import types
from _typeshed import ReadableBuffer, StrOrBytesPath
from _typeshed.importlib import LoaderProtocol
from collections.abc import Callable
from typing import Any, Final
from typing_extensions import ParamSpec

_P = ParamSpec("_P")

if sys.version_info < (3, 12):
    def module_for_loader(fxn: Callable[_P, types.ModuleType]) -> Callable[_P, types.ModuleType]: ...
    def set_loader(fxn: Callable[_P, types.ModuleType]) -> Callable[_P, types.ModuleType]: ...
    def set_package(fxn: Callable[_P, types.ModuleType]) -> Callable[_P, types.ModuleType]: ...

def resolve_name(name: str, package: str | None) -> str: ...

MAGIC_NUMBER: Final[bytes]

def cache_from_source(path: str, debug_override: bool | None = None, *, optimization: Any | None = None) -> str: ...
def source_from_cache(path: str) -> str: ...
def decode_source(source_bytes: ReadableBuffer) -> str: ...
def find_spec(name: str, package: str | None = None) -> importlib.machinery.ModuleSpec | None: ...
def spec_from_loader(
    name: str, loader: LoaderProtocol | None, *, origin: str | None = None, is_package: bool | None = None
) -> importlib.machinery.ModuleSpec | None: ...
def spec_from_file_location(
    name: str,
    location: StrOrBytesPath | None = None,
    *,
    loader: LoaderProtocol | None = None,
    submodule_search_locations: list[str] | None = ...,
) -> importlib.machinery.ModuleSpec | None: ...
def module_from_spec(spec: importlib.machinery.ModuleSpec) -> types.ModuleType: ...

class LazyLoader(importlib.abc.Loader):
    def __init__(self, loader: importlib.abc.Loader) -> None: ...
    @classmethod
    def factory(cls, loader: importlib.abc.Loader) -> Callable[..., LazyLoader]: ...
    def exec_module(self, module: types.ModuleType) -> None: ...

def source_hash(source_bytes: ReadableBuffer) -> bytes: ...
