from _typeshed import Incomplete, StrPath
from typing import IO

class ExcelWriter:
    workbook: Incomplete
    manifest: Incomplete
    vba_modified: Incomplete
    def __init__(self, workbook, archive) -> None: ...
    def write_data(self) -> None: ...
    def write_worksheet(self, ws) -> None: ...
    def save(self) -> None: ...

def save_workbook(workbook, filename: StrPath | IO[bytes]): ...
