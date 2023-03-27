import sys
from array import array
from collections import deque
from collections.abc import Callable
from typing import Any, TypeVar
from typing_extensions import TypeAlias

__all__ = ["Repr", "repr", "recursive_repr"]

_T = TypeVar("_T")
_ReprFunc: TypeAlias = Callable[[_T], str]

def recursive_repr(fillvalue: str = "...") -> Callable[[_ReprFunc], _ReprFunc]: ...

class Repr:
    maxlevel: int
    maxdict: int
    maxlist: int
    maxtuple: int
    maxset: int
    maxfrozenset: int
    maxdeque: int
    maxarray: int
    maxlong: int
    maxstring: int
    maxother: int
    if sys.version_info >= (3, 11):
        fillvalue: str
    if sys.version_info >= (3, 12):
        indent: str | int | None

    if sys.version_info >= (3, 12):
        def __init__(
            self,
            *,
            maxlevel: int = ...,
            maxtuple: int = ...,
            maxlist: int = ...,
            maxarray: int = ...,
            maxdict: int = ...,
            maxset: int = ...,
            maxfrozenset: int = ...,
            maxdeque: int = ...,
            maxstring: int = ...,
            maxlong: int = ...,
            maxother: int = ...,
            fillvalue: str = ...,
            indent: str | int | None = ...,
        ) -> None: ...
    else:
        def __init__(self) -> None: ...

    def repr(self, x: Any) -> str: ...
    def repr1(self, x: Any, level: int) -> str: ...
    def repr_tuple(self, x: tuple[Any, ...], level: int) -> str: ...
    def repr_list(self, x: list[Any], level: int) -> str: ...
    def repr_array(self, x: array[Any], level: int) -> str: ...
    def repr_set(self, x: set[Any], level: int) -> str: ...
    def repr_frozenset(self, x: frozenset[Any], level: int) -> str: ...
    def repr_deque(self, x: deque[Any], level: int) -> str: ...
    def repr_dict(self, x: dict[Any, Any], level: int) -> str: ...
    def repr_str(self, x: str, level: int) -> str: ...
    def repr_int(self, x: int, level: int) -> str: ...
    def repr_instance(self, x: Any, level: int) -> str: ...

aRepr: Repr

def repr(x: object) -> str: ...
