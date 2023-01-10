from collections.abc import Generator
from typing_extensions import Literal, TypeAlias

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

_Unused: TypeAlias = object

class NamedStyle(Serialisable):  # type: ignore[misc]
    font: Font
    fill: Fill
    border: Border
    alignment: Alignment
    number_format: str
    protection: Protection
    builtinId: int | None
    hidden: bool | None
    # Overwritten by property below
    # xfId: int | None
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
        builtinId: int | None = ...,
        hidden: bool | None = ...,
        xfId: _Unused = ...,
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
    xfId: int
    builtinId: int | None
    iLevel: int | None
    hidden: bool | None
    customBuiltin: bool | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        name: str,
        xfId: int,
        builtinId: int | None = ...,
        iLevel: int | None = ...,
        hidden: bool | None = ...,
        customBuiltin: bool | None = ...,
        extLst: _Unused = ...,
    ) -> None: ...

class _NamedCellStyleList(Serialisable):
    tagname: str
    # Overwritten by property below
    # count: int | None
    cellStyle: _Sequence[_NamedCellStyle]
    __attrs__: tuple[str, ...]
    def __init__(self, count: _Unused = ..., cellStyle: _Sequence[_NamedCellStyle] = ...) -> None: ...
    @property
    def count(self) -> int | None: ...
    @property
    def names(self) -> NamedStyleList: ...
