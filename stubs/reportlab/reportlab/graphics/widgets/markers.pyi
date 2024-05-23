from _typeshed import Incomplete

from reportlab.graphics.widgetbase import Widget
from reportlab.lib.validators import Validator

__version__: str

class Marker(Widget):
    def __init__(self, *args, **kw) -> None: ...
    def clone(self, **kwds): ...
    def draw(self): ...

def uSymbol2Symbol(uSymbol, x, y, color): ...

class _isSymbol(Validator):
    def test(self, x): ...

isSymbol: Incomplete

def makeMarker(name, **kw): ...
