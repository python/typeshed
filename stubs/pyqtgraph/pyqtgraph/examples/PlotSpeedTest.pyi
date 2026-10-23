from _typeshed import Incomplete

import pyqtgraph as pg

parser: Incomplete
args: Incomplete
use_opengl: Incomplete
sfmt: Incomplete

class MonkeyCurveItem(pg.PlotCurveItem):
    monkey_mode: str
    def __init__(self, *args, **kwds) -> None: ...
    def setMethod(self, value) -> None: ...
    def paint(self, painter, opt, widget): ...

app: Incomplete
default_pen: Incomplete
params: Incomplete
pt: Incomplete
pw: Incomplete
splitter: Incomplete
interactor: Incomplete
curve: Incomplete
iterations_counter: Incomplete

def makeData(noise=..., nsamples=..., frames=..., fsample=..., frequency=..., amplitude=...) -> None: ...
def update(antialias=..., connect: str = "all", skipFiniteCheck: bool = False) -> None: ...
def updateOptions(
    curvePen=..., plotMethod: str = "pyqtgraph", fillLevel: bool = False, enableExperimental=..., useOpenGL=...
) -> None: ...

timer: Incomplete
framecnt: Incomplete
