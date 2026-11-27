from collections.abc import Mapping
from typing import Any, type_check_only
from typing_extensions import Unpack

from apscheduler.schedulers.base import BaseScheduler, _SchedulerOptions

# reactor may be given as a textual reference ("module:attribute") to the reactor; absent, it is
# Twisted's global reactor.
@type_check_only
class _TwistedSchedulerOptions(_SchedulerOptions, total=False):
    reactor: Any  # Any: Twisted's global reactor, which type checkers see as a module

class TwistedScheduler(BaseScheduler):
    # gconfig holds the options under keys starting with prefix, as BaseScheduler's does.
    def __init__(self, gconfig: Mapping[str, Any] = ..., **options: Unpack[_TwistedSchedulerOptions]) -> None: ...
    def configure(
        self, gconfig: Mapping[str, Any] = ..., prefix: str | None = "apscheduler.", **options: Unpack[_TwistedSchedulerOptions]
    ) -> None: ...
    def shutdown(self, wait: bool = True) -> None: ...
    def wakeup(self) -> None: ...
