import enum
import sys
from _typeshed import Unused
from collections import deque
from collections.abc import Callable
from types import TracebackType
from typing import Any, Literal, TypeVar
from typing_extensions import Self

from .events import AbstractEventLoop
from .futures import Future

if sys.version_info >= (3, 10):
    from .mixins import _LoopBoundMixin
else:
    _LoopBoundMixin = object

# Keep asyncio.__all__ updated with any changes to __all__ here
if sys.version_info >= (3, 11):
    __all__ = ("Lock", "Event", "Condition", "Semaphore", "BoundedSemaphore", "Barrier")
else:
    __all__ = ("Lock", "Event", "Condition", "Semaphore", "BoundedSemaphore")

_T = TypeVar("_T")

class _ContextManagerMixin:
    async def __aenter__(self) -> None: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None: ...

class Lock(_ContextManagerMixin, _LoopBoundMixin):
    _waiters: deque[Future[Any]] | None
    if sys.version_info >= (3, 10):
        def __init__(self) -> None: ...
    else:
        def __init__(self, *, loop: AbstractEventLoop | None = None) -> None: ...

    def locked(self) -> bool: ...
    async def acquire(self) -> Literal[True]: ...
    def release(self) -> None: ...

class Event(_LoopBoundMixin):
    _waiters: deque[Future[Any]]
    if sys.version_info >= (3, 10):
        def __init__(self) -> None: ...
    else:
        def __init__(self, *, loop: AbstractEventLoop | None = None) -> None: ...

    def is_set(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    async def wait(self) -> Literal[True]: ...

class Condition(_ContextManagerMixin, _LoopBoundMixin):
    _waiters: deque[Future[Any]]
    if sys.version_info >= (3, 10):
        def __init__(self, lock: Lock | None = None) -> None: ...
    else:
        def __init__(self, lock: Lock | None = None, *, loop: AbstractEventLoop | None = None) -> None: ...

    def locked(self) -> bool: ...
    async def acquire(self) -> Literal[True]: ...
    def release(self) -> None: ...
    async def wait(self) -> Literal[True]: ...
    async def wait_for(self, predicate: Callable[[], _T]) -> _T: ...
    def notify(self, n: int = 1) -> None: ...
    def notify_all(self) -> None: ...

class Semaphore(_ContextManagerMixin, _LoopBoundMixin):
    _value: int
    _waiters: deque[Future[Any]] | None
    if sys.version_info >= (3, 10):
        def __init__(self, value: int = 1) -> None: ...
    else:
        def __init__(self, value: int = 1, *, loop: AbstractEventLoop | None = None) -> None: ...

    def locked(self) -> bool: ...
    async def acquire(self) -> Literal[True]: ...
    def release(self) -> None: ...
    def _wake_up_next(self) -> None: ...

class BoundedSemaphore(Semaphore): ...

if sys.version_info >= (3, 11):
    class _BarrierState(enum.Enum):  # undocumented
        FILLING = "filling"
        DRAINING = "draining"
        RESETTING = "resetting"
        BROKEN = "broken"

    class Barrier(_LoopBoundMixin):
        def __init__(self, parties: int) -> None: ...
        async def __aenter__(self) -> Self: ...
        async def __aexit__(self, *args: Unused) -> None: ...
        async def wait(self) -> int: ...
        async def abort(self) -> None: ...
        async def reset(self) -> None: ...
        @property
        def parties(self) -> int: ...
        @property
        def n_waiting(self) -> int: ...
        @property
        def broken(self) -> bool: ...
