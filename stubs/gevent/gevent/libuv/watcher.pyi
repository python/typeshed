from gevent._ffi import watcher as _base
from gevent._types import _IoWatcher

class watcher(_base.watcher):
    @property
    def ref(self) -> bool: ...
    @ref.setter
    def ref(self, value: bool) -> None: ...

class io(_base.IoMixin, watcher):
    EVENT_MASK: int
    def multiplex(self, events: int) -> _IoWatcher: ...

class fork(_base.ForkMixin, watcher): ...
class child(_base.ChildMixin, watcher): ...

# for some reason pending on this has been overwritten with None, but we don't
# necessarily want to change our Protocol to reflect that, so for now we ignore it
class async_(_base.AsyncMixin, watcher): ...
class timer(_base.TimerMixin, watcher): ...

class stat(_base.StatMixin, watcher):
    MIN_STAT_INTERVAL: float

class signal(_base.SignalMixin, watcher): ...
class idle(_base.IdleMixin, watcher): ...
class check(_base.CheckMixin, watcher): ...
class prepare(_base.PrepareMixin, watcher): ...
