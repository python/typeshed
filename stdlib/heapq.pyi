from _heapq import *
from _typeshed import SupportsRichComparison
from typing import Any, Callable, Iterable, TypeVar

_T = TypeVar("_T")

def merge(*iterables: Iterable[_T], key: Callable[[_T], Any] | None = ..., reverse: bool = ...) -> Iterable[_T]: ...
def nlargest(n: int, iterable: Iterable[_T], key: Callable[[_T], SupportsRichComparison] | None = ...) -> list[_T]: ...
def nsmallest(n: int, iterable: Iterable[_T], key: Callable[[_T], SupportsRichComparison] | None = ...) -> list[_T]: ...
def _heapify_max(__x: list[Any]) -> None: ...  # undocumented
