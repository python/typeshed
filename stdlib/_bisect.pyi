import sys
from _typeshed import SupportsLessThan
from typing import Callable, MutableSequence, Optional, Sequence, TypeVar

_T = TypeVar("_T")

if sys.version_info >= (3, 10):
    def bisect_left(
        a: Sequence[_T], x: _T, lo: int = ..., hi: int | None = ..., *, key: Callable[[_T], SupportsLessThan] | None = ...
    ) -> int: ...
    def bisect_right(
        a: Sequence[_T], x: _T, lo: int = ..., hi: int | None = ..., *, key: Callable[[_T], SupportsLessThan] | None = ...
    ) -> int: ...
    def insort_left(
        a: MutableSequence[_T],
        x: _T,
        lo: int = ...,
        hi: int | None = ...,
        *,
        key: Callable[[_T], SupportsLessThan] | None = ...,
    ) -> None: ...
    def insort_right(
        a: MutableSequence[_T],
        x: _T,
        lo: int = ...,
        hi: int | None = ...,
        *,
        key: Callable[[_T], SupportsLessThan] | None = ...,
    ) -> None: ...

else:
    def bisect_left(a: Sequence[_T], x: _T, lo: int = ..., hi: int | None = ...) -> int: ...
    def bisect_right(a: Sequence[_T], x: _T, lo: int = ..., hi: int | None = ...) -> int: ...
    def insort_left(a: MutableSequence[_T], x: _T, lo: int = ..., hi: int | None = ...) -> None: ...
    def insort_right(a: MutableSequence[_T], x: _T, lo: int = ..., hi: int | None = ...) -> None: ...
