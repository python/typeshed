from _typeshed import Incomplete

from .GraphicsObject import GraphicsObject
from .GraphicsWidgetAnchor import GraphicsWidgetAnchor

__all__ = ["ScaleBar"]

class ScaleBar(GraphicsWidgetAnchor, GraphicsObject):
    brush: Incomplete
    pen: Incomplete
    size: Incomplete
    offset: Incomplete
    bar: Incomplete
    text: Incomplete
    def __init__(self, size, width: int = 5, brush=None, pen=None, suffix: str = "m", offset=None) -> None: ...
    def changeParent(self) -> None: ...
    def updateBar(self) -> None: ...
    def boundingRect(self): ...
    def setParentItem(self, p): ...
