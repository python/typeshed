from _typeshed import Self
from collections.abc import Generator
from re import Pattern
from typing import TypeVar, overload
from typing_extensions import TypeAlias

from openpyxl.descriptors import Typed
from openpyxl.descriptors.sequence import _Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.colors import SystemColor

_Unused: TypeAlias = object
_S = TypeVar("_S", bound=Serialisable)

COLOR_INDEX: tuple[
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
    str,
]
BLACK: str
WHITE: str
BLUE: str
aRGB_REGEX: Pattern[str]

class RGB(Typed):
    expected_type: type[str]
    def __set__(self, instance: Color | SystemColor | RgbColor, value: str) -> None: ...

class Color(Serialisable):
    tagname: str
    rgb: str
    indexed: int
    auto: bool
    theme: int
    tint: float
    type: str
    def __init__(
        self,
        rgb: str = ...,
        indexed: int | None = ...,
        auto: bool | None = ...,
        theme: int | None = ...,
        tint: float = ...,
        index: int | None = ...,
        type: _Unused = ...,
    ) -> None: ...
    @property
    def value(self) -> str | float | bool: ...
    @value.setter
    def value(self, value: str | float | bool) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...
    @property
    def index(self) -> str | float | bool: ...
    @overload
    def __add__(self: Self, other: Color) -> Self: ...
    @overload
    def __add__(self, other: _S) -> _S: ...

class ColorDescriptor(Typed):
    expected_type: type[Color]
    def __set__(self, instance: Serialisable, value: str | Color) -> None: ...

class RgbColor(Serialisable):
    tagname: str
    rgb: str
    def __init__(self, rgb: str) -> None: ...

class ColorList(Serialisable):
    tagname: str
    indexedColors: _Sequence[RgbColor]
    mruColors: _Sequence[Color]
    __elements__: tuple[str, ...]
    def __init__(self, indexedColors: _Sequence[RgbColor] = ..., mruColors: _Sequence[Color] = ...) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def index(self) -> list[str]: ...
