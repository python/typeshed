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
        guid: Incomplete | None = ...,
        scale: Incomplete | None = ...,
        state: _SheetVisibilityType = ...,
        zoomToFit: Incomplete | None = ...,
        pageMargins: Incomplete | None = ...,
        pageSetup: Incomplete | None = ...,
        headerFooter: Incomplete | None = ...,
    ) -> None: ...

class CustomChartsheetViews(Serialisable):
    tagname: str
    customSheetView: Incomplete
    __elements__: Incomplete
    def __init__(self, customSheetView: Incomplete | None = ...) -> None: ...
