"""Stub file for the '_functools' module."""

from typing import Any, Callable, Iterator, Optional, TypeVar, Tuple

_T = TypeVar("_T")
def reduce(function: Callable[[_T, _T], _T],
           sequence: Iterator[_T], initial=Optional[_T]) -> _T: ...

class partial(object):
    func = ...  # type: Callable[..., Any]
    args = ...  # type: Tuple[Any]
    keywords = ...  # type: Dict[str, Any]
    def __init__(self, func: Callable[..., Any], *args, **kwargs) -> None: ...
    def __call__(self, *args, **kwargs) -> Any: ...
