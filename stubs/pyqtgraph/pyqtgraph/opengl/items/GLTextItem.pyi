from _typeshed import Incomplete

from OpenGL.GL import *

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLTextItem"]

class GLTextItem(GLGraphicsItem):
    pos: Incomplete
    color: Incomplete
    text: str
    font: Incomplete
    def __init__(self, parentItem=None, **kwds) -> None: ...
    def setData(self, **kwds) -> None: ...
    def paint(self) -> None: ...
