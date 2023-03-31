from _typeshed import Incomplete, Unused
from abc import abstractmethod
from typing_extensions import Literal, TypeAlias

from openpyxl.chart.layout import Layout
from openpyxl.chart.legend import Legend
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.descriptors.base import MinMax, Set, Typed
from openpyxl.descriptors.serialisable import Serialisable

_ChartBaseDisplayBlanks: TypeAlias = Literal["span", "gap", "zero"]

class AxId(Serialisable):
    val: Incomplete
    def __init__(self, val) -> None: ...

def PlotArea(): ...

class ChartBase(Serialisable):
    legend: Typed[Legend, Literal[True]]
    layout: Typed[Layout, Literal[True]]
    roundedCorners: Incomplete
    axId: Incomplete
    visible_cells_only: Incomplete
    display_blanks: Set[_ChartBaseDisplayBlanks]
    ser: Incomplete
    series: Incomplete
    title: Incomplete
    anchor: str
    width: int
    height: float
    style: MinMax[float, Literal[True]]
    mime_type: str
    graphical_properties: Typed[GraphicalProperties, Literal[True]]
    __elements__: Incomplete
    plot_area: Incomplete
    pivotSource: Incomplete
    pivotFormats: Incomplete
    idx_base: int
    def __init__(self, axId=(), **kw: Unused) -> None: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, other): ...
    def to_tree(self, namespace: Incomplete | None = None, tagname: Incomplete | None = None, idx: Incomplete | None = None): ...  # type: ignore[override]
    def set_categories(self, labels) -> None: ...
    def add_data(self, data, from_rows: bool = False, titles_from_data: bool = False) -> None: ...
    def append(self, value) -> None: ...
    @property
    def path(self): ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...
