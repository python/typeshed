import sys
from types import GenericAlias
from typing import Any, Generic, TypeVar

__all__ = ["Queue", "SimpleQueue", "JoinableQueue"]

_T = TypeVar("_T")

class Queue(Generic[_T]):
    # FIXME: `ctx` is a circular dependency and it's not actually optional.
    # It's marked as such to be able to use the generic Queue in __init__.pyi.
    def __init__(self, maxsize: int = 0, *, ctx: Any = ...) -> None: ...
    def put(self, obj: _T, block: bool = True, timeout: float | None = None) -> None: ...
    def get(self, block: bool = True, timeout: float | None = None) -> _T: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def get_nowait(self) -> _T: ...
    def put_nowait(self, obj: _T) -> None: ...
    def close(self) -> None: ...
    def join_thread(self) -> None: ...
    def cancel_join_thread(self) -> None: ...
    if sys.version_info >= (3, 12):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

class JoinableQueue(Queue[_T]):
    def task_done(self) -> None: ...
    def join(self) -> None: ...

class SimpleQueue(Generic[_T]):
    def __init__(self, *, ctx: Any = ...) -> None: ...
    def close(self) -> None: ...
    def empty(self) -> bool: ...
    def get(self) -> _T: ...
    def put(self, obj: _T) -> None: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
