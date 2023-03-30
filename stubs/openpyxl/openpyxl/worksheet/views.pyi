from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import NoneSet, Set, Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

_Pane: TypeAlias = Literal["bottomRight", "topRight", "bottomLeft", "topLeft"]
_SheetViewView: TypeAlias = Literal["normal", "pageBreakPreview", "pageLayout"]
_PaneState: TypeAlias = Literal["split", "frozen", "frozenSplit"]

class Pane(Serialisable):  # type: ignore[misc]
    xSplit: Incomplete
    ySplit: Incomplete
    topLeftCell: Incomplete
    activePane: Set[_Pane]
    state: Set[_PaneState]
    def __init__(
        self,
        xSplit: Incomplete | None = None,
        ySplit: Incomplete | None = None,
        topLeftCell: Incomplete | None = None,
        activePane: _Pane = "topLeft",
        state: _PaneState = "split",
    ) -> None: ...

class Selection(Serialisable):  # type: ignore[misc]
    pane: NoneSet[_Pane]
    activeCell: Incomplete
    activeCellId: Incomplete
    sqref: Incomplete
    def __init__(
        self,
        pane: _Pane | Literal["none"] | None = None,
        activeCell: str = "A1",
        activeCellId: Incomplete | None = None,
        sqref: str = "A1",
    ) -> None: ...

class SheetView(Serialisable):
    tagname: str
    windowProtection: Incomplete
    showFormulas: Incomplete
    showGridLines: Incomplete
    showRowColHeaders: Incomplete
    showZeros: Incomplete
    rightToLeft: Incomplete
    tabSelected: Incomplete
    showRuler: Incomplete
    showOutlineSymbols: Incomplete
    defaultGridColor: Incomplete
    showWhiteSpace: Incomplete
    view: NoneSet[_SheetViewView]
    topLeftCell: Incomplete
    colorId: Incomplete
    zoomScale: Incomplete
    zoomScaleNormal: Incomplete
    zoomScaleSheetLayoutView: Incomplete
    zoomScalePageLayoutView: Incomplete
    zoomToFit: Incomplete
    workbookViewId: Incomplete
    selection: Incomplete
    pane: Typed[Pane, Literal[True]]
    def __init__(
        self,
        windowProtection: Incomplete | None = None,
        showFormulas: Incomplete | None = None,
        showGridLines: Incomplete | None = None,
        showRowColHeaders: Incomplete | None = None,
        showZeros: Incomplete | None = None,
        rightToLeft: Incomplete | None = None,
        tabSelected: Incomplete | None = None,
        showRuler: Incomplete | None = None,
        showOutlineSymbols: Incomplete | None = None,
        defaultGridColor: Incomplete | None = None,
        showWhiteSpace: Incomplete | None = None,
        view: _SheetViewView | Literal["none"] | None = None,
        topLeftCell: Incomplete | None = None,
        colorId: Incomplete | None = None,
        zoomScale: Incomplete | None = None,
        zoomScaleNormal: Incomplete | None = None,
        zoomScaleSheetLayoutView: Incomplete | None = None,
        zoomScalePageLayoutView: Incomplete | None = None,
        zoomToFit: Incomplete | None = None,
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
