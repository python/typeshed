from typing import Any, Callable, Hashable, SupportsInt, TypeVar, Union
from typing_extensions import TypeAlias

_T = TypeVar("_T")
_Reduce: TypeAlias = Union[tuple[Callable[..., _T], tuple[Any, ...]], tuple[Callable[..., _T], tuple[Any, ...], Any | None]]

__all__ = ["pickle", "constructor", "add_extension", "remove_extension", "clear_extension_cache"]

def pickle(
    ob_type: type[_T],
    pickle_function: Callable[[_T], str | _Reduce[_T]],
    constructor_ob: Callable[[_Reduce[_T]], _T] | None = ...,
) -> None: ...
def constructor(object: Callable[[_Reduce[_T]], _T]) -> None: ...
def add_extension(module: Hashable, name: Hashable, code: SupportsInt) -> None: ...
def remove_extension(module: Hashable, name: Hashable, code: int) -> None: ...
def clear_extension_cache() -> None: ...

_DispatchTableType: TypeAlias = dict[type, Callable[[Any], str | _Reduce[Any]]]  # imported by multiprocessing.reduction
dispatch_table: _DispatchTableType  # undocumented
