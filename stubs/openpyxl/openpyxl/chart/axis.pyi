from _typeshed import Incomplete, Self
from abc import abstractmethod
from typing_extensions import Literal, TypeAlias

from openpyxl.chart.data_source import NumFmt
from openpyxl.chart.title import Title
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .layout import Layout
from .shapes import GraphicalProperties
from .text import RichText, Text

_Unused: TypeAlias = object

class ChartLines(Serialisable):
    tagname: str
    spPr: GraphicalProperties | None = ...
    graphicalProperties = spPr
    def __init__(self, spPr: GraphicalProperties | None = ...) -> None: ...

class Scaling(Serialisable):
    tagname: str
    logBase: float | None
    orientation: Literal["maxMin", "minMax"]
    max: float | None
    min: float | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        logBase: float | None = ...,
        orientation: Literal["maxMin", "minMax"] = ...,
        max: float | None = ...,
        min: float | None = ...,
        extLst: _Unused = ...,
    ) -> None: ...

class _BaseAxis(Serialisable):
    axId: int
    scaling: Scaling
    delete: bool | None
    axPos: Literal["b", "l", "r", "t"]
    majorGridlines: ChartLines | None
    minorGridlines: ChartLines | None
    title: Title | None
    numFmt: NumFmt | None = ...
    number_format = numFmt
    majorTickMark: Literal["cross", "in", "out", None]
    minorTickMark: Literal["cross", "in", "out", None]
    tickLblPos: Literal["high", "low", "nextTo", None]
    spPr: GraphicalProperties | None = ...
    graphicalProperties = spPr
    txPr: RichText | None = ...
    textProperties = txPr
    crossAx: int
    crosses: Literal["autoZero", "max", "min", None]
    crossesAt: float | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        axId: int,
        scaling: Scaling | None,
        delete: bool | None,
        axPos: str,
        majorGridlines: ChartLines | None,
        minorGridlines: ChartLines | None,
        title: Title | None,
        numFmt: Incomplete | None,
        majorTickMark: Literal["cross", "in", "out", None],
        minorTickMark: Literal["cross", "in", "out", None],
        tickLblPos: Literal["high", "low", "nextTo", None],
        spPr: GraphicalProperties | None,
        txPr: RichText | None,
        crossAx: int,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: float | None = ...,
    ) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class DisplayUnitsLabel(Serialisable):
    tagname: str
    layout: Layout | None
    tx: Text | None = ...
    text = tx
    spPr: GraphicalProperties | None = ...
    graphicalProperties = spPr
    txPr: RichText | None = ...
    textPropertes = txPr
    __elements__: tuple[str, ...]
    def __init__(
        self,
        layout: Layout | None = ...,
        tx: Text | None = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
    ) -> None: ...

class DisplayUnitsLabelList(Serialisable):
    tagname: str
    custUnit: float | None
    builtInUnit: Literal[
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
    dispUnitsLbl: DisplayUnitsLabel | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        custUnit: float | None = ...,
        builtInUnit: Literal[
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
        ] = ...,
        dispUnitsLbl: DisplayUnitsLabel | None = ...,
        extLst: _Unused = ...,
    ) -> None: ...

class NumericAxis(_BaseAxis):
    tagname: str
    crossBetween: Literal["between", "midCat", None]
    majorUnit: float | None
    minorUnit: float | None
    dispUnits: DisplayUnitsLabelList | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        crossBetween: Incomplete | None = ...,
        majorUnit: Incomplete | None = ...,
        minorUnit: Incomplete | None = ...,
        dispUnits: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        axId: int = ...,
        scaling: Scaling | None = ...,
        delete: bool | None = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Literal["cross", "in", "out", None] = ...,
        minorTickMark: Literal["cross", "in", "out", None] = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: int = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: float | None = ...,
    ) -> None: ...
    @classmethod
    def from_tree(cls: Self, node: _Element) -> Self: ...

class TextAxis(_BaseAxis):
    tagname: str
    auto: bool | None
    lblAlgn: Literal["ctr", "l", "r", None]
    lblOffset: float
    tickLblSkip: int | None
    tickMarkSkip: int | None
    noMultiLvlLbl: bool | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        auto: bool | None = ...,
        lblAlgn: Literal["ctr", "l", "r", None] = ...,
        lblOffset: float = ...,
        tickLblSkip: int | None = ...,
        tickMarkSkip: int | None = ...,
        noMultiLvlLbl: bool | None = ...,
        extLst: _Unused = ...,
        axId: int = ...,
        scaling: Scaling | None = ...,
        delete: bool | None = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Literal["cross", "in", "out", None] = ...,
        minorTickMark: Literal["cross", "in", "out", None] = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: int = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: float | None = ...,
    ) -> None: ...

class DateAxis(TextAxis):
    tagname: str
    auto: bool | None
    lblOffset: int | None  # type: ignore[assignment]
    baseTimeUnit: Literal["days", "months", "years", None]
    majorUnit: float | None
    majorTimeUnit: Literal["days", "months", "years", None]
    minorUnit: float | None
    minorTimeUnit: Literal["days", "months", "years", None]
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        auto: bool | None = ...,
        lblOffset: int | None = ...,
        baseTimeUnit: Literal["days", "months", "years", None] = ...,
        majorUnit: float | None = ...,
        majorTimeUnit: Literal["days", "months", "years", None] = ...,
        minorUnit: float | None = ...,
        minorTimeUnit: Literal["days", "months", "years", None] = ...,
        extLst: ExtensionList | None = ...,
        axId: int = ...,
        scaling: Scaling | None = ...,
        delete: bool | None = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Literal["cross", "in", "out", None] = ...,
        minorTickMark: Literal["cross", "in", "out", None] = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: int = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: float | None = ...,
    ) -> None: ...

class SeriesAxis(_BaseAxis):
    tagname: str
    tickLblSkip: int | None
    tickMarkSkip: int | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        tickLblSkip: int | None = ...,
        tickMarkSkip: int | None = ...,
        extLst: _Unused = ...,
        axId: int = ...,
        scaling: Scaling | None = ...,
        delete: bool | None = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Literal["cross", "in", "out", None] = ...,
        minorTickMark: Literal["cross", "in", "out", None] = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: int = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: float | None = ...,
    ) -> None: ...
