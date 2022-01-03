from collections.abc import Generator
from typing import Any

from openpyxl.cell import Cell as Cell, MergedCell as MergedCell
from openpyxl.cell.text import Text as Text
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.formatting.formatting import ConditionalFormatting as ConditionalFormatting
from openpyxl.formula.translate import Translator as Translator
from openpyxl.utils import coordinate_to_tuple as coordinate_to_tuple, get_column_letter as get_column_letter
from openpyxl.utils.datetime import WINDOWS_EPOCH as WINDOWS_EPOCH, from_excel as from_excel, from_ISO8601 as from_ISO8601
from openpyxl.worksheet.dimensions import (
    ColumnDimension as ColumnDimension,
    RowDimension as RowDimension,
    SheetFormatProperties as SheetFormatProperties,
)
from openpyxl.xml.constants import EXT_TYPES as EXT_TYPES, SHEET_MAIN_NS as SHEET_MAIN_NS
from openpyxl.xml.functions import iterparse as iterparse

from .datavalidation import DataValidationList as DataValidationList
from .dimensions import SheetDimension as SheetDimension
from .filters import AutoFilter as AutoFilter
from .header_footer import HeaderFooter as HeaderFooter
from .hyperlink import HyperlinkList as HyperlinkList
from .merge import MergeCells as MergeCells
from .page import PageMargins as PageMargins, PrintOptions as PrintOptions, PrintPageSetup as PrintPageSetup
from .pagebreak import ColBreak as ColBreak, RowBreak as RowBreak
from .properties import WorksheetProperties as WorksheetProperties
from .protection import SheetProtection as SheetProtection
from .related import Related as Related
from .scenario import ScenarioList as ScenarioList
from .table import TablePartList as TablePartList
from .views import SheetViewList as SheetViewList

CELL_TAG: Any
VALUE_TAG: Any
FORMULA_TAG: Any
MERGE_TAG: Any
INLINE_STRING: Any
COL_TAG: Any
ROW_TAG: Any
CF_TAG: Any
LEGACY_TAG: Any
PROT_TAG: Any
EXT_TAG: Any
HYPERLINK_TAG: Any
TABLE_TAG: Any
PRINT_TAG: Any
MARGINS_TAG: Any
PAGE_TAG: Any
HEADER_TAG: Any
FILTER_TAG: Any
VALIDATION_TAG: Any
PROPERTIES_TAG: Any
VIEWS_TAG: Any
FORMAT_TAG: Any
ROW_BREAK_TAG: Any
COL_BREAK_TAG: Any
SCENARIOS_TAG: Any
DATA_TAG: Any
DIMENSION_TAG: Any
CUSTOM_VIEWS_TAG: Any

class WorkSheetParser:
    min_row: Any
    epoch: Any
    source: Any
    shared_strings: Any
    data_only: Any
    shared_formulae: Any
    array_formulae: Any
    row_counter: int
    tables: Any
    date_formats: Any
    timedelta_formats: Any
    row_dimensions: Any
    column_dimensions: Any
    number_formats: Any
    keep_vba: bool
    hyperlinks: Any
    formatting: Any
    legacy_drawing: Any
    merged_cells: Any
    row_breaks: Any
    col_breaks: Any
    def __init__(
        self, src, shared_strings, data_only: bool = ..., epoch=..., date_formats=..., timedelta_formats=...
    ) -> None: ...
    def parse(self) -> Generator[Any, None, None]: ...
    def parse_dimensions(self): ...
    col_counter: Any
    def parse_cell(self, element): ...
    def parse_formula(self, element): ...
    def parse_column_dimensions(self, col) -> None: ...
    def parse_row(self, row): ...
    def parse_formatting(self, element) -> None: ...
    protection: Any
    def parse_sheet_protection(self, element) -> None: ...
    def parse_extensions(self, element) -> None: ...
    def parse_legacy(self, element) -> None: ...
    def parse_row_breaks(self, element) -> None: ...
    def parse_col_breaks(self, element) -> None: ...
    def parse_custom_views(self, element) -> None: ...

class WorksheetReader:
    ws: Any
    parser: Any
    tables: Any
    def __init__(self, ws, xml_source, shared_strings, data_only) -> None: ...
    def bind_cells(self) -> None: ...
    def bind_formatting(self) -> None: ...
    def bind_tables(self) -> None: ...
    def bind_merged_cells(self) -> None: ...
    def bind_hyperlinks(self) -> None: ...
    def normalize_merged_cell_link(self, coord): ...
    def bind_col_dimensions(self) -> None: ...
    def bind_row_dimensions(self) -> None: ...
    def bind_properties(self) -> None: ...
    def bind_all(self) -> None: ...
