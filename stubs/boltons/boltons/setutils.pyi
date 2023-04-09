from collections.abc import Generator, Iterable, Iterator, MutableSet
from itertools import islice
from typing import Any
from typing_extensions import Self

class IndexedSet(MutableSet[Any]):
    item_index_map: dict[Any, Any]
    item_list: list[Any]
    dead_indices: list[int]
    def __init__(self, other: Iterable[Any] | None = ...) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, item: Any) -> bool: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __reversed__(self) -> Generator[Any, None, None]: ...
    @classmethod
    def from_iterable(cls, it: Iterable[Any]) -> set[Any]: ...
    def add(self, item: Any) -> None: ...
    def remove(self, item: Any) -> None: ...
    def discard(self, item: Any) -> None: ...
    def clear(self) -> None: ...
    def isdisjoint(self, other: Iterable[Any]) -> bool: ...
    def issubset(self, other: Iterable[Any]) -> bool: ...
    def issuperset(self, other: Iterable[Any]) -> bool: ...
    def union(self, *others: Iterable[Any]) -> set[Any]: ...
    def iter_intersection(self, *others: Iterable[Any]) -> Generator[Any, None, None]: ...
    def intersection(self, *others: Iterable[Any]) -> set[Any]: ...
    def iter_difference(self, *others: Iterable[Any]) -> Generator[Any, None, None]: ...
    def difference(self, *others: Iterable[Any]) -> Any: ...
    def symmetric_difference(self, *others: Iterable[Any]) -> set[Any]: ...
    # __or__ = union
    __ror__ = union
    # __and__ = intersection
    __rand__ = intersection
    # __sub__ = difference
    # __xor__ = symmetric_difference
    __rxor__ = symmetric_difference
    def __rsub__(self, other: Iterable[Any]) -> Any: ...
    def update(self, *others: Iterable[Any]) -> None: ...
    def intersection_update(self, *others: Iterable[Any]) -> None: ...
    def difference_update(self, *others: Iterable[Any]) -> None: ...
    def symmetric_difference_update(self, other: Iterable[Any]) -> None: ...
    def iter_slice(self, start: int, stop: int, step: int | None = ...) -> islice[Iterable[Any]]: ...
    def __getitem__(self, index: int) -> Any: ...
    def pop(self, index: int | None = ...) -> Any: ...
    def count(self, val: Any) -> int: ...
    def reverse(self) -> None: ...
    def sort(self, **kwargs) -> None: ...
    def index(self, val: Any) -> int: ...

def complement(wrapped: set[Any]) -> set[Any]: ...

class _ComplementSet:
    def __init__(self, included: set[Any] | None = ..., excluded: set[Any] | None = ...) -> None: ...
    def complemented(self) -> set[Any]: ...
    __invert__ = complemented
    def complement(self) -> None: ...
    def __contains__(self, item: Any) -> bool: ...
    def add(self, item: Any) -> None: ...
    def remove(self, item: Any) -> None: ...
    def pop(self) -> Any: ...
    def intersection(self, other: set[Any]) -> set[Any]: ...
    def __and__(self, other: set[Any]) -> set[Any]: ...
    __rand__ = __and__
    def __iand__(self, other: set[Any]) -> Self: ...
    def union(self, other: set[Any]) -> set[Any]: ...
    def __or__(self, other: set[Any]) -> set[Any]: ...
    __ror__ = __or__
    def __ior__(self, other: set[Any]) -> Self: ...
    def update(self, items: Iterable[Any]) -> None: ...
    def discard(self, items: Iterable[Any]) -> None: ...
    def symmetric_difference(self, other: set[Any]) -> set[Any]: ...
    def __xor__(self, other: set[Any]) -> set[Any]: ...
    __rxor__ = __xor__
    def symmetric_difference_update(self, other: set[Any]) -> None: ...
    def isdisjoint(self, other: set[Any]) -> bool: ...
    def issubset(self, other: set[Any]) -> bool: ...
    def __le__(self, other: set[Any]) -> bool: ...
    def __lt__(self, other: set[Any]) -> bool: ...
    def issuperset(self, other: set[Any]) -> bool: ...
    def __ge__(self, other: set[Any]) -> bool: ...
    def __gt__(self, other: set[Any]) -> bool: ...
    def difference(self, other: set[Any]) -> set[Any]: ...
    def __sub__(self, other: set[Any]) -> set[Any]: ...
    def __rsub__(self, other: set[Any]) -> set[Any]: ...
    def difference_update(self, other: set[Any]) -> None: ...
    def __isub__(self, other: set[Any]) -> Self: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __bool__(self) -> bool: ...
