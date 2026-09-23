from _typeshed import Incomplete

from .GraphicsView import GraphicsView

__all__ = ["HistogramLUTWidget"]

class HistogramLUTWidget(GraphicsView):
    item: Incomplete
    orientation: Incomplete
    def __init__(self, parent=None, *args, **kargs) -> None: ...
    def sizeHint(self): ...
    def __getattr__(self, attr): ...
