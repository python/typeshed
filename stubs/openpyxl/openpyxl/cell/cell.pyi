import datetime
from re import Pattern
from typing_extensions import Final, Literal, TypeAlias

from openpyxl.comments.comments import Comment
from openpyxl.compat.numbers import NUMERIC_TYPES as NUMERIC_TYPES, _NumericTypes
from openpyxl.styles.cell_style import StyleArray
from openpyxl.styles.styleable import StyleableObject
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.worksheet.hyperlink import Hyperlink

__docformat__: str
TIME_TYPES: tuple[type[datetime.datetime], type[datetime.date], type[datetime.time], type[datetime.timedelta]]
_TimeTypes: TypeAlias = datetime.datetime | datetime.date | datetime.time | datetime.timedelta
TIME_FORMATS: dict[_TimeTypes, str]
STRING_TYPES: tuple[type[str], type[bytes]]
_StringTypes: TypeAlias = str | bytes
# mypy will simplify the type. Pyright fully expands it.
KNOWN_TYPES = NUMERIC_TYPES + TIME_TYPES + STRING_TYPES + (bool, type(None))  # noqa: F821,Y026
_KnownTypes: TypeAlias = _NumericTypes | _TimeTypes | _StringTypes | bool | None
ILLEGAL_CHARACTERS_RE: Pattern[str]
ERROR_CODES: Final = ("#NULL!", "#DIV/0!", "#VALUE!", "#REF!", "#NAME?", "#NUM!", "#N/A")
TYPE_STRING: Final = "s"
TYPE_FORMULA: Final = "f"
TYPE_NUMERIC: Final = "n"
TYPE_BOOL: Final = "b"
TYPE_NULL: Final = "n"
TYPE_INLINE: Final = "inlineStr"
TYPE_ERROR: Final = "e"
TYPE_FORMULA_CACHE_STRING: Final = "str"

VALID_TYPES = (TYPE_STRING, TYPE_FORMULA, TYPE_NUMERIC, TYPE_BOOL, TYPE_NULL, TYPE_INLINE, TYPE_ERROR, TYPE_FORMULA_CACHE_STRING)

def get_type(t, value) -> Literal["n", "s", "d", None]: ...
def get_time_format(t) -> str: ...

class Cell(StyleableObject):
    row: int | None
    column: int | None
    data_type: str
    def __init__(
        self,
        worksheet: _WorkbookChild,
        row: int | None = ...,
        column: int | None = ...,
        value: _KnownTypes = ...,
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
    def base_date(self): ...
    def check_string(self, value: str | bytes): ...
    def check_error(self, value): ...
    @property
    def value(self) -> _KnownTypes: ...
    @value.setter
    def value(self, value: _KnownTypes) -> None: ...
    @property
    def internal_value(self): ...
    @property
    def hyperlink(self) -> Hyperlink | None: ...
    @hyperlink.setter
    def hyperlink(self, val: Hyperlink | str | None) -> None: ...
    @property
    def is_date(self) -> bool: ...
    def offset(self, row: int = ..., column: int = ...): ...
    @property
    def comment(self) -> Comment | None: ...
    @comment.setter
    def comment(self, value: Comment | None) -> None: ...

class MergedCell(StyleableObject):
    data_type: str
    comment: Comment | None
    hyperlink: Hyperlink | None
    row: int | None
    column: int | None
    def __init__(self, worksheet: _WorkbookChild, row: int | None = ..., column: int | None = ...) -> None: ...
    @property
    def coordinate(self) -> str: ...
    value: _KnownTypes

def WriteOnlyCell(ws: _WorkbookChild | None = ..., value: _KnownTypes = ...) -> Cell: ...
