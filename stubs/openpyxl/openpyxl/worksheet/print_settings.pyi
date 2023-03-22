from .cell_range import MultiCellRange
from _typeshed import Incomplete
from openpyxl.descriptors import Strict
from openpyxl.utils.cell import SHEETRANGE_RE as SHEETRANGE_RE

COL_RANGE: str
COL_RANGE_RE: Incomplete
ROW_RANGE: str
ROW_RANGE_RE: Incomplete
TITLES_REGEX: Incomplete
PRINT_AREA_RE: Incomplete

class ColRange(Strict):
    min_col: Incomplete
    max_col: Incomplete
    def __init__(
        self, range_string: Incomplete | None = ..., min_col: Incomplete | None = ..., max_col: Incomplete | None = ...
    ) -> None: ...
    def __eq__(self, other): ...

class RowRange(Strict):
    min_row: Incomplete
    max_row: Incomplete
    def __init__(
        self, range_string: Incomplete | None = ..., min_row: Incomplete | None = ..., max_row: Incomplete | None = ...
    ) -> None: ...
    def __eq__(self, other): ...

class PrintTitles(Strict):
    cols: Incomplete
    rows: Incomplete
    title: Incomplete
    def __init__(self, cols: Incomplete | None = ..., rows: Incomplete | None = ..., title: str = ...) -> None: ...
    @classmethod
    def from_string(cls, value): ...
    def __eq__(self, other): ...

class PrintArea(MultiCellRange):
    @classmethod
    def from_string(cls, value): ...
    title: str
    def __init__(self, ranges=..., title: str = ...) -> None: ...
    def __eq__(self, other): ...
