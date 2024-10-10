import sys
from asyncio.events import AbstractEventLoop
from collections.abc import Awaitable, Callable, Coroutine, Generator, Iterable
from contextvars import Context
from types import FrameType
from typing import Any, Literal, TextIO, TypeVar
from typing_extensions import Self, TypeAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_TaskYieldType: TypeAlias = Future[object] | None

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
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

if sys.version_info >= (3, 12):
    _TaskCompatibleCoro: TypeAlias = Coroutine[Any, Any, _T_co]
elif sys.version_info >= (3, 9):
    _TaskCompatibleCoro: TypeAlias = Generator[_TaskYieldType, None, _T_co] | Coroutine[Any, Any, _T_co]
else:
    _TaskCompatibleCoro: TypeAlias = Generator[_TaskYieldType, None, _T_co] | Awaitable[_T_co]

# mypy and pyright complain that a subclass of an invariant class shouldn't be covariant.
# While this is true in general, here it's sort-of okay to have a covariant subclass,
# since the only reason why `asyncio.Future` is invariant is the `set_result()` method,
# and `asyncio.Task.set_result()` always raises.
class Task(Future[_T_co]):  # type: ignore[type-var]  # pyright: ignore[reportInvalidTypeArguments]
    if sys.version_info >= (3, 12):
        def __init__(
            self,
            coro: _TaskCompatibleCoro[_T_co],
            *,
            loop: AbstractEventLoop = ...,
            name: str | None = ...,
            context: Context | None = None,
            eager_start: bool = False,
        ) -> None: ...
    elif sys.version_info >= (3, 11):
        def __init__(
            self,
            coro: _TaskCompatibleCoro[_T_co],
            *,
            loop: AbstractEventLoop = ...,
            name: str | None = ...,
            context: Context | None = None,
        ) -> None: ...
    else:
        def __init__(
            self, coro: _TaskCompatibleCoro[_T_co], *, loop: AbstractEventLoop = ..., name: str | None = ...
        ) -> None: ...

    if sys.version_info >= (3, 12):
        def get_coro(self) -> _TaskCompatibleCoro[_T_co] | None: ...
    else:
        def get_coro(self) -> _TaskCompatibleCoro[_T_co]: ...

    def get_name(self) -> str: ...
    def set_name(self, value: object, /) -> None: ...
    if sys.version_info >= (3, 12):
        def get_context(self) -> Context: ...

    def get_stack(self, *, limit: int | None = None) -> list[FrameType]: ...
    def print_stack(self, *, limit: int | None = None, file: TextIO | None = None) -> None: ...
    if sys.version_info >= (3, 11):
        def cancelling(self) -> int: ...
        def uncancel(self) -> int: ...
    if sys.version_info < (3, 9):
        @classmethod
        def current_task(cls, loop: AbstractEventLoop | None = None) -> Task[Any] | None: ...
        @classmethod
        def all_tasks(cls, loop: AbstractEventLoop | None = None) -> set[Task[Any]]: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

def get_event_loop() -> AbstractEventLoop: ...
def get_running_loop() -> AbstractEventLoop: ...
