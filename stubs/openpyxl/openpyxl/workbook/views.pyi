from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, NoneSet, Typed, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

_BookViewVilibility: TypeAlias = Literal["visible", "hidden", "veryHidden"]
_CustomWorkbookViewShowComments: TypeAlias = Literal["commNone", "commIndicator", "commIndAndComment"]
_CustomWorkbookViewShowObjects: TypeAlias = Literal["all", "placeholders"]

class BookView(Serialisable):
    tagname: str
    visibility: NoneSet[_BookViewVilibility]
    minimized: Bool[Literal[True]]
    showHorizontalScroll: Bool[Literal[True]]
    showVerticalScroll: Bool[Literal[True]]
    showSheetTabs: Bool[Literal[True]]
    xWindow: Incomplete
    yWindow: Incomplete
    windowWidth: Incomplete
    windowHeight: Incomplete
    tabRatio: Incomplete
    firstSheet: Incomplete
    activeTab: Incomplete
    autoFilterDateGrouping: Bool[Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        visibility: _BookViewVilibility | Literal["none"] | None = "visible",
        minimized: _ConvertibleToBool | None = False,
        showHorizontalScroll: _ConvertibleToBool | None = True,
        showVerticalScroll: _ConvertibleToBool | None = True,
        showSheetTabs: _ConvertibleToBool | None = True,
        xWindow: Incomplete | None = None,
        yWindow: Incomplete | None = None,
        windowWidth: Incomplete | None = None,
        windowHeight: Incomplete | None = None,
        tabRatio: int = 600,
        firstSheet: int = 0,
        activeTab: int = 0,
        autoFilterDateGrouping: _ConvertibleToBool | None = True,
        extLst: Unused = None,
    ) -> None: ...

class CustomWorkbookView(Serialisable):
    tagname: str
    name: Incomplete
    guid: Incomplete
    autoUpdate: Bool[Literal[True]]
    mergeInterval: Incomplete
    changesSavedWin: Bool[Literal[True]]
    onlySync: Bool[Literal[True]]
    personalView: Bool[Literal[True]]
    includePrintSettings: Bool[Literal[True]]
    includeHiddenRowCol: Bool[Literal[True]]
    maximized: Bool[Literal[True]]
    minimized: Bool[Literal[True]]
    showHorizontalScroll: Bool[Literal[True]]
    showVerticalScroll: Bool[Literal[True]]
    showSheetTabs: Bool[Literal[True]]
    xWindow: Incomplete
    yWindow: Incomplete
    windowWidth: Incomplete
    windowHeight: Incomplete
    tabRatio: Incomplete
    activeSheetId: Incomplete
    showFormulaBar: Bool[Literal[True]]
    showStatusbar: Bool[Literal[True]]
    showComments: NoneSet[_CustomWorkbookViewShowComments]
    showObjects: NoneSet[_CustomWorkbookViewShowObjects]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        guid: Incomplete | None = None,
        autoUpdate: _ConvertibleToBool | None = None,
        mergeInterval: Incomplete | None = None,
        changesSavedWin: _ConvertibleToBool | None = None,
        onlySync: _ConvertibleToBool | None = None,
        personalView: _ConvertibleToBool | None = None,
        includePrintSettings: _ConvertibleToBool | None = None,
        includeHiddenRowCol: _ConvertibleToBool | None = None,
        maximized: _ConvertibleToBool | None = None,
        minimized: _ConvertibleToBool | None = None,
        showHorizontalScroll: _ConvertibleToBool | None = None,
        showVerticalScroll: _ConvertibleToBool | None = None,
        showSheetTabs: _ConvertibleToBool | None = None,
        xWindow: Incomplete | None = None,
        yWindow: Incomplete | None = None,
        windowWidth: Incomplete | None = None,
        windowHeight: Incomplete | None = None,
        tabRatio: Incomplete | None = None,
        activeSheetId: Incomplete | None = None,
        showFormulaBar: _ConvertibleToBool | None = None,
        showStatusbar: _ConvertibleToBool | None = None,
        showComments: _CustomWorkbookViewShowComments | Literal["none"] | None = "commIndicator",
        showObjects: _CustomWorkbookViewShowObjects | Literal["none"] | None = "all",
        extLst: Unused = None,
    ) -> None: ...
