from typing import Any

class _TimeoutGarbageCollector:
    def __init__(self): ...

class Condition(_TimeoutGarbageCollector):
    io_loop = ...  # type: Any
    def __init__(self): ...
    def wait(self, timeout=None): ...
    def notify(self, n=1): ...
    def notify_all(self): ...

class Event:
    def __init__(self): ...
    def is_set(self): ...
    def set(self): ...
    def clear(self): ...
    def wait(self, timeout=None): ...

class _ReleasingContextManager:
    def __init__(self, obj): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...

class Semaphore(_TimeoutGarbageCollector):
    def __init__(self, value=1): ...
    def release(self): ...
    def acquire(self, timeout=None): ...
    def __enter__(self): ...
    __exit__ = ...  # type: Any
    def __aenter__(self): ...
    def __aexit__(self, typ, value, tb): ...

class BoundedSemaphore(Semaphore):
    def __init__(self, value=1): ...
    def release(self): ...

class Lock:
    def __init__(self): ...
    def acquire(self, timeout=None): ...
    def release(self): ...
    def __enter__(self): ...
    __exit__ = ...  # type: Any
    def __aenter__(self): ...
    def __aexit__(self, typ, value, tb): ...
