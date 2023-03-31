from _typeshed import Incomplete

from openpyxl import _Decodable
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.worksheet.worksheet import _SheetVisibilityType

class Chartsheet(_WorkbookChild, Serialisable):
    tagname: str
    mime_type: str
    sheetPr: Incomplete
    sheetViews: Incomplete
    sheetProtection: Incomplete
    customSheetViews: Incomplete
    pageMargins: Incomplete
    pageSetup: Incomplete
    drawing: Incomplete
    drawingHF: Incomplete
    picture: Incomplete
    webPublishItems: Incomplete
    extLst: Incomplete
    sheet_state: _SheetVisibilityType
    headerFooter: Incomplete
    HeaderFooter: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        sheetPr: Incomplete | None = None,
        sheetViews: Incomplete | None = None,
        sheetProtection: Incomplete | None = None,
        customSheetViews: Incomplete | None = None,
        pageMargins: Incomplete | None = None,
        pageSetup: Incomplete | None = None,
        headerFooter: Incomplete | None = None,
        drawing: Incomplete | None = None,
        drawingHF: Incomplete | None = None,
        picture: Incomplete | None = None,
        webPublishItems: Incomplete | None = None,
        extLst: Incomplete | None = None,
        parent: Incomplete | None = None,
        title: str | _Decodable = "",
        sheet_state: _SheetVisibilityType = "visible",
    ) -> None: ...
    def add_chart(self, chart) -> None: ...
    def to_tree(self): ...
