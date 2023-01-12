from collections.abc import Generator
from typing_extensions import Final, Literal, TypeAlias

from openpyxl.descriptors.base import _BoolSetter, _FloatSetter
from openpyxl.descriptors.serialisable import Serialisable

_Unused: TypeAlias = object

horizontal_alignments: Final = ("general", "left", "center", "right", "fill", "justify", "centerContinuous", "distributed")
_HorizontalAlignementsType: TypeAlias = Literal[
    "general", "left", "center", "right", "fill", "justify", "centerContinuous", "distributed"
]
vertical_aligments: Final = ("top", "center", "bottom", "justify", "distributed")
_VerticalAlignementsType: TypeAlias = Literal["top", "center", "bottom", "justify", "distributed"]

class Alignment(Serialisable):
    tagname: str
    __fields__: tuple[str, ...]
    horizontal: _HorizontalAlignementsType | None
    vertical: _VerticalAlignementsType | None
    textRotation: int | None
    text_rotation = textRotation  # noqa: F821
    @property
    def wrapText(self) -> bool | None: ...
    @wrapText.setter
    def wrapText(self, __value: _BoolSetter) -> None: ...
    wrap_text = wrapText
    @property
    def shrinkToFit(self) -> bool | None: ...
    @shrinkToFit.setter
    def shrinkToFit(self, __value: _BoolSetter) -> None: ...
    shrink_to_fit = shrinkToFit
    @property
    def indent(self) -> float: ...
    @indent.setter
    def indent(self, __value: _FloatSetter) -> None: ...
    @property
    def relativeIndent(self) -> float: ...
    @relativeIndent.setter
    def relativeIndent(self, __value: _FloatSetter) -> None: ...
    @property
    def justifyLastLine(self) -> bool | None: ...
    @justifyLastLine.setter
    def justifyLastLine(self, __value: _BoolSetter) -> None: ...
    @property
    def readingOrder(self) -> float: ...
    @readingOrder.setter
    def readingOrder(self, __value: _FloatSetter) -> None: ...
    def __init__(
        self,
        horizontal: _HorizontalAlignementsType | None = ...,
        vertical: _VerticalAlignementsType | None = ...,
        textRotation: float | None = ...,
        wrapText: _BoolSetter = ...,
        shrinkToFit: _BoolSetter = ...,
        indent: _FloatSetter = ...,
        relativeIndent: _FloatSetter = ...,
        justifyLastLine: _BoolSetter = ...,
        readingOrder: _FloatSetter = ...,
        text_rotation: int | None = ...,
        wrap_text: _BoolSetter = ...,
        shrink_to_fit: _BoolSetter = ...,
        mergeCell: _Unused = ...,
    ) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...
