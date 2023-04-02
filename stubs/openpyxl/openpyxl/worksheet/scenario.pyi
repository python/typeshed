from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, Convertible, String, _ConvertibleToBool, _ConvertibleToMultiCellRange
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.cell_range import MultiCellRange

class InputCells(Serialisable):
    tagname: str
    r: String[Literal[False]]
    deleted: Bool[Literal[True]]
    undone: Bool[Literal[True]]
    val: String[Literal[False]]
    numFmtId: Incomplete
    def __init__(
        self,
        r: str,
        deleted: _ConvertibleToBool | None,
        undone: _ConvertibleToBool | None,
        val: str,
        numFmtId: Incomplete | None = None,
    ) -> None: ...

class Scenario(Serialisable):
    tagname: str
    inputCells: Incomplete
    name: String[Literal[False]]
    locked: Bool[Literal[True]]
    hidden: Bool[Literal[True]]
    user: String[Literal[True]]
    comment: String[Literal[True]]
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        inputCells,
        name: str,
        locked: _ConvertibleToBool | None = False,
        hidden: _ConvertibleToBool | None = False,
        count: Unused = None,
        user: str | None = None,
        comment: str | None = None,
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
