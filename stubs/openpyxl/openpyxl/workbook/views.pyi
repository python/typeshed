from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import NoneSet, Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

_BookViewVilibility: TypeAlias = Literal["visible", "hidden", "veryHidden"]
_CustomWorkbookViewShowComments: TypeAlias = Literal["commNone", "commIndicator", "commIndAndComment"]
_CustomWorkbookViewShowObjects: TypeAlias = Literal["all", "placeholders"]

class BookView(Serialisable):
    tagname: str
    visibility: NoneSet[_BookViewVilibility]
    minimized: Incomplete
    showHorizontalScroll: Incomplete
    showVerticalScroll: Incomplete
    showSheetTabs: Incomplete
    xWindow: Incomplete
    yWindow: Incomplete
    windowWidth: Incomplete
    windowHeight: Incomplete
    tabRatio: Incomplete
    firstSheet: Incomplete
    activeTab: Incomplete
    autoFilterDateGrouping: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        visibility: _BookViewVilibility | Literal["none"] | None = "visible",
        minimized: bool = False,
        showHorizontalScroll: bool = True,
        showVerticalScroll: bool = True,
        showSheetTabs: bool = True,
        xWindow: Incomplete | None = None,
        yWindow: Incomplete | None = None,
        windowWidth: Incomplete | None = None,
        windowHeight: Incomplete | None = None,
        tabRatio: int = 600,
        firstSheet: int = 0,
        activeTab: int = 0,
        autoFilterDateGrouping: bool = True,
        extLst: Unused = None,
    ) -> None: ...

class CustomWorkbookView(Serialisable):
    tagname: str
    name: Incomplete
    guid: Incomplete
    autoUpdate: Incomplete
    mergeInterval: Incomplete
    changesSavedWin: Incomplete
    onlySync: Incomplete
    personalView: Incomplete
    includePrintSettings: Incomplete
    includeHiddenRowCol: Incomplete
    maximized: Incomplete
    minimized: Incomplete
    showHorizontalScroll: Incomplete
    showVerticalScroll: Incomplete
    showSheetTabs: Incomplete
    xWindow: Incomplete
    yWindow: Incomplete
    windowWidth: Incomplete
    windowHeight: Incomplete
    tabRatio: Incomplete
    activeSheetId: Incomplete
    showFormulaBar: Incomplete
    showStatusbar: Incomplete
    showComments: NoneSet[_CustomWorkbookViewShowComments]
    showObjects: NoneSet[_CustomWorkbookViewShowObjects]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        guid: Incomplete | None = None,
        autoUpdate: Incomplete | None = None,
        mergeInterval: Incomplete | None = None,
        changesSavedWin: Incomplete | None = None,
        onlySync: Incomplete | None = None,
        personalView: Incomplete | None = None,
        includePrintSettings: Incomplete | None = None,
        includeHiddenRowCol: Incomplete | None = None,
        maximized: Incomplete | None = None,
        minimized: Incomplete | None = None,
        showHorizontalScroll: Incomplete | None = None,
        showVerticalScroll: Incomplete | None = None,
        showSheetTabs: Incomplete | None = None,
        xWindow: Incomplete | None = None,
        yWindow: Incomplete | None = None,
        windowWidth: Incomplete | None = None,
        windowHeight: Incomplete | None = None,
        tabRatio: Incomplete | None = None,
        activeSheetId: Incomplete | None = None,
        showFormulaBar: Incomplete | None = None,
        showStatusbar: Incomplete | None = None,
        showComments: _CustomWorkbookViewShowComments | Literal["none"] | None = "commIndicator",
        showObjects: _CustomWorkbookViewShowObjects | Literal["none"] | None = "all",
        extLst: Unused = None,
    ) -> None: ...
