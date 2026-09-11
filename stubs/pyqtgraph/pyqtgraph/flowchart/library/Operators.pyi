from _typeshed import Incomplete

from ..Node import Node
from .common import CtrlNode

class UniOpNode(Node):
    fn: Incomplete
    def __init__(self, name, fn) -> None: ...
    def process(self, **args): ...

class BinOpNode(CtrlNode):
    uiTemplate: Incomplete
    fn: Incomplete
    def __init__(self, name, fn) -> None: ...
    def process(self, **args): ...

class AbsNode(UniOpNode):
    nodeName: str
    def __init__(self, name) -> None: ...

class AddNode(BinOpNode):
    nodeName: str
    def __init__(self, name) -> None: ...

class SubtractNode(BinOpNode):
    nodeName: str
    def __init__(self, name) -> None: ...

class MultiplyNode(BinOpNode):
    nodeName: str
    def __init__(self, name) -> None: ...

class DivideNode(BinOpNode):
    nodeName: str
    def __init__(self, name) -> None: ...

class FloorDivideNode(BinOpNode):
    nodeName: str
    def __init__(self, name) -> None: ...
