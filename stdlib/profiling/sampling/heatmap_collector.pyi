from _typeshed import StrOrBytesPath
from collections import Counter
from dataclasses import dataclass
from typing import Any

from .collector import extract_lineno as extract_lineno, normalize_location as normalize_location
from .opcode_utils import format_opcode as format_opcode, get_opcode_info as get_opcode_info
from .stack_collector import StackTraceCollector as StackTraceCollector

@dataclass
class FileStats:
    filename: str
    module_name: str
    module_type: str
    total_samples: int
    total_self_samples: int
    num_lines: int
    max_samples: int
    max_self_samples: int
    percentage: float = ...

@dataclass
class TreeNode:
    files: list[FileStats] = ...
    samples: int = ...
    count: int = ...
    children: dict[str, TreeNode] = ...

def get_python_path_info() -> dict[str, Any]: ...
def extract_module_name(filename: str, path_info: dict[str, Any]) -> str: ...

class HeatmapCollector(StackTraceCollector):
    FILE_INDEX_FORMAT: str
    line_samples: Counter[Any]
    file_samples: dict[str, Counter[int]]
    line_self_samples: Counter[Any]
    file_self_samples: dict[str, Counter[int]]
    call_graph: dict[Any, set[Any]]
    callers_graph: dict[Any, set[Any]]
    function_definitions: dict[Any, Any]
    line_to_function: dict[Any, Any]
    edge_samples: Counter[Any]
    line_opcodes: dict[Any, dict[Any, Any]]
    stats: dict[str, Any]
    opcodes_enabled: bool
    file_index: dict[str, str]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def set_stats(
        self,
        sample_interval_usec: int,
        duration_sec: float,
        sample_rate: float,
        error_rate: float | None = None,
        missed_samples: int | None = None,
        **kwargs: Any,
    ) -> None: ...
    def process_frames(self, frames: list[Any], thread_id: int, weight: int = 1) -> None: ...
    def export(self, output_path: StrOrBytesPath) -> None: ...
