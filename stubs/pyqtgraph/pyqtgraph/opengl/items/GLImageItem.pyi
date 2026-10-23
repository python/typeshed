from _typeshed import Incomplete

from OpenGL.GL import *

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLImageItem"]

class GLImageItem(GLGraphicsItem):
    smooth: Incomplete
    texture: Incomplete
    def __init__(self, data, smooth: bool = False, glOptions: str = "translucent", parentItem=None) -> None: ...
    def initializeGL(self) -> None: ...
    data: Incomplete
    def setData(self, data) -> None: ...
    def paint(self) -> None: ...
