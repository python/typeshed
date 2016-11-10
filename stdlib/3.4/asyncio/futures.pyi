from typing import Any, Union, Callable, TypeVar, List, Generic, Iterable, Generator, Awaitable
from .events import AbstractEventLoop

__all__ = ... # type: str

_T = TypeVar('_T')

from concurrent.futures._base import (
    Error as Error,
)
from concurrent.futures import (
    CancelledError as CancelledError,
    TimeoutError as TimeoutError,
)
class InvalidStateError(Error): ...

class _TracebackLogger:
    __slots__ = ... # type: List[str]
    exc = ...  # type: BaseException
    tb = ... # type: List[str]
    def __init__(self, exc: Any, loop: AbstractEventLoop) -> None: ...
    def activate(self) -> None: ...
    def clear(self) -> None: ...
    def __del__(self) -> None: ...

class Future(Iterable[_T], Awaitable[_T], Generic[_T]):
    _state = ...  # type: str
    _exception = ... # type: BaseException
    _blocking = False
    _log_traceback = False
    _tb_logger = _TracebackLogger
    def __init__(self, *, loop: AbstractEventLoop = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __del__(self) -> None: ...
    def cancel(self) -> bool: ...
    def _schedule_callbacks(self) -> None: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self) -> _T: ...
    def exception(self) -> BaseException: ...
    def add_done_callback(self, fn: Callable[[Future[_T]], Any]) -> None: ...
    def remove_done_callback(self, fn: Callable[[Future[_T]], Any]) -> int: ...
    def set_result(self, result: _T) -> None: ...
    def set_exception(self, exception: Union[type, BaseException]) -> None: ...
    def _copy_state(self, other: Any) -> None: ...
    def __iter__(self) -> Generator[Any, None, _T]: ...
    def __await__(self) -> Generator[Any, None, _T]: ...
