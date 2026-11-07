from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class ProgressBarParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...

class ProgressBarParameter(Parameter):
    itemClass = ProgressBarParameterItem
