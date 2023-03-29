from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

class ChartsheetView(Serialisable):
    tagname: str
    tabSelected: Incomplete
    zoomScale: Incomplete
    workbookViewId: Incomplete
    zoomToFit: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        tabSelected: Incomplete | None = None,
        zoomScale: Incomplete | None = None,
        workbookViewId: int = 0,
        zoomToFit: Incomplete | None = True,
        extLst: Unused = None,
    ) -> None: ...

class ChartsheetViewList(Serialisable):
    tagname: str
    sheetView: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, sheetView: Incomplete | None = None, extLst: Unused = None) -> None: ...
