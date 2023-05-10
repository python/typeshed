from typing_extensions import Final, Literal, Self, TypeAlias

from openpyxl.descriptors.base import _ConvertibleToBool, _ConvertibleToFloat, _ConvertibleToInt
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .colors import Color

_UnderlineType: TypeAlias = Literal["single", "double", "singleAccounting", "doubleAccounting", None]

class Font(Serialisable):
    UNDERLINE_DOUBLE: Final = "double"
    UNDERLINE_DOUBLE_ACCOUNTING: Final = "doubleAccounting"
    UNDERLINE_SINGLE: Final = "single"
    UNDERLINE_SINGLE_ACCOUNTING: Final = "singleAccounting"
    name: str | None
    @property
    def charset(self) -> int | None: ...
    @charset.setter
    def charset(self, __value: _ConvertibleToInt | None) -> None: ...
    @property
    def family(self) -> float | None: ...
    @family.setter
    def family(self, __value: _ConvertibleToFloat | None) -> None: ...
    @property
    def sz(self) -> float | None: ...
    @sz.setter
    def sz(self, __value: _ConvertibleToFloat | None) -> None: ...
    size = sz
    @property
    def b(self) -> bool: ...
    @b.setter
    def b(self, __value: _ConvertibleToBool) -> None: ...
    bold = b
    @property
    def i(self) -> bool: ...
    @i.setter
    def i(self, __value: _ConvertibleToBool) -> None: ...
    italic = i
    @property
    def strike(self) -> bool | None: ...
    @strike.setter
    def strike(self, __value: _ConvertibleToBool) -> None: ...
    strikethrough = strike
    @property
    def outline(self) -> bool | None: ...
    @outline.setter
    def outline(self, __value: _ConvertibleToBool) -> None: ...
    @property
    def shadow(self) -> bool | None: ...
    @shadow.setter
    def shadow(self, __value: _ConvertibleToBool) -> None: ...
    @property
    def condense(self) -> bool | None: ...
    @condense.setter
    def condense(self, __value: _ConvertibleToBool) -> None: ...
    @property
    def extend(self) -> bool | None: ...
    @extend.setter
    def extend(self, __value: _ConvertibleToBool) -> None: ...
    u: _UnderlineType
    underline = u  # noqa: F821
    vertAlign: Literal["superscript", "subscript", "baseline", None]
    color: Color | None
    scheme: Literal["major", "minor", None]

    tagname: str

    __elements__: tuple[str, ...]
    def __init__(
        self,
        name: str | None = None,
        sz: _ConvertibleToFloat | None = None,
        b: _ConvertibleToBool = None,
        i: _ConvertibleToBool = None,
        charset: _ConvertibleToInt | None = None,
        u: _UnderlineType = None,
        strike: _ConvertibleToBool = None,
        color: Color | None = None,
        scheme: Literal["major", "minor", None] = None,
        family: _ConvertibleToFloat | None = None,
        size: _ConvertibleToFloat | None = None,
        bold: _ConvertibleToBool = None,
        italic: _ConvertibleToBool = None,
        strikethrough: _ConvertibleToBool = None,
        underline: _UnderlineType = None,
        vertAlign: Literal["superscript", "subscript", "baseline", None] = None,
        outline: _ConvertibleToBool = None,
        shadow: _ConvertibleToBool = None,
        condense: _ConvertibleToBool = None,
        extend: _ConvertibleToBool = None,
    ) -> None: ...
    @classmethod
    def from_tree(cls, node: _Element) -> Self: ...

DEFAULT_FONT: Font
