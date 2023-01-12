from _typeshed import Self
from typing_extensions import Final, Literal

from openpyxl.descriptors.base import _BoolSetter, _FloatSetter, _IntegerSetter
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .colors import Color

class Font(Serialisable):
    UNDERLINE_DOUBLE: Final = "double"
    UNDERLINE_DOUBLE_ACCOUNTING: Final = "doubleAccounting"
    UNDERLINE_SINGLE: Final = "single"
    UNDERLINE_SINGLE_ACCOUNTING: Final = "singleAccounting"
    name: str | None
    @property
    def charset(self) -> int | None: ...
    @charset.setter
    def charset(self, __value: _IntegerSetter | None) -> None: ...
    @property
    def family(self) -> float | None: ...
    @family.setter
    def family(self, __value: _FloatSetter | None) -> None: ...
    @property
    def sz(self) -> float | None: ...
    @sz.setter
    def sz(self, __value: _FloatSetter | None) -> None: ...
    size = sz
    @property
    def b(self) -> bool: ...
    @b.setter
    def b(self, __value: _BoolSetter) -> None: ...
    bold = b
    @property
    def i(self) -> bool: ...
    @i.setter
    def i(self, __value: _BoolSetter) -> None: ...
    italic = i
    @property
    def strike(self) -> bool | None: ...
    @strike.setter
    def strike(self, __value: _BoolSetter) -> None: ...
    strikethrough = strike
    @property
    def outline(self) -> bool | None: ...
    @outline.setter
    def outline(self, __value: _BoolSetter) -> None: ...
    @property
    def shadow(self) -> bool | None: ...
    @shadow.setter
    def shadow(self, __value: _BoolSetter) -> None: ...
    @property
    def condense(self) -> bool | None: ...
    @condense.setter
    def condense(self, __value: _BoolSetter) -> None: ...
    @property
    def extend(self) -> bool | None: ...
    @extend.setter
    def extend(self, __value: _BoolSetter) -> None: ...
    u: Literal["single", "double", "singleAccounting", "doubleAccounting", None]
    underline = u  # noqa: F821
    vertAlign: Literal["superscript", "subscript", "baseline", None]
    color: Color | None
    scheme: Literal["major", "minor", None]

    tagname: str

    __elements__: tuple[str, ...]
    def __init__(
        self,
        name: str | None = ...,
        sz: _FloatSetter | None = ...,
        b: _BoolSetter = ...,
        i: _BoolSetter = ...,
        charset: _IntegerSetter | None = ...,
        u: Literal["single", "double", "singleAccounting", "doubleAccounting", None] = ...,
        strike: _BoolSetter = ...,
        color: Color | None = ...,
        scheme: Literal["major", "minor", None] = ...,
        family: _FloatSetter | None = ...,
        size: _FloatSetter | None = ...,
        bold: _BoolSetter = ...,
        italic: _BoolSetter = ...,
        strikethrough: _BoolSetter = ...,
        underline: Literal["single", "double", "singleAccounting", "doubleAccounting", None] = ...,
        vertAlign: Literal["superscript", "subscript", "baseline", None] = ...,
        outline: _BoolSetter = ...,
        shadow: _BoolSetter = ...,
        condense: _BoolSetter = ...,
        extend: _BoolSetter = ...,
    ) -> None: ...
    @classmethod
    def from_tree(cls: Self, node: _Element) -> Self: ...

DEFAULT_FONT: Font
