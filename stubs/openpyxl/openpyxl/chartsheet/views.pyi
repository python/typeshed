from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, Typed, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

class ChartsheetView(Serialisable):
    tagname: str
    tabSelected: Bool[Literal[True]]
    zoomScale: Incomplete
    workbookViewId: Incomplete
    zoomToFit: Bool[Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        tabSelected: _ConvertibleToBool | None = None,
        zoomScale: Incomplete | None = None,
        workbookViewId: int = 0,
        zoomToFit: _ConvertibleToBool | None = True,
        extLst: Unused = None,
    ) -> None: ...

class ChartsheetViewList(Serialisable):
    tagname: str
    sheetView: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, sheetView: Incomplete | None = None, extLst: Unused = None) -> None: ...
