from _typeshed import StrOrBytesPath
from typing import Any

from .collector import Collector as Collector, extract_lineno as extract_lineno
from .constants import MICROSECONDS_PER_SECOND as MICROSECONDS_PER_SECOND, PROFILING_MODE_CPU as PROFILING_MODE_CPU

class PstatsCollector(Collector):
    result: dict[Any, Any]
    stats: dict[Any, Any]
    sample_interval_usec: int
    callers: dict[Any, Any]
    skip_idle: bool
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False) -> None: ...
    def collect(self, stack_frames: Any, timestamps_us: list[int] | None = None) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...
    def create_stats(self) -> None: ...
    def print_stats(self, sort: str | int = -1, limit: int | None = None, show_summary: bool = True, mode: int | None = None) -> None: ...
