from _typeshed import Incomplete

import pyqtgraph as pg

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def mouseDragEvent(self, ev, axis=None) -> None: ...

class CustomTickSliderItem(pg.TickSliderItem):
    all_ticks: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def setTicks(self, ticks) -> None: ...
    def updateRange(self, vb, viewRange) -> None: ...

app: Incomplete
axis: Incomplete
vb: Incomplete
pw: Incomplete
dates: Incomplete
tickViewer: Incomplete
r: Incomplete
