from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import MinMax, NoneSet, Set, Typed, _ConvertibleToFloat
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

_SortConditionSortBy: TypeAlias = Literal["value", "cellColor", "fontColor", "icon"]
_IconSet: TypeAlias = Literal[
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
_SortStateSortMethod: TypeAlias = Literal["stroke", "pinYin"]
_CustomFilterOperator: TypeAlias = Literal[
    "equal", "lessThan", "lessThanOrEqual", "notEqual", "greaterThanOrEqual", "greaterThan"
]
_FiltersCalendarType: TypeAlias = Literal[
    "gregorian",
    "gregorianUs",
    "gregorianMeFrench",
    "gregorianArabic",
    "hijri",
    "hebrew",
    "taiwan",
    "japan",
    "thai",
    "korea",
    "saka",
    "gregorianXlitEnglish",
    "gregorianXlitFrench",
]
_DynamicFilterType: TypeAlias = Literal[
    "null",
    "aboveAverage",
    "belowAverage",
    "tomorrow",
    "today",
    "yesterday",
    "nextWeek",
    "thisWeek",
    "lastWeek",
    "nextMonth",
    "thisMonth",
    "lastMonth",
    "nextQuarter",
    "thisQuarter",
    "lastQuarter",
    "nextYear",
    "thisYear",
    "lastYear",
    "yearToDate",
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "M1",
    "M2",
    "M3",
    "M4",
    "M5",
    "M6",
    "M7",
    "M8",
    "M9",
    "M10",
    "M11",
    "M12",
]
_DateGroupItemDateTimeGrouping: TypeAlias = Literal["year", "month", "day", "hour", "minute", "second"]

class SortCondition(Serialisable):
    tagname: str
    descending: Incomplete
    sortBy: NoneSet[_SortConditionSortBy]
    ref: Incomplete
    customList: Incomplete
    dxfId: Incomplete
    iconSet: NoneSet[_IconSet]
    iconId: Incomplete
    def __init__(
        self,
        ref: Incomplete | None = None,
        descending: Incomplete | None = None,
        sortBy: _SortConditionSortBy | Literal["none"] | None = None,
        customList: Incomplete | None = None,
        dxfId: Incomplete | None = None,
        iconSet: _IconSet | Literal["none"] | None = None,
        iconId: Incomplete | None = None,
    ) -> None: ...

class SortState(Serialisable):
    tagname: str
    columnSort: Incomplete
    caseSensitive: Incomplete
    sortMethod: NoneSet[_SortStateSortMethod]
    ref: Incomplete
    sortCondition: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        columnSort: Incomplete | None = None,
        caseSensitive: Incomplete | None = None,
        sortMethod: _SortStateSortMethod | Literal["none"] | None = None,
        ref: Incomplete | None = None,
        sortCondition=(),
        extLst: Unused = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...

class IconFilter(Serialisable):
    tagname: str
    iconSet: Set[_IconSet]
    iconId: Incomplete
    def __init__(self, iconSet: _IconSet, iconId: Incomplete | None = None) -> None: ...

class ColorFilter(Serialisable):
    tagname: str
    dxfId: Incomplete
    cellColor: Incomplete
    def __init__(self, dxfId: Incomplete | None = None, cellColor: Incomplete | None = None) -> None: ...

class DynamicFilter(Serialisable):
    tagname: str
    type: Set[_DynamicFilterType]
    val: Incomplete
    valIso: Incomplete
    maxVal: Incomplete
    maxValIso: Incomplete
    def __init__(
        self,
        type: _DynamicFilterType,
        val: Incomplete | None = None,
        valIso: Incomplete | None = None,
        maxVal: Incomplete | None = None,
        maxValIso: Incomplete | None = None,
    ) -> None: ...

class CustomFilter(Serialisable):
    tagname: str
    operator: NoneSet[_CustomFilterOperator]
    val: Incomplete
    def __init__(
        self, operator: _CustomFilterOperator | Literal["none"] | None = None, val: Incomplete | None = None
    ) -> None: ...

class CustomFilters(Serialisable):
    tagname: str
    customFilter: Incomplete
    __elements__: Incomplete
    def __init__(self, _and: Incomplete | None = False, customFilter=()) -> None: ...

class Top10(Serialisable):
    tagname: str
    top: Incomplete
    percent: Incomplete
    val: Incomplete
    filterVal: Incomplete
    def __init__(
        self,
        top: Incomplete | None = None,
        percent: Incomplete | None = None,
        val: Incomplete | None = None,
        filterVal: Incomplete | None = None,
    ) -> None: ...

class DateGroupItem(Serialisable):
    tagname: str
    year: Incomplete
    month: MinMax[float, Literal[True]]
    day: MinMax[float, Literal[True]]
    hour: MinMax[float, Literal[True]]
    minute: MinMax[float, Literal[True]]
    second: Incomplete
    dateTimeGrouping: Set[_DateGroupItemDateTimeGrouping]
    def __init__(
        self,
        year: Incomplete | None,
        month: _ConvertibleToFloat | None,
        day: _ConvertibleToFloat | None,
        hour: _ConvertibleToFloat | None,
        minute: _ConvertibleToFloat | None,
        second: Incomplete | None,
        dateTimeGrouping: _DateGroupItemDateTimeGrouping,
    ) -> None: ...

class Filters(Serialisable):
    tagname: str
    blank: Incomplete
    calendarType: NoneSet[_FiltersCalendarType]
    filter: Incomplete
    dateGroupItem: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        blank: Incomplete | None = None,
        calendarType: _FiltersCalendarType | Literal["none"] | None = None,
        filter=(),
        dateGroupItem=(),
    ) -> None: ...

class FilterColumn(Serialisable):
    tagname: str
    colId: Incomplete
    col_id: Incomplete
    hiddenButton: Incomplete
    showButton: Incomplete
    filters: Typed[Filters, Literal[True]]
    top10: Typed[Top10, Literal[True]]
    customFilters: Typed[CustomFilters, Literal[True]]
    dynamicFilter: Typed[DynamicFilter, Literal[True]]
    colorFilter: Typed[ColorFilter, Literal[True]]
    iconFilter: Typed[IconFilter, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        colId: Incomplete | None = None,
        hiddenButton: Incomplete | None = False,
        showButton: Incomplete | None = True,
        filters: Filters | None = None,
        top10: Top10 | None = None,
        customFilters: CustomFilters | None = None,
        dynamicFilter: DynamicFilter | None = None,
        colorFilter: ColorFilter | None = None,
        iconFilter: IconFilter | None = None,
        extLst: Unused = None,
        blank: Incomplete | None = None,
        vals: Incomplete | None = None,
    ) -> None: ...

class AutoFilter(Serialisable):
    tagname: str
    ref: Incomplete
    filterColumn: Incomplete
    sortState: Typed[SortState, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, ref: Incomplete | None = None, filterColumn=(), sortState: SortState | None = None, extLst: Unused = None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def add_filter_column(self, col_id, vals, blank: bool = False) -> None: ...
    def add_sort_condition(self, ref, descending: bool = False) -> None: ...
