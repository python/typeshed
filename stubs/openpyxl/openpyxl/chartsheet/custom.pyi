from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.header_footer import HeaderFooter
from openpyxl.worksheet.page import PageMargins, PrintPageSetup

class CustomChartsheetView(Serialisable):
    tagname: str
    guid: Incomplete
    scale: Incomplete
    state: Incomplete
    zoomToFit: Incomplete
    pageMargins: Typed[PageMargins, Literal[True]]
    pageSetup: Typed[PrintPageSetup, Literal[True]]
    headerFooter: Typed[HeaderFooter, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        guid: Incomplete | None = None,
        scale: Incomplete | None = None,
        state: str = "visible",
        zoomToFit: Incomplete | None = None,
        pageMargins: PageMargins | None = None,
        pageSetup: PrintPageSetup | None = None,
        headerFooter: HeaderFooter | None = None,
    ) -> None: ...

class CustomChartsheetViews(Serialisable):
    tagname: str
    customSheetView: Incomplete
    __elements__: Incomplete
    def __init__(self, customSheetView: Incomplete | None = None) -> None: ...
