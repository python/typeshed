from _typeshed import Incomplete, Unused
from array import array
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.alignment import Alignment
from openpyxl.styles.protection import Protection

class ArrayDescriptor:
    key: Incomplete
    def __init__(self, key) -> None: ...
    def __get__(self, instance: Serialisable, cls: Unused): ...
    def __set__(self, instance: Serialisable, value) -> None: ...

class StyleArray(array[Incomplete]):
    tagname: str
    fontId: Incomplete
    fillId: Incomplete
    borderId: Incomplete
    numFmtId: Incomplete
    protectionId: Incomplete
    alignmentId: Incomplete
    pivotButton: Incomplete
    quotePrefix: Incomplete
    xfId: Incomplete
    def __new__(cls, args=[0, 0, 0, 0, 0, 0, 0, 0, 0]): ...
    def __hash__(self) -> int: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

class CellStyle(Serialisable):
    tagname: str
    numFmtId: Incomplete
    fontId: Incomplete
    fillId: Incomplete
    borderId: Incomplete
    xfId: Incomplete
    quotePrefix: Incomplete
    pivotButton: Incomplete
    applyNumberFormat: Incomplete
    applyFont: Incomplete
    applyFill: Incomplete
    applyBorder: Incomplete
    # Overwritten by properties below
    # applyAlignment: Bool
    # applyProtection: Bool
    alignment: Typed[Alignment, Literal[True]]
    protection: Typed[Protection, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        numFmtId: int = 0,
        fontId: int = 0,
        fillId: int = 0,
        borderId: int = 0,
        xfId: Incomplete | None = None,
        quotePrefix: Incomplete | None = None,
        pivotButton: Incomplete | None = None,
        applyNumberFormat: Incomplete | None = None,
        applyFont: Incomplete | None = None,
        applyFill: Incomplete | None = None,
        applyBorder: Incomplete | None = None,
        applyAlignment: Unused = None,
        applyProtection: Unused = None,
        alignment: Alignment | None = None,
        protection: Protection | None = None,
        extLst: Unused = None,
    ) -> None: ...
    def to_array(self): ...
    @classmethod
    def from_array(cls, style): ...
    @property
    def applyProtection(self): ...
    @property
    def applyAlignment(self): ...

class CellStyleList(Serialisable):
    tagname: str
    __attrs__: Incomplete
    # Overwritten by property below
    # count: Integer
    xf: Incomplete
    alignment: Incomplete
    protection: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, xf=()) -> None: ...
    @property
    def count(self): ...
    def __getitem__(self, idx): ...
