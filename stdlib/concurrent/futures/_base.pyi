import sys
import threading
from _typeshed import Self
from abc import abstractmethod
from collections.abc import Container, Iterable, Iterator, Sequence
from logging import Logger
from typing import Any, Callable, Generic, Protocol, TypeVar, overload
from typing_extensions import Literal, ParamSpec, SupportsIndex

if sys.version_info >= (3, 9):
    from types import GenericAlias

FIRST_COMPLETED: Literal["FIRST_COMPLETED"]
FIRST_EXCEPTION: Literal["FIRST_EXCEPTION"]
ALL_COMPLETED: Literal["ALL_COMPLETED"]
PENDING: Literal["PENDING"]
RUNNING: Literal["RUNNING"]
CANCELLED: Literal["CANCELLED"]
CANCELLED_AND_NOTIFIED: Literal["CANCELLED_AND_NOTIFIED"]
FINISHED: Literal["FINISHED"]
_FUTURE_STATES: list[str]
_STATE_TO_DESCRIPTION_MAP: dict[str, str]
LOGGER: Logger

class Error(Exception): ...
class CancelledError(Error): ...
class TimeoutError(Error): ...

if sys.version_info >= (3, 8):
    class InvalidStateError(Error): ...

if sys.version_info >= (3, 7):
    class BrokenExecutor(RuntimeError): ...

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_P = ParamSpec("_P")

# Copied over Collection implementation as it does not exist in Python 2 and <3.6.
# Also to solve pytype issues with _Collection.
class _Collection(Iterable[_T_co], Container[_T_co], Protocol[_T_co]):
    # Implement Sized (but don't have it as a base class).
    @abstractmethod
    def __len__(self) -> int: ...

class Future(Generic[_T]):
    def __init__(self) -> None: ...
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def running(self) -> bool: ...
    def done(self) -> bool: ...
    def add_done_callback(self, fn: Callable[[Future[_T]], Any]) -> None: ...
    def result(self, timeout: float | None = ...) -> _T: ...
    def set_running_or_notify_cancel(self) -> bool: ...
    def set_result(self, result: _T) -> None: ...
    def exception(self, timeout: float | None = ...) -> BaseException | None: ...
    def set_exception(self, exception: BaseException | None) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

class Executor:
    if sys.version_info >= (3, 9):
        def submit(self, __fn: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> Future[_T]: ...
    else:
        def submit(self, fn: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> Future[_T]: ...

    def map(
        self, fn: Callable[..., _T], *iterables: Iterable[Any], timeout: float | None = ..., chunksize: int = ...
    ) -> Iterator[_T]: ...
    if sys.version_info >= (3, 9):
        def shutdown(self, wait: bool = ..., *, cancel_futures: bool = ...) -> None: ...
    else:
        def shutdown(self, wait: bool = ...) -> None: ...

    def __enter__(self: Self) -> Self: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool | None: ...

def as_completed(fs: Iterable[Future[_T]], timeout: float | None = ...) -> Iterator[Future[_T]]: ...

# Ideally this would be a namedtuple, but mypy doesn't support generic tuple types. See #1976
class DoneAndNotDoneFutures(Sequence[set[Future[_T]]]):
    __match_args__ = ("done", "not_done")
    @property
    def done(self) -> set[Future[_T]]: ...
    @property
    def not_done(self) -> set[Future[_T]]: ...
    def __new__(_cls, done: set[Future[_T]], not_done: set[Future[_T]]) -> DoneAndNotDoneFutures[_T]: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, __i: SupportsIndex) -> set[Future[_T]]: ...
    @overload
    def __getitem__(self, __s: slice) -> DoneAndNotDoneFutures[_T]: ...

def wait(fs: Iterable[Future[_T]], timeout: float | None = ..., return_when: str = ...) -> DoneAndNotDoneFutures[_T]: ...

class _Waiter:
    event: threading.Event
    finished_futures: list[Future[Any]]
    def __init__(self) -> None: ...
    def add_result(self, future: Future[Any]) -> None: ...
    def add_exception(self, future: Future[Any]) -> None: ...
    def add_cancelled(self, future: Future[Any]) -> None: ...

class _AsCompletedWaiter(_Waiter):
    lock: threading.Lock
    def __init__(self) -> None: ...
    def add_result(self, future: Future[Any]) -> None: ...
    def add_exception(self, future: Future[Any]) -> None: ...
    def add_cancelled(self, future: Future[Any]) -> None: ...

class _FirstCompletedWaiter(_Waiter):
    def add_result(self, future: Future[Any]) -> None: ...
    def add_exception(self, future: Future[Any]) -> None: ...
    def add_cancelled(self, future: Future[Any]) -> None: ...

class _AllCompletedWaiter(_Waiter):
    num_pending_calls: int
    stop_on_exception: bool
    lock: threading.Lock
    def __init__(self, num_pending_calls: int, stop_on_exception: bool) -> None: ...
    def add_result(self, future: Future[Any]) -> None: ...
    def add_exception(self, future: Future[Any]) -> None: ...
    def add_cancelled(self, future: Future[Any]) -> None: ...

class _AcquireFutures:
    futures: Iterable[Future[Any]]
    def __init__(self, futures: Iterable[Future[Any]]) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Any) -> None: ...
