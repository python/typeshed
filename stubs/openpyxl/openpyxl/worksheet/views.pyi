from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, NoneSet, Set, String, Typed, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

_Pane: TypeAlias = Literal["bottomRight", "topRight", "bottomLeft", "topLeft"]
_SheetViewView: TypeAlias = Literal["normal", "pageBreakPreview", "pageLayout"]
_PaneState: TypeAlias = Literal["split", "frozen", "frozenSplit"]

class Pane(Serialisable):
    xSplit: Incomplete
    ySplit: Incomplete
    topLeftCell: String[Literal[True]]
    activePane: Set[_Pane]
    state: Set[_PaneState]
    def __init__(
        self,
        xSplit: Incomplete | None = None,
        ySplit: Incomplete | None = None,
        topLeftCell: str | None = None,
        activePane: _Pane = "topLeft",
        state: _PaneState = "split",
    ) -> None: ...

class Selection(Serialisable):
    pane: NoneSet[_Pane]
    activeCell: String[Literal[True]]
    activeCellId: Incomplete
    sqref: String[Literal[True]]
    def __init__(
        self,
        pane: _Pane | Literal["none"] | None = None,
        activeCell: str | None = "A1",
        activeCellId: Incomplete | None = None,
        sqref: str | None = "A1",
    ) -> None: ...

class SheetView(Serialisable):
    tagname: str
    windowProtection: Bool[Literal[True]]
    showFormulas: Bool[Literal[True]]
    showGridLines: Bool[Literal[True]]
    showRowColHeaders: Bool[Literal[True]]
    showZeros: Bool[Literal[True]]
    rightToLeft: Bool[Literal[True]]
    tabSelected: Bool[Literal[True]]
    showRuler: Bool[Literal[True]]
    showOutlineSymbols: Bool[Literal[True]]
    defaultGridColor: Bool[Literal[True]]
    showWhiteSpace: Bool[Literal[True]]
    view: NoneSet[_SheetViewView]
    topLeftCell: String[Literal[True]]
    colorId: Incomplete
    zoomScale: Incomplete
    zoomScaleNormal: Incomplete
    zoomScaleSheetLayoutView: Incomplete
    zoomScalePageLayoutView: Incomplete
    zoomToFit: Bool[Literal[True]]
    workbookViewId: Incomplete
    selection: Incomplete
    pane: Typed[Pane, Literal[True]]
    def __init__(
        self,
        windowProtection: _ConvertibleToBool | None = None,
        showFormulas: _ConvertibleToBool | None = None,
        showGridLines: _ConvertibleToBool | None = None,
        showRowColHeaders: _ConvertibleToBool | None = None,
        showZeros: _ConvertibleToBool | None = None,
        rightToLeft: _ConvertibleToBool | None = None,
        tabSelected: _ConvertibleToBool | None = None,
        showRuler: _ConvertibleToBool | None = None,
        showOutlineSymbols: _ConvertibleToBool | None = None,
        defaultGridColor: _ConvertibleToBool | None = None,
        showWhiteSpace: _ConvertibleToBool | None = None,
        view: _SheetViewView | Literal["none"] | None = None,
        topLeftCell: str | None = None,
        colorId: Incomplete | None = None,
        zoomScale: Incomplete | None = None,
        zoomScaleNormal: Incomplete | None = None,
        zoomScaleSheetLayoutView: Incomplete | None = None,
        zoomScalePageLayoutView: Incomplete | None = None,
        zoomToFit: _ConvertibleToBool | None = None,
        workbookViewId: int = 0,
        selection: Incomplete | None = None,
        pane: Pane | None = None,
    ) -> None: ...

class SheetViewList(Serialisable):
    tagname: str
    sheetView: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, sheetView: Incomplete | None = None, extLst: Unused = None) -> None: ...
