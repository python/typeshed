from _typeshed import FloatInt, Incomplete

from reportlab.graphics.widgetbase import Widget
from reportlab.lib.attrmap import *
from reportlab.lib.validators import *

class DotBox(Widget):
    xlabels: Incomplete
    ylabels: Incomplete
    labelFontName: str
    labelFontSize: int
    labelOffset: int
    strokeWidth: FloatInt
    gridDivWidth: Incomplete
    gridColor: Incomplete
    dotDiameter: Incomplete
    dotColor: Incomplete
    dotXPosition: int
    dotYPosition: int
    x: int
    y: int
    def __init__(self) -> None: ...
    def demo(self, drawing=None): ...
    def draw(self): ...
