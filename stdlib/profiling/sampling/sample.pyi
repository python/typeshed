from _typeshed import Incomplete
from collections import deque

from .binary_collector import BinaryCollector as BinaryCollector
from .collector import Collector as Collector
from .constants import (
    PROFILING_MODE_ALL as PROFILING_MODE_ALL,
    PROFILING_MODE_CPU as PROFILING_MODE_CPU,
    PROFILING_MODE_EXCEPTION as PROFILING_MODE_EXCEPTION,
    PROFILING_MODE_GIL as PROFILING_MODE_GIL,
    PROFILING_MODE_WALL as PROFILING_MODE_WALL,
)
from .gecko_collector import GeckoCollector as GeckoCollector
from .heatmap_collector import HeatmapCollector as HeatmapCollector
from .live_collector import LiveStatsCollector as LiveStatsCollector
from .pstats_collector import PstatsCollector as PstatsCollector
from .stack_collector import CollapsedStackCollector as CollapsedStackCollector, FlamegraphCollector as FlamegraphCollector

class SampleProfiler:
    pid: int
    sample_interval_usec: int
    all_threads: bool
    mode: int
    collect_stats: bool
    blocking: bool
    unwinder: Incomplete
    sample_intervals: deque[float]
    total_samples: int
    realtime_stats: bool
    def __init__(
        self,
        pid: int,
        sample_interval_usec: int,
        all_threads: bool,
        *,
        mode: int = ...,
        native: bool = False,
        gc: bool = True,
        opcodes: bool = False,
        skip_non_matching_threads: bool = True,
        collect_stats: bool = False,
        blocking: bool = False,
    ) -> None: ...
    def sample(self, collector: Collector, duration_sec: float | None = None, *, async_aware: bool | str = False) -> None: ...

def sample(
    pid: int,
    collector: Collector,
    *,
    duration_sec: float | None = None,
    all_threads: bool = False,
    realtime_stats: bool = False,
    mode: int = ...,
    async_aware: str | bool | None = None,
    native: bool = False,
    gc: bool = True,
    opcodes: bool = False,
    blocking: bool = False,
) -> None: ...
def sample_live(
    pid: int,
    collector: Collector,
    *,
    duration_sec: float | None = None,
    all_threads: bool = False,
    realtime_stats: bool = False,
    mode: int = ...,
    async_aware: str | bool | None = None,
    native: bool = False,
    gc: bool = True,
    opcodes: bool = False,
    blocking: bool = False,
) -> None: ...
