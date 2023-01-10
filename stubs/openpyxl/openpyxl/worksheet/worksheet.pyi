from _typeshed import Incomplete
from collections.abc import Generator, Iterable, Iterator
from typing import overload
from typing_extensions import TypeAlias

from openpyxl import _Decodable
from openpyxl.cell.cell import Cell, MergedCell, _KnownTypes
from openpyxl.chart._chart import ChartBase
from openpyxl.drawing.image import Image
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.cell_range import CellRange
from openpyxl.worksheet.table import Table, TableList
from openpyxl.worksheet.views import SheetView

_Cell: TypeAlias = Cell | MergedCell
_Unused: TypeAlias = object

class Worksheet(_WorkbookChild):
    mime_type: str
    BREAK_NONE: int
    BREAK_ROW: int
    BREAK_COLUMN: int
    SHEETSTATE_VISIBLE: str
    SHEETSTATE_HIDDEN: str
    SHEETSTATE_VERYHIDDEN: str
    PAPERSIZE_LETTER: str
    PAPERSIZE_LETTER_SMALL: str
    PAPERSIZE_TABLOID: str
    PAPERSIZE_LEDGER: str
    PAPERSIZE_LEGAL: str
    PAPERSIZE_STATEMENT: str
    PAPERSIZE_EXECUTIVE: str
    PAPERSIZE_A3: str
    PAPERSIZE_A4: str
    PAPERSIZE_A4_SMALL: str
    PAPERSIZE_A5: str
    ORIENTATION_PORTRAIT: str
    ORIENTATION_LANDSCAPE: str
    def __init__(self, parent: Workbook | None, title: str | _Decodable | None = ...) -> None: ...
    @property
    def sheet_view(self) -> SheetView: ...
    @property
    def selected_cell(self) -> str: ...
    @property
    def active_cell(self) -> str: ...
    @property
    def page_breaks(self): ...
    @property
    def show_gridlines(self) -> bool | None: ...
    @property
    def show_summary_below(self): ...
    @property
    def show_summary_right(self): ...
    @property
    def freeze_panes(self) -> str | None: ...
    @freeze_panes.setter
    def freeze_panes(self, topLeftCell: Incomplete | None = ...) -> None: ...
    def cell(self, row: int, column: int, value: _KnownTypes = ...) -> Cell | MergedCell: ...
    def __getitem__(self, key: str | slice | int): ...
    def __setitem__(self, key: str | slice | int, value: _KnownTypes) -> None: ...
    def __iter__(self) -> (Iterator[_Cell] | Generator[tuple[_Cell, ...], None, None]): ...
    def __delitem__(self, key: Iterable[str]) -> None: ...
    @property
    def min_row(self) -> int: ...
    @property
    def max_row(self) -> int: ...
    @property
    def min_column(self) -> int: ...
    @property
    def max_column(self) -> int: ...
    def calculate_dimension(self) -> str: ...
    @property
    def dimensions(self): ...
    def iter_rows(
        self,
        min_row: int | None = ...,
        max_row: int | None = ...,
        min_col: int | None = ...,
        max_col: int | None = ...,
        values_only: bool = ...,
    ): ...
    @property
    def rows(self) -> Iterator[tuple[_Cell, ...]] | Generator[tuple[_Cell, ...], None, None]: ...
    @property
    def values(self) -> Generator[tuple[_Cell, ...], None, None]: ...
    def iter_cols(
        self,
        min_col: int | None = ...,
        max_col: int | None = ...,
        min_row: int | None = ...,
        max_row: int | None = ...,
        values_only: bool = ...,
    ): ...
    @property
    def columns(self) -> Iterator[_Cell] | Generator[tuple[_Cell, ...], None, None]: ...
    def set_printer_settings(self, paper_size, orientation) -> None: ...
    def add_data_validation(self, data_validation) -> None: ...
    def add_chart(self, chart: ChartBase, anchor: str | None = ...) -> None: ...
    def add_image(self, img: Image, anchor: str | None = ...) -> None: ...
    def add_table(self, table: Table) -> None: ...
    @property
    def tables(self) -> TableList: ...
    def add_pivot(self, pivot) -> None: ...
    # Same overload as CellRange.__init__
    @overload
    def merge_cells(self, *, start_row: int, start_column: int, end_row: int, end_column: int) -> None: ...
    @overload
    def merge_cells(self, range_string: None, start_row: int, start_column: int, end_row: int, end_column: int) -> None: ...
    @overload
    def merge_cells(
        self,
        range_string: str,
        start_row: _Unused = ...,
        start_column: _Unused = ...,
        end_row: _Unused = ...,
        end_column: _Unused = ...,
    ) -> None: ...
    @property
    def merged_cell_ranges(self): ...
    def unmerge_cells(
        self,
        range_string: str | None = ...,
        start_row: int | None = ...,
        start_column: int | None = ...,
        end_row: int | None = ...,
        end_column: int | None = ...,
    ) -> None: ...
    def append(self, iterable) -> None: ...
    def insert_rows(self, idx: int, amount: int = ...) -> None: ...
    def insert_cols(self, idx: int, amount: int = ...) -> None: ...
    def delete_rows(self, idx: int, amount: int = ...) -> None: ...
    def delete_cols(self, idx: int, amount: int = ...) -> None: ...
    def move_range(self, cell_range: str | CellRange, rows: int = ..., cols: int = ..., translate: bool = ...) -> None: ...
    @property
    def print_title_rows(self): ...
    @print_title_rows.setter
    def print_title_rows(self, rows) -> None: ...
    @property
    def print_title_cols(self): ...
    @print_title_cols.setter
    def print_title_cols(self, cols) -> None: ...
    @property
    def print_titles(self) -> str | None: ...
    @property
    def print_area(self): ...
    @print_area.setter
    def print_area(self, value) -> None: ...
