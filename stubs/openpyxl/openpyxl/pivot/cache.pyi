from _typeshed import Incomplete
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, DateTime, Set, String, Typed, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.pivot.fields import Error, Missing, Number, Text, TupleList
from openpyxl.pivot.table import PivotArea

_RangePrGroupBy: TypeAlias = Literal["range", "seconds", "minutes", "hours", "days", "months", "quarters", "years"]
_CacheSourceType: TypeAlias = Literal["worksheet", "external", "consolidation", "scenario"]

class MeasureDimensionMap(Serialisable):
    tagname: str
    measureGroup: Incomplete
    dimension: Incomplete
    def __init__(self, measureGroup: Incomplete | None = None, dimension: Incomplete | None = None) -> None: ...

class MeasureGroup(Serialisable):
    tagname: str
    name: String[Literal[False]]
    caption: String[Literal[False]]
    def __init__(self, name: str, caption: str) -> None: ...

class PivotDimension(Serialisable):
    tagname: str
    measure: Bool[Literal[False]]
    name: String[Literal[False]]
    uniqueName: String[Literal[False]]
    caption: String[Literal[False]]
    def __init__(self, measure: _ConvertibleToBool, name: str, uniqueName: str, caption: str) -> None: ...

class CalculatedMember(Serialisable):
    tagname: str
    name: String[Literal[False]]
    mdx: String[Literal[False]]
    memberName: String[Literal[False]]
    hierarchy: String[Literal[False]]
    parent: String[Literal[False]]
    solveOrder: Incomplete
    set: Bool[Literal[False]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        name: str,
        mdx: str,
        memberName: str,
        hierarchy: str,
        parent: str,
        solveOrder: Incomplete | None,
        set: _ConvertibleToBool,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class CalculatedItem(Serialisable):
    tagname: str
    field: Incomplete
    formula: String[Literal[False]]
    pivotArea: Typed[PivotArea, Literal[False]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, field: Incomplete | None, formula: str, pivotArea: PivotArea, extLst: Incomplete | None = None
    ) -> None: ...

class ServerFormat(Serialisable):
    tagname: str
    culture: String[Literal[True]]
    format: String[Literal[True]]
    def __init__(self, culture: str | None = None, format: str | None = None) -> None: ...

class ServerFormatList(Serialisable):
    tagname: str
    serverFormat: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, serverFormat: Incomplete | None = None) -> None: ...
    @property
    def count(self): ...

class Query(Serialisable):
    tagname: str
    mdx: String[Literal[False]]
    tpls: Typed[TupleList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, mdx: str, tpls: TupleList | None = None) -> None: ...

class QueryCache(Serialisable):
    tagname: str
    count: Incomplete
    query: Typed[Query, Literal[False]]
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None, query: Query) -> None: ...

class OLAPSet(Serialisable):
    tagname: str
    count: Incomplete
    maxRank: Incomplete
    setDefinition: String[Literal[False]]
    sortType: Incomplete
    queryFailed: Bool[Literal[False]]
    tpls: Typed[TupleList, Literal[True]]
    sortByTuple: Typed[TupleList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        count: Incomplete | None,
        maxRank: Incomplete | None,
        setDefinition: str,
        sortType: Incomplete | None,
        queryFailed: _ConvertibleToBool,
        tpls: TupleList | None = None,
        sortByTuple: TupleList | None = None,
    ) -> None: ...

class OLAPSets(Serialisable):
    count: Incomplete
    set: Typed[OLAPSet, Literal[False]]
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None, set: OLAPSet) -> None: ...

class PCDSDTCEntries(Serialisable):
    tagname: str
    count: Incomplete
    m: Typed[Missing, Literal[False]]
    n: Typed[Number, Literal[False]]
    e: Typed[Error, Literal[False]]
    s: Typed[Text, Literal[False]]
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None, m: Missing, n: Number, e: Error, s: Text) -> None: ...

class TupleCache(Serialisable):
    tagname: str
    entries: Typed[PCDSDTCEntries, Literal[True]]
    sets: Typed[OLAPSets, Literal[True]]
    queryCache: Typed[QueryCache, Literal[True]]
    serverFormats: Typed[ServerFormatList, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        entries: PCDSDTCEntries | None = None,
        sets: OLAPSets | None = None,
        queryCache: QueryCache | None = None,
        serverFormats: ServerFormatList | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class PCDKPI(Serialisable):
    tagname: str
    uniqueName: String[Literal[False]]
    caption: String[Literal[True]]
    displayFolder: String[Literal[False]]
    measureGroup: String[Literal[False]]
    parent: String[Literal[False]]
    value: String[Literal[False]]
    goal: String[Literal[False]]
    status: String[Literal[False]]
    trend: String[Literal[False]]
    weight: String[Literal[False]]
    time: String[Literal[False]]
    def __init__(
        self,
        uniqueName: str,
        caption: str | None,
        displayFolder: str,
        measureGroup: str,
        parent: str,
        value: str,
        goal: str,
        status: str,
        trend: str,
        weight: str,
        time: str,
    ) -> None: ...

class GroupMember(Serialisable):
    tagname: str
    uniqueName: String[Literal[False]]
    group: Bool[Literal[False]]
    def __init__(self, uniqueName: str, group: _ConvertibleToBool) -> None: ...

class GroupMembers(Serialisable):
    count: Incomplete
    groupMember: Typed[GroupMember, Literal[False]]
    __elements__: Incomplete
    def __init__(self, count: GroupMember, groupMember: Incomplete | None = None) -> None: ...

class LevelGroup(Serialisable):
    tagname: str
    name: String[Literal[False]]
    uniqueName: String[Literal[False]]
    caption: String[Literal[False]]
    uniqueParent: String[Literal[False]]
    id: Incomplete
    groupMembers: Typed[GroupMembers, Literal[False]]
    __elements__: Incomplete
    def __init__(
        self, name: str, uniqueName: str, caption: str, uniqueParent: str, id: Incomplete | None, groupMembers: GroupMembers
    ) -> None: ...

class Groups(Serialisable):
    tagname: str
    count: Incomplete
    group: Typed[LevelGroup, Literal[False]]
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None, group: LevelGroup) -> None: ...

class GroupLevel(Serialisable):
    tagname: str
    uniqueName: String[Literal[False]]
    caption: String[Literal[False]]
    user: Bool[Literal[False]]
    customRollUp: Bool[Literal[False]]
    groups: Typed[Groups, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        uniqueName: str,
        caption: str,
        user: _ConvertibleToBool,
        customRollUp: _ConvertibleToBool,
        groups: Groups | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class GroupLevels(Serialisable):
    count: Incomplete
    groupLevel: Typed[GroupLevel, Literal[False]]
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None, groupLevel: GroupLevel) -> None: ...

class FieldUsage(Serialisable):
    tagname: str
    x: Incomplete
    def __init__(self, x: Incomplete | None = None) -> None: ...

class FieldsUsage(Serialisable):
    count: Incomplete
    fieldUsage: Typed[FieldUsage, Literal[True]]
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, fieldUsage: FieldUsage | None = None) -> None: ...

class CacheHierarchy(Serialisable):
    tagname: str
    uniqueName: String[Literal[False]]
    caption: String[Literal[True]]
    measure: Bool[Literal[False]]
    set: Bool[Literal[False]]
    parentSet: Incomplete
    iconSet: Incomplete
    attribute: Bool[Literal[False]]
    time: Bool[Literal[False]]
    keyAttribute: Bool[Literal[False]]
    defaultMemberUniqueName: String[Literal[True]]
    allUniqueName: String[Literal[True]]
    allCaption: String[Literal[True]]
    dimensionUniqueName: String[Literal[True]]
    displayFolder: String[Literal[True]]
    measureGroup: String[Literal[True]]
    measures: Bool[Literal[False]]
    count: Incomplete
    oneField: Bool[Literal[False]]
    memberValueDatatype: Incomplete
    unbalanced: Bool[Literal[True]]
    unbalancedGroup: Bool[Literal[True]]
    hidden: Bool[Literal[False]]
    fieldsUsage: Typed[FieldsUsage, Literal[True]]
    groupLevels: Typed[GroupLevels, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        uniqueName: str,
        caption: str | None,
        measure: _ConvertibleToBool,
        set: _ConvertibleToBool,
        parentSet: Incomplete | None,
        iconSet: int,
        attribute: _ConvertibleToBool,
        time: _ConvertibleToBool,
        keyAttribute: _ConvertibleToBool,
        defaultMemberUniqueName: str | None,
        allUniqueName: str | None,
        allCaption: str | None,
        dimensionUniqueName: str | None,
        displayFolder: str | None,
        measureGroup: str | None,
        measures: _ConvertibleToBool,
        count: Incomplete | None,
        oneField: _ConvertibleToBool,
        memberValueDatatype: Incomplete | None,
        unbalanced: _ConvertibleToBool | None,
        unbalancedGroup: _ConvertibleToBool | None,
        hidden: _ConvertibleToBool,
        fieldsUsage: FieldsUsage | None = None,
        groupLevels: GroupLevels | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class GroupItems(Serialisable):
    tagname: str
    m: Incomplete
    n: Incomplete
    b: Incomplete
    e: Incomplete
    s: Incomplete
    d: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, m=(), n=(), b=(), e=(), s=(), d=()) -> None: ...
    @property
    def count(self): ...

class DiscretePr(Serialisable):
    tagname: str
    count: Incomplete
    x: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, x: Incomplete | None = None) -> None: ...

class RangePr(Serialisable):
    tagname: str
    autoStart: Bool[Literal[True]]
    autoEnd: Bool[Literal[True]]
    groupBy: Set[_RangePrGroupBy]
    startNum: Incomplete
    endNum: Incomplete
    startDate: DateTime[Literal[True]]
    endDate: DateTime[Literal[True]]
    groupInterval: Incomplete
    def __init__(
        self,
        autoStart: _ConvertibleToBool | None = True,
        autoEnd: _ConvertibleToBool | None = True,
        groupBy: _RangePrGroupBy = "range",
        startNum: Incomplete | None = None,
        endNum: Incomplete | None = None,
        startDate: datetime | str | None = None,
        endDate: datetime | str | None = None,
        groupInterval: int = 1,
    ) -> None: ...

class FieldGroup(Serialisable):
    tagname: str
    par: Incomplete
    base: Incomplete
    rangePr: Typed[RangePr, Literal[True]]
    discretePr: Typed[DiscretePr, Literal[True]]
    groupItems: Typed[GroupItems, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        par: Incomplete | None = None,
        base: Incomplete | None = None,
        rangePr: RangePr | None = None,
        discretePr: DiscretePr | None = None,
        groupItems: GroupItems | None = None,
    ) -> None: ...

class SharedItems(Serialisable):
    tagname: str
    m: Incomplete
    n: Incomplete
    b: Incomplete
    e: Incomplete
    s: Incomplete
    d: Incomplete
    containsSemiMixedTypes: Bool[Literal[True]]
    containsNonDate: Bool[Literal[True]]
    containsDate: Bool[Literal[True]]
    containsString: Bool[Literal[True]]
    containsBlank: Bool[Literal[True]]
    containsMixedTypes: Bool[Literal[True]]
    containsNumber: Bool[Literal[True]]
    containsInteger: Bool[Literal[True]]
    minValue: Incomplete
    maxValue: Incomplete
    minDate: DateTime[Literal[True]]
    maxDate: DateTime[Literal[True]]
    longText: Bool[Literal[True]]
    __attrs__: Incomplete
    def __init__(
        self,
        _fields=(),
        containsSemiMixedTypes: _ConvertibleToBool | None = None,
        containsNonDate: _ConvertibleToBool | None = None,
        containsDate: _ConvertibleToBool | None = None,
        containsString: _ConvertibleToBool | None = None,
        containsBlank: _ConvertibleToBool | None = None,
        containsMixedTypes: _ConvertibleToBool | None = None,
        containsNumber: _ConvertibleToBool | None = None,
        containsInteger: _ConvertibleToBool | None = None,
        minValue: Incomplete | None = None,
        maxValue: Incomplete | None = None,
        minDate: datetime | str | None = None,
        maxDate: datetime | str | None = None,
        count: Incomplete | None = None,
        longText: _ConvertibleToBool | None = None,
    ) -> None: ...
    @property
    def count(self): ...

class CacheField(Serialisable):
    tagname: str
    sharedItems: Typed[SharedItems, Literal[True]]
    fieldGroup: Typed[FieldGroup, Literal[True]]
    mpMap: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    name: String[Literal[False]]
    caption: String[Literal[True]]
    propertyName: String[Literal[True]]
    serverField: Bool[Literal[True]]
    uniqueList: Bool[Literal[True]]
    numFmtId: Incomplete
    formula: String[Literal[True]]
    sqlType: Incomplete
    hierarchy: Incomplete
    level: Incomplete
    databaseField: Bool[Literal[True]]
    mappingCount: Incomplete
    memberPropertyField: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        sharedItems: SharedItems | None,
        fieldGroup: FieldGroup | None,
        mpMap: Incomplete | None,
        extLst: ExtensionList | None,
        name: str,
        caption: str | None = None,
        propertyName: str | None = None,
        serverField: _ConvertibleToBool | None = None,
        uniqueList: _ConvertibleToBool | None = True,
        numFmtId: Incomplete | None = None,
        formula: str | None = None,
        sqlType: int = 0,
        hierarchy: int = 0,
        level: int = 0,
        databaseField: _ConvertibleToBool | None = True,
        mappingCount: Incomplete | None = None,
        memberPropertyField: _ConvertibleToBool | None = None,
    ) -> None: ...

class RangeSet(Serialisable):
    tagname: str
    i1: Incomplete
    i2: Incomplete
    i3: Incomplete
    i4: Incomplete
    ref: String[Literal[False]]
    name: String[Literal[True]]
    sheet: String[Literal[True]]
    def __init__(
        self,
        i1: Incomplete | None,
        i2: Incomplete | None,
        i3: Incomplete | None,
        i4: Incomplete | None,
        ref: str,
        name: str | None = None,
        sheet: str | None = None,
    ) -> None: ...

class PageItem(Serialisable):
    tagname: str
    name: String[Literal[False]]
    def __init__(self, name: str) -> None: ...

class Page(Serialisable):
    tagname: str
    pageItem: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, pageItem: Incomplete | None = None) -> None: ...
    @property
    def count(self): ...

class Consolidation(Serialisable):
    tagname: str
    autoPage: Bool[Literal[True]]
    pages: Incomplete
    rangeSets: Incomplete
    __elements__: Incomplete
    def __init__(self, autoPage: _ConvertibleToBool | None = None, pages=(), rangeSets=()) -> None: ...

class WorksheetSource(Serialisable):
    tagname: str
    ref: String[Literal[True]]
    name: String[Literal[True]]
    sheet: String[Literal[True]]
    def __init__(self, ref: str | None = None, name: str | None = None, sheet: str | None = None) -> None: ...

class CacheSource(Serialisable):
    tagname: str
    type: Set[_CacheSourceType]
    connectionId: Incomplete
    worksheetSource: Typed[WorksheetSource, Literal[True]]
    consolidation: Typed[Consolidation, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        type: _CacheSourceType,
        connectionId: Incomplete | None = None,
        worksheetSource: WorksheetSource | None = None,
        consolidation: Consolidation | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class CacheDefinition(Serialisable):
    mime_type: str
    rel_type: str
    records: Incomplete
    tagname: str
    invalid: Bool[Literal[True]]
    saveData: Bool[Literal[True]]
    refreshOnLoad: Bool[Literal[True]]
    optimizeMemory: Bool[Literal[True]]
    enableRefresh: Bool[Literal[True]]
    refreshedBy: String[Literal[True]]
    refreshedDate: Incomplete
    refreshedDateIso: DateTime[Literal[True]]
    backgroundQuery: Bool[Literal[True]]
    missingItemsLimit: Incomplete
    createdVersion: Incomplete
    refreshedVersion: Incomplete
    minRefreshableVersion: Incomplete
    recordCount: Incomplete
    upgradeOnRefresh: Bool[Literal[True]]
    tupleCache: Typed[TupleCache, Literal[True]]
    supportSubquery: Bool[Literal[True]]
    supportAdvancedDrill: Bool[Literal[True]]
    cacheSource: Typed[CacheSource, Literal[True]]
    cacheFields: Incomplete
    cacheHierarchies: Incomplete
    kpis: Incomplete
    calculatedItems: Incomplete
    calculatedMembers: Incomplete
    dimensions: Incomplete
    measureGroups: Incomplete
    maps: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        invalid: _ConvertibleToBool | None,
        saveData: _ConvertibleToBool | None,
        refreshOnLoad: _ConvertibleToBool | None,
        optimizeMemory: _ConvertibleToBool | None,
        enableRefresh: _ConvertibleToBool | None,
        refreshedBy: str | None,
        refreshedDate: Incomplete | None,
        refreshedDateIso: datetime | str | None,
        backgroundQuery: _ConvertibleToBool | None,
        missingItemsLimit: Incomplete | None,
        createdVersion: Incomplete | None,
        refreshedVersion: Incomplete | None,
        minRefreshableVersion: Incomplete | None,
        recordCount: Incomplete | None,
        upgradeOnRefresh: _ConvertibleToBool | None,
        tupleCache: TupleCache | None,
        supportSubquery: _ConvertibleToBool | None,
        supportAdvancedDrill: _ConvertibleToBool | None,
        cacheSource: CacheSource,
        cacheFields=(),
        cacheHierarchies=(),
        kpis=(),
        calculatedItems=(),
        calculatedMembers=(),
        dimensions=(),
        measureGroups=(),
        maps=(),
        extLst: ExtensionList | None = None,
        id: Incomplete | None = None,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...
