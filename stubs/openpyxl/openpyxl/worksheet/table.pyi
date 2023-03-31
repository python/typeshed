from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors import String
from openpyxl.descriptors.base import Bool, NoneSet, Typed, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.filters import AutoFilter, SortState

_TableColumnTotalsRowFunction: TypeAlias = Literal[
    "sum", "min", "max", "average", "count", "countNums", "stdDev", "var", "custom"
]
_TableTableType: TypeAlias = Literal["worksheet", "xml", "queryTable"]

TABLESTYLES: Incomplete
PIVOTSTYLES: Incomplete

class TableStyleInfo(Serialisable):
    tagname: str
    name: Incomplete
    showFirstColumn: Bool[Literal[True]]
    showLastColumn: Bool[Literal[True]]
    showRowStripes: Bool[Literal[True]]
    showColumnStripes: Bool[Literal[True]]
    def __init__(
        self,
        name: Incomplete | None = None,
        showFirstColumn: _ConvertibleToBool | None = None,
        showLastColumn: _ConvertibleToBool | None = None,
        showRowStripes: _ConvertibleToBool | None = None,
        showColumnStripes: _ConvertibleToBool | None = None,
    ) -> None: ...

class XMLColumnProps(Serialisable):
    tagname: str
    mapId: Incomplete
    xpath: Incomplete
    denormalized: Bool[Literal[True]]
    xmlDataType: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        mapId: Incomplete | None = None,
        xpath: Incomplete | None = None,
        denormalized: _ConvertibleToBool | None = None,
        xmlDataType: Incomplete | None = None,
        extLst: Unused = None,
    ) -> None: ...

class TableFormula(Serialisable):
    tagname: str
    array: Bool[Literal[True]]
    attr_text: Incomplete
    text: Incomplete
    def __init__(self, array: _ConvertibleToBool | None = None, attr_text: Incomplete | None = None) -> None: ...

class TableColumn(Serialisable):
    tagname: str
    id: Incomplete
    uniqueName: Incomplete
    name: Incomplete
    totalsRowFunction: NoneSet[_TableColumnTotalsRowFunction]
    totalsRowLabel: Incomplete
    queryTableFieldId: Incomplete
    headerRowDxfId: Incomplete
    dataDxfId: Incomplete
    totalsRowDxfId: Incomplete
    headerRowCellStyle: Incomplete
    dataCellStyle: Incomplete
    totalsRowCellStyle: Incomplete
    calculatedColumnFormula: Typed[TableFormula, Literal[True]]
    totalsRowFormula: Typed[TableFormula, Literal[True]]
    xmlColumnPr: Typed[XMLColumnProps, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        uniqueName: Incomplete | None = None,
        name: Incomplete | None = None,
        totalsRowFunction: _TableColumnTotalsRowFunction | Literal["none"] | None = None,
        totalsRowLabel: Incomplete | None = None,
        queryTableFieldId: Incomplete | None = None,
        headerRowDxfId: Incomplete | None = None,
        dataDxfId: Incomplete | None = None,
        totalsRowDxfId: Incomplete | None = None,
        headerRowCellStyle: Incomplete | None = None,
        dataCellStyle: Incomplete | None = None,
        totalsRowCellStyle: Incomplete | None = None,
        calculatedColumnFormula: TableFormula | None = None,
        totalsRowFormula: TableFormula | None = None,
        xmlColumnPr: XMLColumnProps | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...
    def __iter__(self): ...
    @classmethod
    def from_tree(cls, node): ...

class TableNameDescriptor(String):
    def __set__(self, instance: Serialisable, value) -> None: ...

class Table(Serialisable):
    mime_type: str
    tagname: str
    id: Incomplete
    name: Incomplete
    displayName: Incomplete
    comment: Incomplete
    ref: Incomplete
    tableType: NoneSet[_TableTableType]
    headerRowCount: Incomplete
    insertRow: Bool[Literal[True]]
    insertRowShift: Bool[Literal[True]]
    totalsRowCount: Incomplete
    totalsRowShown: Bool[Literal[True]]
    published: Bool[Literal[True]]
    headerRowDxfId: Incomplete
    dataDxfId: Incomplete
    totalsRowDxfId: Incomplete
    headerRowBorderDxfId: Incomplete
    tableBorderDxfId: Incomplete
    totalsRowBorderDxfId: Incomplete
    headerRowCellStyle: Incomplete
    dataCellStyle: Incomplete
    totalsRowCellStyle: Incomplete
    connectionId: Incomplete
    autoFilter: Typed[AutoFilter, Literal[True]]
    sortState: Typed[SortState, Literal[True]]
    tableColumns: Incomplete
    tableStyleInfo: Typed[TableStyleInfo, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        id: int = 1,
        displayName: Incomplete | None = None,
        ref: Incomplete | None = None,
        name: Incomplete | None = None,
        comment: Incomplete | None = None,
        tableType: _TableTableType | Literal["none"] | None = None,
        headerRowCount: int = 1,
        insertRow: _ConvertibleToBool | None = None,
        insertRowShift: _ConvertibleToBool | None = None,
        totalsRowCount: Incomplete | None = None,
        totalsRowShown: _ConvertibleToBool | None = None,
        published: _ConvertibleToBool | None = None,
        headerRowDxfId: Incomplete | None = None,
        dataDxfId: Incomplete | None = None,
        totalsRowDxfId: Incomplete | None = None,
        headerRowBorderDxfId: Incomplete | None = None,
        tableBorderDxfId: Incomplete | None = None,
        totalsRowBorderDxfId: Incomplete | None = None,
        headerRowCellStyle: Incomplete | None = None,
        dataCellStyle: Incomplete | None = None,
        totalsRowCellStyle: Incomplete | None = None,
        connectionId: Incomplete | None = None,
        autoFilter: AutoFilter | None = None,
        sortState: SortState | None = None,
        tableColumns=(),
        tableStyleInfo: TableStyleInfo | None = None,
        extLst: Unused = None,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...
    @property
    def column_names(self): ...

class TablePartList(Serialisable):
    tagname: str
    # Overwritten by property below
    # count: Integer
    tablePart: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, tablePart=()) -> None: ...
    def append(self, part) -> None: ...
    @property
    def count(self): ...
    def __bool__(self) -> bool: ...

class TableList(dict[Incomplete, Incomplete]):
    def add(self, table) -> None: ...
    def get(self, name: Incomplete | None = None, table_range: Incomplete | None = None): ...
    def items(self): ...
