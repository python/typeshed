from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, String, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

class CellSmartTagPr(Serialisable):
    tagname: str
    key: String[Literal[False]]
    val: String[Literal[False]]
    def __init__(self, key: str, val: str) -> None: ...

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
    r: String[Literal[False]]
    __elements__: Incomplete
    def __init__(self, cellSmartTag, r: str) -> None: ...

class SmartTags(Serialisable):
    tagname: str
    cellSmartTags: Incomplete
    __elements__: Incomplete
    def __init__(self, cellSmartTags=()) -> None: ...
