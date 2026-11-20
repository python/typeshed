from asyncio import AbstractEventLoop
from collections.abc import Mapping
from typing import Any, type_check_only
from typing_extensions import Unpack

from apscheduler.schedulers.base import BaseScheduler, _SchedulerOptions

# event_loop may be given as a textual reference ("module:attribute") to the loop; None takes the
# running loop when the scheduler starts.
@type_check_only
class _AsyncIOSchedulerOptions(_SchedulerOptions, total=False):
    event_loop: AbstractEventLoop | str | None

class AsyncIOScheduler(BaseScheduler):
    # gconfig holds the options under keys starting with prefix, as BaseScheduler's does.
    def __init__(self, gconfig: Mapping[str, Any] = ..., **options: Unpack[_AsyncIOSchedulerOptions]) -> None: ...
    def configure(
        self, gconfig: Mapping[str, Any] = ..., prefix: str | None = "apscheduler.", **options: Unpack[_AsyncIOSchedulerOptions]
    ) -> None: ...
    def start(self, paused: bool = False) -> None: ...
    def shutdown(self, wait: bool = True) -> None: ...
    def wakeup(self) -> None: ...
