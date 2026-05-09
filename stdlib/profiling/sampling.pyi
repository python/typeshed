from _typeshed import StrOrBytesPath
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Protocol, TypeAlias

__all__ = (
    "Collector",
    "PstatsCollector",
    "CollapsedStackCollector",
    "HeatmapCollector",
    "GeckoCollector",
    "JsonlCollector",
    "StringTable",
)

_Location: TypeAlias = int | tuple[int, int, int, int] | None
_Timestamps: TypeAlias = Sequence[int] | None

class _FrameInfo(Protocol):
    filename: str
    location: _Location
    funcname: str
    def __getitem__(self, index: int, /) -> object: ...

class _ThreadInfo(Protocol):
    status: int
    thread_id: int
    frame_info: Sequence[_FrameInfo]

class _InterpreterInfo(Protocol):
    threads: Sequence[_ThreadInfo]

class _CoroutineInfo(Protocol):
    call_stack: Sequence[_FrameInfo]

class _TaskInfo(Protocol):
    task_id: int
    task_name: str
    awaited_by: Sequence[_TaskInfo]
    coroutine_stack: Sequence[_CoroutineInfo]

class _AwaitedInfo(Protocol):
    thread_id: int
    awaited_by: Sequence[_TaskInfo]

_StackFrames: TypeAlias = Sequence[_InterpreterInfo] | Sequence[_AwaitedInfo]

class Collector(ABC):
    @abstractmethod
    def collect(self, stack_frames: _StackFrames, timestamps_us: _Timestamps = None) -> None: ...
    def collect_failed_sample(self) -> None: ...
    @abstractmethod
    def export(self, filename: StrOrBytesPath) -> None: ...

class PstatsCollector(Collector):
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False) -> None: ...
    def collect(self, stack_frames: _StackFrames, timestamps_us: _Timestamps = None) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...
    def create_stats(self) -> None: ...
    def print_stats(
        self, sort: int = -1, limit: int | None = None, show_summary: bool = True, mode: int | None = None
    ) -> None: ...

class CollapsedStackCollector(Collector):
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False) -> None: ...
    def collect(self, stack_frames: _StackFrames, timestamps_us: _Timestamps = None) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...
    def process_frames(self, frames: Sequence[_FrameInfo], thread_id: int, weight: int = 1) -> None: ...

class HeatmapCollector(Collector):
    FILE_INDEX_FORMAT: str
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False) -> None: ...
    def collect(self, stack_frames: _StackFrames, timestamps_us: _Timestamps = None) -> None: ...
    def export(self, output_path: StrOrBytesPath) -> None: ...
    def process_frames(self, frames: Sequence[_FrameInfo], thread_id: int, weight: int = 1) -> None: ...
    def set_stats(
        self,
        sample_interval_usec: int,
        duration_sec: float,
        sample_rate: float,
        error_rate: float | None = None,
        missed_samples: float | None = None,
        **kwargs: object,
    ) -> None: ...

class GeckoCollector(Collector):
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False, opcodes: bool = False) -> None: ...
    def collect(self, stack_frames: _StackFrames, timestamps_us: _Timestamps = None) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...

class JsonlCollector(Collector):
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False, mode: int | None = None) -> None: ...
    def collect(self, stack_frames: _StackFrames, timestamps_us: _Timestamps = None) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...
    def process_frames(self, frames: Sequence[_FrameInfo], _thread_id: int, weight: int = 1) -> None: ...

class StringTable:
    def intern(self, string: object) -> int: ...
    def get_string(self, index: int) -> str: ...
    def get_strings(self) -> list[str]: ...
    def __len__(self) -> int: ...
