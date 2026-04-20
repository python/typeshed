from _typeshed import StrOrBytesPath
from typing import Any

from ..collector import Collector as Collector
from .display import DisplayInterface as DisplayInterface

class LiveStatsCollector(Collector):
    result: dict[Any, Any]
    sample_interval_usec: int
    sample_interval_sec: float
    skip_idle: bool
    sort_by: str
    limit: int
    total_samples: int
    successful_samples: int
    failed_samples: int
    start_time: float | None
    running: bool
    finished: bool
    finish_timestamp: float | None
    finish_wall_time: float | None
    pid: int | None
    mode: int | None
    async_aware: str | bool | None
    max_sample_rate: int
    display: DisplayInterface | None
    thread_ids: list[int]
    def __init__(
        self,
        sample_interval_usec: int,
        *,
        skip_idle: bool = False,
        sort_by: str = ...,
        limit: int = ...,
        pid: int | None = None,
        display: DisplayInterface | None = None,
        mode: int | None = None,
        opcodes: bool = False,
        async_aware: str | bool | None = None,
    ) -> None: ...
    @property
    def elapsed_time(self) -> float: ...
    @property
    def current_time_display(self) -> str: ...
    def collect_failed_sample(self) -> None: ...
    def collect(self, stack_frames: Any, timestamp_us: int | None = None) -> None: ...
    def build_stats_list(self) -> list[Any]: ...
    def reset_stats(self) -> None: ...
    def mark_finished(self) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...
