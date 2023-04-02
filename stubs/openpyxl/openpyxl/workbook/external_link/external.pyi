from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, NoneSet, String, Typed, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.packaging.relationship import Relationship

_ExternalCellType: TypeAlias = Literal["b", "d", "n", "e", "s", "str", "inlineStr"]

class ExternalCell(Serialisable):
    r: String[Literal[False]]
    t: NoneSet[_ExternalCellType]
    vm: Incomplete
    v: Incomplete
    def __init__(
        self,
        r: str,
        t: _ExternalCellType | Literal["none"] | None = None,
        vm: Incomplete | None = None,
        v: Incomplete | None = None,
    ) -> None: ...

class ExternalRow(Serialisable):
    r: Incomplete
    cell: Incomplete
    __elements__: Incomplete
    def __init__(self, r=(), cell: Incomplete | None = None) -> None: ...

class ExternalSheetData(Serialisable):
    sheetId: Incomplete
    refreshError: Bool[Literal[True]]
    row: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetId: Incomplete | None = None, refreshError: _ConvertibleToBool | None = None, row=()) -> None: ...

class ExternalSheetDataSet(Serialisable):
    sheetData: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetData: Incomplete | None = None) -> None: ...

class ExternalSheetNames(Serialisable):
    sheetName: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetName=()) -> None: ...

class ExternalDefinedName(Serialisable):
    tagname: str
    name: String[Literal[False]]
    refersTo: String[Literal[True]]
    sheetId: Incomplete
    def __init__(self, name: str, refersTo: str | None = None, sheetId: Incomplete | None = None) -> None: ...

class ExternalBook(Serialisable):
    tagname: str
    sheetNames: Typed[ExternalSheetNames, Literal[True]]
    definedNames: Incomplete
    sheetDataSet: Typed[ExternalSheetDataSet, Literal[True]]
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        sheetNames: ExternalSheetNames | None = None,
        definedNames=(),
        sheetDataSet: ExternalSheetDataSet | None = None,
        id: Incomplete | None = None,
    ) -> None: ...

class ExternalLink(Serialisable):
    tagname: str
    mime_type: str
    externalBook: Typed[ExternalBook, Literal[True]]
    file_link: Typed[Relationship, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, externalBook: ExternalBook | None = None, ddeLink: Unused = None, oleLink: Unused = None, extLst: Unused = None
    ) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...

def read_external_link(archive, book_path): ...
