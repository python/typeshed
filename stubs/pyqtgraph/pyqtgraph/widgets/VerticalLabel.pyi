from _typeshed import Incomplete

from ..Qt import QtWidgets

__all__ = ["VerticalLabel"]

class VerticalLabel(QtWidgets.QLabel):
    forceWidth: Incomplete
    orientation: Incomplete
    def __init__(self, text, orientation: str = "vertical", forceWidth: bool = True) -> None: ...
    def setOrientation(self, o) -> None: ...
    hint: Incomplete
    def paintEvent(self, ev) -> None: ...
    def sizeHint(self): ...
