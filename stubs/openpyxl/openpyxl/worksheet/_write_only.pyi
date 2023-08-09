from _typeshed import Incomplete
from collections.abc import Iterable

from openpyxl.workbook.child import _WorkbookChild
from openpyxl.worksheet.table import TableList
from openpyxl.worksheet.worksheet import Worksheet

class WriteOnlyWorksheet(_WorkbookChild):
    mime_type = Worksheet.mime_type
    add_chart = Worksheet.add_chart
    add_image = Worksheet.add_image
    add_table = Worksheet.add_table

    # Same properties as Worksheet
    @property
    def tables(self) -> TableList: ...
    @property
    def print_titles(self) -> str | None: ...
    @property
    def print_title_cols(self) -> str | None: ...
    @print_title_cols.setter
    def print_title_cols(self, cols: str | None) -> None: ...
    @property
    def print_title_rows(self) -> str | None: ...
    @print_title_rows.setter
    def print_title_rows(self, rows: str | None) -> None: ...
    @property
    def freeze_panes(self) -> str | None: ...
    @freeze_panes.setter
    def freeze_panes(self, topLeftCell: Incomplete | None = ...) -> None: ...
    @property
    def print_area(self) -> list[str]: ...
    @print_area.setter
    def print_area(self, value: str | Iterable[str]) -> None: ...
    @property
    def sheet_view(self): ...
    def __init__(self, parent, title) -> None: ...
    @property
    def closed(self): ...
    def close(self) -> None: ...
    def append(self, row) -> None: ...
