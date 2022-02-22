import sys
from _typeshed import Self
from concurrent.futures._base import Error, Future as _ConcurrentFuture
from typing import Any, Awaitable, Callable, Generator, Iterable, TypeVar

from .base_futures import isfuture
from .events import AbstractEventLoop

if sys.version_info < (3, 8):
    from concurrent.futures import CancelledError as CancelledError, TimeoutError as TimeoutError

    class InvalidStateError(Error): ...

if sys.version_info >= (3, 7):
    from contextvars import Context

if sys.version_info >= (3, 9):
    from types import GenericAlias

if sys.version_info >= (3, 8):
    __all__ = ("Future", "wrap_future", "isfuture")
elif sys.version_info >= (3, 7):
    __all__ = ("CancelledError", "TimeoutError", "InvalidStateError", "Future", "wrap_future", "isfuture")
else:
    __all__ = ["CancelledError", "TimeoutError", "InvalidStateError", "Future", "wrap_future", "isfuture"]

_T = TypeVar("_T")

if sys.version_info < (3, 7):
    class _TracebackLogger:
        exc: BaseException
        tb: list[str]
        def __init__(self, exc: Any, loop: AbstractEventLoop) -> None: ...
        def activate(self) -> None: ...
        def clear(self) -> None: ...
        def __del__(self) -> None: ...

class Future(Awaitable[_T], Iterable[_T]):
    _state: str
    _exception: BaseException
    _blocking: bool
    _log_traceback: bool
    _asyncio_future_blocking: bool  # is a part of duck-typing contract for `Future`
    def __init__(self, *, loop: AbstractEventLoop | None = ...) -> None: ...
    def __del__(self) -> None: ...
    if sys.version_info >= (3, 7):
        def get_loop(self) -> AbstractEventLoop: ...
        def _callbacks(self: Self) -> list[tuple[Callable[[Self], Any], Context]]: ...
        def add_done_callback(self: Self, __fn: Callable[[Self], Any], *, context: Context | None = ...) -> None: ...
    else:
        @property
        def _callbacks(self: Self) -> list[Callable[[Self], Any]]: ...
        def add_done_callback(self: Self, __fn: Callable[[Self], Any]) -> None: ...
    if sys.version_info >= (3, 9):
        def cancel(self, msg: Any | None = ...) -> bool: ...
    else:
        def cancel(self) -> bool: ...

    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self) -> _T: ...
    def exception(self) -> BaseException | None: ...
    def remove_done_callback(self: Self, __fn: Callable[[Self], Any]) -> int: ...
    def set_result(self, __result: _T) -> None: ...
    def set_exception(self, __exception: type | BaseException) -> None: ...
    def __iter__(self) -> Generator[Any, None, _T]: ...
    def __await__(self) -> Generator[Any, None, _T]: ...
    @property
    def _loop(self) -> AbstractEventLoop: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

def wrap_future(future: _ConcurrentFuture[_T] | Future[_T], *, loop: AbstractEventLoop | None = ...) -> Future[_T]: ...
