import sys
from _typeshed import FileDescriptor
from collections.abc import Callable
from types import TracebackType
from typing import Protocol
from typing_extensions import TypeAlias, TypeVarTuple, Unpack

from gevent._types import _AsyncWatcher, _Callback, _ChildWatcher, _IoWatcher, _StatWatcher, _TimerWatcher, _Watcher

_Ts = TypeVarTuple("_Ts")
_ErrorHandlerFunc: TypeAlias = Callable[
    [object | None, type[BaseException] | None, BaseException | None, TracebackType | None], object
]

class _SupportsHandleError(Protocol):
    handle_error: _ErrorHandlerFunc

_ErrorHandler: TypeAlias = _ErrorHandlerFunc | _SupportsHandleError

class AbstractLoop:
    CALLBACK_CHECK_COUNT: int
    error_handler: _ErrorHandler | None
    starting_timer_may_update_loop_time: bool
    # internal API, this __init__ will only be called from subclasses
    def __init__(
        self, ffi: object, lib: object, watchers: object, flags: int | None = ..., default: bool | None = ...
    ) -> None: ...
    def destroy(self) -> bool | None: ...
    @property
    def ptr(self) -> int: ...
    @property
    def WatcherType(self) -> type[_Watcher]: ...
    @property
    def MAXPRI(self) -> int: ...
    @property
    def MINPRI(self) -> int: ...
    def handle_error(
        self, context: object | None, type: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None
    ) -> None: ...
    def run(self, nowait: bool = False, once: bool = False) -> None: ...
    def reinit(self) -> None: ...
    def ref(self) -> None: ...
    def unref(self) -> None: ...
    def break_(self, how: int | None = ...) -> None: ...
    def verify(self) -> None: ...
    def now(self) -> float: ...
    def update_now(self) -> None: ...
    update = update_now  # deprecated
    @property
    def default(self) -> bool: ...
    @property
    def iteration(self) -> int: ...
    @property
    def depth(self) -> int: ...
    @property
    def backend_int(self) -> int: ...
    @property
    def backend(self) -> str | int: ...
    @property
    def pendingcnt(self) -> int: ...
    @property
    def activecnt(self) -> int: ...
    def io(self, fd: FileDescriptor, events: int, ref: bool = True, priority: int | None = None) -> _IoWatcher: ...
    def closing_fd(self, fd: FileDescriptor) -> bool: ...
    def timer(self, after: float, repeat: float = 0.0, ref: bool = True, priority: int | None = None) -> _TimerWatcher: ...
    def signal(self, signum: int, ref: bool = True, priority: int | None = None) -> _Watcher: ...
    def idle(self, ref: bool = True, priority: int | None = None) -> _Watcher: ...
    def prepare(self, ref: bool = True, priority: int | None = None) -> _Watcher: ...
    def check(self, ref: bool = True, priority: int | None = None) -> _Watcher: ...
    if sys.platform != "win32":
        def fork(self, ref: bool = True, priority: int | None = None) -> _Watcher: ...
        def child(self, pid: int, trace: int = 0, ref: bool = True) -> _ChildWatcher: ...
        def install_sigchld(self) -> None: ...

    def async_(self, ref: bool = True, priority: int | None = None) -> _AsyncWatcher: ...
    def stat(self, path: str, interval: float = 0.0, ref: bool = True, priority: bool | None = ...) -> _StatWatcher: ...
    def run_callback(self, func: Callable[[Unpack[_Ts]], object], *args: Unpack[_Ts]) -> _Callback: ...
    def run_callback_threadsafe(self, func: Callable[[Unpack[_Ts]], object], *args: Unpack[_Ts]) -> _Callback: ...
    def callback(self, priority: float | None = ...) -> _Callback: ...
    def fileno(self) -> FileDescriptor | None: ...
