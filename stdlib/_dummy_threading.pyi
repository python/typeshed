import sys
from types import FrameType, TracebackType
from typing import Any, Callable, Iterable, Mapping,  Type, TypeVar

# TODO recursive type
_TF = Callable[[FrameType, str, Any], Callable[..., Any] | None]

_PF = Callable[[FrameType, str, Any], None]
_T = TypeVar("_T")

__all__: list[str]

def active_count() -> int: ...
def current_thread() -> Thread: ...
def currentThread() -> Thread: ...
def get_ident() -> int: ...
def enumerate() -> list[Thread]: ...
def main_thread() -> Thread: ...

if sys.version_info >= (3, 8):
    from _thread import get_native_id as get_native_id

def settrace(func: _TF) -> None: ...
def setprofile(func: _PF | None) -> None: ...
def stack_size(size: int = ...) -> int: ...

TIMEOUT_MAX: float

class ThreadError(Exception): ...

class local(object):
    def __getattribute__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

class Thread:
    name: str
    ident: int | None
    daemon: bool
    def __init__(
        self,
        group: None = ...,
        target: Callable[..., Any] | None = ...,
        name: str | None = ...,
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] | None = ...,
        *,
        daemon: bool | None = ...,
    ) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: float | None = ...) -> None: ...
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    if sys.version_info >= (3, 8):
        @property
        def native_id(self) -> int | None: ...  # only available on some platforms
    def is_alive(self) -> bool: ...
    if sys.version_info < (3, 9):
        def isAlive(self) -> bool: ...
    def isDaemon(self) -> bool: ...
    def setDaemon(self, daemonic: bool) -> None: ...

class _DummyThread(Thread): ...

class Lock:
    def __init__(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
    def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...

class _RLock:
    def __init__(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
    def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    def release(self) -> None: ...

RLock = _RLock

class Condition:
    def __init__(self, lock: Lock | _RLock | None = ...) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
    def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    def release(self) -> None: ...
    def wait(self, timeout: float | None = ...) -> bool: ...
    def wait_for(self, predicate: Callable[[], _T], timeout: float | None = ...) -> _T: ...
    def notify(self, n: int = ...) -> None: ...
    def notify_all(self) -> None: ...
    def notifyAll(self) -> None: ...

class Semaphore:
    def __init__(self, value: int = ...) -> None: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
    def acquire(self, blocking: bool = ..., timeout: float | None = ...) -> bool: ...
    def __enter__(self, blocking: bool = ..., timeout: float | None = ...) -> bool: ...
    if sys.version_info >= (3, 9):
        def release(self, n: int = ...) -> None: ...
    else:
        def release(self) -> None: ...

class BoundedSemaphore(Semaphore): ...

class Event:
    def __init__(self) -> None: ...
    def is_set(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: float | None = ...) -> bool: ...

if sys.version_info >= (3, 8):
    from _thread import _excepthook, _ExceptHookArgs

    excepthook = _excepthook
    ExceptHookArgs = _ExceptHookArgs

class Timer(Thread):
    def __init__(
        self,
        interval: float,
        function: Callable[..., Any],
        args: Iterable[Any] | None = ...,
        kwargs: Mapping[str, Any] | None = ...,
    ) -> None: ...
    def cancel(self) -> None: ...

class Barrier:
    parties: int
    n_waiting: int
    broken: bool
    def __init__(self, parties: int, action: Callable[[], None] | None = ..., timeout: float | None = ...) -> None: ...
    def wait(self, timeout: float | None = ...) -> int: ...
    def reset(self) -> None: ...
    def abort(self) -> None: ...

class BrokenBarrierError(RuntimeError): ...
