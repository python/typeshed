from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class FontParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...
    def updateDisplayLabel(self, value=None) -> None: ...

class FontParameter(Parameter):
    itemClass = FontParameterItem
    def saveState(self, filter=None): ...
