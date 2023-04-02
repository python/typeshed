from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import String
from openpyxl.descriptors.serialisable import Serialisable

class FunctionGroup(Serialisable):
    tagname: str
    name: String[Literal[False]]
    def __init__(self, name: str) -> None: ...

class FunctionGroupList(Serialisable):
    tagname: str
    builtInGroupCount: Incomplete
    functionGroup: Incomplete
    __elements__: Incomplete
    def __init__(self, builtInGroupCount: int = 16, functionGroup=()) -> None: ...
