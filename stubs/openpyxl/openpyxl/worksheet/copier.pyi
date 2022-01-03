from typing import Any

from .worksheet import Worksheet as Worksheet

class WorksheetCopy:
    source: Any
    target: Any
    def __init__(self, source_worksheet, target_worksheet) -> None: ...
    def copy_worksheet(self) -> None: ...
