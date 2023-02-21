from _typeshed import Unused
from collections.abc import Generator
from typing_extensions import Literal

from openpyxl.descriptors.base import _BoolSetter, _IntegerSetter
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.sequence import _Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.workbook.workbook import Workbook

from .alignment import Alignment
from .borders import Border
from .cell_style import CellStyle, StyleArray
from .fills import Fill, PatternFill
from .fonts import Font
from .protection import Protection

class NamedStyle(Serialisable):  # type: ignore[misc]
    font: Font
    fill: Fill
    border: Border
    alignment: Alignment
    number_format: str
    protection: Protection
    @property
    def builtinId(self) -> int | None: ...
    @builtinId.setter
    def builtinId(self, __value: _IntegerSetter | None) -> None: ...
    @property
    def hidden(self) -> bool: ...
    @hidden.setter
    def hidden(self, __value: _BoolSetter) -> None: ...
    name: str
    def __init__(
        self,
        name: str = ...,
        font: Font = ...,
        fill: PatternFill = ...,
        border: Border = ...,
        alignment: Alignment = ...,
        number_format: str | None = ...,
        protection: Protection = ...,
        builtinId: _IntegerSetter | None = ...,
        hidden: _BoolSetter = ...,
        xfId: Unused = ...,
    ) -> None: ...
    def __setattr__(self, attr: str, value) -> None: ...
    def __iter__(self) -> Generator[tuple[Literal["name", "builtinId", "hidden", "xfId"], str], None, None]: ...
    @property
    def xfId(self) -> int | None: ...
    def bind(self, wb: Workbook) -> None: ...
    def as_tuple(self) -> StyleArray: ...
    def as_xf(self) -> CellStyle: ...
    def as_name(self) -> _NamedCellStyle: ...

class NamedStyleList(list[NamedStyle]):
    @property
    def names(self) -> list[str]: ...
    def __getitem__(self, key: int | str) -> NamedStyle: ...  # type: ignore[override]
    def append(self, style: NamedStyle) -> None: ...

class _NamedCellStyle(Serialisable):
    tagname: str
    name: str
    @property
    def xfId(self) -> int: ...
    @xfId.setter
    def xfId(self, __value: _IntegerSetter) -> None: ...
    @property
    def builtinId(self) -> int | None: ...
    @builtinId.setter
    def builtinId(self, __value: _IntegerSetter | None) -> None: ...
    @property
    def iLevel(self) -> int | None: ...
    @iLevel.setter
    def iLevel(self, __value: _IntegerSetter | None) -> None: ...
    @property
    def hidden(self) -> bool: ...
    @hidden.setter
    def hidden(self, __value: _BoolSetter) -> None: ...
    @property
    def customBuiltin(self) -> bool: ...
    @customBuiltin.setter
    def customBuiltin(self, __value: _BoolSetter) -> None: ...
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        name: str,
        xfId: _IntegerSetter,
        builtinId: _IntegerSetter | None = ...,
        iLevel: _IntegerSetter | None = ...,
        hidden: _BoolSetter = ...,
        customBuiltin: _BoolSetter = ...,
        extLst: Unused = ...,
    ) -> None: ...

class _NamedCellStyleList(Serialisable):
    tagname: str
    cellStyle: _Sequence[_NamedCellStyle]
    __attrs__: tuple[str, ...]
    def __init__(self, count: Unused = ..., cellStyle: _Sequence[_NamedCellStyle] = ...) -> None: ...
    @property
    def count(self) -> int: ...
    @property
    def names(self) -> NamedStyleList: ...
