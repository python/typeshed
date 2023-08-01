import sys
from _typeshed import FileDescriptor
from collections.abc import Callable
from typing_extensions import ParamSpec, TypeAlias

from gevent._ffi import watcher as _base
from gevent.libev.corecffi import loop as cffi_loop

if sys.platform != "win32":
    from gevent.libev.corecext import loop as cext_loop

    _Loop: TypeAlias = cffi_loop | cext_loop
else:
    _Loop: TypeAlias = cffi_loop

_P = ParamSpec("_P")

class watcher(_base.watcher):
    def __init__(self, _loop: _Loop, ref: bool = True, priority: int | None = None) -> None: ...
    @property
    def ref(self) -> bool: ...
    @ref.setter
    def ref(self, value: bool) -> None: ...
    # does not accept keyword arguments
    def feed(self, revents: int, callback: Callable[_P, object], *args: _P.args, **_: _P.kwargs) -> None: ...

class io(_base.IoMixin, watcher):
    EVENT_MASK: int
    @property
    def fd(self) -> FileDescriptor: ...
    @fd.setter
    def fd(self, value: FileDescriptor) -> None: ...
    @property
    def events(self) -> int: ...
    @events.setter
    def events(self, events: int) -> None: ...
    @property
    def events_str(self) -> str: ...

class timer(_base.TimerMixin, watcher):
    @property
    def at(self) -> float: ...

class signal(_base.SignalMixin, watcher): ...
class idle(_base.IdleMixin, watcher): ...
class prepare(_base.PrepareMixin, watcher): ...
class check(_base.CheckMixin, watcher): ...
class fork(_base.ForkMixin, watcher): ...
class async_(_base.AsyncMixin, watcher): ...

class child(_base.ChildMixin, watcher):
    @property
    def rpid(self) -> int: ...
    @rpid.setter
    def rpid(self, value: int) -> None: ...
    @property
    def rstatus(self) -> int: ...
    @rstatus.setter
    def rstatus(self, value: int) -> None: ...

class stat(_base.StatMixin, watcher):
    @property
    def interval(self) -> float: ...
    @interval.setter
    def interval(self, value: float) -> None: ...

__all__: list[str] = []
