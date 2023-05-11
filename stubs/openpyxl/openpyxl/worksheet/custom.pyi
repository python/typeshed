from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import String
from openpyxl.descriptors.serialisable import Serialisable

class CustomProperty(Serialisable):
    tagname: str
    name: String[Literal[False]]
    def __init__(self, name: str) -> None: ...

class CustomProperties(Serialisable):
    tagname: str
    customPr: Incomplete
    __elements__: Incomplete
    def __init__(self, customPr=()) -> None: ...
