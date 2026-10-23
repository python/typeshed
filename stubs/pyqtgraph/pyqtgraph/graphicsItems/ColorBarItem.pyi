from _typeshed import Incomplete

from .PlotItem import PlotItem

__all__ = ["ColorBarItem"]

class ColorBarItem(PlotItem):
    sigLevelsChanged: Incomplete
    sigLevelsChangeFinished: Incomplete
    img_list: Incomplete
    values: Incomplete
    rounding: Incomplete
    horizontal: Incomplete
    lo_lim: Incomplete
    hi_lim: Incomplete
    colorMapMenu: Incomplete
    axis: Incomplete
    bar: Incomplete
    interactive: Incomplete
    region: Incomplete
    region_changed_enable: bool
    def __init__(
        self,
        values=None,
        width: int = 25,
        colorMap=None,
        label=None,
        interactive: bool = True,
        limits=None,
        rounding: int = 1,
        orientation: str = "vertical",
        pen: str = "w",
        hoverPen: str = "r",
        hoverBrush: str = "#FF000080",
        *,
        colorMapMenu: bool = True,
    ) -> None: ...
    def setImageItem(self, img, insert_in=None) -> None: ...
    def setColorMap(self, colorMap) -> None: ...
    def colorMap(self): ...
    def setLevels(self, values=None, low=None, high=None, update_items: bool = True) -> None: ...
    def levels(self): ...
    def mouseClickEvent(self, ev) -> None: ...
