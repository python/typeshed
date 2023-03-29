from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.chart.data_source import NumDataSource
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

class ErrorBars(Serialisable):
    tagname: str
    errDir: Incomplete
    direction: Incomplete
    errBarType: Incomplete
    style: Incomplete
    errValType: Incomplete
    size: Incomplete
    noEndCap: Incomplete
    plus: Typed[NumDataSource, Literal[True]]
    minus: Typed[NumDataSource, Literal[True]]
    val: Incomplete
    spPr: Typed[GraphicalProperties, Literal[True]]
    graphicalProperties: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        errDir: Incomplete | None = None,
        errBarType: str = "both",
        errValType: str = "fixedVal",
        noEndCap: Incomplete | None = None,
        plus: NumDataSource | None = None,
        minus: NumDataSource | None = None,
        val: Incomplete | None = None,
        spPr: GraphicalProperties | None = None,
        extLst: Unused = None,
    ) -> None: ...
