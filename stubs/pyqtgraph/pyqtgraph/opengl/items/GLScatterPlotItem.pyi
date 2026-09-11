from _typeshed import Incomplete

from OpenGL.GL import *

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLScatterPlotItem"]

class GLScatterPlotItem(GLGraphicsItem):
    pos: Incomplete
    size: int
    color: Incomplete
    pxMode: bool
    shader: Incomplete
    def __init__(self, parentItem=None, **kwds) -> None: ...
    def setData(self, **kwds) -> None: ...
    pointTexture: Incomplete
    def initializeGL(self): ...
    def paint(self) -> None: ...
