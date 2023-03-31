from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.worksheet import _SheetVisibilityType

class CustomChartsheetView(Serialisable):
    tagname: str
    guid: Incomplete
    scale: Incomplete
    state: _SheetVisibilityType
    zoomToFit: Incomplete
    pageMargins: Incomplete
    pageSetup: Incomplete
    headerFooter: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        guid: Incomplete | None = None,
        scale: Incomplete | None = None,
        state: _SheetVisibilityType = "visible",
        zoomToFit: Incomplete | None = None,
        pageMargins: Incomplete | None = None,
        pageSetup: Incomplete | None = None,
        headerFooter: Incomplete | None = None,
    ) -> None: ...

class CustomChartsheetViews(Serialisable):
    tagname: str
    customSheetView: Incomplete
    __elements__: Incomplete
    def __init__(self, customSheetView: Incomplete | None = None) -> None: ...
