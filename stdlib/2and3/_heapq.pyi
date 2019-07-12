"""Stub file for the '_heapq' module."""

from typing import TypeVar, List, Iterable, Any, Callable, Optional

_T = TypeVar("_T")

def heapify(heap: List[_T]) -> None: ...
def heappop(heap: List[_T]) -> _T:
    raise IndexError()  # if list is empty
def heappush(heap: List[_T], item: _T) -> None: ...
def heappushpop(heap: List[_T], item: _T) -> _T: ...
def heapreplace(heap: List[_T], item: _T) -> _T:
    raise IndexError()  # if list is empty
def nlargest(n: int, iterable: Iterable[_T],
             key: Optional[Callable[[_T], Any]] = ...) -> List[_T]: ...
def nsmallest(n: int, iterable: Iterable[_T],
              key: Optional[Callable[[_T], Any]] = ...) -> List[_T]: ...
