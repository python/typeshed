from collections.abc import Generator
from re import Pattern
from typing_extensions import Final, TypeAlias

# "1:1" | "A1:A1" | "A:A"
_RangeBoundariesTuple: TypeAlias = tuple[None, int, None, int] | tuple[int, int, int, int] | tuple[int, None, int, None]

COORD_RE: Final[Pattern[str]]
COL_RANGE: Final = "[A-Z]{1,3}:[A-Z]{1,3}:"
ROW_RANGE: Final = r"\d+:\d+:"
RANGE_EXPR: Final[str]
ABSOLUTE_RE: Final[Pattern[str]]
SHEET_TITLE: Final[str]
SHEETRANGE_RE: Final[Pattern[str]]

def get_column_interval(start: str | int, end: str | int) -> list[str]: ...
def coordinate_from_string(coord_string: str) -> tuple[str, int]: ...
def absolute_coordinate(coord_string: str) -> str: ...
def get_column_letter(idx: int) -> str: ...
def column_index_from_string(str_col: str) -> int: ...
def range_boundaries(range_string: str) -> _RangeBoundariesTuple: ...
def rows_from_range(range_string: str) -> Generator[tuple[str, ...], None, None]: ...
def cols_from_range(range_string: str) -> Generator[tuple[str, ...], None, None]: ...
def coordinate_to_tuple(coordinate: str) -> tuple[int, int]: ...
def range_to_tuple(range_string: str) -> tuple[str, _RangeBoundariesTuple]: ...
def quote_sheetname(sheetname: str) -> str: ...
