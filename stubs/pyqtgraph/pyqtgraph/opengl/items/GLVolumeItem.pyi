from _typeshed import Incomplete

from OpenGL.GL import *

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLVolumeItem"]

class GLVolumeItem(GLGraphicsItem):
    sliceDensity: Incomplete
    smooth: Incomplete
    data: Incomplete
    texture: Incomplete
    def __init__(
        self, data, sliceDensity: int = 1, smooth: bool = True, glOptions: str = "translucent", parentItem=None
    ) -> None: ...
    def setData(self, data) -> None: ...
    def paint(self) -> None: ...
    def drawVolume(self, ax, d) -> None: ...
