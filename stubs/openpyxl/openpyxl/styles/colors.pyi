from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors import Typed
from openpyxl.descriptors.base import Bool, MinMax, _ConvertibleToBool, _ConvertibleToFloat
from openpyxl.descriptors.serialisable import Serialisable

COLOR_INDEX: Incomplete
BLACK: Incomplete
WHITE: Incomplete
BLUE: Incomplete
aRGB_REGEX: Incomplete

class RGB(Typed):
    expected_type: type[str]
    def __set__(self, instance: Serialisable, value) -> None: ...

class Color(Serialisable):
    tagname: str
    rgb: Incomplete
    indexed: Incomplete
    auto: Bool[Literal[False]]
    theme: Incomplete
    tint: MinMax[float, Literal[False]]
    type: Incomplete
    def __init__(
        self,
        rgb="00000000",
        indexed: Incomplete | None = None,
        auto: _ConvertibleToBool | None = None,
        theme: Incomplete | None = None,
        tint: _ConvertibleToFloat = 0.0,
        index: Incomplete | None = None,
        type: str = "rgb",
    ) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    def __iter__(self): ...
    @property
    def index(self): ...
    def __add__(self, other): ...

class ColorDescriptor(Typed):
    expected_type: type[Color]
    def __set__(self, instance: Serialisable, value) -> None: ...

class RgbColor(Serialisable):
    tagname: str
    rgb: Incomplete
    def __init__(self, rgb: Incomplete | None = None) -> None: ...

class ColorList(Serialisable):
    tagname: str
    indexedColors: Incomplete
    mruColors: Incomplete
    __elements__: Incomplete
    def __init__(self, indexedColors=(), mruColors=()) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def index(self): ...
