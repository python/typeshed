from _typeshed import Incomplete

from . import GraphicsLayout

__all__ = ["MultiPlotItem"]

class MultiPlotItem(GraphicsLayout.GraphicsLayout):
    plots: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def plot(self, data, **plotArgs) -> None: ...
    def close(self) -> None: ...
