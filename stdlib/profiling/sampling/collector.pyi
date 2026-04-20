import abc
from _typeshed import StrOrBytesPath
from abc import ABC, abstractmethod
from typing import Any

from .constants import (
    DEFAULT_LOCATION as DEFAULT_LOCATION,
    THREAD_STATUS_GIL_REQUESTED as THREAD_STATUS_GIL_REQUESTED,
    THREAD_STATUS_HAS_EXCEPTION as THREAD_STATUS_HAS_EXCEPTION,
    THREAD_STATUS_HAS_GIL as THREAD_STATUS_HAS_GIL,
    THREAD_STATUS_ON_CPU as THREAD_STATUS_ON_CPU,
    THREAD_STATUS_UNKNOWN as THREAD_STATUS_UNKNOWN,
)

def normalize_location(location: tuple[int, int, int, int] | None) -> tuple[int, int, int, int]: ...
def extract_lineno(location: tuple[int, int, int, int] | None) -> int: ...
def filter_internal_frames(frames: list[Any]) -> list[Any]: ...

class Collector(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def collect(self, stack_frames: Any, timestamps_us: list[int] | None = None) -> None: ...
    def collect_failed_sample(self) -> None: ...
    @abstractmethod
    def export(self, filename: StrOrBytesPath) -> None: ...
