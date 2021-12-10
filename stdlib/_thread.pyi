import sys
from _typeshed import structseq
from threading import Thread
from types import TracebackType
from typing import Any, Callable, NoReturn, Optional, Tuple, Type
from typing_extensions import final

error = RuntimeError

def _count() -> int: ...

_dangling: Any

@final
class LockType:
    def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...
    def __enter__(self) -> bool: ...
    def __exit__(
        self, type: Type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...

def start_new_thread(function: Callable[..., Any], args: Tuple[Any, ...], kwargs: dict[str, Any] = ...) -> int: ...
def interrupt_main() -> None: ...
def exit() -> NoReturn: ...
def allocate_lock() -> LockType: ...
def get_ident() -> int: ...
def stack_size(size: int = ...) -> int: ...

TIMEOUT_MAX: float

if sys.version_info >= (3, 8):
    def get_native_id() -> int: ...  # only available on some platforms
    # Constructor of _ExceptHookArgs takes an iterable of length 4.
    @final
    class _ExceptHookArgs(structseq[Any], Tuple[Type[BaseException], Optional[BaseException], Optional[TracebackType], Optional[Thread]]):
        @property
        def exc_type(self) -> Type[BaseException]: ...
        @property
        def exc_value(self) -> BaseException | None: ...
        @property
        def exc_traceback(self) -> TracebackType | None: ...
        @property
        def thread(self) -> Thread | None: ...
    _excepthook: Callable[[_ExceptHookArgs], Any]
