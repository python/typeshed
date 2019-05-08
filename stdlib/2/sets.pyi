# Stubs for sets (Python 2)
from typing import Any, Callable, Hashable, Iterable, Iterator, MutableMapping, Optional, TypeVar, Union

_T = TypeVar('_T')
_Setlike = Union[BaseSet[_T], Iterable[_T]]
_S = TypeVar('_S', bound=BaseSet)

class BaseSet(Iterable[_T]):
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __cmp__(self, other: Any) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def copy(self: _S) -> _S: ...
    def __copy__(self: _S) -> _S: ...
    def __deepcopy__(self: _S, memo: MutableMapping[int, BaseSet[_T]]) -> _S: ...
    def __or__(self: _S, other: BaseSet[_T]) -> _S: ...
    def union(self: _S, other: _Setlike) -> _S: ...
    def __and__(self: _S, other: BaseSet[_T]) -> _S: ...
    def intersection(self: _S, other: _Setlike) -> _S: ...
    def __xor__(self: _S, other: BaseSet[_T]) -> _S: ...
    def symmetric_difference(self: _S, other: _Setlike) -> _S: ...
    def __sub__(self: _S, other: BaseSet[_T]) -> _S: ...
    def difference(self: _S, other: _Setlike) -> _S: ...
    def __contains__(self, element: Any) -> bool: ...
    def issubset(self, other: BaseSet[_T]) -> bool: ...
    def issuperset(self, other: BaseSet[_T]) -> bool: ...
    def __le__(self, other: BaseSet[_T]) -> bool: ...
    def __ge__(self, other: BaseSet[_T]) -> bool: ...
    def __lt__(self, other: BaseSet[_T]) -> bool: ...
    def __gt__(self, other: BaseSet[_T]) -> bool: ...

class ImmutableSet(BaseSet[_T], Hashable):
    def __init__(self, iterable: Optional[_Setlike] = ...) -> None: ...
    def __hash__(self) -> int: ...

class Set(BaseSet[_T]):
    def __init__(self, iterable: Optional[_Setlike] = ...) -> None: ...
    def __ior__(self, other: BaseSet[_T]) -> Set: ...
    def union_update(self, other: _Setlike) -> None: ...
    def __iand__(self, other: BaseSet[_T]) -> Set: ...
    def intersection_update(self, other: _Setlike) -> None: ...
    def __ixor__(self, other: BaseSet[_T]) -> Set: ...
    def symmetric_difference_update(self, other: _Setlike) -> None: ...
    def __isub__(self, other: BaseSet[_T]) -> Set: ...
    def difference_update(self, other: _Setlike) -> None: ...
    def update(self, iterable: _Setlike) -> None: ...
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
