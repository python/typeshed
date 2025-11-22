from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class CalendarParameterItem(WidgetParameterItem):
    asSubItem: bool
    hideWidget: bool
    def makeWidget(self): ...

class CalendarParameter(Parameter):
    itemClass = CalendarParameterItem
    def __init__(self, **opts) -> None: ...
    def saveState(self, filter=None): ...
