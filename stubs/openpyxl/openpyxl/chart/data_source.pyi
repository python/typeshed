from _typeshed import Incomplete, Unused
from typing import NoReturn, overload
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.nested import NestedText
from openpyxl.descriptors.serialisable import Serialisable

class NumFmt(Serialisable):  # type: ignore[misc]
    formatCode: Incomplete
    sourceLinked: Incomplete
    def __init__(self, formatCode: Incomplete | None = None, sourceLinked: bool = False) -> None: ...

class NumberValueDescriptor(NestedText):
    allow_none: bool
    expected_type: Incomplete
    def __set__(self, instance: Serialisable, value) -> None: ...

class NumVal(Serialisable):  # type: ignore[misc]
    idx: Incomplete
    formatCode: Incomplete
    v: Incomplete
    def __init__(
        self, idx: Incomplete | None = None, formatCode: Incomplete | None = None, v: Incomplete | None = None
    ) -> None: ...

class NumData(Serialisable):  # type: ignore[misc]
    formatCode: Incomplete
    ptCount: Incomplete
    pt: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, formatCode: Incomplete | None = None, ptCount: Incomplete | None = None, pt=(), extLst: Unused = None
    ) -> None: ...

class NumRef(Serialisable):  # type: ignore[misc]
    f: Incomplete
    ref: Incomplete
    numCache: Typed[NumData, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, f: Incomplete | None = None, numCache: NumData | None = None, extLst: Unused = None) -> None: ...

class StrVal(Serialisable):
    tagname: str
    idx: Incomplete
    v: Incomplete
    def __init__(self, idx: int = 0, v: Incomplete | None = None) -> None: ...

class StrData(Serialisable):
    tagname: str
    ptCount: Incomplete
    pt: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, ptCount: Incomplete | None = None, pt=(), extLst: Unused = None) -> None: ...

class StrRef(Serialisable):
    tagname: str
    f: Incomplete
    strCache: Typed[StrData, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, f: Incomplete | None = None, strCache: StrData | None = None, extLst: Unused = None) -> None: ...

class NumDataSource(Serialisable):  # type: ignore[misc]
    numRef: Typed[NumRef, Literal[True]]
    numLit: Typed[NumData, Literal[True]]
    def __init__(self, numRef: NumRef | None = None, numLit: NumData | None = None) -> None: ...

class Level(Serialisable):
    tagname: str
    pt: Incomplete
    __elements__: Incomplete
    def __init__(self, pt=()) -> None: ...

class MultiLevelStrData(Serialisable):
    tagname: str
    ptCount: Incomplete
    lvl: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, ptCount: Incomplete | None = None, lvl=(), extLst: Unused = None) -> None: ...

class MultiLevelStrRef(Serialisable):
    tagname: str
    f: Incomplete
    multiLvlStrCache: Typed[MultiLevelStrData, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, f: Incomplete | None = None, multiLvlStrCache: MultiLevelStrData | None = None, extLst: Unused = None
    ) -> None: ...

class AxDataSource(Serialisable):
    tagname: str
    numRef: Typed[NumRef, Literal[True]]
    numLit: Typed[NumData, Literal[True]]
    strRef: Typed[StrRef, Literal[True]]
    strLit: Typed[StrData, Literal[True]]
    multiLvlStrRef: Typed[MultiLevelStrRef, Literal[True]]
    @overload
    def __init__(
        self, numRef: None = None, numLit: None = None, strRef: None = None, strLit: None = None, multiLvlStrRef: None = None
    ) -> NoReturn: ...
    @overload
    def __init__(
        self,
        numRef: NumRef | None = None,
        numLit: NumData | None = None,
        strRef: StrRef | None = None,
        strLit: StrData | None = None,
        multiLvlStrRef: MultiLevelStrRef | None = None,
    ) -> None: ...
