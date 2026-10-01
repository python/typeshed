from _typeshed import Incomplete

from OpenGL.GL import *

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLLinePlotItem"]

class GLLinePlotItem(GLGraphicsItem):
    pos: Incomplete
    mode: str
    width: float
    color: Incomplete
    def __init__(self, parentItem=None, **kwds) -> None: ...
    antialias: bool
    def setData(self, **kwds) -> None: ...
    def paint(self) -> None: ...
