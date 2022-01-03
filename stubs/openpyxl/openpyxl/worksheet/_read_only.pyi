from typing import Any

from openpyxl.cell.read_only import EMPTY_CELL as EMPTY_CELL, ReadOnlyCell as ReadOnlyCell
from openpyxl.utils import get_column_letter as get_column_letter

from ._reader import WorkSheetParser as WorkSheetParser
from .worksheet import Worksheet as Worksheet

def read_dimension(source): ...

class ReadOnlyWorksheet:
    cell: Any
    iter_rows: Any
    values: Any
    rows: Any
    __getitem__: Any
    __iter__: Any
    parent: Any
    title: Any
    sheet_state: str
    def __init__(self, parent_workbook, title, worksheet_path, shared_strings) -> None: ...
    def calculate_dimension(self, force: bool = ...): ...
    def reset_dimensions(self) -> None: ...
    @property
    def min_row(self): ...
    @property
    def max_row(self): ...
    @property
    def min_column(self): ...
    @property
    def max_column(self): ...
