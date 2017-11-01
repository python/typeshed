# Stubs for threading

from typing import (
    Any, Callable, Iterable, List, Mapping, Optional, Tuple, Type, Union,
    TypeVar,
)
from types import FrameType, TracebackType
import sys

# TODO recursive type
_TF = Callable[[FrameType, str, Any], Optional[Callable[..., Any]]]

_PF = Callable[[FrameType, str, Any], None]
_T = TypeVar('_T')


def active_count() -> int: ...
if sys.version_info < (3,):
    def activeCount() -> int: ...

def current_thread() -> Thread: ...
if sys.version_info < (3,):
    def currentThread() -> Thread: ...

if sys.version_info >= (3,):
    def get_ident() -> int: ...

def enumerate() -> List[Thread]: ...

if sys.version_info >= (3, 4):
    def main_thread() -> Thread: ...

def settrace(func: _TF) -> None: ...
def setprofile(func: _PF) -> None: ...
def stack_size(size: int = ...) -> int: ...

if sys.version_info >= (3,):
    TIMEOUT_MAX = ...  # type: float

class ThreadError(Exception): ...


# TODO: Change to a class with __getattr__ and __setattr__
# once mypy supports universal __setattr__.
# See https://github.com/python/mypy/issues/521
local = ...  # type: Any


class Thread:
    name = ...  # type: str
    ident = ...  # type: Optional[int]
    daemon = ...  # type: bool
    if sys.version_info >= (3,):
        def __init__(self, group: None = ...,
                     target: Optional[Callable[..., None]] = ...,
                     name: Optional[str] = ...,
                     args: Iterable = ...,
                     kwargs: Mapping[str, Any] = ...,
                     *, daemon: Optional[bool] = ...) -> None: ...
    else:
        def __init__(self, group: None = ...,
                     target: Optional[Callable[..., None]] = ...,
                     name: Optional[str] = ...,
                     args: Iterable = ...,
                     kwargs: Mapping[str, Any] = ...) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: Optional[float] = ...) -> None: ...
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def is_alive(self) -> bool: ...
    if sys.version_info < (3,):
        def isAlive(self) -> bool: ...
    def isDaemon(self) -> bool: ...
    def setDaemon(self, daemonic: bool) -> None: ...


class _DummyThread(Thread):
    pass


class Lock:
    def __init__(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[Exception],
                 exc_tb: Optional[TracebackType]) -> bool: ...
    if sys.version_info >= (3,):
        def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    else:
        def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...


class _RLock:
    def __init__(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[Exception],
                 exc_tb: Optional[TracebackType]) -> bool: ...
    if sys.version_info >= (3,):
        def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    else:
        def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...


RLock = _RLock


class Condition:
    def __init__(self, lock: Union[Lock, _RLock, None] = ...) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[Exception],
                 exc_tb: Optional[TracebackType]) -> bool: ...
    if sys.version_info >= (3,):
        def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    else:
        def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...
    def wait(self, timeout: Optional[float] = ...) -> bool: ...
    if sys.version_info >= (3,):
        def wait_for(self, predicate: Callable[[], _T],
                     timeout: Optional[float]) -> _T: ...
    def notify(self, n: int = ...) -> None: ...
    def notify_all(self) -> None: ...
    def notifyAll(self) -> None: ...


class Semaphore:
    def __init__(self, value: int = ...) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[Exception],
                 exc_tb: Optional[TracebackType]) -> bool: ...
    if sys.version_info >= (3,):
        def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    else:
        def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...

class BoundedSemaphore:
    def __init__(self, value: int = ...) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[Exception],
                 exc_tb: Optional[TracebackType]) -> bool: ...
    if sys.version_info >= (3,):
        def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    else:
        def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...


class Event:
    def __init__(self) -> None: ...
    def is_set(self) -> bool: ...
    if sys.version_info < (3,):
        def isSet(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: Optional[float] = ...) -> bool: ...


class Timer(Thread):
    if sys.version_info >= (3,):
        def __init__(self, interval: float, function: Callable[..., None],
                     args: Optional[List[Any]] = ...,
                     kwargs: Optional[Mapping[str, Any]] = ...) -> None: ...
    else:
        def __init__(self, interval: float, function: Callable[..., None],
                     args: List[Any] = ...,
                     kwargs: Mapping[str, Any] = ...) -> None: ...
    def cancel(self) -> None: ...


if sys.version_info >= (3,):
    class Barrier:
        parties = ...  # type: int
        n_waiting = ...  # type: int
        broken = ...  # type: bool
        def __init__(self, parties: int, action: Optional[Callable[[], None]] = ...,
                     timeout: Optional[float] = ...) -> None: ...
        def wait(self, timeout: Optional[float] = ...) -> int: ...
        def reset(self) -> None: ...
        def abort(self) -> None: ...

    class BrokenBarrierError(RuntimeError): ...
