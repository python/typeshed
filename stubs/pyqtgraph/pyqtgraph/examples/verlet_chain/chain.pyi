from _typeshed import Incomplete

import pyqtgraph as pg

class ChainSim(pg.QtCore.QObject):
    stepped: Incomplete
    relaxed: Incomplete
    damping: float
    relaxPerStep: int
    maxTimeStep: float
    pos: Incomplete
    mass: Incomplete
    fixed: Incomplete
    links: Incomplete
    lengths: Incomplete
    push: Incomplete
    pull: Incomplete
    initialized: bool
    lasttime: Incomplete
    lastpos: Incomplete
    def __init__(self) -> None: ...
    mrel1: Incomplete
    mrel2: Incomplete
    def init(self) -> None: ...
    def makeGraph(self): ...
    def update(self) -> None: ...
    def relax(self, n: int = 50) -> None: ...
