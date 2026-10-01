from _typeshed import Incomplete

from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class TextParameterItem(WidgetParameterItem):
    hideWidget: bool
    asSubItem: bool
    textBox: Incomplete
    def makeWidget(self): ...

class TextParameter(Parameter):
    itemClass = TextParameterItem
