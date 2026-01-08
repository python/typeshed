from _typeshed import Incomplete

from pyqtgraph.Qt import QtCore

examples_: Incomplete
others: Incomplete
trivial: Incomplete
skiptest: Incomplete

class FrameCounter(QtCore.QObject):
    sigFpsUpdate: Incomplete
    count: int
    last_update: int
    interval: Incomplete
    def __init__(self, interval: int = 1000) -> None: ...
    def update(self) -> None: ...
    def timerEvent(self, evt) -> None: ...
