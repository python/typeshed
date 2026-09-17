from _typeshed import Incomplete

from ..graphicsItems.ViewBox import ViewBox
from ..widgets.GraphicsView import GraphicsView

translate: Incomplete

class FlowchartGraphicsView(GraphicsView):
    sigHoverOver: Incomplete
    sigClicked: Incomplete
    def __init__(self, widget, *args) -> None: ...
    def viewBox(self): ...

class FlowchartViewBox(ViewBox):
    widget: Incomplete
    def __init__(self, widget, *args, **kwargs) -> None: ...
    def getMenu(self, ev): ...
    def getContextMenus(self, ev): ...
