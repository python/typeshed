from collections.abc import Callable, Sequence
from _typeshed import StrOrBytesPath
from typing import Optional

_CompleterT = Optional[Callable[[str, int], Optional[str]]]
_CompDispT = Optional[Callable[[str, Sequence[str], int], None]]

def parse_and_bind(__string: str) -> None: ...
def read_init_file(__filename: StrOrBytesPath | None = ...) -> None: ...
def get_line_buffer() -> str: ...
def insert_text(__string: str) -> None: ...
def redisplay() -> None: ...
def read_history_file(__filename: StrOrBytesPath | None = ...) -> None: ...
def write_history_file(__filename: StrOrBytesPath | None = ...) -> None: ...
def append_history_file(__nelements: int, __filename: StrOrBytesPath | None = ...) -> None: ...
def get_history_length() -> int: ...
def set_history_length(__length: int) -> None: ...
def clear_history() -> None: ...
def get_current_history_length() -> int: ...
def get_history_item(__index: int) -> str: ...
def remove_history_item(__pos: int) -> None: ...
def replace_history_item(__pos: int, __line: str) -> None: ...
def add_history(__string: str) -> None: ...
def set_auto_history(__enabled: bool) -> None: ...
def set_startup_hook(__function: Callable[[], None] | None = ...) -> None: ...
def set_pre_input_hook(__function: Callable[[], None] | None = ...) -> None: ...
def set_completer(__function: _CompleterT = ...) -> None: ...
def get_completer() -> _CompleterT: ...
def get_completion_type() -> int: ...
def get_begidx() -> int: ...
def get_endidx() -> int: ...
def set_completer_delims(__string: str) -> None: ...
def get_completer_delims() -> str: ...
def set_completion_display_matches_hook(__function: _CompDispT = ...) -> None: ...
