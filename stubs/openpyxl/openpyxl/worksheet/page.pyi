from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, NoneSet, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

_PrintPageSetupOrientation: TypeAlias = Literal["default", "portrait", "landscape"]
_PrintPageSetupPageOrder: TypeAlias = Literal["downThenOver", "overThenDown"]
_PrintPageSetupCellComments: TypeAlias = Literal["asDisplayed", "atEnd"]
_PrintPageSetupErrors: TypeAlias = Literal["displayed", "blank", "dash", "NA"]

class PrintPageSetup(Serialisable):
    tagname: str
    orientation: NoneSet[_PrintPageSetupOrientation]
    paperSize: Incomplete
    scale: Incomplete
    fitToHeight: Incomplete
    fitToWidth: Incomplete
    firstPageNumber: Incomplete
    useFirstPageNumber: Bool[Literal[True]]
    paperHeight: Incomplete
    paperWidth: Incomplete
    pageOrder: NoneSet[_PrintPageSetupPageOrder]
    usePrinterDefaults: Bool[Literal[True]]
    blackAndWhite: Bool[Literal[True]]
    draft: Bool[Literal[True]]
    cellComments: NoneSet[_PrintPageSetupCellComments]
    errors: NoneSet[_PrintPageSetupErrors]
    horizontalDpi: Incomplete
    verticalDpi: Incomplete
    copies: Incomplete
    id: Incomplete
    def __init__(
        self,
        worksheet: Incomplete | None = None,
        orientation: _PrintPageSetupOrientation | Literal["none"] | None = None,
        paperSize: Incomplete | None = None,
        scale: Incomplete | None = None,
        fitToHeight: Incomplete | None = None,
        fitToWidth: Incomplete | None = None,
        firstPageNumber: Incomplete | None = None,
        useFirstPageNumber: _ConvertibleToBool | None = None,
        paperHeight: Incomplete | None = None,
        paperWidth: Incomplete | None = None,
        pageOrder: _PrintPageSetupPageOrder | Literal["none"] | None = None,
        usePrinterDefaults: _ConvertibleToBool | None = None,
        blackAndWhite: _ConvertibleToBool | None = None,
        draft: _ConvertibleToBool | None = None,
        cellComments: _PrintPageSetupCellComments | Literal["none"] | None = None,
        errors: _PrintPageSetupErrors | Literal["none"] | None = None,
        horizontalDpi: Incomplete | None = None,
        verticalDpi: Incomplete | None = None,
        copies: Incomplete | None = None,
        id: Incomplete | None = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def sheet_properties(self): ...
    @property
    def fitToPage(self): ...
    @fitToPage.setter
    def fitToPage(self, value) -> None: ...
    @property
    def autoPageBreaks(self): ...
    @autoPageBreaks.setter
    def autoPageBreaks(self, value) -> None: ...
    @classmethod
    def from_tree(cls, node): ...

class PrintOptions(Serialisable):
    tagname: str
    horizontalCentered: Bool[Literal[True]]
    verticalCentered: Bool[Literal[True]]
    headings: Bool[Literal[True]]
    gridLines: Bool[Literal[True]]
    gridLinesSet: Bool[Literal[True]]
    def __init__(
        self,
        horizontalCentered: _ConvertibleToBool | None = None,
        verticalCentered: _ConvertibleToBool | None = None,
        headings: _ConvertibleToBool | None = None,
        gridLines: _ConvertibleToBool | None = None,
        gridLinesSet: _ConvertibleToBool | None = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...

class PageMargins(Serialisable):
    tagname: str
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    header: Incomplete
    footer: Incomplete
    def __init__(
        self, left: float = 0.75, right: float = 0.75, top: int = 1, bottom: int = 1, header: float = 0.5, footer: float = 0.5
    ) -> None: ...
