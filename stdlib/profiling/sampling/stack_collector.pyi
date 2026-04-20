import abc
from _typeshed import StrOrBytesPath
from collections import Counter
from typing import Any

from .collector import Collector as Collector, extract_lineno as extract_lineno
from .opcode_utils import get_opcode_mapping as get_opcode_mapping
from .string_table import StringTable as StringTable

class StackTraceCollector(Collector, metaclass=abc.ABCMeta):
    sample_interval_usec: int
    skip_idle: bool
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False) -> None: ...
    def collect(self, stack_frames: Any, timestamps_us: list[int] | None = None) -> None: ...
    def process_frames(self, frames: list[Any], thread_id: int, weight: int = 1) -> None: ...

class CollapsedStackCollector(StackTraceCollector):
    stack_counter: Counter[str]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def process_frames(self, frames: list[Any], thread_id: int, weight: int = 1) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...

class FlamegraphCollector(StackTraceCollector):
    stats: dict[str, Any]
    thread_status_counts: dict[str, int]
    samples_with_gc_frames: int
    per_thread_stats: dict[int, Any]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def collect(self, stack_frames: Any, timestamps_us: list[int] | None = None) -> None: ...
    def set_stats(
        self,
        sample_interval_usec: int,
        duration_sec: float,
        sample_rate: float,
        error_rate: float | None = None,
        missed_samples: int | None = None,
        mode: int | None = None,
    ) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...
    def process_frames(self, frames: list[Any], thread_id: int, weight: int = 1) -> None: ...

class DiffFlamegraphCollector(FlamegraphCollector):
    baseline_binary_path: str
    def __init__(self, sample_interval_usec: int, *, baseline_binary_path: str, skip_idle: bool = False) -> None: ...
