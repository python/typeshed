from _typeshed import Incomplete
from collections.abc import Container, Generator, Sequence
from datetime import datetime
from typing import Any
from typing_extensions import Final
from xml.etree.ElementTree import _FileRead

from openpyxl.cell.cell import Cell
from openpyxl.cell.rich_text import CellRichText
from openpyxl.descriptors.serialisable import _ChildSerialisableTreeElement
from openpyxl.worksheet.hyperlink import HyperlinkList
from openpyxl.worksheet.pagebreak import ColBreak, RowBreak
from openpyxl.worksheet.protection import SheetProtection
from openpyxl.worksheet.table import TablePartList
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.xml.functions import Element

CELL_TAG: Final[str]
VALUE_TAG: Final[str]
FORMULA_TAG: Final[str]
MERGE_TAG: Final[str]
INLINE_STRING: Final[str]
COL_TAG: Final[str]
ROW_TAG: Final[str]
CF_TAG: Final[str]
LEGACY_TAG: Final[str]
PROT_TAG: Final[str]
EXT_TAG: Final[str]
HYPERLINK_TAG: Final[str]
TABLE_TAG: Final[str]
PRINT_TAG: Final[str]
MARGINS_TAG: Final[str]
PAGE_TAG: Final[str]
HEADER_TAG: Final[str]
FILTER_TAG: Final[str]
VALIDATION_TAG: Final[str]
PROPERTIES_TAG: Final[str]
VIEWS_TAG: Final[str]
FORMAT_TAG: Final[str]
ROW_BREAK_TAG: Final[str]
COL_BREAK_TAG: Final[str]
SCENARIOS_TAG: Final[str]
DATA_TAG: Final[str]
DIMENSION_TAG: Final[str]
CUSTOM_VIEWS_TAG: Final[str]

def parse_richtext_string(element: _ChildSerialisableTreeElement) -> CellRichText | str: ...

class WorkSheetParser:
    min_row: Incomplete | None
    min_col: Incomplete | None
    epoch: datetime
    source: _FileRead
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
        src: _FileRead,
        shared_strings: Sequence[str],
        data_only: bool = False,
        epoch: datetime = ...,
        date_formats: Container[int] = ...,
        timedelta_formats: Container[int] = ...,
        rich_text: bool = False,
    ) -> None: ...
    def parse(self) -> Generator[Incomplete, None, None]: ...
    def parse_dimensions(self) -> tuple[int, int, int, int]: ...
    # dict[str, AnyOf[time, date, datetime, timedelta, float, int, bool | str, None]]
    def parse_cell(self, element: Element) -> dict[str, Any]: ...
    def parse_formula(self, element: Element): ...
    def parse_column_dimensions(self, col: Element) -> None: ...
    # tuple[int, list[dict[str, AnyOf[time, date, datetime, timedelta, float, int, bool | str, None]]]]
    def parse_row(self, row: Element) -> tuple[int, list[dict[str, Any]]]: ...
    def parse_formatting(self, element: Element) -> None: ...
    def parse_sheet_protection(self, element: Element) -> None: ...
    def parse_extensions(self, element: Element) -> None: ...
    def parse_legacy(self, element: Element) -> None: ...
    def parse_row_breaks(self, element: Element) -> None: ...
    def parse_col_breaks(self, element: Element) -> None: ...
    def parse_custom_views(self, element: Element) -> None: ...

class WorksheetReader:
    ws: Worksheet
    parser: WorkSheetParser
    tables: list[Incomplete]
    def __init__(
        self, ws: Worksheet, xml_source: _FileRead, shared_strings: Sequence[str] | None, data_only: bool | None, rich_text: bool
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
