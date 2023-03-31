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
        type: Literal["halfwidthKatakana", "fullwidthKatakana", "Hiragana", "noConversion", None] = None,
        alignment: Literal["noControl", "left", "center", "distributed", None] = None,
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
        rFont: str | None = None,
        charset: int | None = None,
        family: float | None = None,
        b: bool | None = None,
        i: bool | None = None,
        strike: bool | None = None,
        outline: bool | None = None,
        shadow: bool | None = None,
        condense: bool | None = None,
        extend: bool | None = None,
        color: Color | None = None,
        sz: float | None = None,
        u: _UnderlineType = None,
        vertAlign: Literal["superscript", "subscript", "baseline", None] = None,
        scheme: Literal["major", "minor", None] = None,
    ) -> None: ...

class RichText(Serialisable):
    tagname: str
    rPr: InlineFont | None
    font = rPr  # noqa: F821
    t: str | None
    text = t  # noqa: F821
    __elements__: tuple[str, ...]
    def __init__(self, rPr: InlineFont | None = None, t: str | None = None) -> None: ...

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
        t: str | None = None,
        r: _Sequence[RichText] | None = (),
        rPh: _Sequence[RichText] | None = (),
        phoneticPr: _PhoneticProperties | None = None,
    ) -> None: ...
    @property
    def content(self) -> str: ...
