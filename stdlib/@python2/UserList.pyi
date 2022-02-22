from _typeshed import Self
from typing import Iterable, MutableSequence, TypeVar, overload

_T = TypeVar("_T")

class UserList(MutableSequence[_T]):
    data: list[_T]
    def insert(self, index: int, object: _T) -> None: ...
    @overload
    def __setitem__(self, i: int, o: _T) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None: ...
    def __delitem__(self, i: int | slice) -> None: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, i: int) -> _T: ...
    @overload
    def __getitem__(self: Self, s: slice) -> Self: ...
    def sort(self) -> None: ...
