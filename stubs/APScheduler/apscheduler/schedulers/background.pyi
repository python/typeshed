from collections.abc import Mapping
from typing import Any, type_check_only
from typing_extensions import Unpack

from apscheduler.schedulers.base import _SchedulerOptions
from apscheduler.schedulers.blocking import BlockingScheduler

# daemon may be given as a string such as "true" or "off".
@type_check_only
class _BackgroundSchedulerOptions(_SchedulerOptions, total=False):
    daemon: bool | str

class BackgroundScheduler(BlockingScheduler):
    # gconfig holds the options under keys starting with prefix, as BaseScheduler's does.
    def __init__(self, gconfig: Mapping[str, Any] = ..., **options: Unpack[_BackgroundSchedulerOptions]) -> None: ...
    def configure(
        self,
        gconfig: Mapping[str, Any] = ...,
        prefix: str | None = "apscheduler.",
        **options: Unpack[_BackgroundSchedulerOptions],
    ) -> None: ...
