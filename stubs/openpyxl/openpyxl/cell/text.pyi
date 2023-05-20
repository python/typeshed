from _typeshed import Incomplete
from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Alias, Integer, NoneSet, Typed, _ConvertibleToInt
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.colors import Color
from openpyxl.styles.fonts import Font, _UnderlineType

_PhoneticPropertiesType: TypeAlias = Literal["halfwidthKatakana", "fullwidthKatakana", "Hiragana", "noConversion"]
_PhoneticPropertiesAlignment: TypeAlias = Literal["noControl", "left", "center", "distributed"]
_PhoneticProperties: TypeAlias = PhoneticProperties

class PhoneticProperties(Serialisable):
    tagname: str
    fontId: Integer[Literal[False]]
    type: NoneSet[_PhoneticPropertiesType]
    alignment: NoneSet[_PhoneticPropertiesAlignment]
    def __init__(
        self,
        fontId: _ConvertibleToInt,
        type: _PhoneticPropertiesType | Literal["none"] | None = None,
        alignment: _PhoneticPropertiesAlignment | Literal["none"] | None = None,
    ) -> None: ...

class PhoneticText(Serialisable):
    tagname: str
    sb: Integer[Literal[False]]
    eb: Integer[Literal[False]]
    t: Incomplete
    text: Alias
    def __init__(self, sb: _ConvertibleToInt, eb: _ConvertibleToInt, t: Incomplete | None = None) -> None: ...

class InlineFont(Font):
    tagname: str
    rFont: Incomplete
    charset: Incomplete
    family: Incomplete
    b: Incomplete
    i: Incomplete
    strike: Incomplete
    outline: Incomplete
    shadow: Incomplete
    condense: Incomplete
    extend: Incomplete
    color: Incomplete
    sz: Incomplete
    u: Incomplete
    vertAlign: Incomplete
    scheme: Incomplete
    __elements__: ClassVar[tuple[str, ...]]
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
    rPr: Typed[InlineFont, Literal[True]]
    font: Alias
    t: Incomplete
    text: Alias
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(self, rPr: InlineFont | None = None, t: Incomplete | None = None) -> None: ...

class Text(Serialisable):
    tagname: str
    t: Incomplete
    plain: Alias
    r: Incomplete
    formatted: Alias
    rPh: Incomplete
    phonetic: Alias
    phoneticPr: Typed[_PhoneticProperties, Literal[True]]
    PhoneticProperties: Alias
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(self, t: Incomplete | None = None, r=(), rPh=(), phoneticPr: _PhoneticProperties | None = None) -> None: ...
    @property
    def content(self) -> str: ...
