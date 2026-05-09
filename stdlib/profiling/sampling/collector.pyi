from _typeshed import StrOrBytesPath
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Protocol, TypeAlias

_Location: TypeAlias = int | tuple[int, int, int, int] | _LocationInfo | None
_Frame: TypeAlias = _FrameInfo | tuple[str, _Location, str, int | None]
_Timestamps: TypeAlias = Sequence[int] | None
_StackFrames: TypeAlias = Sequence[_InterpreterInfo] | Sequence[_AwaitedInfo]

class _LocationInfo(Protocol):
    lineno: int
    end_lineno: int
    col_offset: int
    end_col_offset: int
    def __getitem__(self, index: int, /) -> int: ...

class _FrameInfo(Protocol):
    filename: str
    location: _Location
    funcname: str
    opcode: int | None
    def __getitem__(self, index: int, /) -> object: ...

class _ThreadInfo(Protocol):
    thread_id: int
    status: int
    frame_info: Sequence[_Frame]

class _InterpreterInfo(Protocol):
    interpreter_id: int
    threads: Sequence[_ThreadInfo]

class _CoroInfo(Protocol):
    call_stack: Sequence[_Frame]
    task_name: int | str

class _TaskInfo(Protocol):
    task_id: int
    task_name: str
    coroutine_stack: Sequence[_CoroInfo]
    awaited_by: Sequence[_CoroInfo]

class _AwaitedInfo(Protocol):
    thread_id: int
    awaited_by: Sequence[_TaskInfo]

def normalize_location(location: _Location) -> tuple[int, int, int, int]: ...
def extract_lineno(location: _Location) -> int: ...
def filter_internal_frames(frames: Sequence[_Frame]) -> list[_Frame]: ...
def iter_async_frames(awaited_info_list: Sequence[_AwaitedInfo]) -> object: ...

class Collector(ABC):
    @abstractmethod
    def collect(self, stack_frames: _StackFrames, timestamps_us: _Timestamps = None) -> None: ...
    def collect_failed_sample(self) -> None: ...
    @abstractmethod
    def export(self, filename: StrOrBytesPath) -> None: ...
