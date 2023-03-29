from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors import Strict
from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.serialisable import Serialisable

FONT_PATTERN: str
COLOR_PATTERN: str
SIZE_REGEX: str
FORMAT_REGEX: Incomplete

class _HeaderFooterPart(Strict):
    text: Incomplete
    font: Incomplete
    size: Incomplete
    RGB: str
    color: Incomplete
    def __init__(
        self,
        text: Incomplete | None = None,
        font: Incomplete | None = None,
        size: Incomplete | None = None,
        color: Incomplete | None = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    @classmethod
    def from_str(cls, text): ...

class HeaderFooterItem(Strict):
    left: Typed[_HeaderFooterPart, Literal[False]]
    center: Typed[_HeaderFooterPart, Literal[False]]
    centre: Incomplete
    right: Typed[_HeaderFooterPart, Literal[False]]
    def __init__(
        self,
        left: _HeaderFooterPart | None = None,
        right: _HeaderFooterPart | None = None,
        center: _HeaderFooterPart | None = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def to_tree(self, tagname): ...
    @classmethod
    def from_tree(cls, node): ...

class HeaderFooter(Serialisable):
    tagname: str
    differentOddEven: Incomplete
    differentFirst: Incomplete
    scaleWithDoc: Incomplete
    alignWithMargins: Incomplete
    oddHeader: Typed[HeaderFooterItem, Literal[True]]
    oddFooter: Typed[HeaderFooterItem, Literal[True]]
    evenHeader: Typed[HeaderFooterItem, Literal[True]]
    evenFooter: Typed[HeaderFooterItem, Literal[True]]
    firstHeader: Typed[HeaderFooterItem, Literal[True]]
    firstFooter: Typed[HeaderFooterItem, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        differentOddEven: Incomplete | None = None,
        differentFirst: Incomplete | None = None,
        scaleWithDoc: Incomplete | None = None,
        alignWithMargins: Incomplete | None = None,
        oddHeader: HeaderFooterItem | None = None,
        oddFooter: HeaderFooterItem | None = None,
        evenHeader: HeaderFooterItem | None = None,
        evenFooter: HeaderFooterItem | None = None,
        firstHeader: HeaderFooterItem | None = None,
        firstFooter: HeaderFooterItem | None = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...
