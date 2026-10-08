from _typeshed import Incomplete

from pyqtgraph.opengl import GLGraphicsItem

SIZE: int

class GLPainterItem(GLGraphicsItem.GLGraphicsItem):
    def __init__(self, **kwds) -> None: ...
    def compute_projection(self): ...
    def paint(self) -> None: ...
    def draw(self, painter) -> None: ...

glv: Incomplete
griditem: Incomplete
axisitem: Incomplete
paintitem: Incomplete
