import sys
from _typeshed import structseq
from collections.abc import Callable
from signal import SIGINT, Signals
from threading import Thread
from types import TracebackType
from typing import Any, Final, NoReturn, final, overload
from typing_extensions import TypeVarTuple, Unpack

_Ts = TypeVarTuple("_Ts")

error = RuntimeError

def _count() -> int: ...
@final
class LockType:
    def acquire(self, blocking: bool = True, timeout: float = -1) -> bool: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...
    def __enter__(self) -> bool: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...

@final
class _ThreadHandle:
    ident: int
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def join(self, timeout: float | None = -1) -> None: ...
    def _set_done(self) -> None: ...
    def is_done(self) -> bool: ...

@overload
def start_new_thread(function: Callable[[Unpack[_Ts]], object], args: tuple[Unpack[_Ts]], /) -> int: ...
@overload
def start_new_thread(function: Callable[..., object], args: tuple[Any, ...], kwargs: dict[str, Any], /) -> int: ...
def interrupt_main(signum: Signals = SIGINT, /) -> None: ...
def exit() -> NoReturn: ...
def allocate_lock() -> LockType: ...
def get_ident() -> int: ...
def stack_size(size: int = 0, /) -> int: ...

if sys.version_info >= (3, 13):
    def start_joinable_thread(
        function: Callable[..., object], handle: _ThreadHandle | None = None, daemon: Any = True
    ) -> _ThreadHandle: ...

TIMEOUT_MAX: float

def get_native_id() -> int: ...  # only available on some platforms
@final
class _ExceptHookArgs(structseq[Any], tuple[type[BaseException], BaseException | None, TracebackType | None, Thread | None]):
    if sys.version_info >= (3, 10):
        __match_args__: Final = ("exc_type", "exc_value", "exc_traceback", "thread")

    @property
    def exc_type(self) -> type[BaseException]: ...
    @property
    def exc_value(self) -> BaseException | None: ...
    @property
    def exc_traceback(self) -> TracebackType | None: ...
    @property
    def thread(self) -> Thread | None: ...

_excepthook: Callable[[_ExceptHookArgs], Any]

if sys.version_info >= (3, 12):
    def daemon_threads_allowed() -> bool: ...

class _local:
    def __getattribute__(self, name: str, /) -> Any: ...
    def __setattr__(self, name: str, value: Any, /) -> None: ...
    def __delattr__(self, name: str, /) -> None: ...
