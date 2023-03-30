from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors import Float
from openpyxl.descriptors.base import NoneSet, Set, Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.differential import DifferentialStyle

_IconSetIconSet: TypeAlias = Literal[
    "3Arrows",
    "3ArrowsGray",
    "3Flags",
    "3TrafficLights1",
    "3TrafficLights2",
    "3Signs",
    "3Symbols",
    "3Symbols2",
    "4Arrows",
    "4ArrowsGray",
    "4RedToBlack",
    "4Rating",
    "4TrafficLights",
    "5Arrows",
    "5ArrowsGray",
    "5Rating",
    "5Quarters",
]
_RuleOperator: TypeAlias = Literal[
    "lessThan",
    "lessThanOrEqual",
    "equal",
    "notEqual",
    "greaterThanOrEqual",
    "greaterThan",
    "between",
    "notBetween",
    "containsText",
    "notContains",
    "beginsWith",
    "endsWith",
]
_RuleTimePeriod: TypeAlias = Literal[
    "today", "yesterday", "tomorrow", "last7Days", "thisMonth", "lastMonth", "nextMonth", "thisWeek", "lastWeek", "nextWeek"
]
_FormatObjectType: TypeAlias = Literal["num", "percent", "max", "min", "formula", "percentile"]
_RuleType: TypeAlias = Literal[
    "expression",
    "cellIs",
    "colorScale",
    "dataBar",
    "iconSet",
    "top10",
    "uniqueValues",
    "duplicateValues",
    "containsText",
    "notContainsText",
    "beginsWith",
    "endsWith",
    "containsBlanks",
    "notContainsBlanks",
    "containsErrors",
    "notContainsErrors",
    "timePeriod",
    "aboveAverage",
]

class ValueDescriptor(Float):
    expected_type: Incomplete
    def __set__(self, instance: Serialisable, value) -> None: ...

class FormatObject(Serialisable):
    tagname: str
    type: Set[_FormatObjectType]
    val: Incomplete
    gte: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, type: _FormatObjectType, val: Incomplete | None = None, gte: Incomplete | None = None, extLst: Unused = None
    ) -> None: ...

class RuleType(Serialisable):
    cfvo: Incomplete

class IconSet(RuleType):
    tagname: str
    iconSet: NoneSet[_IconSetIconSet]
    showValue: Incomplete
    percent: Incomplete
    reverse: Incomplete
    __elements__: Incomplete
    cfvo: Incomplete
    def __init__(
        self,
        iconSet: _IconSetIconSet | Literal["none"] | None = None,
        showValue: Incomplete | None = None,
        percent: Incomplete | None = None,
        reverse: Incomplete | None = None,
        cfvo: Incomplete | None = None,
    ) -> None: ...

class DataBar(RuleType):
    tagname: str
    minLength: Incomplete
    maxLength: Incomplete
    showValue: Incomplete
    color: Incomplete
    __elements__: Incomplete
    cfvo: Incomplete
    def __init__(
        self,
        minLength: Incomplete | None = None,
        maxLength: Incomplete | None = None,
        showValue: Incomplete | None = None,
        cfvo: Incomplete | None = None,
        color: Incomplete | None = None,
    ) -> None: ...

class ColorScale(RuleType):
    tagname: str
    color: Incomplete
    __elements__: Incomplete
    cfvo: Incomplete
    def __init__(self, cfvo: Incomplete | None = None, color: Incomplete | None = None) -> None: ...

class Rule(Serialisable):
    tagname: str
    type: Set[_RuleType]
    dxfId: Incomplete
    priority: Incomplete
    stopIfTrue: Incomplete
    aboveAverage: Incomplete
    percent: Incomplete
    bottom: Incomplete
    operator: NoneSet[_RuleOperator]
    text: Incomplete
    timePeriod: NoneSet[_RuleTimePeriod]
    rank: Incomplete
    stdDev: Incomplete
    equalAverage: Incomplete
    formula: Incomplete
    colorScale: Typed[ColorScale, Literal[True]]
    dataBar: Typed[DataBar, Literal[True]]
    iconSet: Typed[IconSet, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    dxf: Typed[DifferentialStyle, Literal[True]]
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        type: _RuleType,
        dxfId: Incomplete | None = None,
        priority: int = 0,
        stopIfTrue: Incomplete | None = None,
        aboveAverage: Incomplete | None = None,
        percent: Incomplete | None = None,
        bottom: Incomplete | None = None,
        operator: _RuleOperator | Literal["none"] | None = None,
        text: Incomplete | None = None,
        timePeriod: _RuleTimePeriod | Literal["none"] | None = None,
        rank: Incomplete | None = None,
        stdDev: Incomplete | None = None,
        equalAverage: Incomplete | None = None,
        formula=(),
        colorScale: ColorScale | None = None,
        dataBar: DataBar | None = None,
        iconSet: IconSet | None = None,
        extLst: Unused = None,
        dxf: DifferentialStyle | None = None,
    ) -> None: ...

def ColorScaleRule(
    start_type: Incomplete | None = None,
    start_value: Incomplete | None = None,
    start_color: Incomplete | None = None,
    mid_type: Incomplete | None = None,
    mid_value: Incomplete | None = None,
    mid_color: Incomplete | None = None,
    end_type: Incomplete | None = None,
    end_value: Incomplete | None = None,
    end_color: Incomplete | None = None,
): ...
def FormulaRule(
    formula: Incomplete | None = None,
    stopIfTrue: Incomplete | None = None,
    font: Incomplete | None = None,
    border: Incomplete | None = None,
    fill: Incomplete | None = None,
): ...
def CellIsRule(
    operator: Incomplete | None = None,
    formula: Incomplete | None = None,
    stopIfTrue: Incomplete | None = None,
    font: Incomplete | None = None,
    border: Incomplete | None = None,
    fill: Incomplete | None = None,
): ...
def IconSetRule(
    icon_style: Incomplete | None = None,
    type: Incomplete | None = None,
    values: Incomplete | None = None,
    showValue: Incomplete | None = None,
    percent: Incomplete | None = None,
    reverse: Incomplete | None = None,
): ...
def DataBarRule(
    start_type: Incomplete | None = None,
    start_value: Incomplete | None = None,
    end_type: Incomplete | None = None,
    end_value: Incomplete | None = None,
    color: Incomplete | None = None,
    showValue: Incomplete | None = None,
    minLength: Incomplete | None = None,
    maxLength: Incomplete | None = None,
): ...
