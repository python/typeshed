from collections.abc import Callable, Hashable
from typing import Any, SupportsInt, TypeVar
from typing_extensions import TypeAlias

_T = TypeVar("_T")
_Reduce: TypeAlias = tuple[Callable[..., _T], tuple[Any, ...]] | tuple[Callable[..., _T], tuple[Any, ...], Any | None]

__all__ = ["add_extension", "clear_extension_cache", "constructor", "pickle", "remove_extension"]

def pickle(
    ob_type: type[_T],
    pickle_function: Callable[[_T], str | _Reduce[_T]],
    constructor_ob: Callable[[_Reduce[_T]], _T] | None = None,
) -> None: ...
def constructor(object: Callable[[_Reduce[_T]], _T]) -> None: ...
def add_extension(module: Hashable, name: Hashable, code: SupportsInt) -> None: ...
def remove_extension(module: Hashable, name: Hashable, code: int) -> None: ...
def clear_extension_cache() -> None: ...

_DispatchTableType: TypeAlias = dict[type, Callable[[Any], str | _Reduce[Any]]]  # imported by multiprocessing.reduction
dispatch_table: _DispatchTableType  # undocumented
