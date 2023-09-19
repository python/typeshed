from _typeshed import StrPath
from typing import IO
from zipfile import ZipFile

from openpyxl.packaging.manifest import Manifest
from openpyxl.workbook.workbook import Workbook

class ExcelWriter:
    workbook: Workbook
    manifest: Manifest
    vba_modified: set[str | None]
    def __init__(self, workbook: Workbook, archive: ZipFile) -> None: ...
    def write_data(self) -> None: ...
    def write_worksheet(self, ws) -> None: ...
    def save(self) -> None: ...

def save_workbook(workbook, filename: StrPath | IO[bytes]): ...
