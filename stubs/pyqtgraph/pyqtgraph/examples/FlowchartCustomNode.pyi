from _typeshed import Incomplete

from pyqtgraph.flowchart import Node
from pyqtgraph.flowchart.library.common import CtrlNode

app: Incomplete
win: Incomplete
cw: Incomplete
layout: Incomplete
fc: Incomplete
w: Incomplete
v1: Incomplete
v2: Incomplete
data: Incomplete

class ImageViewNode(Node):
    nodeName: str
    view: Incomplete
    def __init__(self, name) -> None: ...
    def setView(self, view) -> None: ...
    def process(self, data, display: bool = True) -> None: ...

class UnsharpMaskNode(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def __init__(self, name) -> None: ...
    def process(self, dataIn, display: bool = True): ...

library: Incomplete
v1Node: Incomplete
v2Node: Incomplete
fNode: Incomplete
