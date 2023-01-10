from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable

class ChartsheetProperties(Serialisable):
    tagname: str
    published: Incomplete
    codeName: Incomplete
    tabColor: Incomplete
    __elements__: tuple[str, ...]
    def __init__(
        self, published: Incomplete | None = ..., codeName: Incomplete | None = ..., tabColor: Incomplete | None = ...
    ) -> None: ...
