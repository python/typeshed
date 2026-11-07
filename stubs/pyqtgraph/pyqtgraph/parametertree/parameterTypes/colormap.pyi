from .basetypes import SimpleParameter, WidgetParameterItem

class ColorMapParameterItem(WidgetParameterItem):
    hideWidget: bool
    asSubItem: bool
    def makeWidget(self): ...

class ColorMapParameter(SimpleParameter):
    itemClass = ColorMapParameterItem
