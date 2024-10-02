import types
from collections.abc import Sequence
from importlib import abc, machinery
from typing_extensions import Self

def _should_skip(loader: abc.Loader) -> bool: ...

class AtherisMetaPathFinder(abc.MetaPathFinder):
    def __init__(
        self, include_packages: set[str], exclude_modules: set[str], enable_loader_override: bool, trace_dataflow: bool
    ) -> None: ...
    def find_spec(
        self, fullname: str, path: Sequence[str] | None, target: types.ModuleType | None = None
    ) -> machinery.ModuleSpec | None: ...
    def invalidate_caches(self) -> None: ...

class AtherisSourceFileLoader:
    def __init__(self, name: str, path: str, trace_dataflow: bool) -> None: ...
    def get_code(self, fullname: str) -> types.CodeType | None: ...

class AtherisSourcelessFileLoader:
    def __init__(self, name: str, path: str, trace_dataflow: bool) -> None: ...
    def get_code(self, fullname: str) -> types.CodeType | None: ...

def make_dynamic_atheris_loader(loader: abc.Loader | type[abc.Loader], trace_dataflow: bool) -> abc.Loader: ...

class HookManager:
    def __init__(
        self, include_packages: set[str], exclude_modules: set[str], enable_loader_override: bool, trace_dataflow: bool
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...

def instrument_imports(
    include: Sequence[str] | None = None, exclude: Sequence[str] | None = None, enable_loader_override: bool = True
) -> HookManager: ...
