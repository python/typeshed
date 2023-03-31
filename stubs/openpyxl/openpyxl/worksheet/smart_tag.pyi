from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

class CellSmartTagPr(Serialisable):
    tagname: str
    key: Incomplete
    val: Incomplete
    def __init__(self, key: Incomplete | None = None, val: Incomplete | None = None) -> None: ...

class CellSmartTag(Serialisable):
    tagname: str
    cellSmartTagPr: Incomplete
    type: Incomplete
    deleted: Bool[Literal[True]]
    xmlBased: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        cellSmartTagPr=(),
        type: Incomplete | None = None,
        deleted: _ConvertibleToBool | None = False,
        xmlBased: _ConvertibleToBool | None = False,
    ) -> None: ...

class CellSmartTags(Serialisable):
    tagname: str
    cellSmartTag: Incomplete
    r: Incomplete
    __elements__: Incomplete
    def __init__(self, cellSmartTag=(), r: Incomplete | None = None) -> None: ...

class SmartTags(Serialisable):
    tagname: str
    cellSmartTags: Incomplete
    __elements__: Incomplete
    def __init__(self, cellSmartTags=()) -> None: ...
