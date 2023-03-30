from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Set
from openpyxl.descriptors.serialisable import Serialisable

_TableStyleElementType: TypeAlias = Literal[
    "wholeTable",
    "headerRow",
    "totalRow",
    "firstColumn",
    "lastColumn",
    "firstRowStripe",
    "secondRowStripe",
    "firstColumnStripe",
    "secondColumnStripe",
    "firstHeaderCell",
    "lastHeaderCell",
    "firstTotalCell",
    "lastTotalCell",
    "firstSubtotalColumn",
    "secondSubtotalColumn",
    "thirdSubtotalColumn",
    "firstSubtotalRow",
    "secondSubtotalRow",
    "thirdSubtotalRow",
    "blankRow",
    "firstColumnSubheading",
    "secondColumnSubheading",
    "thirdColumnSubheading",
    "firstRowSubheading",
    "secondRowSubheading",
    "thirdRowSubheading",
    "pageFieldLabels",
    "pageFieldValues",
]

class TableStyleElement(Serialisable):
    tagname: str
    type: Set[_TableStyleElementType]
    size: Incomplete
    dxfId: Incomplete
    def __init__(self, type: _TableStyleElementType, size: Incomplete | None = None, dxfId: Incomplete | None = None) -> None: ...

class TableStyle(Serialisable):
    tagname: str
    name: Incomplete
    pivot: Incomplete
    table: Incomplete
    count: Incomplete
    tableStyleElement: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        pivot: Incomplete | None = None,
        table: Incomplete | None = None,
        count: Incomplete | None = None,
        tableStyleElement=(),
    ) -> None: ...

class TableStyleList(Serialisable):
    tagname: str
    defaultTableStyle: Incomplete
    defaultPivotStyle: Incomplete
    tableStyle: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        count: Incomplete | None = None,
        defaultTableStyle: str = "TableStyleMedium9",
        defaultPivotStyle: str = "PivotStyleLight16",
        tableStyle=(),
    ) -> None: ...
    @property
    def count(self): ...
