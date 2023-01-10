from _typeshed import Incomplete
from typing_extensions import TypeAlias

from openpyxl.descriptors.sequence import _Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles import Alignment, Border, Fill, Font, Protection

from .numbers import NumberFormat

_Unused: TypeAlias = object

class DifferentialStyle(Serialisable):
    tagname: str
    __elements__: tuple[str, ...]
    font: Font | None
    numFmt: NumberFormat | None
    fill: Fill | None
    alignment: Alignment | None
    border: Border | None
    protection: Protection | None
    extLst: _Sequence[Incomplete] | None
    def __init__(
        self,
        font: Font | None = ...,
        numFmt: NumberFormat | None = ...,
        fill: Fill | None = ...,
        alignment: Alignment | None = ...,
        border: Border | None = ...,
        protection: Protection | None = ...,
        extLst: _Sequence[Incomplete] | None = ...,
    ) -> None: ...

class DifferentialStyleList(Serialisable):
    tagname: str
    dxf: _Sequence[DifferentialStyle]
    styles: Incomplete
    __attrs__: Incomplete
    def __init__(self, dxf: _Sequence[DifferentialStyle] = ..., count: _Unused = ...) -> None: ...
    def append(self, dxf: DifferentialStyle) -> None: ...
    def add(self, dxf: DifferentialStyle) -> int: ...
    def __bool__(self) -> bool: ...
    def __getitem__(self, idx: int) -> DifferentialStyle: ...
    @property
    def count(self): ...
