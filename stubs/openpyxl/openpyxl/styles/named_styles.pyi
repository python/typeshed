from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.alignment import Alignment
from openpyxl.styles.borders import Border
from openpyxl.styles.fills import Fill
from openpyxl.styles.fonts import Font
from openpyxl.styles.protection import Protection

class NamedStyle(Serialisable):
    font: Typed[Font, Literal[False]]
    fill: Typed[Fill, Literal[False]]
    border: Typed[Border, Literal[False]]
    alignment: Typed[Alignment, Literal[False]]
    number_format: Incomplete
    protection: Typed[Protection, Literal[False]]
    builtinId: Incomplete
    hidden: Incomplete
    # Overwritten by property below
    # xfId: Integer
    name: Incomplete
    def __init__(
        self,
        name: str = "Normal",
        font: Font | None = None,
        fill: Fill | None = None,
        border: Border | None = None,
        alignment: Alignment | None = None,
        number_format: Incomplete | None = None,
        protection: Protection | None = None,
        builtinId: Incomplete | None = None,
        hidden: bool = False,
        xfId: Incomplete | None = None,
    ) -> None: ...
    def __setattr__(self, attr: str, value) -> None: ...
    def __iter__(self): ...
    @property
    def xfId(self): ...
    def bind(self, wb) -> None: ...
    def as_tuple(self): ...
    def as_xf(self): ...
    def as_name(self): ...

class NamedStyleList(list[Incomplete]):
    @property
    def names(self): ...
    def __getitem__(self, key): ...
    def append(self, style) -> None: ...

class _NamedCellStyle(Serialisable):
    tagname: str
    name: Incomplete
    xfId: Incomplete
    builtinId: Incomplete
    iLevel: Incomplete
    hidden: Incomplete
    customBuiltin: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        xfId: Incomplete | None = None,
        builtinId: Incomplete | None = None,
        iLevel: Incomplete | None = None,
        hidden: Incomplete | None = None,
        customBuiltin: Incomplete | None = None,
        extLst: Unused = None,
    ) -> None: ...

class _NamedCellStyleList(Serialisable):
    tagname: str
    # Overwritten by property below
    # count: Integer
    cellStyle: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, cellStyle=()) -> None: ...
    @property
    def count(self): ...
    @property
    def names(self): ...
