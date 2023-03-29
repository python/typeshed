from _typeshed import Incomplete
from abc import abstractmethod
from typing_extensions import Literal

from openpyxl.chart.axis import NumericAxis, SeriesAxis, TextAxis
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

from ._3d import _3DBase
from ._chart import ChartBase

class BandFormat(Serialisable):
    tagname: str
    idx: Incomplete
    spPr: Typed[GraphicalProperties, Literal[True]]
    graphicalProperties: Incomplete
    __elements__: Incomplete
    def __init__(self, idx: int = 0, spPr: GraphicalProperties | None = None) -> None: ...

class BandFormatList(Serialisable):
    tagname: str
    bandFmt: Incomplete
    __elements__: Incomplete
    def __init__(self, bandFmt=()) -> None: ...

class _SurfaceChartBase(ChartBase):
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Typed[BandFormatList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, wireframe: Incomplete | None = None, ser=(), bandFmts: BandFormatList | None = None, **kw) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class SurfaceChart3D(_SurfaceChartBase, _3DBase):
    tagname: str
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    x_axis: Typed[TextAxis, Literal[False]]
    y_axis: Typed[NumericAxis, Literal[False]]
    z_axis: Typed[SeriesAxis, Literal[False]]
    __elements__: Incomplete
    def __init__(self, **kw) -> None: ...

class SurfaceChart(SurfaceChart3D):
    tagname: str
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, **kw) -> None: ...
