from _typeshed import Incomplete

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLGradientLegendItem"]

class GLGradientLegendItem(GLGraphicsItem):
    pos: Incomplete
    size: Incomplete
    fontColor: Incomplete
    gradient: Incomplete
    labels: Incomplete
    def __init__(self, parentItem=None, **kwds) -> None: ...
    antialias: bool
    def setData(self, **kwds) -> None: ...
    def paint(self) -> None: ...
