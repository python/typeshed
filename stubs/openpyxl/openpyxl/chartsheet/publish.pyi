from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, Set, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

_WebPublishItemSourceType: TypeAlias = Literal[
    "sheet", "printArea", "autoFilter", "range", "chart", "pivotTable", "query", "label"
]

class WebPublishItem(Serialisable):
    tagname: str
    id: Incomplete
    divId: Incomplete
    sourceType: Set[_WebPublishItemSourceType]
    sourceRef: Incomplete
    sourceObject: Incomplete
    destinationFile: Incomplete
    title: Incomplete
    autoRepublish: Bool[Literal[True]]
    def __init__(
        self,
        id: Incomplete | None,
        divId: Incomplete | None,
        sourceType: _WebPublishItemSourceType,
        sourceRef: Incomplete | None = None,
        sourceObject: Incomplete | None = None,
        destinationFile: Incomplete | None = None,
        title: Incomplete | None = None,
        autoRepublish: _ConvertibleToBool | None = None,
    ) -> None: ...

class WebPublishItems(Serialisable):
    tagname: str
    count: Incomplete
    webPublishItem: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, webPublishItem: Incomplete | None = None) -> None: ...
