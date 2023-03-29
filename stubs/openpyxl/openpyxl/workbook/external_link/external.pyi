from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import NoneSet, Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.packaging.relationship import Relationship

class ExternalCell(Serialisable):  # type: ignore[misc]
    r: Incomplete
    t: NoneSet(values=(["b", "d", "n", "e", "s", "str", "inlineStr"]))
    vm: Incomplete
    v: Incomplete
    def __init__(
        self, r: Incomplete | None = None, t: Incomplete | None = None, vm: Incomplete | None = None, v: Incomplete | None = None
    ) -> None: ...

class ExternalRow(Serialisable):  # type: ignore[misc]
    r: Incomplete
    cell: Incomplete
    __elements__: Incomplete
    def __init__(self, r=(), cell: Incomplete | None = None) -> None: ...

class ExternalSheetData(Serialisable):  # type: ignore[misc]
    sheetId: Incomplete
    refreshError: Incomplete
    row: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetId: Incomplete | None = None, refreshError: Incomplete | None = None, row=()) -> None: ...

class ExternalSheetDataSet(Serialisable):  # type: ignore[misc]
    sheetData: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetData: Incomplete | None = None) -> None: ...

class ExternalSheetNames(Serialisable):  # type: ignore[misc]
    sheetName: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetName=()) -> None: ...

class ExternalDefinedName(Serialisable):
    tagname: str
    name: Incomplete
    refersTo: Incomplete
    sheetId: Incomplete
    def __init__(
        self, name: Incomplete | None = None, refersTo: Incomplete | None = None, sheetId: Incomplete | None = None
    ) -> None: ...

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
