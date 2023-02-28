from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import _IntegerSetter
from openpyxl.descriptors.sequence import _Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.colors import Color
from openpyxl.styles.fonts import Font, _UnderlineType

class PhoneticProperties(Serialisable):
    tagname: str
    @property
    def fontId(self) -> int: ...
    @fontId.setter
    def fontId(self, __value: _IntegerSetter | None) -> None: ...
    type: Literal["halfwidthKatakana", "fullwidthKatakana", "Hiragana", "noConversion", None]
    alignment: Literal["noControl", "left", "center", "distributed", None]
    def __init__(
        self,
        fontId: _IntegerSetter,
        type: Literal["halfwidthKatakana", "fullwidthKatakana", "Hiragana", "noConversion", None] = ...,
        alignment: Literal["noControl", "left", "center", "distributed", None] = ...,
    ) -> None: ...

class PhoneticText(Serialisable):
    tagname: str
    @property
    def sb(self) -> int: ...
    @sb.setter
    def sb(self, __value: _IntegerSetter) -> None: ...
    @property
    def eb(self) -> int: ...
    @eb.setter
    def eb(self, __value: _IntegerSetter) -> None: ...
    t: str
    text = t  # noqa: F821
    def __init__(self, sb: _IntegerSetter, eb: _IntegerSetter, t: str) -> None: ...

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
        u: _UnderlineType = ...,
        vertAlign: Literal["superscript", "subscript", "baseline", None] = ...,
        scheme: Literal["major", "minor", None] = ...,
    ) -> None: ...

class RichText(Serialisable):
    tagname: str
    rPr: InlineFont | None
    font = rPr  # noqa: F821
    t: str | None
    text = t  # noqa: F821
    __elements__: tuple[str, ...]
    def __init__(self, rPr: InlineFont | None = ..., t: str | None = ...) -> None: ...

_PhoneticProperties: TypeAlias = PhoneticProperties

class Text(Serialisable):
    tagname: str
    t: str | None
    plain = t  # noqa: F821
    r: _Sequence[RichText] | None
    formatted = r  # noqa: F821
    rPh: _Sequence[PhoneticText] | None
    phonetic = rPh  # noqa: F821
    phoneticPr: _PhoneticProperties | None
    PhoneticProperties = phoneticPr  # noqa: F821
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
