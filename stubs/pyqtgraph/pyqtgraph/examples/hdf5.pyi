from _typeshed import Incomplete

import pyqtgraph as pg

plt: Incomplete

class HDF5Plot(pg.PlotCurveItem):
    hdf5: Incomplete
    limit: int
    def __init__(self, *args, **kwds) -> None: ...
    def setHDF5(self, data) -> None: ...
    def viewRangeChanged(self) -> None: ...
    def updateHDF5Plot(self) -> None: ...

def createFile(finalSize: int = 2000000000) -> None: ...

fileName: Incomplete
size: Incomplete
ok: Incomplete
f: Incomplete
curve: Incomplete
