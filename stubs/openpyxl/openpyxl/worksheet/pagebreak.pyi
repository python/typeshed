from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

class Break(Serialisable):
    tagname: str
    id: Incomplete
    min: Incomplete
    max: Incomplete
    man: Bool[Literal[True]]
    pt: Bool[Literal[True]]
    def __init__(
        self,
        id: int = 0,
        min: int = 0,
        max: int = 16383,
        man: _ConvertibleToBool | None = True,
        pt: _ConvertibleToBool | None = None,
    ) -> None: ...

class RowBreak(Serialisable):
    tagname: str
    # Overwritten by properties below
    # count: Integer
    # manualBreakCount: Integer
    brk: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, manualBreakCount: Incomplete | None = None, brk=()) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    @property
    def count(self): ...
    @property
    def manualBreakCount(self): ...
    def append(self, brk: Incomplete | None = None) -> None: ...

PageBreak = RowBreak

class ColBreak(RowBreak):
    tagname: str
    @property
    def count(self): ...
    @property
    def manualBreakCount(self): ...
    brk: Incomplete
    __attrs__: Incomplete
