from .basetypes import Parameter, WidgetParameterItem

class ColorMapLutParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...

class ColorMapLutParameter(Parameter):
    itemClass = ColorMapLutParameterItem
