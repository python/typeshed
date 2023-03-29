from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

class SortCondition(Serialisable):
    tagname: str
    descending: Incomplete
    sortBy: Incomplete
    ref: Incomplete
    customList: Incomplete
    dxfId: Incomplete
    iconSet: Incomplete
    iconId: Incomplete
    def __init__(
        self,
        ref: Incomplete | None = None,
        descending: Incomplete | None = None,
        sortBy: Incomplete | None = None,
        customList: Incomplete | None = None,
        dxfId: Incomplete | None = None,
        iconSet: Incomplete | None = None,
        iconId: Incomplete | None = None,
    ) -> None: ...

class SortState(Serialisable):
    tagname: str
    columnSort: Incomplete
    caseSensitive: Incomplete
    sortMethod: Incomplete
    ref: Incomplete
    sortCondition: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        columnSort: Incomplete | None = None,
        caseSensitive: Incomplete | None = None,
        sortMethod: Incomplete | None = None,
        ref: Incomplete | None = None,
        sortCondition=(),
        extLst: Unused = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...

class IconFilter(Serialisable):
    tagname: str
    iconSet: Incomplete
    iconId: Incomplete
    def __init__(self, iconSet: Incomplete | None = None, iconId: Incomplete | None = None) -> None: ...

class ColorFilter(Serialisable):
    tagname: str
    dxfId: Incomplete
    cellColor: Incomplete
    def __init__(self, dxfId: Incomplete | None = None, cellColor: Incomplete | None = None) -> None: ...

class DynamicFilter(Serialisable):
    tagname: str
    type: Incomplete
    val: Incomplete
    valIso: Incomplete
    maxVal: Incomplete
    maxValIso: Incomplete
    def __init__(
        self,
        type: Incomplete | None = None,
        val: Incomplete | None = None,
        valIso: Incomplete | None = None,
        maxVal: Incomplete | None = None,
        maxValIso: Incomplete | None = None,
    ) -> None: ...

class CustomFilter(Serialisable):
    tagname: str
    operator: Incomplete
    val: Incomplete
    def __init__(self, operator: Incomplete | None = None, val: Incomplete | None = None) -> None: ...

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
    month: Incomplete
    day: Incomplete
    hour: Incomplete
    minute: Incomplete
    second: Incomplete
    dateTimeGrouping: Incomplete
    def __init__(
        self,
        year: Incomplete | None = None,
        month: Incomplete | None = None,
        day: Incomplete | None = None,
        hour: Incomplete | None = None,
        minute: Incomplete | None = None,
        second: Incomplete | None = None,
        dateTimeGrouping: Incomplete | None = None,
    ) -> None: ...

class Filters(Serialisable):
    tagname: str
    blank: Incomplete
    calendarType: Incomplete
    filter: Incomplete
    dateGroupItem: Incomplete
    __elements__: Incomplete
    def __init__(
        self, blank: Incomplete | None = None, calendarType: Incomplete | None = None, filter=(), dateGroupItem=()
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
