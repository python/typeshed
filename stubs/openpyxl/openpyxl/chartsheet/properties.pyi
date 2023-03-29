from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.styles.colors import Color

class ChartsheetProperties(Serialisable):
    tagname: str
    published: Incomplete
    codeName: Incomplete
    tabColor: Typed[Color, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, published: Incomplete | None = None, codeName: Incomplete | None = None, tabColor: Color | None = None
    ) -> None: ...
