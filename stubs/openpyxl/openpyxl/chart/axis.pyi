from _typeshed import Incomplete, Unused
from abc import abstractmethod
from typing_extensions import Literal, Self, TypeAlias

from openpyxl.chart.data_source import NumFmt
from openpyxl.chart.title import Title
from openpyxl.descriptors.base import _ConvertibleToBool, _ConvertibleToFloat, _ConvertibleToInt
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .layout import Layout
from .shapes import GraphicalProperties
from .text import RichText, Text

_AxisTickMarkType: TypeAlias = Literal["cross", "in", "out", None]

class ChartLines(Serialisable):
    tagname: str
    spPr: GraphicalProperties | None
    graphicalProperties = spPr  # noqa: F821
    def __init__(self, spPr: GraphicalProperties | None = None) -> None: ...

class Scaling(Serialisable):
    tagname: str
    @property
    def logBase(self) -> float | None: ...
    @logBase.setter
    def logBase(self, __value: _ConvertibleToFloat | None) -> None: ...
    orientation: Literal["maxMin", "minMax"]
    @property
    def max(self) -> float | None: ...
    @max.setter
    def max(self, __value: _ConvertibleToFloat | None) -> None: ...
    @property
    def min(self) -> float | None: ...
    @min.setter
    def min(self, __value: _ConvertibleToFloat | None) -> None: ...
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        logBase: _ConvertibleToFloat | None = None,
        orientation: Literal["maxMin", "minMax"] = "minMax",
        max: _ConvertibleToFloat | None = None,
        min: _ConvertibleToFloat | None = None,
        extLst: Unused = None,
    ) -> None: ...

class _BaseAxis(Serialisable):
    @property
    def axId(self) -> int: ...
    @axId.setter
    def axId(self, __value: _ConvertibleToInt) -> None: ...
    scaling: Scaling
    @property
    def delete(self) -> bool: ...
    @delete.setter
    def delete(self, __value: _ConvertibleToBool) -> None: ...
    axPos: Literal["b", "l", "r", "t"]
    majorGridlines: ChartLines | None
    minorGridlines: ChartLines | None
    title: Title | None
    numFmt: NumFmt | None
    number_format = numFmt  # noqa: F821
    majorTickMark: _AxisTickMarkType
    minorTickMark: _AxisTickMarkType
    tickLblPos: Literal["high", "low", "nextTo", None]
    spPr: GraphicalProperties | None
    graphicalProperties = spPr  # noqa: F821
    txPr: RichText | None
    textProperties = txPr  # noqa: F821
    @property
    def crossAx(self) -> int: ...
    @crossAx.setter
    def crossAx(self, __value: _ConvertibleToInt) -> None: ...
    crosses: Literal["autoZero", "max", "min", None]
    @property
    def crossesAt(self) -> float | None: ...
    @crossesAt.setter
    def crossesAt(self, __value: _ConvertibleToFloat | None) -> None: ...
    __elements__: tuple[str, ...]
    def __init__(
        self,
        axId: _ConvertibleToInt,
        scaling: Scaling | None,
        delete: _ConvertibleToBool,
        axPos: str,
        majorGridlines: ChartLines | None,
        minorGridlines: ChartLines | None,
        title: Title | None,
        numFmt: Incomplete | None,
        majorTickMark: _AxisTickMarkType,
        minorTickMark: _AxisTickMarkType,
        tickLblPos: Literal["high", "low", "nextTo", None],
        spPr: GraphicalProperties | None,
        txPr: RichText | None,
        crossAx: _ConvertibleToInt,
        crosses: Literal["autoZero", "max", "min", None] = None,
        crossesAt: _ConvertibleToFloat | None = None,
    ) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class DisplayUnitsLabel(Serialisable):
    tagname: str
    layout: Layout | None
    tx: Text | None
    text = tx  # noqa: F821
    spPr: GraphicalProperties | None
    graphicalProperties = spPr  # noqa: F821
    txPr: RichText | None
    textPropertes = txPr  # noqa: F821
    __elements__: tuple[str, ...]
    def __init__(
        self,
        layout: Layout | None = None,
        tx: Text | None = None,
        spPr: GraphicalProperties | None = None,
        txPr: RichText | None = None,
    ) -> None: ...

_BuiltInUnitType: TypeAlias = Literal[
    "hundreds",
    "thousands",
    "tenThousands",
    "hundredThousands",
    "millions",
    "tenMillions",
    "hundredMillions",
    "billions",
    "trillions",
    None,
]

class DisplayUnitsLabelList(Serialisable):
    tagname: str
    @property
    def custUnit(self) -> float | None: ...
    @custUnit.setter
    def custUnit(self, __value: _ConvertibleToFloat | None) -> None: ...
    builtInUnit: _BuiltInUnitType
    dispUnitsLbl: DisplayUnitsLabel | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        custUnit: float | None = None,
        builtInUnit: _BuiltInUnitType = None,
        dispUnitsLbl: DisplayUnitsLabel | None = None,
        extLst: Unused = None,
    ) -> None: ...

class NumericAxis(_BaseAxis):
    tagname: str
    crossBetween: Literal["between", "midCat", None]
    @property
    def majorUnit(self) -> float | None: ...
    @majorUnit.setter
    def majorUnit(self, __value: _ConvertibleToFloat | None) -> None: ...
    @property
    def minorUnit(self) -> float | None: ...
    @minorUnit.setter
    def minorUnit(self, __value: _ConvertibleToFloat | None) -> None: ...
    dispUnits: DisplayUnitsLabelList | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        crossBetween: Literal["between", "midCat", None] = None,
        majorUnit: _ConvertibleToFloat | None = None,
        minorUnit: _ConvertibleToFloat | None = None,
        dispUnits: DisplayUnitsLabelList | None = None,
        extLst: Unused = None,
        axId: _ConvertibleToInt = ...,
        scaling: Scaling | None = ...,
        delete: _ConvertibleToBool = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: _AxisTickMarkType = ...,
        minorTickMark: _AxisTickMarkType = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: _ConvertibleToInt = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _ConvertibleToFloat | None = ...,
    ) -> None: ...
    @classmethod
    def from_tree(cls, node: _Element) -> Self: ...

class TextAxis(_BaseAxis):
    tagname: str
    @property
    def auto(self) -> bool | None: ...
    @auto.setter
    def auto(self, __value: _ConvertibleToBool) -> None: ...
    lblAlgn: Literal["ctr", "l", "r", None]
    @property
    def lblOffset(self) -> float: ...
    @lblOffset.setter
    def lblOffset(self, __value: _ConvertibleToFloat) -> None: ...
    @property
    def tickLblSkip(self) -> int | None: ...
    @tickLblSkip.setter
    def tickLblSkip(self, __value: _ConvertibleToInt | None) -> None: ...
    @property
    def tickMarkSkip(self) -> int | None: ...
    @tickMarkSkip.setter
    def tickMarkSkip(self, __value: _ConvertibleToInt | None) -> None: ...
    @property
    def noMultiLvlLbl(self) -> bool | None: ...
    @noMultiLvlLbl.setter
    def noMultiLvlLbl(self, __value: _ConvertibleToBool) -> None: ...
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        auto: _ConvertibleToBool = None,
        lblAlgn: Literal["ctr", "l", "r", None] = None,
        lblOffset: _ConvertibleToFloat = 100,
        tickLblSkip: _ConvertibleToInt | None = None,
        tickMarkSkip: _ConvertibleToInt | None = None,
        noMultiLvlLbl: _ConvertibleToBool = None,
        extLst: Unused = None,
        axId: _ConvertibleToInt = ...,
        scaling: Scaling | None = ...,
        delete: _ConvertibleToBool = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: _AxisTickMarkType = ...,
        minorTickMark: _AxisTickMarkType = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: _ConvertibleToInt = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _ConvertibleToFloat | None = ...,
    ) -> None: ...

_TimeUnitType: TypeAlias = Literal["days", "months", "years", None]

class DateAxis(TextAxis):
    tagname: str
    @property
    def auto(self) -> bool | None: ...
    @auto.setter
    def auto(self, __value: _ConvertibleToBool) -> None: ...
    @property  # type: ignore[override]
    def lblOffset(self) -> int | None: ...
    @lblOffset.setter
    def lblOffset(self, __value: _ConvertibleToInt | None) -> None: ...
    baseTimeUnit: _TimeUnitType
    @property
    def majorUnit(self) -> float | None: ...
    @majorUnit.setter
    def majorUnit(self, __value: _ConvertibleToFloat | None) -> None: ...
    majorTimeUnit: _TimeUnitType
    @property
    def minorUnit(self) -> float | None: ...
    @minorUnit.setter
    def minorUnit(self, __value: _ConvertibleToFloat | None) -> None: ...
    minorTimeUnit: _TimeUnitType
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        auto: _ConvertibleToBool = None,
        lblOffset: _ConvertibleToInt | None = None,
        baseTimeUnit: _TimeUnitType = None,
        majorUnit: _ConvertibleToFloat | None = None,
        majorTimeUnit: _TimeUnitType = None,
        minorUnit: _ConvertibleToFloat | None = None,
        minorTimeUnit: _TimeUnitType = None,
        extLst: ExtensionList | None = None,
        axId: _ConvertibleToInt = ...,
        scaling: Scaling | None = ...,
        delete: _ConvertibleToBool = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: _AxisTickMarkType = ...,
        minorTickMark: _AxisTickMarkType = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: _ConvertibleToInt = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _ConvertibleToFloat | None = ...,
    ) -> None: ...

class SeriesAxis(_BaseAxis):
    tagname: str
    @property
    def tickLblSkip(self) -> int | None: ...
    @tickLblSkip.setter
    def tickLblSkip(self, __value: _ConvertibleToInt | None) -> None: ...
    @property
    def tickMarkSkip(self) -> int | None: ...
    @tickMarkSkip.setter
    def tickMarkSkip(self, __value: _ConvertibleToInt | None) -> None: ...
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        tickLblSkip: _ConvertibleToInt | None = None,
        tickMarkSkip: _ConvertibleToInt | None = None,
        extLst: Unused = None,
        axId: _ConvertibleToInt = ...,
        scaling: Scaling | None = ...,
        delete: _ConvertibleToBool = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: _AxisTickMarkType = ...,
        minorTickMark: _AxisTickMarkType = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: _ConvertibleToInt = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _ConvertibleToFloat | None = ...,
    ) -> None: ...
