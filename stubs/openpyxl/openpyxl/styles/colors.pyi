from _typeshed import Unused
from collections.abc import Generator
from re import Pattern
from typing import TypeVar, overload
from typing_extensions import Self

from openpyxl.descriptors import Typed
from openpyxl.descriptors.base import _BoolSetter, _FloatSetter, _IntegerSetter
from openpyxl.descriptors.sequence import _Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.colors import SystemColor

_S = TypeVar("_S", bound=Serialisable)

COLOR_INDEX: tuple[str, ...]
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
    @property
    def indexed(self) -> int: ...
    @indexed.setter
    def indexed(self, __value: _IntegerSetter) -> None: ...
    @property
    def auto(self) -> bool: ...
    @auto.setter
    def auto(self, __value: _BoolSetter) -> None: ...
    @property
    def theme(self) -> int: ...
    @theme.setter
    def theme(self, __value: _IntegerSetter) -> None: ...
    @property
    def tint(self) -> float: ...
    @tint.setter
    def tint(self, __value: _FloatSetter) -> None: ...
    type: str
    def __init__(
        self,
        rgb: str = ...,
        indexed: _IntegerSetter | None = ...,
        auto: _BoolSetter = ...,
        theme: _IntegerSetter | None = ...,
        tint: _FloatSetter = ...,
        index: _IntegerSetter | None = ...,
        type: Unused = ...,
    ) -> None: ...
    @property
    def value(self) -> str | float | bool: ...
    @value.setter
    def value(self, value: str | float | bool) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...
    @property
    def index(self) -> str | float | bool: ...
    @overload
    def __add__(self, other: Color) -> Self: ...
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
