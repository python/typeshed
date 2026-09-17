from _typeshed import Incomplete

from OpenGL.GL import *

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLAxisItem"]

class GLAxisItem(GLGraphicsItem):
    antialias: Incomplete
    def __init__(self, size=None, antialias: bool = True, glOptions: str = "translucent", parentItem=None) -> None: ...
    def setSize(self, x=None, y=None, z=None, size=None) -> None: ...
    def size(self): ...
    def paint(self) -> None: ...
