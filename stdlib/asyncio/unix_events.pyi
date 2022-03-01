import sys
import types
from _typeshed import Self
from abc import ABCMeta, abstractmethod
from socket import socket
from typing import Any, Callable
from typing_extensions import Literal

from .base_events import Server
from .events import AbstractEventLoop, BaseDefaultEventLoopPolicy, _ProtocolFactory, _SSLContext
from .selector_events import BaseSelectorEventLoop

# This is also technically not available on Win,
# but other parts of typeshed need this defintion.
# So, it is special cased.
class AbstractChildWatcher:
    @abstractmethod
    def add_child_handler(self, pid: int, callback: Callable[..., Any], *args: Any) -> None: ...
    @abstractmethod
    def remove_child_handler(self, pid: int) -> bool: ...
    @abstractmethod
    def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...
    @abstractmethod
    def close(self) -> None: ...
    @abstractmethod
    def __enter__(self: Self) -> Self: ...
    @abstractmethod
    def __exit__(self, typ: type[BaseException] | None, exc: BaseException | None, tb: types.TracebackType | None) -> None: ...
    if sys.version_info >= (3, 8):
        @abstractmethod
        def is_active(self) -> bool: ...

if sys.platform != "win32":
    if sys.version_info >= (3, 9):
        __all__ = (
            "SelectorEventLoop",
            "AbstractChildWatcher",
            "SafeChildWatcher",
            "FastChildWatcher",
            "PidfdChildWatcher",
            "MultiLoopChildWatcher",
            "ThreadedChildWatcher",
            "DefaultEventLoopPolicy",
        )
    elif sys.version_info >= (3, 8):
        __all__ = (
            "SelectorEventLoop",
            "AbstractChildWatcher",
            "SafeChildWatcher",
            "FastChildWatcher",
            "MultiLoopChildWatcher",
            "ThreadedChildWatcher",
            "DefaultEventLoopPolicy",
        )
    elif sys.version_info >= (3, 7):
        __all__ = ("SelectorEventLoop", "AbstractChildWatcher", "SafeChildWatcher", "FastChildWatcher", "DefaultEventLoopPolicy")
    else:
        __all__ = ["SelectorEventLoop", "AbstractChildWatcher", "SafeChildWatcher", "FastChildWatcher", "DefaultEventLoopPolicy"]

    class BaseChildWatcher(AbstractChildWatcher, metaclass=ABCMeta):
        def __init__(self) -> None: ...
        def close(self) -> None: ...
        if sys.version_info >= (3, 8):
            def is_active(self) -> bool: ...

        def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...

    class SafeChildWatcher(BaseChildWatcher):
        def __enter__(self: Self) -> Self: ...
        def __exit__(self, a: type[BaseException] | None, b: BaseException | None, c: types.TracebackType | None) -> None: ...
        def add_child_handler(self, pid: int, callback: Callable[..., Any], *args: Any) -> None: ...
        def remove_child_handler(self, pid: int) -> bool: ...

    class FastChildWatcher(BaseChildWatcher):
        def __enter__(self: Self) -> Self: ...
        def __exit__(self, a: type[BaseException] | None, b: BaseException | None, c: types.TracebackType | None) -> None: ...
        def add_child_handler(self, pid: int, callback: Callable[..., Any], *args: Any) -> None: ...
        def remove_child_handler(self, pid: int) -> bool: ...

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
            ) -> Server: ...

    class _UnixDefaultEventLoopPolicy(BaseDefaultEventLoopPolicy):
        def get_child_watcher(self) -> AbstractChildWatcher: ...
        def set_child_watcher(self, watcher: AbstractChildWatcher | None) -> None: ...
    SelectorEventLoop = _UnixSelectorEventLoop

    DefaultEventLoopPolicy = _UnixDefaultEventLoopPolicy

    if sys.version_info >= (3, 8):

        from typing import Protocol

        class _Warn(Protocol):
            def __call__(
                self, message: str, category: type[Warning] | None = ..., stacklevel: int = ..., source: Any | None = ...
            ) -> None: ...

        class MultiLoopChildWatcher(AbstractChildWatcher):
            def __init__(self) -> None: ...
            def is_active(self) -> bool: ...
            def close(self) -> None: ...
            def __enter__(self: Self) -> Self: ...
            def __exit__(
                self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None
            ) -> None: ...
            def add_child_handler(self, pid: int, callback: Callable[..., Any], *args: Any) -> None: ...
            def remove_child_handler(self, pid: int) -> bool: ...
            def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...

        class ThreadedChildWatcher(AbstractChildWatcher):
            def __init__(self) -> None: ...
            def is_active(self) -> Literal[True]: ...
            def close(self) -> None: ...
            def __enter__(self: Self) -> Self: ...
            def __exit__(
                self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None
            ) -> None: ...
            def __del__(self, _warn: _Warn = ...) -> None: ...
            def add_child_handler(self, pid: int, callback: Callable[..., Any], *args: Any) -> None: ...
            def remove_child_handler(self, pid: int) -> bool: ...
            def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...

    if sys.version_info >= (3, 9):
        class PidfdChildWatcher(AbstractChildWatcher):
            def __init__(self) -> None: ...
            def __enter__(self: Self) -> Self: ...
            def __exit__(
                self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None
            ) -> None: ...
            def is_active(self) -> bool: ...
            def close(self) -> None: ...
            def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...
            def add_child_handler(self, pid: int, callback: Callable[..., Any], *args: Any) -> None: ...
            def remove_child_handler(self, pid: int) -> bool: ...
