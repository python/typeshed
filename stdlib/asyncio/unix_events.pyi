import sys
import types
from socket import socket
from typing import Any, Callable, Type, TypeVar

from .events import AbstractEventLoop, AbstractServer, BaseDefaultEventLoopPolicy, _ProtocolFactory, _SSLContext
from .selector_events import BaseSelectorEventLoop

_T1 = TypeVar("_T1", bound=AbstractChildWatcher)
_T2 = TypeVar("_T2", bound=SafeChildWatcher)
_T3 = TypeVar("_T3", bound=FastChildWatcher)

class AbstractChildWatcher:
    def add_child_handler(self, pid: int, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_child_handler(self, pid: int) -> bool: ...
    def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...
    def close(self) -> None: ...
    def __enter__(self: _T1) -> _T1: ...
    def __exit__(self, typ: Type[BaseException] | None, exc: BaseException | None, tb: types.TracebackType | None) -> None: ...
    if sys.version_info >= (3, 8):
        def is_active(self) -> bool: ...

class BaseChildWatcher(AbstractChildWatcher):
    def __init__(self) -> None: ...

class SafeChildWatcher(BaseChildWatcher):
    def __enter__(self: _T2) -> _T2: ...

class FastChildWatcher(BaseChildWatcher):
    def __enter__(self: _T3) -> _T3: ...

class _UnixSelectorEventLoop(BaseSelectorEventLoop):
    if sys.version_info < (3, 7):
        async def create_unix_server(
            self,
            protocol_factory: _ProtocolFactory,
            path: str | None = ...,
            *,
            sock: socket | None = ...,
            backlog: int = ...,
            ssl: _SSLContext = ...,
        ) -> AbstractServer: ...

class _UnixDefaultEventLoopPolicy(BaseDefaultEventLoopPolicy):
    def get_child_watcher(self) -> AbstractChildWatcher: ...
    def set_child_watcher(self, watcher: AbstractChildWatcher | None) -> None: ...

SelectorEventLoop = _UnixSelectorEventLoop

DefaultEventLoopPolicy = _UnixDefaultEventLoopPolicy

if sys.version_info >= (3, 8):

    from typing import Protocol

    _T4 = TypeVar("_T4", bound=MultiLoopChildWatcher)
    _T5 = TypeVar("_T5", bound=ThreadedChildWatcher)
    class _Warn(Protocol):
        def __call__(
            self, message: str, category: Type[Warning] | None = ..., stacklevel: int = ..., source: Any | None = ...
        ) -> None: ...
    class MultiLoopChildWatcher(AbstractChildWatcher):
        def __enter__(self: _T4) -> _T4: ...
    class ThreadedChildWatcher(AbstractChildWatcher):
        def __enter__(self: _T5) -> _T5: ...
        def __del__(self, _warn: _Warn = ...) -> None: ...
