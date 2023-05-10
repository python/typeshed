from _typeshed import Unused
from collections.abc import Generator
from typing_extensions import Final, Literal, TypeAlias

from openpyxl.descriptors.base import _ConvertibleToBool, _ConvertibleToFloat
from openpyxl.descriptors.serialisable import Serialisable

_HorizontalAlignmentsType: TypeAlias = Literal[
    "general", "left", "center", "right", "fill", "justify", "centerContinuous", "distributed"
]
horizontal_alignments: Final[tuple[_HorizontalAlignmentsType, ...]]
_VerticalAlignmentsType: TypeAlias = Literal["top", "center", "bottom", "justify", "distributed"]
vertical_aligments: Final[tuple[_VerticalAlignmentsType, ...]]

class Alignment(Serialisable):
    tagname: str
    __fields__: tuple[str, ...]
    horizontal: _HorizontalAlignmentsType | None
    vertical: _VerticalAlignmentsType | None
    textRotation: int | None
    text_rotation = textRotation  # noqa: F821
    @property
    def wrapText(self) -> bool | None: ...
    @wrapText.setter
    def wrapText(self, __value: _ConvertibleToBool) -> None: ...
    wrap_text = wrapText
    @property
    def shrinkToFit(self) -> bool | None: ...
    @shrinkToFit.setter
    def shrinkToFit(self, __value: _ConvertibleToBool) -> None: ...
    shrink_to_fit = shrinkToFit
    @property
    def indent(self) -> float: ...
    @indent.setter
    def indent(self, __value: _ConvertibleToFloat) -> None: ...
    @property
    def relativeIndent(self) -> float: ...
    @relativeIndent.setter
    def relativeIndent(self, __value: _ConvertibleToFloat) -> None: ...
    @property
    def justifyLastLine(self) -> bool | None: ...
    @justifyLastLine.setter
    def justifyLastLine(self, __value: _ConvertibleToBool) -> None: ...
    @property
    def readingOrder(self) -> float: ...
    @readingOrder.setter
    def readingOrder(self, __value: _ConvertibleToFloat) -> None: ...
    def __init__(
        self,
        horizontal: _HorizontalAlignmentsType | None = None,
        vertical: _VerticalAlignmentsType | None = None,
        textRotation: float | None = 0,
        wrapText: _ConvertibleToBool = None,
        shrinkToFit: _ConvertibleToBool = None,
        indent: _ConvertibleToFloat = 0,
        relativeIndent: _ConvertibleToFloat = 0,
        justifyLastLine: _ConvertibleToBool = None,
        readingOrder: _ConvertibleToFloat = 0,
        text_rotation: int | None = None,
        wrap_text: _ConvertibleToBool = None,
        shrink_to_fit: _ConvertibleToBool = None,
        mergeCell: Unused = None,
    ) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...
