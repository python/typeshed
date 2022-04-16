from array import array
from collections import deque
from typing import Any, Callable
from typing_extensions import TypeAlias

__all__ = ["Repr", "repr", "recursive_repr"]

_ReprFunc: TypeAlias = Callable[[Any], str]

def recursive_repr(fillvalue: str = ...) -> Callable[[_ReprFunc], _ReprFunc]: ...

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
