from typing import Any, Callable, Iterable, List, Optional, TypeVar

_T = TypeVar("_T")

def heappush(__heap: List[_T], __item: _T) -> None: ...
def heappop(__heap: List[_T]) -> _T: ...
def heappushpop(__heap: List[_T], __item: _T) -> _T: ...
def heapify(__heap: List[_T]) -> None: ...
def heapreplace(__heap: List[_T], __item: _T) -> _T: ...
def merge(*iterables: Iterable[_T], key: Optional[Callable[[_T], Any]] = ..., reverse: bool = ...) -> Iterable[_T]: ...
def nlargest(n: int, iterable: Iterable[_T], key: Optional[Callable[[_T], Any]] = ...) -> List[_T]: ...
def nsmallest(n: int, iterable: Iterable[_T], key: Optional[Callable[[_T], Any]] = ...) -> List[_T]: ...
def _heapify_max(x: List[_T]) -> None: ...  # undocumented
