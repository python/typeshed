from datetime import datetime
from typing import Any

from openpyxl.comments.comments import Comment
from openpyxl.styles.cell_style import StyleArray
from openpyxl.styles.styleable import StyleableObject
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.worksheet.worksheet import Worksheet

__docformat__: str
TIME_TYPES: Any
TIME_FORMATS: Any
STRING_TYPES: Any
KNOWN_TYPES: Any
ILLEGAL_CHARACTERS_RE: Any
ERROR_CODES: Any
TYPE_STRING: str
TYPE_FORMULA: str
TYPE_NUMERIC: str
TYPE_BOOL: str
TYPE_NULL: str
TYPE_INLINE: str
TYPE_ERROR: str
TYPE_FORMULA_CACHE_STRING: str
VALID_TYPES: Any

def get_type(t: Any, value: Any) -> Any: ...
def get_time_format(t: Any) -> Any: ...

class Cell(StyleableObject):
    row: int
    column: int
    data_type: str
    def __init__(
        self,
        worksheet: Worksheet,
        row: int | None = ...,
        column: int | None = ...,
        value: str | float | int | datetime | None = ...,
        style_array: StyleArray | None = ...,
    ) -> None: ...
    @property
    def coordinate(self) -> str: ...
    @property
    def col_idx(self) -> int: ...
    @property
    def column_letter(self) -> str: ...
    @property
    def encoding(self) -> str: ...
    @property
    def base_date(self) -> Any: ...
    def check_string(self, value: str): ...
    def check_error(self, value: Any) -> Any | str: ...
    @property
    def value(self) -> str | float | int | datetime | None: ...
    @value.setter
    def value(self, value: str | float | int | datetime | None) -> None: ...
    @property
    def internal_value(self) -> Any: ...
    @property
    def hyperlink(self) -> Hyperlink | str: ...
    @hyperlink.setter
    def hyperlink(self, val: Hyperlink | str | None) -> None: ...
    @property
    def is_date(self) -> bool: ...
    def offset(self, row: int = ..., column: int = ...) -> Cell: ...
    @property
    def comment(self) -> Comment: ...
    @comment.setter
    def comment(self, value: Comment) -> None: ...

class MergedCell(StyleableObject):
    data_type: str
    comment: Comment
    hyperlink: Hyperlink
    row: int
    column: int
    def __init__(self, worksheet: Worksheet, row: int | None = ..., column: int | None = ...) -> None: ...
    @property
    def coordinate(self) -> str: ...
    value: str | float | int | datetime | None

def WriteOnlyCell(ws: Worksheet | None = ..., value: str | float | int | datetime | None = ...) -> Cell: ...
