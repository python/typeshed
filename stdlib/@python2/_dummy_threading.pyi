from types import FrameType, TracebackType
from typing import Any, Callable, Iterable, List, Mapping, Optional, Text, Type, TypeVar

# TODO recursive type
_TF = Callable[[FrameType, str, Any], Optional[Callable[..., Any]]]

_PF = Callable[[FrameType, str, Any], None]
_T = TypeVar("_T")

__all__: List[str]

def active_count() -> int: ...
def activeCount() -> int: ...
def current_thread() -> Thread: ...
def currentThread() -> Thread: ...
def enumerate() -> List[Thread]: ...
def settrace(func: _TF) -> None: ...
def setprofile(func: _PF | None) -> None: ...
def stack_size(size: int = ...) -> int: ...

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
        name: Text | None = ...,
        args: Iterable[Any] = ...,
        kwargs: Mapping[Text, Any] | None = ...,
    ) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: float | None = ...) -> None: ...
    def getName(self) -> str: ...
    def setName(self, name: Text) -> None: ...
    def is_alive(self) -> bool: ...
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
    def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...

class _RLock:
    def __init__(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
    def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...

RLock = _RLock

class Condition:
    def __init__(self, lock: Lock | _RLock | None = ...) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
    def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...
    def wait(self, timeout: float | None = ...) -> bool: ...
    def notify(self, n: int = ...) -> None: ...
    def notify_all(self) -> None: ...
    def notifyAll(self) -> None: ...

class Semaphore:
    def __init__(self, value: int = ...) -> None: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
    def acquire(self, blocking: bool = ...) -> bool: ...
    def __enter__(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...

class BoundedSemaphore(Semaphore): ...

class Event:
    def __init__(self) -> None: ...
    def is_set(self) -> bool: ...
    def isSet(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: float | None = ...) -> bool: ...

class Timer(Thread):
    def __init__(
        self, interval: float, function: Callable[..., Any], args: Iterable[Any] = ..., kwargs: Mapping[str, Any] = ...
    ) -> None: ...
    def cancel(self) -> None: ...
