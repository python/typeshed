import sys
from typing import Any, Callable, Iterable, List, Optional, TypeVar

_T = TypeVar("_T")

def heapify(__heap: List[Any]) -> None: ...
def heappop(__heap: List[_T]) -> _T: ...
def heappush(__heap: List[_T], __item: _T) -> None: ...
def heappushpop(__heap: List[_T], __item: _T) -> _T: ...
def heapreplace(__heap: List[_T], __item: _T) -> _T: ...
def nlargest(__n: int, __iterable: Iterable[_T], __key: Optional[Callable[[_T], Any]] = ...) -> List[_T]: ...
def nsmallest(__n: int, __iterable: Iterable[_T], __key: Optional[Callable[[_T], Any]] = ...) -> List[_T]: ...
