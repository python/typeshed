import curses
from _typeshed import StrOrBytesPath
from dataclasses import dataclass, field
from typing import Any

from ..collector import Collector as Collector, extract_lineno as extract_lineno
from ..constants import (
    PROFILING_MODE_CPU as PROFILING_MODE_CPU,
    PROFILING_MODE_GIL as PROFILING_MODE_GIL,
    PROFILING_MODE_WALL as PROFILING_MODE_WALL,
    THREAD_STATUS_GIL_REQUESTED as THREAD_STATUS_GIL_REQUESTED,
    THREAD_STATUS_HAS_EXCEPTION as THREAD_STATUS_HAS_EXCEPTION,
    THREAD_STATUS_HAS_GIL as THREAD_STATUS_HAS_GIL,
    THREAD_STATUS_ON_CPU as THREAD_STATUS_ON_CPU,
    THREAD_STATUS_UNKNOWN as THREAD_STATUS_UNKNOWN,
)
from .constants import (
    COLOR_PAIR_CYAN as COLOR_PAIR_CYAN,
    COLOR_PAIR_FILE as COLOR_PAIR_FILE,
    COLOR_PAIR_FUNC as COLOR_PAIR_FUNC,
    COLOR_PAIR_GREEN as COLOR_PAIR_GREEN,
    COLOR_PAIR_HEADER_BG as COLOR_PAIR_HEADER_BG,
    COLOR_PAIR_MAGENTA as COLOR_PAIR_MAGENTA,
    COLOR_PAIR_RED as COLOR_PAIR_RED,
    COLOR_PAIR_SAMPLES as COLOR_PAIR_SAMPLES,
    COLOR_PAIR_SORTED_HEADER as COLOR_PAIR_SORTED_HEADER,
    COLOR_PAIR_YELLOW as COLOR_PAIR_YELLOW,
    DEFAULT_DISPLAY_LIMIT as DEFAULT_DISPLAY_LIMIT,
    DEFAULT_SORT_BY as DEFAULT_SORT_BY,
    DISPLAY_UPDATE_INTERVAL_SEC as DISPLAY_UPDATE_INTERVAL_SEC,
    FINISHED_BANNER_EXTRA_LINES as FINISHED_BANNER_EXTRA_LINES,
    FOOTER_LINES as FOOTER_LINES,
    HEADER_LINES as HEADER_LINES,
    MICROSECONDS_PER_SECOND as MICROSECONDS_PER_SECOND,
    MIN_TERMINAL_HEIGHT as MIN_TERMINAL_HEIGHT,
    MIN_TERMINAL_WIDTH as MIN_TERMINAL_WIDTH,
    SAFETY_MARGIN as SAFETY_MARGIN,
)
from .display import CursesDisplay as CursesDisplay, DisplayInterface as DisplayInterface
from .trend_tracker import TrendTracker as TrendTracker
from .widgets import (
    FooterWidget as FooterWidget,
    HeaderWidget as HeaderWidget,
    HelpWidget as HelpWidget,
    OpcodePanel as OpcodePanel,
    TableWidget as TableWidget,
)

@dataclass
class ThreadData:
    thread_id: int
    result: dict[Any, Any] = field(default_factory=dict)
    has_gil: int = ...
    on_cpu: int = ...
    gil_requested: int = ...
    unknown: int = ...
    has_exception: int = ...
    total: int = ...
    sample_count: int = ...
    gc_frame_samples: int = ...
    opcode_stats: dict[Any, Any] = field(default_factory=dict)
    def increment_status_flag(self, status_flags: int) -> None: ...
    def as_status_dict(self) -> dict[str, int]: ...

class LiveStatsCollector(Collector):
    result: dict[Any, Any]
    sample_interval_usec: int
    sample_interval_sec: float
    skip_idle: bool
    sort_by: str
    limit: int
    total_samples: int
    start_time: float | None
    stdscr: curses.window | None
    display: DisplayInterface | None
    running: bool
    pid: int | None
    mode: int | None
    async_aware: str | bool | None
    max_sample_rate: int
    successful_samples: int
    failed_samples: int
    display_update_interval_sec: float
    thread_status_counts: dict[str, int]
    gc_frame_samples: int
    opcode_stats: dict[Any, Any]
    show_opcodes: bool
    selected_row: int
    scroll_offset: int
    paused: bool
    show_help: bool
    filter_pattern: str | None
    filter_input_mode: bool
    filter_input_buffer: str
    finished: bool
    finish_timestamp: float | None
    finish_wall_time: float | None
    thread_ids: list[int]
    view_mode: str
    current_thread_index: int
    per_thread_data: dict[int, ThreadData]
    header_widget: HeaderWidget | None
    table_widget: TableWidget | None
    footer_widget: FooterWidget | None
    help_widget: HelpWidget | None
    opcode_panel: OpcodePanel | None
    def __init__(
        self,
        sample_interval_usec: int,
        *,
        skip_idle: bool = False,
        sort_by: str = ...,
        limit: int = ...,
        pid: int | None = None,
        display: DisplayInterface | None = None,
        mode: int | None = None,
        opcodes: bool = False,
        async_aware: str | bool | None = None,
    ) -> None: ...
    @property
    def elapsed_time(self) -> float: ...
    @property
    def current_time_display(self) -> str: ...
    def simplify_path(self, filepath: str) -> str: ...
    def process_frames(self, frames: Any, thread_id: int | None = None) -> None: ...
    def collect_failed_sample(self) -> None: ...
    def collect(self, stack_frames: Any, timestamp_us: int | None = None) -> None: ...
    def build_stats_list(self) -> list[Any]: ...
    def reset_stats(self) -> None: ...
    def mark_finished(self) -> None: ...
    def init_curses(self, stdscr: curses.window) -> None: ...
    def cleanup_curses(self) -> None: ...
    def export(self, filename: StrOrBytesPath) -> None: ...
