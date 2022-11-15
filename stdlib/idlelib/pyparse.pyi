from typing import Any, Callable, Hashable

C_NONE: int
C_BACKSLASH: int
C_STRING_FIRST_LINE: int
C_STRING_NEXT_LINES: int
C_BRACKET: int

class ParseMap(dict[Hashable, Any]):
    def __missing__(self, key: Hashable) -> None: ...

trans: ParseMap

class Parser:
    indentwidth: int
    tabwidth: int
    def __init__(self, indentwidth: int, tabwidth: int) -> None: ...
    code: str
    study_level: int
    def set_code(self, s: str) -> None: ...
    def find_good_parse_start(self, is_char_in_string: Callable[[str], bool]) -> None | int: ...
    def set_lo(self, lo: int) -> None: ...
    def get_continuation_type(self) -> int: ...
    def compute_bracket_indent(self) -> int: ...
    def get_num_lines_in_stmt(self) -> int: ...
    def compute_backslash_indent(self) -> int: ...
    def get_base_indent_string(self) -> str: ...
    def is_block_opener(self) -> bool: ...
    def is_block_closer(self) -> bool: ...
    def get_last_stmt_bracketing(self) -> tuple[tuple[int, int], ...]: ...
