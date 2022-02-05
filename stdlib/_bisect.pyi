import sys
from _typeshed import SupportsRichComparison
from typing import Callable, MutableSequence, Sequence, TypeVar, overload

_SupportsRichComparisonT = TypeVar("_SupportsRichComparisonT", bound=SupportsRichComparison)

if sys.version_info >= (3, 10):
    _KeyReturnT = TypeVar("_KeyReturnT", bound=SupportsRichComparison)

    @overload
    def bisect_left(a: Sequence[_SupportsRichComparisonT], x: _SupportsRichComparisonT, lo: int = ..., hi: int | None = ..., *, key: None = ...) -> int: ...
    @overload
    def bisect_left(
        a: Sequence[_SupportsRichComparisonT], x: _KeyReturnT, lo: int = ..., hi: int | None = ..., *, key: Callable[[_SupportsRichComparisonT], _KeyReturnT] = ...
    ) -> int: ...
    @overload
    def bisect_right(a: Sequence[_SupportsRichComparisonT], x: _SupportsRichComparisonT, lo: int = ..., hi: int | None = ..., *, key: None = ...) -> int: ...
    @overload
    def bisect_right(
        a: Sequence[_SupportsRichComparisonT], x: _KeyReturnT, lo: int = ..., hi: int | None = ..., *, key: Callable[[_SupportsRichComparisonT], _KeyReturnT] = ...
    ) -> int: ...
    def insort_left(
        a: MutableSequence[_SupportsRichComparisonT],
        x: _SupportsRichComparisonT,
        lo: int = ...,
        hi: int | None = ...,
        *,
        key: Callable[[_SupportsRichComparisonT], _KeyReturnT] | None = ...,
    ) -> None: ...
    def insort_right(
        a: MutableSequence[_SupportsRichComparisonT],
        x: _SupportsRichComparisonT,
        lo: int = ...,
        hi: int | None = ...,
        *,
        key: Callable[[_SupportsRichComparisonT], _KeyReturnT] | None = ...,
    ) -> None: ...

else:
    def bisect_left(a: Sequence[_SupportsRichComparisonT], x: _SupportsRichComparisonT, lo: int = ..., hi: int | None = ...) -> int: ...
    def bisect_right(a: Sequence[_SupportsRichComparisonT], x: _SupportsRichComparisonT, lo: int = ..., hi: int | None = ...) -> int: ...
    def insort_left(a: MutableSequence[_SupportsRichComparisonT], x: _SupportsRichComparisonT, lo: int = ..., hi: int | None = ...) -> None: ...
    def insort_right(a: MutableSequence[_SupportsRichComparisonT], x: _SupportsRichComparisonT, lo: int = ..., hi: int | None = ...) -> None: ...
