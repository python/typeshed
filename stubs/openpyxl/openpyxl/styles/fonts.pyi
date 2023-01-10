from _typeshed import Self
from typing_extensions import Literal

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .colors import Color

class Font(Serialisable):
    UNDERLINE_DOUBLE: str
    UNDERLINE_DOUBLE_ACCOUNTING: str
    UNDERLINE_SINGLE: str
    UNDERLINE_SINGLE_ACCOUNTING: str
    name: str | None
    charset: int | None
    family: float | None
    sz: float | None = ...
    size = sz
    b: bool = ...
    bold = b
    i: bool = ...
    italic = i
    strike: bool | None = ...
    strikethrough = strike
    outline: bool | None
    shadow: bool | None
    condense: bool | None
    extend: bool | None
    u: Literal["single", "double", "singleAccounting", "doubleAccounting", None] = ...
    underline = u
    vertAlign: Literal["superscript", "subscript", "baseline", None]
    color: Color | None
    scheme: Literal["major", "minor", None]

    tagname: str

    __elements__: tuple[str, ...]
    def __init__(
        self,
        name: str | None = ...,
        sz: float | None = ...,
        b: bool | None = ...,
        i: bool | None = ...,
        charset: int | None = ...,
        u: Literal["single", "double", "singleAccounting", "doubleAccounting", None] = ...,
        strike: bool | None = ...,
        color: Color | None = ...,
        scheme: Literal["major", "minor", None] = ...,
        family: float | None = ...,
        size: float | None = ...,
        bold: bool | None = ...,
        italic: bool | None = ...,
        strikethrough: bool | None = ...,
        underline: Literal["single", "double", "singleAccounting", "doubleAccounting", None] = ...,
        vertAlign: Literal["superscript", "subscript", "baseline", None] = ...,
        outline: bool | None = ...,
        shadow: bool | None = ...,
        condense: bool | None = ...,
        extend: bool | None = ...,
    ) -> None: ...
    @classmethod
    def from_tree(cls: Self, node: _Element) -> Self: ...

DEFAULT_FONT: Font
