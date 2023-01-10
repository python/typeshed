from _typeshed import Self
from collections.abc import Generator, Sequence
from typing_extensions import Final, Literal, TypeAlias

from openpyxl.descriptors import Sequence as SequenceDescriptor
from openpyxl.descriptors.sequence import _Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .colors import Color

_Unused: TypeAlias = object

FILL_NONE: Final = "none"
FILL_SOLID: Final = "solid"
FILL_PATTERN_DARKDOWN: Final = "darkDown"
FILL_PATTERN_DARKGRAY: Final = "darkGray"
FILL_PATTERN_DARKGRID: Final = "darkGrid"
FILL_PATTERN_DARKHORIZONTAL: Final = "darkHorizontal"
FILL_PATTERN_DARKTRELLIS: Final = "darkTrellis"
FILL_PATTERN_DARKUP: Final = "darkUp"
FILL_PATTERN_DARKVERTICAL: Final = "darkVertical"
FILL_PATTERN_GRAY0625: Final = "gray0625"
FILL_PATTERN_GRAY125: Final = "gray125"
FILL_PATTERN_LIGHTDOWN: Final = "lightDown"
FILL_PATTERN_LIGHTGRAY: Final = "lightGray"
FILL_PATTERN_LIGHTGRID: Final = "lightGrid"
FILL_PATTERN_LIGHTHORIZONTAL: Final = "lightHorizontal"
FILL_PATTERN_LIGHTTRELLIS: Final = "lightTrellis"
FILL_PATTERN_LIGHTUP: Final = "lightUp"
FILL_PATTERN_LIGHTVERTICAL: Final = "lightVertical"
FILL_PATTERN_MEDIUMGRAY: Final = "mediumGray"

fills: Final = (
    FILL_SOLID,
    FILL_PATTERN_DARKDOWN,
    FILL_PATTERN_DARKGRAY,
    FILL_PATTERN_DARKGRID,
    FILL_PATTERN_DARKHORIZONTAL,
    FILL_PATTERN_DARKTRELLIS,
    FILL_PATTERN_DARKUP,
    FILL_PATTERN_DARKVERTICAL,
    FILL_PATTERN_GRAY0625,
    FILL_PATTERN_GRAY125,
    FILL_PATTERN_LIGHTDOWN,
    FILL_PATTERN_LIGHTGRAY,
    FILL_PATTERN_LIGHTGRID,
    FILL_PATTERN_LIGHTHORIZONTAL,
    FILL_PATTERN_LIGHTTRELLIS,
    FILL_PATTERN_LIGHTUP,
    FILL_PATTERN_LIGHTVERTICAL,
    FILL_PATTERN_MEDIUMGRAY,
)
_FillsType: TypeAlias = Literal[
    "none",
    "solid",
    "darkDown",
    "darkGray",
    "darkGrid",
    "darkHorizontal",
    "darkTrellis",
    "darkUp",
    "darkVertical",
    "gray0625",
    "gray125",
    "lightDown",
    "lightGray",
    "lightGrid",
    "lightHorizontal",
    "lightTrellis",
    "lightUp",
    "lightVertical",
    "mediumGray",
]

class Fill(Serialisable):
    tagname: str
    @classmethod
    def from_tree(cls: Self, el: _Element) -> Self: ...

class PatternFill(Fill):
    tagname: str
    __elements__: tuple[str, ...]
    patternType: _FillsType | None = ...
    fill_type = patternType
    fgColor: Color = ...
    start_color = fgColor
    bgColor: Color = ...
    end_color = bgColor
    def __init__(
        self,
        patternType: _FillsType | None = ...,
        fgColor: Color = ...,
        bgColor: Color = ...,
        fill_type: _FillsType | None = ...,
        start_color: Color | None = ...,
        end_color: Color | None = ...,
    ) -> None: ...
    def to_tree(self, tagname: _Unused = ..., idx: _Unused = ...): ...  # type: ignore[override]

DEFAULT_EMPTY_FILL: PatternFill
DEFAULT_GRAY_FILL: PatternFill

class Stop(Serialisable):
    tagname: str
    position: float
    color: Color
    def __init__(self, color: Color, position: float) -> None: ...

class StopList(SequenceDescriptor):
    expected_type: type[Stop]
    def __set__(self, obj: GradientFill, values: Sequence[Stop]) -> None: ...

class GradientFill(Fill):
    tagname: str
    type: Literal["linear", "path"]
    fill_type = type
    degree: float
    left: float
    right: float
    top: float
    bottom: float
    stop: _Sequence[Stop]
    def __init__(
        self,
        type: Literal["linear", "path"] = ...,
        degree: float = ...,
        left: float = ...,
        right: float = ...,
        top: float = ...,
        bottom: float = ...,
        stop: _Sequence[Stop] = ...,
    ) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...
    def to_tree(  # type: ignore[override]
        self, tagname: _Unused = ..., namespace: _Unused = ..., idx: _Unused = ...
    ) -> _Element: ...
