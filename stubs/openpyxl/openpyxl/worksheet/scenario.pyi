from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, Convertible, _ConvertibleToBool, _ConvertibleToMultiCellRange
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.cell_range import MultiCellRange

class InputCells(Serialisable):
    tagname: str
    r: Incomplete
    deleted: Bool[Literal[True]]
    undone: Bool[Literal[True]]
    val: Incomplete
    numFmtId: Incomplete
    def __init__(
        self,
        r: Incomplete | None = None,
        deleted: _ConvertibleToBool | None = False,
        undone: _ConvertibleToBool | None = False,
        val: Incomplete | None = None,
        numFmtId: Incomplete | None = None,
    ) -> None: ...

class Scenario(Serialisable):
    tagname: str
    inputCells: Incomplete
    name: Incomplete
    locked: Bool[Literal[True]]
    hidden: Bool[Literal[True]]
    user: Incomplete
    comment: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        inputCells=(),
        name: Incomplete | None = None,
        locked: _ConvertibleToBool | None = False,
        hidden: _ConvertibleToBool | None = False,
        count: Incomplete | None = None,
        user: Incomplete | None = None,
        comment: Incomplete | None = None,
    ) -> None: ...
    @property
    def count(self): ...

class ScenarioList(Serialisable):
    tagname: str
    scenario: Incomplete
    current: Incomplete
    show: Incomplete
    sqref: Convertible[MultiCellRange, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        scenario=(),
        current: Incomplete | None = None,
        show: Incomplete | None = None,
        sqref: _ConvertibleToMultiCellRange | None = None,
    ) -> None: ...
    def append(self, scenario) -> None: ...
    def __bool__(self) -> bool: ...
