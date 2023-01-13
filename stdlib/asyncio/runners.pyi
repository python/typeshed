import sys
from _typeshed import Self
from collections.abc import Callable, Coroutine
from contextvars import Context
from types import TracebackType
from typing import Any, TypeVar
from typing_extensions import final

from .events import AbstractEventLoop

if sys.version_info >= (3, 11):
    __all__ = ("Runner", "run")
else:
    __all__ = ("run",)
_T = TypeVar("_T")

if sys.version_info >= (3, 11):
    @final
    class Runner:
        def __init__(self, *, debug: bool | None = ..., loop_factory: Callable[[], AbstractEventLoop] | None = ...) -> None: ...
        def __enter__(self: Self) -> Self: ...
        def __exit__(
            self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
        ) -> None: ...
        def close(self) -> None: ...
        def get_loop(self) -> AbstractEventLoop: ...
        def run(self, coro: Coroutine[Any, Any, _T], *, context: Context | None = ...) -> _T: ...

if sys.version_info >= (3, 12):
    def run(
        main: Coroutine[Any, Any, _T], *, debug: bool | None = ..., loop_factory: Callable[[], AbstractEventLoop] | None = ...
    ) -> _T: ...

elif sys.version_info >= (3, 8):
    def run(main: Coroutine[Any, Any, _T], *, debug: bool | None = ...) -> _T: ...

else:
    def run(main: Coroutine[Any, Any, _T], *, debug: bool = ...) -> _T: ...
