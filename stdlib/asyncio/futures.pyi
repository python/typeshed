import sys
from collections.abc import Awaitable, Callable, Generator, Iterable
from concurrent.futures._base import Future as _ConcurrentFuture
from contextvars import Context
from typing import Any, Literal, TypeVar
from typing_extensions import Self, TypeGuard

from .events import AbstractEventLoop

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = ("Future", "wrap_future", "isfuture")

_T = TypeVar("_T")

# asyncio defines 'isfuture()' in base_futures.py and re-imports it in futures.py
# but it leads to circular import error in pytype tool.
# That's why the import order is reversed.
def isfuture(obj: object) -> TypeGuard[Future[Any]]: ...

class Future(Awaitable[_T], Iterable[_T]):
    _state: str
    @property
    def _exception(self) -> BaseException | None: ...
    _blocking: bool
    @property
    def _log_traceback(self) -> bool: ...
    @_log_traceback.setter
    def _log_traceback(self, val: Literal[False]) -> None: ...
    _asyncio_future_blocking: bool  # is a part of duck-typing contract for `Future`
    def __init__(self, *, loop: AbstractEventLoop | None = ...) -> None: ...
    def __del__(self) -> None: ...
    def get_loop(self) -> AbstractEventLoop: ...
    @property
    def _callbacks(self) -> list[tuple[Callable[[Self], Any], Context]]: ...
    def add_done_callback(self, fn: Callable[[Self], object], /, *, context: Context | None = None) -> None: ...
    if sys.version_info >= (3, 9):
        def cancel(self, msg: Any | None = None) -> bool: ...
    else:
        def cancel(self) -> bool: ...

    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self) -> _T: ...
    def exception(self) -> BaseException | None: ...
    def remove_done_callback(self, fn: Callable[[Self], object], /) -> int: ...
    def set_result(self, result: _T, /) -> None: ...
    def set_exception(self, exception: type | BaseException, /) -> None: ...
    def __iter__(self) -> Generator[Any, None, _T]: ...
    def __await__(self) -> Generator[Any, None, _T]: ...
    @property
    def _loop(self) -> AbstractEventLoop: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

def wrap_future(future: _ConcurrentFuture[_T] | Future[_T], *, loop: AbstractEventLoop | None = None) -> Future[_T]: ...
