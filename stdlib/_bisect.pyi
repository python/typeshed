import sys
from _typeshed import SupportsDunderLT, SupportsLenAndGetItem
from collections.abc import Callable, MutableSequence
from typing import TypeVar, overload

_T = TypeVar("_T")
_U = TypeVar("_U")

if sys.version_info >= (3, 10):
    @overload
    def bisect_left(
        # Valid comparison: a[i] < x
        a: SupportsLenAndGetItem[SupportsDunderLT[_T]],
        x: _T,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> int: ...
    @overload
    def bisect_left(
        # Valid comparison: key(a[i]) < x
        a: SupportsLenAndGetItem[_T],
        x: _U,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: Callable[[_T], SupportsDunderLT[_U]],
    ) -> int: ...
    @overload
    def bisect_right(
        # Valid comparison: x < a[i]
        a: SupportsLenAndGetItem[_T],
        x: SupportsDunderLT[_T],
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> int: ...
    @overload
    def bisect_right(
        # Valid comparison: x < key(a[i])
        a: SupportsLenAndGetItem[_T],
        x: SupportsDunderLT[_U],
        lo: int = 0,
        hi: int | None = None,
        *,
        key: Callable[[_T], _U],
    ) -> int: ...
    @overload
    def insort_left(
        # Valid comparison: a[i] < x
        a: MutableSequence[SupportsDunderLT[_T]],
        x: _T,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> None: ...
    @overload
    def insort_left(
        # Valid comparison: key(a[i]) < x
        a: MutableSequence[_T],
        x: _U,
        lo: int = 0,
        hi: int | None = None,
        *,
        key: Callable[[_U], SupportsDunderLT[_T]],
    ) -> None: ...
    @overload
    def insort_right(
        # Valid comparison: x < a[i]
        a: MutableSequence[_T],
        x: SupportsDunderLT[_T],
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> None: ...
    @overload
    def insort_right(
        # Valid comparison: x < key(a[i])
        a: MutableSequence[_T],
        x: SupportsDunderLT[_U],
        lo: int = 0,
        hi: int | None = None,
        *,
        key: Callable[[_T], _U],
    ) -> None: ...

else:
    def bisect_left(
        # Valid comparison: a[i] < x
        a: SupportsLenAndGetItem[SupportsDunderLT[_T]],
        x: _T,
        lo: int = 0,
        hi: int | None = None,
    ) -> int: ...
    def bisect_right(
        # Valid comparison: x < a[i]
        a: SupportsLenAndGetItem[_T],
        x: SupportsDunderLT[_T],
        lo: int = 0,
        hi: int | None = None,
    ) -> int: ...
    def insort_left(
        # Valid comparison: a[i] < x
        a: MutableSequence[SupportsDunderLT[_T]],
        x: _T,
        lo: int = 0,
        hi: int | None = None,
    ) -> None: ...
    def insort_right(
        # Valid comparison: x < a[i]
        a: MutableSequence[_T],
        x: SupportsDunderLT[_T],
        lo: int = 0,
        hi: int | None = None,
        *,
        key: None = None,
    ) -> None: ...
