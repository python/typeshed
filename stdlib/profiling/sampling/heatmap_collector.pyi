from _typeshed import StrOrBytesPath
from typing import Any

from .stack_collector import StackTraceCollector as StackTraceCollector

class HeatmapCollector(StackTraceCollector):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def set_stats(
        self,
        sample_interval_usec: int,
        duration_sec: float,
        sample_rate: float,
        error_rate: float | None = None,
        missed_samples: int | None = None,
        **kwargs: Any,
    ) -> None: ...
    def process_frames(self, frames: list[Any], thread_id: int, weight: int = 1) -> None: ...
    def export(self, output_path: StrOrBytesPath) -> None: ...
