from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, NoneSet, Set, String, Typed, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.filters import AutoFilter

_PivotAreaType: TypeAlias = Literal["normal", "data", "all", "origin", "button", "topEnd", "topRight"]
_PivotAxis: TypeAlias = Literal["axisRow", "axisCol", "axisPage", "axisValues"]
_ConditionalFormatType: TypeAlias = Literal["all", "row", "column"]
_FormatAction: TypeAlias = Literal["blank", "formatting", "drill", "formula"]
_PivotFilterType: TypeAlias = Literal[
    "unknown",
    "count",
    "percent",
    "sum",
    "captionEqual",
    "captionNotEqual",
    "captionBeginsWith",
    "captionNotBeginsWith",
    "captionEndsWith",
    "captionNotEndsWith",
    "captionContains",
    "captionNotContains",
    "captionGreaterThan",
    "captionGreaterThanOrEqual",
    "captionLessThan",
    "captionLessThanOrEqual",
    "captionBetween",
    "captionNotBetween",
    "valueEqual",
    "valueNotEqual",
    "valueGreaterThan",
    "valueGreaterThanOrEqual",
    "valueLessThan",
    "valueLessThanOrEqual",
    "valueBetween",
    "valueNotBetween",
    "dateEqual",
    "dateNotEqual",
    "dateOlderThan",
    "dateOlderThanOrEqual",
    "dateNewerThan",
    "dateNewerThanOrEqual",
    "dateBetween",
    "dateNotBetween",
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
_ConditionalFormatScope: TypeAlias = Literal["selection", "data", "field"]
_DataFieldSubtotal: TypeAlias = Literal[
    "average", "count", "countNums", "max", "min", "product", "stdDev", "stdDevp", "sum", "var", "varp"
]
_DataFieldShowDataAs: TypeAlias = Literal[
    "normal", "difference", "percent", "percentDiff", "runTotal", "percentOfRow", "percentOfCol", "percentOfTotal", "index"
]
_ItemType: TypeAlias = Literal[
    "data",
    "default",
    "sum",
    "countA",
    "avg",
    "max",
    "min",
    "product",
    "count",
    "stdDev",
    "stdDevP",
    "var",
    "varP",
    "grand",
    "blank",
]
_PivotFieldSortType: TypeAlias = Literal["manual", "ascending", "descending"]

class HierarchyUsage(Serialisable):
    tagname: str
    hierarchyUsage: Incomplete
    def __init__(self, hierarchyUsage: Incomplete | None = None) -> None: ...

class ColHierarchiesUsage(Serialisable):
    tagname: str
    colHierarchyUsage: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, colHierarchyUsage=()) -> None: ...
    @property
    def count(self): ...

class RowHierarchiesUsage(Serialisable):
    tagname: str
    rowHierarchyUsage: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, rowHierarchyUsage=()) -> None: ...
    @property
    def count(self): ...

class PivotFilter(Serialisable):
    tagname: str
    fld: Incomplete
    mpFld: Incomplete
    type: Set[_PivotFilterType]
    evalOrder: Incomplete
    id: Incomplete
    iMeasureHier: Incomplete
    iMeasureFld: Incomplete
    name: String[Literal[True]]
    description: String[Literal[True]]
    stringValue1: String[Literal[True]]
    stringValue2: String[Literal[True]]
    autoFilter: Typed[AutoFilter, Literal[False]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        fld: Incomplete | None,
        mpFld: Incomplete | None,
        type: _PivotFilterType,
        evalOrder: Incomplete | None,
        id: Incomplete | None,
        iMeasureHier: Incomplete | None,
        iMeasureFld: Incomplete | None,
        name: str | None,
        description: str | None,
        stringValue1: str | None,
        stringValue2: str | None,
        autoFilter: AutoFilter,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class PivotFilters(Serialisable):
    count: Incomplete
    filter: Typed[PivotFilter, Literal[True]]
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, filter: PivotFilter | None = None) -> None: ...

class PivotTableStyle(Serialisable):
    tagname: str
    name: String[Literal[True]]
    showRowHeaders: Bool[Literal[False]]
    showColHeaders: Bool[Literal[False]]
    showRowStripes: Bool[Literal[False]]
    showColStripes: Bool[Literal[False]]
    showLastColumn: Bool[Literal[False]]
    def __init__(
        self,
        name: str | None,
        showRowHeaders: _ConvertibleToBool,
        showColHeaders: _ConvertibleToBool,
        showRowStripes: _ConvertibleToBool,
        showColStripes: _ConvertibleToBool,
        showLastColumn: _ConvertibleToBool,
    ) -> None: ...

class MemberList(Serialisable):
    tagname: str
    level: Incomplete
    member: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, level: Incomplete | None = None, member=()) -> None: ...
    @property
    def count(self): ...

class MemberProperty(Serialisable):
    tagname: str
    name: String[Literal[True]]
    showCell: Bool[Literal[True]]
    showTip: Bool[Literal[True]]
    showAsCaption: Bool[Literal[True]]
    nameLen: Incomplete
    pPos: Incomplete
    pLen: Incomplete
    level: Incomplete
    field: Incomplete
    def __init__(
        self,
        name: str | None = None,
        showCell: _ConvertibleToBool | None = None,
        showTip: _ConvertibleToBool | None = None,
        showAsCaption: _ConvertibleToBool | None = None,
        nameLen: Incomplete | None = None,
        pPos: Incomplete | None = None,
        pLen: Incomplete | None = None,
        level: Incomplete | None = None,
        field: Incomplete | None = None,
    ) -> None: ...

class PivotHierarchy(Serialisable):
    tagname: str
    outline: Bool[Literal[False]]
    multipleItemSelectionAllowed: Bool[Literal[False]]
    subtotalTop: Bool[Literal[False]]
    showInFieldList: Bool[Literal[False]]
    dragToRow: Bool[Literal[False]]
    dragToCol: Bool[Literal[False]]
    dragToPage: Bool[Literal[False]]
    dragToData: Bool[Literal[False]]
    dragOff: Bool[Literal[False]]
    includeNewItemsInFilter: Bool[Literal[False]]
    caption: String[Literal[True]]
    mps: Incomplete
    members: Typed[MemberList, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        outline: _ConvertibleToBool,
        multipleItemSelectionAllowed: _ConvertibleToBool,
        subtotalTop: _ConvertibleToBool,
        showInFieldList: _ConvertibleToBool,
        dragToRow: _ConvertibleToBool,
        dragToCol: _ConvertibleToBool,
        dragToPage: _ConvertibleToBool,
        dragToData: _ConvertibleToBool,
        dragOff: _ConvertibleToBool,
        includeNewItemsInFilter: _ConvertibleToBool,
        caption: str | None = None,
        mps=(),
        members: MemberList | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class Reference(Serialisable):
    tagname: str
    field: Incomplete
    selected: Bool[Literal[True]]
    byPosition: Bool[Literal[True]]
    relative: Bool[Literal[True]]
    defaultSubtotal: Bool[Literal[True]]
    sumSubtotal: Bool[Literal[True]]
    countASubtotal: Bool[Literal[True]]
    avgSubtotal: Bool[Literal[True]]
    maxSubtotal: Bool[Literal[True]]
    minSubtotal: Bool[Literal[True]]
    productSubtotal: Bool[Literal[True]]
    countSubtotal: Bool[Literal[True]]
    stdDevSubtotal: Bool[Literal[True]]
    stdDevPSubtotal: Bool[Literal[True]]
    varSubtotal: Bool[Literal[True]]
    varPSubtotal: Bool[Literal[True]]
    x: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        field: Incomplete | None = None,
        count: Unused = None,
        selected: _ConvertibleToBool | None = None,
        byPosition: _ConvertibleToBool | None = None,
        relative: _ConvertibleToBool | None = None,
        defaultSubtotal: _ConvertibleToBool | None = None,
        sumSubtotal: _ConvertibleToBool | None = None,
        countASubtotal: _ConvertibleToBool | None = None,
        avgSubtotal: _ConvertibleToBool | None = None,
        maxSubtotal: _ConvertibleToBool | None = None,
        minSubtotal: _ConvertibleToBool | None = None,
        productSubtotal: _ConvertibleToBool | None = None,
        countSubtotal: _ConvertibleToBool | None = None,
        stdDevSubtotal: _ConvertibleToBool | None = None,
        stdDevPSubtotal: _ConvertibleToBool | None = None,
        varSubtotal: _ConvertibleToBool | None = None,
        varPSubtotal: _ConvertibleToBool | None = None,
        x: Incomplete | None = (),
        extLst: ExtensionList | None = None,
    ) -> None: ...
    @property
    def count(self): ...

class PivotArea(Serialisable):
    tagname: str
    references: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    field: Incomplete
    type: NoneSet[_PivotAreaType]
    dataOnly: Bool[Literal[True]]
    labelOnly: Bool[Literal[True]]
    grandRow: Bool[Literal[True]]
    grandCol: Bool[Literal[True]]
    cacheIndex: Bool[Literal[True]]
    outline: Bool[Literal[True]]
    offset: String[Literal[True]]
    collapsedLevelsAreSubtotals: Bool[Literal[True]]
    axis: NoneSet[_PivotAxis]
    fieldPosition: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        references=(),
        extLst: ExtensionList | None = None,
        field: Incomplete | None = None,
        type: _PivotAreaType | Literal["none"] | None = "normal",
        dataOnly: _ConvertibleToBool | None = True,
        labelOnly: _ConvertibleToBool | None = None,
        grandRow: _ConvertibleToBool | None = None,
        grandCol: _ConvertibleToBool | None = None,
        cacheIndex: _ConvertibleToBool | None = None,
        outline: _ConvertibleToBool | None = True,
        offset: str | None = None,
        collapsedLevelsAreSubtotals: _ConvertibleToBool | None = None,
        axis: _PivotAxis | Literal["none"] | None = None,
        fieldPosition: Incomplete | None = None,
    ) -> None: ...

class ChartFormat(Serialisable):
    tagname: str
    chart: Incomplete
    format: Incomplete
    series: Bool[Literal[False]]
    pivotArea: Typed[PivotArea, Literal[False]]
    __elements__: Incomplete
    def __init__(
        self, chart: Incomplete | None, format: Incomplete | None, series: _ConvertibleToBool, pivotArea: PivotArea
    ) -> None: ...

class ConditionalFormat(Serialisable):
    tagname: str
    scope: Set[_ConditionalFormatScope]
    type: NoneSet[_ConditionalFormatType]
    priority: Incomplete
    pivotAreas: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        scope: _ConditionalFormatScope = "selection",
        type: _ConditionalFormatType | Literal["none"] | None = None,
        priority: Incomplete | None = None,
        pivotAreas=(),
        extLst: ExtensionList | None = None,
    ) -> None: ...

class ConditionalFormatList(Serialisable):
    tagname: str
    conditionalFormat: Incomplete
    __attrs__: Incomplete
    def __init__(self, conditionalFormat=..., count: Incomplete | None = ...) -> None: ...
    def by_priority(self): ...
    @property
    def count(self): ...
    def to_tree(self, tagname: Incomplete | None = ...): ...  # type: ignore[override]

class Format(Serialisable):
    tagname: str
    action: NoneSet[_FormatAction]
    dxfId: Incomplete
    pivotArea: Typed[PivotArea, Literal[False]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        action: _FormatAction | Literal["none"] | None,
        dxfId: Incomplete | None,
        pivotArea: PivotArea,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class DataField(Serialisable):
    tagname: str
    name: String[Literal[True]]
    fld: Incomplete
    subtotal: Set[_DataFieldSubtotal]
    showDataAs: Set[_DataFieldShowDataAs]
    baseField: Incomplete
    baseItem: Incomplete
    numFmtId: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        name: str | None = None,
        fld: Incomplete | None = None,
        subtotal: str = "sum",
        showDataAs: str = "normal",
        baseField: int = -1,
        baseItem: int = 1048832,
        numFmtId: Incomplete | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class PageField(Serialisable):
    tagname: str
    fld: Incomplete
    item: Incomplete
    hier: Incomplete
    name: String[Literal[True]]
    cap: String[Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        fld: Incomplete | None = None,
        item: Incomplete | None = None,
        hier: Incomplete | None = None,
        name: str | None = None,
        cap: str | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class RowColItem(Serialisable):
    tagname: str
    t: Set[_ItemType]
    r: Incomplete
    i: Incomplete
    x: Incomplete
    __elements__: Incomplete
    def __init__(self, t: _ItemType = "data", r: int = 0, i: int = 0, x=()) -> None: ...

class RowColField(Serialisable):
    tagname: str
    x: Incomplete
    def __init__(self, x: Incomplete | None = None) -> None: ...

class AutoSortScope(Serialisable):
    pivotArea: Typed[PivotArea, Literal[False]]
    __elements__: Incomplete
    def __init__(self, pivotArea: PivotArea) -> None: ...

class FieldItem(Serialisable):
    tagname: str
    n: String[Literal[True]]
    t: Set[_ItemType]
    h: Bool[Literal[True]]
    s: Bool[Literal[True]]
    sd: Bool[Literal[True]]
    f: Bool[Literal[True]]
    m: Bool[Literal[True]]
    c: Bool[Literal[True]]
    x: Incomplete
    d: Bool[Literal[True]]
    e: Bool[Literal[True]]
    def __init__(
        self,
        n: str | None = None,
        t: _ItemType = "data",
        h: _ConvertibleToBool | None = None,
        s: _ConvertibleToBool | None = None,
        sd: _ConvertibleToBool | None = True,
        f: _ConvertibleToBool | None = None,
        m: _ConvertibleToBool | None = None,
        c: _ConvertibleToBool | None = None,
        x: Incomplete | None = None,
        d: _ConvertibleToBool | None = None,
        e: _ConvertibleToBool | None = None,
    ) -> None: ...

class PivotField(Serialisable):
    tagname: str
    items: Incomplete
    autoSortScope: Typed[AutoSortScope, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    name: String[Literal[True]]
    axis: NoneSet[_PivotAxis]
    dataField: Bool[Literal[True]]
    subtotalCaption: String[Literal[True]]
    showDropDowns: Bool[Literal[True]]
    hiddenLevel: Bool[Literal[True]]
    uniqueMemberProperty: String[Literal[True]]
    compact: Bool[Literal[True]]
    allDrilled: Bool[Literal[True]]
    numFmtId: Incomplete
    outline: Bool[Literal[True]]
    subtotalTop: Bool[Literal[True]]
    dragToRow: Bool[Literal[True]]
    dragToCol: Bool[Literal[True]]
    multipleItemSelectionAllowed: Bool[Literal[True]]
    dragToPage: Bool[Literal[True]]
    dragToData: Bool[Literal[True]]
    dragOff: Bool[Literal[True]]
    showAll: Bool[Literal[True]]
    insertBlankRow: Bool[Literal[True]]
    serverField: Bool[Literal[True]]
    insertPageBreak: Bool[Literal[True]]
    autoShow: Bool[Literal[True]]
    topAutoShow: Bool[Literal[True]]
    hideNewItems: Bool[Literal[True]]
    measureFilter: Bool[Literal[True]]
    includeNewItemsInFilter: Bool[Literal[True]]
    itemPageCount: Incomplete
    sortType: Set[_PivotFieldSortType]
    dataSourceSort: Bool[Literal[True]]
    nonAutoSortDefault: Bool[Literal[True]]
    rankBy: Incomplete
    defaultSubtotal: Bool[Literal[True]]
    sumSubtotal: Bool[Literal[True]]
    countASubtotal: Bool[Literal[True]]
    avgSubtotal: Bool[Literal[True]]
    maxSubtotal: Bool[Literal[True]]
    minSubtotal: Bool[Literal[True]]
    productSubtotal: Bool[Literal[True]]
    countSubtotal: Bool[Literal[True]]
    stdDevSubtotal: Bool[Literal[True]]
    stdDevPSubtotal: Bool[Literal[True]]
    varSubtotal: Bool[Literal[True]]
    varPSubtotal: Bool[Literal[True]]
    showPropCell: Bool[Literal[True]]
    showPropTip: Bool[Literal[True]]
    showPropAsCaption: Bool[Literal[True]]
    defaultAttributeDrillState: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        items=(),
        autoSortScope: AutoSortScope | None = None,
        name: str | None = None,
        axis: _PivotAxis | Literal["none"] | None = None,
        dataField: _ConvertibleToBool | None = None,
        subtotalCaption: str | None = None,
        showDropDowns: _ConvertibleToBool | None = True,
        hiddenLevel: _ConvertibleToBool | None = None,
        uniqueMemberProperty: str | None = None,
        compact: _ConvertibleToBool | None = True,
        allDrilled: _ConvertibleToBool | None = None,
        numFmtId: Incomplete | None = None,
        outline: _ConvertibleToBool | None = True,
        subtotalTop: _ConvertibleToBool | None = True,
        dragToRow: _ConvertibleToBool | None = True,
        dragToCol: _ConvertibleToBool | None = True,
        multipleItemSelectionAllowed: _ConvertibleToBool | None = None,
        dragToPage: _ConvertibleToBool | None = True,
        dragToData: _ConvertibleToBool | None = True,
        dragOff: _ConvertibleToBool | None = True,
        showAll: _ConvertibleToBool | None = True,
        insertBlankRow: _ConvertibleToBool | None = None,
        serverField: _ConvertibleToBool | None = None,
        insertPageBreak: _ConvertibleToBool | None = None,
        autoShow: _ConvertibleToBool | None = None,
        topAutoShow: _ConvertibleToBool | None = True,
        hideNewItems: _ConvertibleToBool | None = None,
        measureFilter: _ConvertibleToBool | None = None,
        includeNewItemsInFilter: _ConvertibleToBool | None = None,
        itemPageCount: int = 10,
        sortType: _PivotFieldSortType = "manual",
        dataSourceSort: _ConvertibleToBool | None = None,
        nonAutoSortDefault: _ConvertibleToBool | None = None,
        rankBy: Incomplete | None = None,
        defaultSubtotal: _ConvertibleToBool | None = True,
        sumSubtotal: _ConvertibleToBool | None = None,
        countASubtotal: _ConvertibleToBool | None = None,
        avgSubtotal: _ConvertibleToBool | None = None,
        maxSubtotal: _ConvertibleToBool | None = None,
        minSubtotal: _ConvertibleToBool | None = None,
        productSubtotal: _ConvertibleToBool | None = None,
        countSubtotal: _ConvertibleToBool | None = None,
        stdDevSubtotal: _ConvertibleToBool | None = None,
        stdDevPSubtotal: _ConvertibleToBool | None = None,
        varSubtotal: _ConvertibleToBool | None = None,
        varPSubtotal: _ConvertibleToBool | None = None,
        showPropCell: _ConvertibleToBool | None = None,
        showPropTip: _ConvertibleToBool | None = None,
        showPropAsCaption: _ConvertibleToBool | None = None,
        defaultAttributeDrillState: _ConvertibleToBool | None = None,
        extLst: Unused = None,
    ) -> None: ...

class Location(Serialisable):
    tagname: str
    ref: String[Literal[False]]
    firstHeaderRow: Incomplete
    firstDataRow: Incomplete
    firstDataCol: Incomplete
    rowPageCount: Incomplete
    colPageCount: Incomplete
    def __init__(
        self,
        ref: str,
        firstHeaderRow: Incomplete | None = None,
        firstDataRow: Incomplete | None = None,
        firstDataCol: Incomplete | None = None,
        rowPageCount: Incomplete | None = None,
        colPageCount: Incomplete | None = None,
    ) -> None: ...

class TableDefinition(Serialisable):
    mime_type: str
    rel_type: str
    tagname: str
    cache: Incomplete
    name: String[Literal[False]]
    cacheId: Incomplete
    dataOnRows: Bool[Literal[False]]
    dataPosition: Incomplete
    dataCaption: String[Literal[False]]
    grandTotalCaption: String[Literal[True]]
    errorCaption: String[Literal[True]]
    showError: Bool[Literal[False]]
    missingCaption: String[Literal[True]]
    showMissing: Bool[Literal[False]]
    pageStyle: String[Literal[True]]
    pivotTableStyle: String[Literal[True]]
    vacatedStyle: String[Literal[True]]
    tag: String[Literal[True]]
    updatedVersion: Incomplete
    minRefreshableVersion: Incomplete
    asteriskTotals: Bool[Literal[False]]
    showItems: Bool[Literal[False]]
    editData: Bool[Literal[False]]
    disableFieldList: Bool[Literal[False]]
    showCalcMbrs: Bool[Literal[False]]
    visualTotals: Bool[Literal[False]]
    showMultipleLabel: Bool[Literal[False]]
    showDataDropDown: Bool[Literal[False]]
    showDrill: Bool[Literal[False]]
    printDrill: Bool[Literal[False]]
    showMemberPropertyTips: Bool[Literal[False]]
    showDataTips: Bool[Literal[False]]
    enableWizard: Bool[Literal[False]]
    enableDrill: Bool[Literal[False]]
    enableFieldProperties: Bool[Literal[False]]
    preserveFormatting: Bool[Literal[False]]
    useAutoFormatting: Bool[Literal[False]]
    pageWrap: Incomplete
    pageOverThenDown: Bool[Literal[False]]
    subtotalHiddenItems: Bool[Literal[False]]
    rowGrandTotals: Bool[Literal[False]]
    colGrandTotals: Bool[Literal[False]]
    fieldPrintTitles: Bool[Literal[False]]
    itemPrintTitles: Bool[Literal[False]]
    mergeItem: Bool[Literal[False]]
    showDropZones: Bool[Literal[False]]
    createdVersion: Incomplete
    indent: Incomplete
    showEmptyRow: Bool[Literal[False]]
    showEmptyCol: Bool[Literal[False]]
    showHeaders: Bool[Literal[False]]
    compact: Bool[Literal[False]]
    outline: Bool[Literal[False]]
    outlineData: Bool[Literal[False]]
    compactData: Bool[Literal[False]]
    published: Bool[Literal[False]]
    gridDropZones: Bool[Literal[False]]
    immersive: Bool[Literal[False]]
    multipleFieldFilters: Bool[Literal[False]]
    chartFormat: Incomplete
    rowHeaderCaption: String[Literal[True]]
    colHeaderCaption: String[Literal[True]]
    fieldListSortAscending: Bool[Literal[False]]
    mdxSubqueries: Bool[Literal[False]]
    customListSort: Bool[Literal[True]]
    autoFormatId: Incomplete
    applyNumberFormats: Bool[Literal[False]]
    applyBorderFormats: Bool[Literal[False]]
    applyFontFormats: Bool[Literal[False]]
    applyPatternFormats: Bool[Literal[False]]
    applyAlignmentFormats: Bool[Literal[False]]
    applyWidthHeightFormats: Bool[Literal[False]]
    location: Typed[Location, Literal[False]]
    pivotFields: Incomplete
    rowFields: Incomplete
    rowItems: Incomplete
    colFields: Incomplete
    colItems: Incomplete
    pageFields: Incomplete
    dataFields: Incomplete
    formats: Incomplete
    conditionalFormats: Typed[ConditionalFormatList, Literal[True]]
    chartFormats: Incomplete
    pivotHierarchies: Incomplete
    pivotTableStyleInfo: Typed[PivotTableStyle, Literal[True]]
    filters: Incomplete
    rowHierarchiesUsage: Typed[RowHierarchiesUsage, Literal[True]]
    colHierarchiesUsage: Typed[ColHierarchiesUsage, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        name: str,
        cacheId: Incomplete | None,
        dataOnRows: _ConvertibleToBool,
        dataPosition: Incomplete | None,
        dataCaption: str,
        grandTotalCaption: str | None,
        errorCaption: str | None,
        showError: _ConvertibleToBool,
        missingCaption: str | None,
        showMissing: _ConvertibleToBool,
        pageStyle: str | None,
        pivotTableStyle: str | None,
        vacatedStyle: str | None,
        tag: str | None,
        updatedVersion: int,
        minRefreshableVersion: int,
        asteriskTotals: _ConvertibleToBool,
        showItems: _ConvertibleToBool,
        editData: _ConvertibleToBool,
        disableFieldList: _ConvertibleToBool,
        showCalcMbrs: _ConvertibleToBool,
        visualTotals: _ConvertibleToBool,
        showMultipleLabel: _ConvertibleToBool,
        showDataDropDown: _ConvertibleToBool,
        showDrill: _ConvertibleToBool,
        printDrill: _ConvertibleToBool,
        showMemberPropertyTips: _ConvertibleToBool,
        showDataTips: _ConvertibleToBool,
        enableWizard: _ConvertibleToBool,
        enableDrill: _ConvertibleToBool,
        enableFieldProperties: _ConvertibleToBool,
        preserveFormatting: _ConvertibleToBool,
        useAutoFormatting: _ConvertibleToBool,
        pageWrap: int,
        pageOverThenDown: _ConvertibleToBool,
        subtotalHiddenItems: _ConvertibleToBool,
        rowGrandTotals: _ConvertibleToBool,
        colGrandTotals: _ConvertibleToBool,
        fieldPrintTitles: _ConvertibleToBool,
        itemPrintTitles: _ConvertibleToBool,
        mergeItem: _ConvertibleToBool,
        showDropZones: _ConvertibleToBool,
        createdVersion: int,
        indent: int,
        showEmptyRow: _ConvertibleToBool,
        showEmptyCol: _ConvertibleToBool,
        showHeaders: _ConvertibleToBool,
        compact: _ConvertibleToBool,
        outline: _ConvertibleToBool,
        outlineData: _ConvertibleToBool,
        compactData: _ConvertibleToBool,
        published: _ConvertibleToBool,
        gridDropZones: _ConvertibleToBool,
        immersive: _ConvertibleToBool,
        multipleFieldFilters: _ConvertibleToBool,
        chartFormat: int,
        rowHeaderCaption: str | None,
        colHeaderCaption: str | None,
        fieldListSortAscending: _ConvertibleToBool,
        mdxSubqueries: _ConvertibleToBool,
        customListSort: _ConvertibleToBool | None,
        autoFormatId: Incomplete | None,
        applyNumberFormats: _ConvertibleToBool,
        applyBorderFormats: _ConvertibleToBool,
        applyFontFormats: _ConvertibleToBool,
        applyPatternFormats: _ConvertibleToBool,
        applyAlignmentFormats: _ConvertibleToBool,
        applyWidthHeightFormats: _ConvertibleToBool,
        location: Location | None,
        pivotFields=(),
        rowFields=(),
        rowItems=(),
        colFields=(),
        colItems=(),
        pageFields=(),
        dataFields=(),
        formats=(),
        conditionalFormats: ConditionalFormatList | None = None,
        chartFormats=(),
        pivotHierarchies=(),
        pivotTableStyleInfo: PivotTableStyle | None = None,
        filters=(),
        rowHierarchiesUsage: RowHierarchiesUsage | None = None,
        colHierarchiesUsage: ColHierarchiesUsage | None = None,
        extLst: ExtensionList | None = None,
        id: Incomplete | None = None,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...
