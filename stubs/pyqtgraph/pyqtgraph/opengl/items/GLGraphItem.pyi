from _typeshed import Incomplete

from OpenGL.GL import *

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLGraphItem"]

class GLGraphItem(GLGraphicsItem):
    edges: Incomplete
    edgeColor: Incomplete
    edgeWidth: float
    scatter: Incomplete
    def __init__(self, parentItem=None, **kwds) -> None: ...
    def setData(self, **kwds) -> None: ...
    def initializeGL(self) -> None: ...
    def paint(self) -> None: ...
