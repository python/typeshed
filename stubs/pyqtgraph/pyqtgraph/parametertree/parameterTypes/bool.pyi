from .basetypes import WidgetParameterItem

class BoolParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...
