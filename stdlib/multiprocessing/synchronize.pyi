import sys
import threading
from multiprocessing.context import BaseContext
from typing import Any, Callable, ContextManager, Union

_LockLike = Lock | RLock

class Barrier(threading.Barrier):
    def __init__(
        self, parties: int, action: Callable[..., Any] | None = ..., timeout: float | None = ..., *ctx: BaseContext
    ) -> None: ...

class BoundedSemaphore(Semaphore):
    def __init__(self, value: int = ..., *, ctx: BaseContext) -> None: ...

class Condition(ContextManager[bool]):
    def __init__(self, lock: _LockLike | None = ..., *, ctx: BaseContext) -> None: ...
    if sys.version_info >= (3, 7):
        def notify(self, n: int = ...) -> None: ...
    else:
        def notify(self) -> None: ...
    def notify_all(self) -> None: ...
    def wait(self, timeout: float | None = ...) -> bool: ...
    def wait_for(self, predicate: Callable[[], bool], timeout: float | None = ...) -> bool: ...
    def acquire(self, block: bool = ..., timeout: float | None = ...) -> bool: ...
    def release(self) -> None: ...

class Event(ContextManager[bool]):
    def __init__(self, lock: _LockLike | None = ..., *, ctx: BaseContext) -> None: ...
    def is_set(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: float | None = ...) -> bool: ...

class Lock(SemLock):
    def __init__(self, *, ctx: BaseContext) -> None: ...

class RLock(SemLock):
    def __init__(self, *, ctx: BaseContext) -> None: ...

class Semaphore(SemLock):
    def __init__(self, value: int = ..., *, ctx: BaseContext) -> None: ...

# Not part of public API
class SemLock(ContextManager[bool]):
    def acquire(self, block: bool = ..., timeout: float | None = ...) -> bool: ...
    def release(self) -> None: ...
