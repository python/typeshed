"""Stub file for the '_functools' module."""

from typing import Any, Callable, Iterator, Optional, TypeVar, Tuple, overload

_T = TypeVar("_T")

@overload
def reduce(function: Callable[[_T, _T], _T],
           sequence: Iterator[_T]) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T],
           sequence: Iterator[_T], initial: _T) -> _T: ...

class partial(object):
    func = ...  # type: Callable[..., Any]
    args = ...  # type: Tuple[Any, ...]
    keywords = ...  # type: Dict[str, Any]
    def __init__(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
