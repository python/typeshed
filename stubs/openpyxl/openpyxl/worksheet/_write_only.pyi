from typing import Any

from openpyxl.cell import Cell as Cell, WriteOnlyCell as WriteOnlyCell
from openpyxl.utils.exceptions import WorkbookAlreadySaved as WorkbookAlreadySaved
from openpyxl.workbook.child import _WorkbookChild

from ._writer import WorksheetWriter as WorksheetWriter
from .worksheet import Worksheet as Worksheet

class WriteOnlyWorksheet(_WorkbookChild):
    mime_type: Any
    add_chart: Any
    add_image: Any
    add_table: Any
    tables: Any
    print_titles: Any
    print_title_cols: Any
    print_title_rows: Any
    freeze_panes: Any
    print_area: Any
    sheet_view: Any
    def __init__(self, parent, title) -> None: ...
    @property
    def closed(self): ...
    def close(self) -> None: ...
    def append(self, row) -> None: ...
