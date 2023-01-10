from collections.abc import Generator
from typing_extensions import Final, Literal, TypeAlias

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
    textRotation: int | None = ...
    text_rotation = textRotation
    wrapText: bool | None = ...
    wrap_text = wrapText
    shrinkToFit: bool | None = ...
    shrink_to_fit = shrinkToFit
    indent: float
    relativeIndent: float
    justifyLastLine: bool | None
    readingOrder: float
    def __init__(
        self,
        horizontal: _HorizontalAlignementsType | None = ...,
        vertical: _VerticalAlignementsType | None = ...,
        textRotation: float | None = ...,
        wrapText: bool | None = ...,
        shrinkToFit: bool | None = ...,
        indent: float = ...,
        relativeIndent: float = ...,
        justifyLastLine: bool | None = ...,
        readingOrder: float = ...,
        text_rotation: bool | None = ...,
        wrap_text: bool | None = ...,
        shrink_to_fit: bool | None = ...,
        mergeCell: _Unused = ...,
    ) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...
