from _typeshed import Incomplete
from typing import ClassVar
from typing_extensions import Final, Literal, Self, TypeAlias

from openpyxl.descriptors.base import Alias, _ConvertibleToBool, _ConvertibleToFloat, _ConvertibleToInt
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .colors import Color

_UnderlineType: TypeAlias = Literal["single", "double", "singleAccounting", "doubleAccounting", None]

class Font(Serialisable):
    UNDERLINE_DOUBLE: Final = "double"
    UNDERLINE_DOUBLE_ACCOUNTING: Final = "doubleAccounting"
    UNDERLINE_SINGLE: Final = "single"
    UNDERLINE_SINGLE_ACCOUNTING: Final = "singleAccounting"
    name: Incomplete
    charset: Incomplete
    family: Incomplete
    sz: Incomplete
    size: Alias
    b: Incomplete
    bold: Alias
    i: Incomplete
    italic: Alias
    strike: Incomplete
    strikethrough: Alias
    outline: Incomplete
    shadow: Incomplete
    condense: Incomplete
    extend: Incomplete
    u: Incomplete
    underline: Alias
    vertAlign: Incomplete
    color: Incomplete
    scheme: Incomplete
    tagname: str
    __elements__: ClassVar[tuple[str, ...]]
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
