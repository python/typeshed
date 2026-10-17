from _typeshed import Incomplete

from pyqtgraph.Qt import QtWidgets

app: Incomplete
mw: Incomplete
gv: Incomplete
l: Incomplete
vb: Incomplete
p1: Incomplete

class movableRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, *args) -> None: ...
    savedPen: Incomplete
    def hoverEnterEvent(self, ev) -> None: ...
    def hoverLeaveEvent(self, ev) -> None: ...
    pressDelta: Incomplete
    def mousePressEvent(self, ev) -> None: ...
    def mouseMoveEvent(self, ev) -> None: ...

rect: Incomplete
xScale: Incomplete
yScale: Incomplete

def rand(n): ...
def updateData() -> None: ...

yd: Incomplete
xd: Incomplete
t: Incomplete
