import sys
from asyncio.events import AbstractEventLoop
from .coroutines import coroutine
from .futures import Future
from typing import Any, Generator, Generic, List, TypeVar, Optional

__all__: List[str]


class QueueEmpty(Exception): ...
class QueueFull(Exception): ...

_T = TypeVar('_T')

class Queue(Generic[_T]):
    def __init__(self, maxsize: int = ..., *, loop: Optional[AbstractEventLoop] = ...) -> None: ...
    def _init(self, maxsize: int) -> None: ...
    def _get(self) -> _T: ...
    def _put(self, item: _T) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _format(self) -> str: ...
    def _consume_done_getters(self) -> None: ...
    def _consume_done_putters(self) -> None: ...
    def qsize(self) -> int: ...
    @property
    def maxsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    @coroutine
    def put(self, item: _T) -> Generator[Any, None, None]: ...
    def put_nowait(self, item: _T) -> None: ...
    @coroutine
    def get(self) -> Generator[Any, None, _T]: ...
    def get_nowait(self) -> _T: ...
    @coroutine
    def join(self) -> Generator[Any, None, bool]: ...
    def task_done(self) -> None: ...


class PriorityQueue(Queue[_T]): ...


class LifoQueue(Queue[_T]): ...
