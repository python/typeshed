import datetime
from _typeshed import Incomplete
from collections.abc import Container, Generator, Sequence
from datetime import datetime
from typing import Any
from zipfile import ZipExtFile

from openpyxl.cell.cell import Cell
from openpyxl.worksheet.hyperlink import HyperlinkList
from openpyxl.worksheet.pagebreak import ColBreak, RowBreak
from openpyxl.worksheet.protection import SheetProtection
from openpyxl.worksheet.table import TablePartList
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.xml.functions import _Element

CELL_TAG: str
VALUE_TAG: str
FORMULA_TAG: str
MERGE_TAG: str
INLINE_STRING: str
COL_TAG: str
ROW_TAG: str
CF_TAG: str
LEGACY_TAG: str
PROT_TAG: str
EXT_TAG: str
HYPERLINK_TAG: str
TABLE_TAG: str
PRINT_TAG: str
MARGINS_TAG: str
PAGE_TAG: str
HEADER_TAG: str
FILTER_TAG: str
VALIDATION_TAG: str
PROPERTIES_TAG: str
VIEWS_TAG: str
FORMAT_TAG: str
ROW_BREAK_TAG: str
COL_BREAK_TAG: str
SCENARIOS_TAG: str
DATA_TAG: str
DIMENSION_TAG: str
CUSTOM_VIEWS_TAG: str

class WorkSheetParser:
    min_row: Incomplete | None
    min_col: Incomplete | None
    epoch: datetime
    source: ZipExtFile | str
    shared_strings: Sequence[str]
    data_only: bool
    shared_formulae: dict[Incomplete, Incomplete]
    row_counter: int
    col_counter: int
    tables: TablePartList
    date_formats: Container[int]
    timedelta_formats: Container[int]
    row_dimensions: dict[Incomplete, Incomplete]
    column_dimensions: dict[Incomplete, Incomplete]
    number_formats: list[Incomplete]
    keep_vba: bool
    hyperlinks: HyperlinkList
    formatting: list[Incomplete]
    legacy_drawing: Incomplete | None
    merged_cells: Incomplete | None
    row_breaks: RowBreak
    col_breaks: ColBreak
    rich_text: bool
    protection: SheetProtection  # initialized after call to parse_sheet_protection()
    def __init__(
        self,
        src: ZipExtFile | str,
        shared_strings: Sequence[str],
        data_only: bool = False,
        epoch: datetime = ...,
        date_formats: Container[int] = ...,
        timedelta_formats: Container[int] = ...,
        rich_text: bool = False
    ) -> None: ...
    def parse(self) -> Generator[Incomplete, None, None]: ...
    def parse_dimensions(self) -> tuple[int, int, int, int]: ...
    # dict[str, AnyOf[time, date, datetime, timedelta, float, int, bool | str, None]]
    def parse_cell(self, element: _Element) -> dict[str, Any]: ...
    def parse_formula(self, element: _Element): ...
    def parse_column_dimensions(self, col: _Element) -> None: ...
    # tuple[int, list[dict[str, AnyOf[time, date, datetime, timedelta, float, int, bool | str, None]]]]
    def parse_row(self, row: _Element) -> tuple[int, list[dict[str, Any]]]: ...
    def parse_formatting(self, element: _Element) -> None: ...
    def parse_sheet_protection(self, element: _Element) -> None: ...
    def parse_extensions(self, element: _Element) -> None: ...
    def parse_legacy(self, element: _Element) -> None: ...
    def parse_row_breaks(self, element: _Element) -> None: ...
    def parse_col_breaks(self, element: _Element) -> None: ...
    def parse_custom_views(self, element: _Element) -> None: ...

class WorksheetReader:
    ws: Worksheet
    parser: WorkSheetParser
    tables: list[Incomplete]
    def __init__(
        self, ws: Worksheet, xml_source: ZipExtFile | str, shared_strings: Sequence[str] | None, data_only: bool | None, rich_text: bool
    ) -> None: ...
    def bind_cells(self) -> None: ...
    def bind_formatting(self) -> None: ...
    def bind_tables(self) -> None: ...
    def bind_merged_cells(self) -> None: ...
    def bind_hyperlinks(self) -> None: ...
    def normalize_merged_cell_link(self, coord: str) -> Cell | None: ...
    def bind_col_dimensions(self) -> None: ...
    def bind_row_dimensions(self) -> None: ...
    def bind_properties(self) -> None: ...
    def bind_all(self) -> None: ...
