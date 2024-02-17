from collections.abc import Callable
from types import TracebackType
from typing import Any, Literal

from gevent._abstract_linkable import AbstractLinkable
from gevent.hub import Hub

__all__ = ["Semaphore", "BoundedSemaphore", "DummySemaphore", "RLock"]

class Semaphore(AbstractLinkable):
    counter: int
    def __init__(self, value: int = 1, hub: Hub | None = None) -> None: ...
    def acquire(self, blocking: bool = True, timeout: float | None = None) -> bool: ...
    def locked(self) -> bool: ...
    def ready(self) -> bool: ...
    def release(self) -> int: ...
    def wait(self, timeout: float | None = None) -> int: ...
    def __enter__(self) -> None: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...

class BoundedSemaphore(Semaphore): ...

class DummySemaphore:
    def __init__(self, value: int | None = None) -> None: ...
    def locked(self) -> Literal[False]: ...
    def ready(self) -> Literal[True]: ...
    def release(self) -> None: ...
    def rawlink(self, callback: Callable[[Any], object]) -> None: ...
    def unlink(self, callback: Callable[[Any], object]) -> None: ...
    def wait(self, timeout: float | None = None) -> Literal[1]: ...
    def acquire(self, blocking: bool = True, timeout: float | None = None) -> Literal[True]: ...
    def __enter__(self) -> None: ...
    def __exit__(self, typ: type[BaseException] | None, val: BaseException | None, tb: TracebackType | None) -> None: ...

class RLock:
    def __init__(self, hub: Hub | None = None) -> None: ...
    def acquire(self, blocking: bool = True, timeout: float | None = None) -> bool: ...
    def __enter__(self) -> bool: ...
    def release(self) -> None: ...
    def __exit__(self, typ: type[BaseException] | None, val: BaseException | None, tb: TracebackType | None) -> None: ...
