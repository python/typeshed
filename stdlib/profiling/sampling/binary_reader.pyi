import types
from _typeshed import StrOrBytesPath
from collections.abc import Callable
from typing import Any
from typing_extensions import Self

from .collector import Collector as Collector

class BinaryReader:
    filename: str
    def __init__(self, filename: str) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...
    def get_info(self) -> dict[str, Any]: ...
    def replay_samples(self, collector: Collector, progress_callback: Callable[[int, int], None] | None = None) -> int: ...
    @property
    def sample_count(self) -> int: ...
    def get_stats(self) -> dict[str, Any]: ...

def convert_binary_to_format(
    input_file: StrOrBytesPath,
    output_file: StrOrBytesPath,
    output_format: str,
    sample_interval_usec: int | None = None,
    progress_callback: Callable[[int, int], None] | None = None,
) -> None: ...
