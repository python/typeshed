from _typeshed import Self
from contextvars import Context
from .events import AbstractEventLoop
import sys
from collections.abc import Coroutine
from typing import Any, TypeVar

if sys.version_info >= (3, 11):
    __all__ = ("Runner", "run")
else:
    __all__ = ("run",)
_T = TypeVar("_T")

if sys.version_info >= (3, 11):
    class Runner:
        def __init__(self, *, debug: bool | None = ..., loop_factory: Callable[[], AbstractEventLoop] | None = ...) -> None: ...
        def __enter__(self: Self) -> Self: ...
        def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None: ...
        def close(self) -> None: ...
        def get_loop(self) -> AbstractEventLoop: ...
        def run(self, coro: Coroutine[Any, Any, _T], *, context: Context | None = ...) -> _T: ...

if sys.version_info >= (3, 8):
    def run(main: Coroutine[Any, Any, _T], *, debug: bool | None = ...) -> _T: ...

else:
    def run(main: Coroutine[Any, Any, _T], *, debug: bool = ...) -> _T: ...
