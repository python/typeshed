from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Convertible, _ConvertibleToMultiCellRange
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.cell_range import MultiCellRange

class ConditionalFormatting(Serialisable):
    tagname: str
    sqref: Convertible[MultiCellRange, Literal[False]]
    cells: Incomplete
    pivot: Incomplete
    cfRule: Incomplete
    rules: Incomplete
    def __init__(
        self,
        sqref: _ConvertibleToMultiCellRange = (),
        pivot: Incomplete | None = None,
        cfRule=(),
        extLst: Incomplete | None = None,
    ) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self) -> int: ...
    def __contains__(self, coord): ...

class ConditionalFormattingList:
    max_priority: int
    def __init__(self) -> None: ...
    def add(self, range_string, cfRule) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, rule) -> None: ...
