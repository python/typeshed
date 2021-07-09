from types import TracebackType
from typing import Any, NoReturn, Optional, Type

class _TimeoutGarbageCollector:
    def __init__(self) -> None: ...

class Condition(_TimeoutGarbageCollector):
    io_loop: Any
    def __init__(self): ...
    def wait(self, timeout: Optional[Any] = ...): ...
    def notify(self, n: int = ...): ...
    def notify_all(self): ...

class Event:
    def __init__(self) -> None: ...
    def is_set(self) -> bool: ...
    def set(self): ...
    def clear(self): ...
    def wait(self, timeout: Optional[Any] = ...): ...

class _ReleasingContextManager:
    def __init__(self, obj) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...

class Semaphore(_TimeoutGarbageCollector):
    def __init__(self, value: int = ...) -> None: ...
    def release(self) -> None: ...
    def acquire(self, timeout: Optional[Any] = ...): ...
    def __enter__(self) -> NoReturn: ...
    __exit__: Any
    def __aenter__(self) -> None: ...
    def __aexit__(
        self, typ: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[TracebackType]
    ) -> None: ...

class BoundedSemaphore(Semaphore): ...

class Lock:
    def __init__(self) -> None: ...
    def acquire(self, timeout: Optional[Any] = ...): ...
    def release(self) -> None: ...
    def __enter__(self) -> NoReturn: ...
    __exit__: Any
    def __aenter__(self) -> None: ...
    def __aexit__(
        self, typ: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[TracebackType]
    ) -> None: ...
