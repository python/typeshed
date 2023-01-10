from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.sequence import _Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.colors import Color
from openpyxl.styles.fonts import Font

class PhoneticProperties(Serialisable):
    tagname: str
    fontId: int
    type: Literal["halfwidthKatakana", "fullwidthKatakana", "Hiragana", "noConversion", None]
    alignment: Literal["noControl", "left", "center", "distributed", None]
    def __init__(
        self,
        fontId: int,
        type: Literal["halfwidthKatakana", "fullwidthKatakana", "Hiragana", "noConversion", None] = ...,
        alignment: Literal["noControl", "left", "center", "distributed", None] = ...,
    ) -> None: ...

class PhoneticText(Serialisable):
    tagname: str
    sb: int
    eb: int
    t: str = ...
    text = t
    def __init__(self, sb: int, eb: int, t: str) -> None: ...

class InlineFont(Font):
    tagname: str
    rFont: str | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        rFont: str | None = ...,
        charset: int | None = ...,
        family: float | None = ...,
        b: bool | None = ...,
        i: bool | None = ...,
        strike: bool | None = ...,
        outline: bool | None = ...,
        shadow: bool | None = ...,
        condense: bool | None = ...,
        extend: bool | None = ...,
        color: Color | None = ...,
        sz: float | None = ...,
        u: Literal["single", "double", "singleAccounting", "doubleAccounting", None] = ...,
        vertAlign: Literal["superscript", "subscript", "baseline", None] = ...,
        scheme: Literal["major", "minor", None] = ...,
    ) -> None: ...

class RichText(Serialisable):
    tagname: str
    rPr: InlineFont | None = ...
    font = rPr
    t: str | None = ...
    text = t
    __elements__: tuple[str, ...]
    def __init__(self, rPr: InlineFont | None = ..., t: str | None = ...) -> None: ...

_PhoneticProperties: TypeAlias = PhoneticProperties

class Text(Serialisable):
    tagname: str
    t: str | None = ...
    plain = t
    r: _Sequence[RichText] | None = ...
    formatted = r
    rPh: _Sequence[PhoneticText] | None = ...
    phonetic = rPh
    phoneticPr: _PhoneticProperties | None = ...
    PhoneticProperties = phoneticPr
    __elements__: tuple[str, ...]
    def __init__(
        self,
        t: str | None = ...,
        r: _Sequence[RichText] | None = ...,
        rPh: _Sequence[RichText] | None = ...,
        phoneticPr: _PhoneticProperties | None = ...,
    ) -> None: ...
    @property
    def content(self) -> str: ...
