from _typeshed import Incomplete, Unused
from collections.abc import Iterator
from datetime import datetime
from typing import Any, Final
from typing_extensions import deprecated
from zipfile import ZipFile

from openpyxl import _Decodable, _ZipFileFileProtocol
from openpyxl.chartsheet.chartsheet import Chartsheet
from openpyxl.styles.named_styles import NamedStyle
from openpyxl.utils.indexed_list import IndexedList
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.worksheet._read_only import ReadOnlyWorksheet
from openpyxl.worksheet._write_only import WriteOnlyWorksheet
from openpyxl.worksheet.worksheet import Worksheet

INTEGER_TYPES: Final[tuple[type[int]]]

class Workbook:
    template: bool
    path: str
    defined_names: Incomplete
    properties: Incomplete
    security: Incomplete
    shared_strings: IndexedList[str]
    loaded_theme: Incomplete
    vba_archive: ZipFile | None
    is_template: bool
    code_name: Incomplete
    encoding: str
    iso_dates: Incomplete
    rels: Incomplete
    calculation: Incomplete
    views: Incomplete
    # Private, but useful as a reference of what "sheets" can be for other types
    # ExcelReader can add ReadOnlyWorksheet in read_only mode.
    _sheets: list[Worksheet | WriteOnlyWorksheet | Chartsheet | ReadOnlyWorksheet]
    def __init__(self, write_only: bool = False, iso_dates: bool = False) -> None: ...
    @property
    def epoch(self) -> datetime: ...
    @epoch.setter
    def epoch(self, value: datetime) -> None: ...
    @property
    def read_only(self) -> bool: ...
    @property
    def data_only(self) -> bool: ...
    @property
    def write_only(self) -> bool: ...
    @property
    def excel_base_date(self) -> datetime: ...
    @property
    def active(self) -> Worksheet | WriteOnlyWorksheet | Chartsheet | ReadOnlyWorksheet | None: ...
    @active.setter
    def active(self, value: Worksheet | Chartsheet | int) -> None: ...
    # Could be generic based on write_only
    def create_sheet(
        self, title: str | _Decodable | None = None, index: int | None = None
    ) -> Any: ...  # AnyOf[WriteOnlyWorksheet, Worksheet]
    def move_sheet(self, sheet: Worksheet | str, offset: int = 0) -> None: ...
    def remove(self, worksheet: Worksheet | WriteOnlyWorksheet | Chartsheet | ReadOnlyWorksheet) -> None: ...
    @deprecated("Use wb.remove(worksheet) or del wb[sheetname]")
    def remove_sheet(self, worksheet: Worksheet | WriteOnlyWorksheet | Chartsheet | ReadOnlyWorksheet) -> None: ...
    def create_chartsheet(self, title: str | _Decodable | None = None, index: int | None = None) -> Chartsheet: ...
    @deprecated("Use wb[sheetname]")
    def get_sheet_by_name(self, name: str) -> Worksheet | ReadOnlyWorksheet | WriteOnlyWorksheet | Chartsheet: ...
    def __contains__(self, key: str) -> bool: ...
    def index(self, worksheet: Worksheet | ReadOnlyWorksheet | WriteOnlyWorksheet) -> int: ...
    @deprecated("Use wb.index(worksheet)")
    def get_index(self, worksheet: Worksheet | ReadOnlyWorksheet | WriteOnlyWorksheet) -> int: ...
    def __getitem__(self, key: str) -> Worksheet | ReadOnlyWorksheet | WriteOnlyWorksheet | Chartsheet: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[Worksheet | ReadOnlyWorksheet | WriteOnlyWorksheet]: ...
    @deprecated("Use wb.sheetnames")
    def get_sheet_names(self) -> list[Worksheet]: ...
    @property
    def worksheets(self) -> list[Worksheet | ReadOnlyWorksheet | WriteOnlyWorksheet]: ...
    @property
    def chartsheets(self) -> list[Chartsheet]: ...
    @property
    def sheetnames(self) -> list[str]: ...
    @deprecated("Assign scoped named ranges directly to worksheets or global ones to the workbook. Deprecated in 3.1")
    def create_named_range(
        self,
        name: str,
        worksheet: _WorkbookChild | ReadOnlyWorksheet | None = None,
        value: str | Incomplete | None = None,
        scope: Unused = None,
    ) -> None: ...
    def add_named_style(self, style: NamedStyle) -> None: ...
    @property
    def named_styles(self) -> list[str]: ...
    @property
    def mime_type(self) -> str: ...
    def save(self, filename: _ZipFileFileProtocol) -> None: ...
    @property
    def style_names(self) -> list[str]: ...
    def copy_worksheet(self, from_worksheet: Worksheet) -> Worksheet | WriteOnlyWorksheet: ...
    def close(self) -> None: ...
