import abc
from _typeshed import StrOrBytesPath
from abc import ABC, abstractmethod
from typing import Any

class Collector(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def collect(self, stack_frames: Any, timestamps_us: list[int] | None = None) -> None: ...
    def collect_failed_sample(self) -> None: ...
    @abstractmethod
    def export(self, filename: StrOrBytesPath) -> None: ...
