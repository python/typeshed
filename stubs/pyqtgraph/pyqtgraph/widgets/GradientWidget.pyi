from _typeshed import Incomplete

from .GraphicsView import GraphicsView

__all__ = ["GradientWidget"]

class GradientWidget(GraphicsView):
    sigGradientChanged: Incomplete
    sigGradientChangeFinished: Incomplete
    maxDim: int
    item: Incomplete
    def __init__(self, parent=None, orientation: str = "bottom", *args, **kargs) -> None: ...
    orientation: Incomplete
    def setOrientation(self, ort) -> None: ...
    def setMaxDim(self, mx=None) -> None: ...
    def __getattr__(self, attr): ...
    def widgetGroupInterface(self): ...
