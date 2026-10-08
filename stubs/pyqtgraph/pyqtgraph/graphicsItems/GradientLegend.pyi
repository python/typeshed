from _typeshed import Incomplete

from .UIGraphicsItem import UIGraphicsItem

__all__ = ["GradientLegend"]

class GradientLegend(UIGraphicsItem):
    size: Incomplete
    offset: Incomplete
    brush: Incomplete
    pen: Incomplete
    textPen: Incomplete
    labels: Incomplete
    gradient: Incomplete
    def __init__(self, size, offset) -> None: ...
    def setGradient(self, g) -> None: ...
    def setColorMap(self, colormap) -> None: ...
    def setIntColorScale(self, minVal, maxVal, *args, **kargs) -> None: ...
    def setLabels(self, l) -> None: ...
    b: Incomplete
    def paint(self, p, opt, widget) -> None: ...
