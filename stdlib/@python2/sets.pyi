from _typeshed import Self
from typing import Any, Hashable, Iterable, Iterator, MutableMapping, TypeVar, Union

_T = TypeVar("_T")
_Setlike = Union[BaseSet[_T], Iterable[_T]]

class BaseSet(Iterable[_T]):
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __cmp__(self, other: Any) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def copy(self: Self) -> Self: ...
    def __copy__(self: Self) -> Self: ...
    def __deepcopy__(self: Self, memo: MutableMapping[int, BaseSet[_T]]) -> Self: ...
    def __or__(self: Self, other: BaseSet[_T]) -> Self: ...
    def union(self: Self, other: _Setlike[_T]) -> Self: ...
    def __and__(self: Self, other: BaseSet[_T]) -> Self: ...
    def intersection(self: Self, other: _Setlike[Any]) -> Self: ...
    def __xor__(self: Self, other: BaseSet[_T]) -> Self: ...
    def symmetric_difference(self: Self, other: _Setlike[_T]) -> Self: ...
    def __sub__(self: Self, other: BaseSet[_T]) -> Self: ...
    def difference(self: Self, other: _Setlike[Any]) -> Self: ...
    def __contains__(self, element: Any) -> bool: ...
    def issubset(self, other: BaseSet[_T]) -> bool: ...
    def issuperset(self, other: BaseSet[_T]) -> bool: ...
    def __le__(self, other: BaseSet[_T]) -> bool: ...
    def __ge__(self, other: BaseSet[_T]) -> bool: ...
    def __lt__(self, other: BaseSet[_T]) -> bool: ...
    def __gt__(self, other: BaseSet[_T]) -> bool: ...

class ImmutableSet(BaseSet[_T], Hashable):
    def __init__(self, iterable: _Setlike[_T] | None = ...) -> None: ...
    def __hash__(self) -> int: ...

class Set(BaseSet[_T]):
    def __init__(self, iterable: _Setlike[_T] | None = ...) -> None: ...
    def __ior__(self: Self, other: BaseSet[_T]) -> Self: ...
    def union_update(self, other: _Setlike[_T]) -> None: ...
    def __iand__(self: Self, other: BaseSet[_T]) -> Self: ...
    def intersection_update(self, other: _Setlike[Any]) -> None: ...
    def __ixor__(self: Self, other: BaseSet[_T]) -> Self: ...
    def symmetric_difference_update(self, other: _Setlike[_T]) -> None: ...
    def __isub__(self: Self, other: BaseSet[_T]) -> Self: ...
    def difference_update(self, other: _Setlike[Any]) -> None: ...
    def update(self, iterable: _Setlike[_T]) -> None: ...
    def clear(self) -> None: ...
    def add(self, element: _T) -> None: ...
    def remove(self, element: _T) -> None: ...
    def discard(self, element: _T) -> None: ...
    def pop(self) -> _T: ...
    def __as_immutable__(self) -> ImmutableSet[_T]: ...
    def __as_temporarily_immutable__(self) -> _TemporarilyImmutableSet[_T]: ...

class _TemporarilyImmutableSet(BaseSet[_T]):
    def __init__(self, set: BaseSet[_T]) -> None: ...
    def __hash__(self) -> int: ...
