import types
from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Mapping

__all__ = ["attach", "_lazy_import"]

def attach(
    module_name: str, submodules: Iterable[str] | None = None, submod_attrs: Mapping[str, Iterable[str]] | None = None
) -> tuple[Callable[[str], Incomplete], Callable[[], list[str]], list[str]]: ...

class DelayedImportErrorModule(types.ModuleType):
    def __init__(self, frame_data, *args, **kwargs) -> None: ...
    def __getattr__(self, x) -> None: ...

def _lazy_import(fullname: str) -> types.ModuleType | DelayedImportErrorModule: ...
