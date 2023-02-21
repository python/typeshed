from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.serialisable import Serialisable

class CustomChartsheetView(Serialisable):
    tagname: str
    guid: Incomplete
    scale: Incomplete
    state: Literal["visible", "hidden", "veryHidden"]
    zoomToFit: Incomplete
    pageMargins: Incomplete
    pageSetup: Incomplete
    headerFooter: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        guid: Incomplete | None = ...,
        scale: Incomplete | None = ...,
        state: Literal["visible", "hidden", "veryHidden"] = ...,
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
