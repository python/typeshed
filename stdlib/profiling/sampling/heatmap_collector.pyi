from _typeshed import FloatInt, StrOrBytesPath
from collections.abc import Sequence

from _remote_debugging import AwaitedInfo, InterpreterInfo

from .collector import Collector, _Frame, _Timestamps

class HeatmapCollector(Collector):
    FILE_INDEX_FORMAT: str
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False) -> None: ...
    def collect(
        self, stack_frames: Sequence[InterpreterInfo] | Sequence[AwaitedInfo], timestamps_us: _Timestamps = None
    ) -> None: ...
    def export(self, output_path: StrOrBytesPath) -> None: ...
    def process_frames(self, frames: Sequence[_Frame], thread_id: int, weight: int = 1) -> None: ...
    def set_stats(
        self,
        sample_interval_usec: int,
        duration_sec: FloatInt,
        sample_rate: FloatInt,
        error_rate: FloatInt | None = None,
        missed_samples: FloatInt | None = None,
        **kwargs: object,
    ) -> None: ...
