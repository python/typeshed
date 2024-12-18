from _threading_local import local as local
from _typeshed import ProfileFunction, TraceFunction
from threading import (
    TIMEOUT_MAX as TIMEOUT_MAX,
    Barrier as Barrier,
    BoundedSemaphore as BoundedSemaphore,
    BrokenBarrierError as BrokenBarrierError,
    Condition as Condition,
    Event as Event,
    ExceptHookArgs as ExceptHookArgs,
    Lock as Lock,
    RLock as RLock,
    Semaphore as Semaphore,
    Thread as Thread,
    ThreadError as ThreadError,
    Timer as Timer,
    _DummyThread as _DummyThread,
    _RLock as _RLock,
    excepthook as excepthook,
)

__all__ = [
    "TIMEOUT_MAX",
    "Barrier",
    "BoundedSemaphore",
    "BrokenBarrierError",
    "Condition",
    "Event",
    "ExceptHookArgs",
    "Lock",
    "RLock",
    "Semaphore",
    "Thread",
    "ThreadError",
    "Timer",
    "active_count",
    "current_thread",
    "enumerate",
    "excepthook",
    "get_ident",
    "local",
    "main_thread",
    "setprofile",
    "settrace",
    "stack_size",
]

def active_count() -> int: ...
def current_thread() -> Thread: ...
def currentThread() -> Thread: ...
def get_ident() -> int: ...
def enumerate() -> list[Thread]: ...
def main_thread() -> Thread: ...
def settrace(func: TraceFunction) -> None: ...
def setprofile(func: ProfileFunction | None) -> None: ...
def stack_size(size: int | None = None) -> int: ...
