from collections import deque

from .collector import Collector as Collector

class SampleProfiler:
    pid: int
    sample_interval_usec: int
    all_threads: bool
    mode: int
    collect_stats: bool
    blocking: bool
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
