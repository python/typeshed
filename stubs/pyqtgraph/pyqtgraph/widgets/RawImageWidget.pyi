from _typeshed import Incomplete

from OpenGL.GL import *

from ..Qt import QtWidgets

__all__ = ["RawImageWidget", "RawImageGLWidget"]

class RawImageWidget(QtWidgets.QWidget):
    scaled: Incomplete
    opts: Incomplete
    image: Incomplete
    def __init__(self, parent=None, scaled: bool = False) -> None: ...
    def setImage(self, img, *args, **kargs) -> None: ...
    def paintEvent(self, ev) -> None: ...

class RawImageGLWidget(QOpenGLWidget):
    scaled: Incomplete
    image: Incomplete
    uploaded: bool
    smooth: bool
    opts: Incomplete
    def __init__(self, parent=None, scaled: bool = False) -> None: ...
    def setImage(self, img, *args, **kargs) -> None: ...
    texture: Incomplete
    def initializeGL(self) -> None: ...
    def uploadTexture(self) -> None: ...
    def paintGL(self) -> None: ...
