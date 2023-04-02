from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, Set, String, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

_WebPublishItemSourceType: TypeAlias = Literal[
    "sheet", "printArea", "autoFilter", "range", "chart", "pivotTable", "query", "label"
]

class WebPublishItem(Serialisable):
    tagname: str
    id: Incomplete
    divId: String[Literal[False]]
    sourceType: Set[_WebPublishItemSourceType]
    sourceRef: String[Literal[False]]
    sourceObject: String[Literal[True]]
    destinationFile: String[Literal[False]]
    title: String[Literal[True]]
    autoRepublish: Bool[Literal[True]]
    def __init__(
        self,
        id: Incomplete | None,
        divId: str,
        sourceType: _WebPublishItemSourceType,
        sourceRef: str,
        sourceObject: str | None,
        destinationFile: str,
        title: str | None = None,
        autoRepublish: _ConvertibleToBool | None = None,
    ) -> None: ...

class WebPublishItems(Serialisable):
    tagname: str
    count: Incomplete
    webPublishItem: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, webPublishItem: Incomplete | None = None) -> None: ...
