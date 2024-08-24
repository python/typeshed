import signal
import sys
from collections.abc import Callable
from types import TracebackType
from typing import Any, NoReturn, overload
from typing_extensions import TypeVarTuple, Unpack

__all__ = ["error", "start_new_thread", "exit", "get_ident", "allocate_lock", "interrupt_main", "LockType", "RLock"]

_Ts = TypeVarTuple("_Ts")

TIMEOUT_MAX: int
error = RuntimeError

@overload
def start_new_thread(function: Callable[[Unpack[_Ts]], object], args: tuple[Unpack[_Ts]]) -> None: ...
@overload
def start_new_thread(function: Callable[..., object], args: tuple[Any, ...], kwargs: dict[str, Any]) -> None: ...
def exit() -> NoReturn: ...
def get_ident() -> int: ...
def allocate_lock() -> LockType: ...
def stack_size(size: int | None = None) -> int: ...

class LockType:
    locked_status: bool
    def acquire(self, waitflag: bool | None = None, timeout: int = -1) -> bool: ...
    def __enter__(self, waitflag: bool | None = None, timeout: int = -1) -> bool: ...
    def __exit__(self, typ: type[BaseException] | None, val: BaseException | None, tb: TracebackType | None) -> None: ...
    def release(self) -> bool: ...
    def locked(self) -> bool: ...

class RLock(LockType):
    def release(self) -> None: ...  # type: ignore[override]

if sys.version_info >= (3, 10):
    def interrupt_main(signum: signal.Signals = signal.SIGINT, /) -> None: ...
else:
    def interrupt_main() -> None: ...
