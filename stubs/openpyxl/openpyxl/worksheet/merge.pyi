from typing import Any

from openpyxl.cell.cell import MergedCell as MergedCell
from openpyxl.descriptors import Integer as Integer, Sequence as Sequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.styles.borders import Border as Border

from .cell_range import CellRange as CellRange

class MergeCell(CellRange):
    tagname: str
    ref: Any
    __attrs__: Any
    def __init__(self, ref: Any | None = ...) -> None: ...
    def __copy__(self): ...

class MergeCells(Serialisable):
    tagname: str
    count: Any
    mergeCell: Any
    __elements__: Any
    __attrs__: Any
    def __init__(self, count: Any | None = ..., mergeCell=...) -> None: ...
    @property
    def count(self): ...

class MergedCellRange(CellRange):
    ws: Any
    start_cell: Any
    def __init__(self, worksheet, coord) -> None: ...
    def format(self) -> None: ...
    def __contains__(self, coord): ...
    def __copy__(self): ...
