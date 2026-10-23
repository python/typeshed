from _typeshed import Incomplete

import pyqtgraph.parametertree.parameterTypes as pTypes

app: Incomplete

class ComplexParameter(pTypes.GroupParameter):
    a: Incomplete
    b: Incomplete
    def __init__(self, **opts) -> None: ...
    def aChanged(self) -> None: ...
    def bChanged(self) -> None: ...

class ScalableGroup(pTypes.GroupParameter):
    def __init__(self, **opts) -> None: ...
    def addNew(self, typ) -> None: ...

params: Incomplete
p: Incomplete

def change(param, changes) -> None: ...
def valueChanging(param, value) -> None: ...
def save() -> None: ...
def restore() -> None: ...

t: Incomplete
t2: Incomplete
win: Incomplete
layout: Incomplete
state: Incomplete
compareState: Incomplete
