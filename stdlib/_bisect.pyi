import sys
from _typeshed import SupportsRichComparison
from typing import Callable, MutableSequence, Sequence, TypeVar, overload

_ElemT = TypeVar("_ElemT", bound=SupportsRichComparison)

if sys.version_info >= (3, 10):
    _KeyReturnT = TypeVar("_KeyReturnT", bound=SupportsRichComparison)

    @overload
    def bisect_left(a: Sequence[_ElemT], x: _ElemT, lo: int = ..., hi: int | None = ..., *, key: None = ...) -> int: ...
    @overload
    def bisect_left(
        a: Sequence[_ElemT], x: _KeyReturnT, lo: int = ..., hi: int | None = ..., *, key: Callable[[_ElemT], _KeyReturnT] = ...
    ) -> int: ...
    @overload
    def bisect_right(a: Sequence[_ElemT], x: _ElemT, lo: int = ..., hi: int | None = ..., *, key: None = ...) -> int: ...
    @overload
    def bisect_right(
        a: Sequence[_ElemT], x: _KeyReturnT, lo: int = ..., hi: int | None = ..., *, key: Callable[[_ElemT], _KeyReturnT] = ...
    ) -> int: ...
    def insort_left(
        a: MutableSequence[_ElemT],
        x: _ElemT,
        lo: int = ...,
        hi: int | None = ...,
        *,
        key: Callable[[_ElemT], _KeyReturnT] | None = ...,
    ) -> None: ...
    def insort_right(
        a: MutableSequence[_ElemT],
        x: _ElemT,
        lo: int = ...,
        hi: int | None = ...,
        *,
        key: Callable[[_ElemT], _KeyReturnT] | None = ...,
    ) -> None: ...

else:
    def bisect_left(a: Sequence[_ElemT], x: _ElemT, lo: int = ..., hi: int | None = ...) -> int: ...
    def bisect_right(a: Sequence[_ElemT], x: _ElemT, lo: int = ..., hi: int | None = ...) -> int: ...
    def insort_left(a: MutableSequence[_ElemT], x: _ElemT, lo: int = ..., hi: int | None = ...) -> None: ...
    def insort_right(a: MutableSequence[_ElemT], x: _ElemT, lo: int = ..., hi: int | None = ...) -> None: ...
