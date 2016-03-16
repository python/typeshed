# Stubs for contextlib

# NOTE: These are incomplete!

from typing import Callable, Generic, Iterator, TypeVar

_T = TypeVar('_T')

class ContextManager(Generic[_T]):
    def __enter__(self) -> _T: ...
    def __exit__(self, *exc_info) -> None: ...

# TODO this doesn't capture the relationship that the returned function's args are the same as func's.
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., ContextManager[_T]]: ...

class closing(ContextManager[_T], Generic[_T]):
    def __init__(self, thing: _T) -> None: ...
