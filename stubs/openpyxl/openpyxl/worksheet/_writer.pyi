from _typeshed import Incomplete, ReadableBuffer, StrPath, Unused
from collections.abc import Generator
from typing import Protocol
from typing_extensions import TypeAlias

from openpyxl.worksheet._write_only import WriteOnlyWorksheet
from openpyxl.worksheet.worksheet import Worksheet

# WorksheetWriter.read has an explicit BytesIO branch. Let's make sure this protocol is viable for BytesIO too.
class _SupportsCloseAndWrite(Protocol):
    def write(self, buffer: ReadableBuffer, /) -> Unused: ...
    def close(self) -> Unused: ...

# et_xmlfile.xmlfile accepts a str | _SupportsCloseAndWrite
# lxml.etree.xmlfile should accept a StrPath | _SupportsClose https://lxml.de/api/lxml.etree.xmlfile-class.html
_OutType: TypeAlias = _SupportsCloseAndWrite | StrPath

ALL_TEMP_FILES: list[str]

def create_temporary_file(suffix: str = "") -> str: ...

class WorksheetWriter:
    ws: Worksheet | WriteOnlyWorksheet
    out: _OutType
    xf: Generator[Incomplete | None, Incomplete, None]
    def __init__(self, ws: Worksheet | WriteOnlyWorksheet, out: _OutType | None = None) -> None: ...
    def write_properties(self) -> None: ...
    def write_dimensions(self) -> None: ...
    def write_format(self) -> None: ...
    def write_views(self) -> None: ...
    def write_cols(self) -> None: ...
    def write_top(self) -> None: ...
    def rows(self) -> list[tuple[int, list[Incomplete]]]: ...
    def write_rows(self) -> None: ...
    def write_row(self, xf, row, row_idx) -> None: ...
    def write_protection(self) -> None: ...
    def write_scenarios(self) -> None: ...
    def write_filter(self) -> None: ...
    def write_sort(self) -> None: ...
    def write_merged_cells(self) -> None: ...
    def write_formatting(self) -> None: ...
    def write_validations(self) -> None: ...
    def write_hyperlinks(self) -> None: ...
    def write_print(self) -> None: ...
    def write_margins(self) -> None: ...
    def write_page(self) -> None: ...
    def write_header(self) -> None: ...
    def write_breaks(self) -> None: ...
    def write_drawings(self) -> None: ...
    def write_legacy(self) -> None: ...
    def write_tables(self) -> None: ...
    def get_stream(self) -> Generator[Incomplete | None, bool | None, None]: ...
    def write_tail(self) -> None: ...
    def write(self) -> None: ...
    def close(self) -> None: ...
    def read(self) -> bytes: ...
    def cleanup(self) -> None: ...
