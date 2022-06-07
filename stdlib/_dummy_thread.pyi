from collections.abc import Callable
from types import TracebackType
from typing import Any, NoReturn

__all__ = ["error", "start_new_thread", "exit", "get_ident", "allocate_lock", "interrupt_main", "LockType", "RLock"]

TIMEOUT_MAX: int
error = RuntimeError

def start_new_thread(function: Callable[..., Any], args: tuple[Any, ...], kwargs: dict[str, Any] = ...) -> None: ...
def exit() -> NoReturn: ...
def get_ident() -> int: ...
def allocate_lock() -> LockType: ...
def stack_size(size: int | None = ...) -> int: ...

class LockType:
    locked_status: bool
    def __init__(self) -> None: ...
    def acquire(self, waitflag: bool | None = ..., timeout: int = ...) -> bool: ...
    def __enter__(self, waitflag: bool | None = ..., timeout: int = ...) -> bool: ...
    def __exit__(self, typ: type[BaseException] | None, val: BaseException | None, tb: TracebackType | None) -> None: ...
    def release(self) -> bool: ...
    def locked(self) -> bool: ...

def interrupt_main() -> None: ...
