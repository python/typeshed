## Stubs for threading

from typing import Any, Callable, List, Mapping, Optional, Tuple
from types import FrameType
import sys

# TODO recursive type
_TF = Callable[[FrameType, str, Any], Optional[Callable[..., Any]]]

_PF = Callable[[FrameType, str, Any], None]


def active_count() -> int: ...
def current_thread() -> Thread: ...
def get_ident() -> int: ...
def enumerate() -> List[Thread]: ...
if sys.version_info >= (3, 4):
    def main_thread() -> Thread: ...
def settrace(func: _TF) -> None: ...
def setprofile(func: _PF) -> None: ...
def stack_size(size: int = ...) -> int: ...
TIMEOUT_MAX = ...  # type: int


class local: ...


class Thread:
    name = ...  # type: str
    ident = ...  # type: Optional[int]
    daemon = ...  # type: bool
    def __init__(self, group: None = ...,
                 target: Optional[Callable[..., None]] = ...,
                 name: Optional[str] = ...,
                 args: Tuple[Any, ...] = ...,
                 kwargs: Mapping[str, Any] = ...,
                 *, daemon: Optional[bool] = ...) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: Optional[float] = ...) -> None: ...
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def is_alive(self) -> bool: ...
    def isDaemon(self) -> bool: ...
    def setDaemon(self, daemonic: bool) -> None: ...


#ThreadError = ...  # type: Any


#Lock = ...  # type: Any

#def RLock(*args, **kwargs): ...

#class _RLock:
#    def __init__(self) -> None: ...
#    def acquire(self, blocking: bool = ..., timeout: int = ...): ...
#    __enter__ = ...  # type: Any
#    def release(self): ...
#    def __exit__(self, t, v, tb): ...

#class Condition:
#    acquire = ...  # type: Any
#    release = ...  # type: Any
#    def __init__(self, lock: Optional[Any] = ...) -> None: ...
#    def __enter__(self): ...
#    def __exit__(self, *args): ...
#    def wait(self, timeout: Optional[Any] = ...): ...
#    def wait_for(self, predicate, timeout: Optional[Any] = ...): ...
#    def notify(self, n: int = ...): ...
#    def notify_all(self): ...
#    notifyAll = ...  # type: Any

#class Semaphore:
#    def __init__(self, value: int = ...) -> None: ...
#    def acquire(self, blocking: bool = ..., timeout: Optional[Any] = ...): ...
#    __enter__ = ...  # type: Any
#    def release(self): ...
#    def __exit__(self, t, v, tb): ...

#class BoundedSemaphore(Semaphore):
#    def __init__(self, value: int = ...) -> None: ...
#    def release(self): ...

#class Event:
#    def __init__(self) -> None: ...
#    def is_set(self): ...
#    isSet = ...  # type: Any
#    def set(self): ...
#    def clear(self): ...
#    def wait(self, timeout: Optional[Any] = ...): ...

#class Barrier:
#    def __init__(self, parties, action: Optional[Any] = ..., timeout: Optional[Any] = ...) -> None: ...
#    def wait(self, timeout: Optional[Any] = ...): ...
#    def reset(self): ...
#    def abort(self): ...
#    @property
#    def parties(self): ...
#    @property
#    def n_waiting(self): ...
#    @property
#    def broken(self): ...

#class BrokenBarrierError(RuntimeError): ...

#class Timer(Thread):
#    interval = ...  # type: Any
#    function = ...  # type: Any
#    args = ...  # type: Any
#    kwargs = ...  # type: Any
#    finished = ...  # type: Any
#    def __init__(self, interval, function, args: Optional[Any] = ..., kwargs: Optional[Any] = ...) -> None: ...
#    def cancel(self): ...
#    def run(self): ...

#class _MainThread(Thread):
#    def __init__(self) -> None: ...

#class _DummyThread(Thread):
#    def __init__(self) -> None: ...
#    def join(self, timeout: Optional[Any] = ...): ...

