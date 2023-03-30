from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import NoneSet, Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.fonts import Font

_PhoneticPropertiesType: TypeAlias = Literal["halfwidthKatakana", "fullwidthKatakana", "Hiragana", "noConversion"]
_PhoneticPropertiesAlignment: TypeAlias = Literal["noControl", "left", "center", "distributed"]

class PhoneticProperties(Serialisable):
    tagname: str
    fontId: Incomplete
    type: NoneSet[_PhoneticPropertiesType]
    alignment: NoneSet[_PhoneticPropertiesAlignment]
    def __init__(
        self,
        fontId: Incomplete | None = None,
        type: _PhoneticPropertiesType | Literal["none"] | None = None,
        alignment: _PhoneticPropertiesAlignment | Literal["none"] | None = None,
    ) -> None: ...

class PhoneticText(Serialisable):
    tagname: str
    sb: Incomplete
    eb: Incomplete
    t: Incomplete
    text: Incomplete
    def __init__(self, sb: Incomplete | None = None, eb: Incomplete | None = None, t: Incomplete | None = None) -> None: ...

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
    __elements__: Incomplete
    def __init__(
        self,
        rFont: Incomplete | None = None,
        charset: Incomplete | None = None,
        family: Incomplete | None = None,
        b: Incomplete | None = None,
        i: Incomplete | None = None,
        strike: Incomplete | None = None,
        outline: Incomplete | None = None,
        shadow: Incomplete | None = None,
        condense: Incomplete | None = None,
        extend: Incomplete | None = None,
        color: Incomplete | None = None,
        sz: Incomplete | None = None,
        u: Incomplete | None = None,
        vertAlign: Incomplete | None = None,
        scheme: Incomplete | None = None,
    ) -> None: ...

class RichText(Serialisable):
    tagname: str
    rPr: Typed[InlineFont, Literal[True]]
    font: Incomplete
    t: Incomplete
    text: Incomplete
    __elements__: Incomplete
    def __init__(self, rPr: InlineFont | None = None, t: Incomplete | None = None) -> None: ...

class Text(Serialisable):
    tagname: str
    t: Incomplete
    plain: Incomplete
    r: Incomplete
    formatted: Incomplete
    rPh: Incomplete
    phonetic: Incomplete
    phoneticPr: Typed[PhoneticProperties, Literal[True]]
    PhoneticProperties: Incomplete
    __elements__: Incomplete
    def __init__(self, t: Incomplete | None = None, r=(), rPh=(), phoneticPr: PhoneticProperties | None = None) -> None: ...
    @property
    def content(self): ...
