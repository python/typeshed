import sys
from _typeshed import FileDescriptor, StrOrBytesPath
from collections.abc import Callable
from types import TracebackType
from typing import Any, Protocol, overload
from typing_extensions import Literal, TypeAlias, TypeVarTuple, Unpack

_Ts = TypeVarTuple("_Ts")

# gevent uses zope.interface interanlly which does not work well with type checkers
# partially due to the odd call signatures without self and partially due to them
# behaving essentially like a Protocol, so a mypy plugin is necessary to type check
# them correctly, and then you still have to give up on some valuable features due
# to the missing self/cls argument.
# To ensure maximum compatibility with other type checkers and so we don't depend
# on mypy-zope we define an equivalent Protocol for each interface, which we will
# use on arguments in place of the interface
# it also looks like ILoop is possibly too strict, since there are additional
# properties and methods that are available on all event loops, so these have
# been added as well, instead of completely mirroring the internal interface

class _Loop(Protocol):  # noqa: Y046
    @property
    def approx_timer_resolution(self) -> float: ...
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
    def destroy(self) -> None: ...
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
    def run_callback(self, func: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts]) -> _Callback: ...
    def run_callback_threadsafe(self, func: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts]) -> _Callback: ...
    def fileno(self) -> FileDescriptor | None: ...

class _Watcher(Protocol):
    # while IWatcher allows for kwargs the actual implementation does not...
    def start(self, callback: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts]) -> None: ...
    def stop(self) -> None: ...
    def close(self) -> None: ...

# this matches Intersection[_Watcher, TimerMixin]
class _TimerWatcher(_Watcher, Protocol):
    # this has one specific allowed keyword argument, if it is given we don't try to check
    # the passed in arguments, but if it isn't passed in, then we do.
    @overload
    def start(self, callback: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts], update: bool) -> None: ...
    @overload
    def start(self, callback: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts]) -> None: ...
    @overload
    def again(self, callback: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts], update: bool) -> None: ...
    @overload
    def again(self, callback: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts]) -> None: ...

# this matches Intersection[_Watcher, IoMixin]
class _IoWatcher(_Watcher, Protocol):
    EVENT_MASK: int
    # pass_events means the first argument of the callback needs to be an integer, but we can't
    # type check the other passed in args in this case
    @overload
    def start(self, callback: Callable[[int, Unpack[_Ts]], Any], *args: Unpack[_Ts], pass_events: Literal[True]) -> None: ...
    @overload
    def start(self, callback: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts]) -> None: ...

# this matches Intersection[_Watcher, ChildMixin]
class _ChildWatcher(_Watcher, Protocol):
    @property
    def pid(self) -> int: ...
    @property
    def rpid(self) -> int | None: ...
    @property
    def rstatus(self) -> int: ...

# this matches Intersection[_Watcher, AsyncMixin]
class _AsyncWatcher(_Watcher, Protocol):
    def send(self) -> None: ...
    def send_ignoring_arg(self, __ignored: object) -> None: ...
    @property
    def pending(self) -> bool: ...

# all implementations return something of this shape
class _StatResult(Protocol):
    @property
    def st_nlink(self) -> int: ...

# this matches Intersection[_Watcher, StatMixin]
class _StatWatcher(_Watcher, Protocol):
    @property
    def path(self) -> StrOrBytesPath: ...
    @property
    def attr(self) -> _StatResult | None: ...
    @property
    def prev(self) -> _StatResult | None: ...
    @property
    def interval(self) -> float: ...

class _Callback(Protocol):
    pending: bool
    def stop(self) -> None: ...
    def close(self) -> None: ...

_FullSockAddr: TypeAlias = tuple[str, int, int, int]  # host, port, flowinfo, scopeid
_SockAddr: TypeAlias = _FullSockAddr | tuple[str, int]
_AddrinfoResult: TypeAlias = list[tuple[int, int, int, str, _SockAddr]]  # family, type, protocol, cname, sockaddr
_NameinfoResult: TypeAlias = tuple[str, str]

class _Resolver(Protocol):  # noqa: Y046
    def close(self) -> None: ...
    def gethostbyname(self, hostname: str, family: int = 2) -> str: ...
    def gethostbyname_ex(self, hostname: str, family: int = 2) -> tuple[str, list[str], list[str]]: ...
    def getaddrinfo(
        self, host: str, port: int, family: int = 0, socktype: int = 0, proto: int = 0, flags: int = 0
    ) -> _AddrinfoResult: ...
    def gethostbyaddr(self, ip_address: str) -> tuple[str, list[str], list[str]]: ...
    def getnameinfo(self, sockaddr: _SockAddr, flags: int) -> _NameinfoResult: ...
