from collections.abc import Callable, Mapping
from datetime import timedelta
from typing import Any, Protocol, type_check_only
from typing_extensions import Unpack

from apscheduler.schedulers.base import BaseScheduler, _SchedulerOptions

# What the scheduler calls on its loop, such as a tornado.ioloop.IOLoop.
@type_check_only
class _IOLoop(Protocol):
    def add_callback(self, callback: Callable[..., object], /, *args: Any, **kwargs: Any) -> None: ...  # Any: callback's
    def add_timeout(
        self, deadline: timedelta, callback: Callable[..., object], /, *args: Any, **kwargs: Any  # Any: callback's
    ) -> object: ...
    def remove_timeout(self, timeout: object, /) -> None: ...

# io_loop may be given as a textual reference ("module:attribute") to the loop; None takes the
# current IOLoop.
@type_check_only
class _TornadoSchedulerOptions(_SchedulerOptions, total=False):
    io_loop: _IOLoop | str | None

class TornadoScheduler(BaseScheduler):
    # gconfig holds the options under keys starting with prefix, as BaseScheduler's does.
    def __init__(self, gconfig: Mapping[str, Any] = ..., **options: Unpack[_TornadoSchedulerOptions]) -> None: ...
    def configure(
        self, gconfig: Mapping[str, Any] = ..., prefix: str | None = "apscheduler.", **options: Unpack[_TornadoSchedulerOptions]
    ) -> None: ...
    def shutdown(self, wait: bool = True) -> None: ...
    def wakeup(self) -> None: ...
