from typing import Any

from .collector import Collector as Collector, filter_internal_frames as filter_internal_frames
from .opcode_utils import format_opcode as format_opcode, get_opcode_info as get_opcode_info

GECKO_CATEGORIES: list[dict[str, Any]]
CATEGORY_OTHER: int
CATEGORY_PYTHON: int
CATEGORY_NATIVE: int
CATEGORY_GC: int
CATEGORY_GIL: int
CATEGORY_CPU: int
CATEGORY_CODE_TYPE: int
CATEGORY_OPCODES: int
CATEGORY_EXCEPTION: int
DEFAULT_SUBCATEGORY: int
GECKO_FORMAT_VERSION: int
GECKO_PREPROCESSED_VERSION: int
RESOURCE_TYPE_LIBRARY: int
FRAME_ADDRESS_NONE: int
FRAME_INLINE_DEPTH_ROOT: int
PROCESS_TYPE_MAIN: int
STACKWALK_DISABLED: int

class GeckoCollector(Collector):
    sample_interval_usec: int
    skip_idle: bool
    opcodes_enabled: bool
    start_time: float
    global_strings: list[str]
    global_string_map: dict[str, int]
    threads: dict[int, Any]
    libs: list[Any]
    sample_count: int
    last_sample_time: int
    interval: float
    has_gil_start: dict[int, float]
    no_gil_start: dict[int, float]
    on_cpu_start: dict[int, float]
    off_cpu_start: dict[int, float]
    python_code_start: dict[int, float]
    native_code_start: dict[int, float]
    gil_wait_start: dict[int, float]
    exception_start: dict[int, float]
    no_exception_start: dict[int, float]
    gc_start_per_thread: dict[int, float]
    initialized_threads: set[int]
    opcode_state: dict[Any, Any]
    def __init__(self, sample_interval_usec: int, *, skip_idle: bool = False, opcodes: bool = False) -> None: ...
    def collect(self, stack_frames: Any, timestamps_us: list[int] | None = None) -> None: ...
    def export(self, filename: str) -> None: ...
