from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Convertible, _ConvertibleToMultiCellRange
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.cell_range import MultiCellRange

class InputCells(Serialisable):
    tagname: str
    r: Incomplete
    deleted: Incomplete
    undone: Incomplete
    val: Incomplete
    numFmtId: Incomplete
    def __init__(
        self,
        r: Incomplete | None = None,
        deleted: bool = False,
        undone: bool = False,
        val: Incomplete | None = None,
        numFmtId: Incomplete | None = None,
    ) -> None: ...

class Scenario(Serialisable):
    tagname: str
    inputCells: Incomplete
    name: Incomplete
    locked: Incomplete
    hidden: Incomplete
    user: Incomplete
    comment: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        inputCells=(),
        name: Incomplete | None = None,
        locked: bool = False,
        hidden: bool = False,
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
