from .basetypes import SimpleParameter, WidgetParameterItem

class ColorParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...

class ColorParameter(SimpleParameter):
    itemClass = ColorParameterItem
    def value(self): ...
    def saveState(self, filter=None): ...
