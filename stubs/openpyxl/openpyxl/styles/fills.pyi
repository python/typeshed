from _typeshed import Unused
from collections.abc import Generator, Sequence
from typing_extensions import Final, Literal, Self, TypeAlias

from openpyxl.descriptors import Sequence as SequenceDescriptor
from openpyxl.descriptors.base import _FloatSetter
from openpyxl.descriptors.sequence import _Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .colors import Color

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

fills: Final[tuple[_FillsType, ...]]
_FillsType: TypeAlias = Literal[
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
    def from_tree(cls, el: _Element) -> Self: ...

class PatternFill(Fill):
    tagname: str
    __elements__: tuple[str, ...]
    patternType: _FillsType | None
    fill_type = patternType  # noqa: F821
    fgColor: Color
    start_color = fgColor  # noqa: F821
    bgColor: Color
    end_color = bgColor  # noqa: F821
    def __init__(
        self,
        patternType: _FillsType | Literal["none", None] = ...,
        fgColor: Color = ...,
        bgColor: Color = ...,
        fill_type: _FillsType | Literal["none", None] = ...,
        start_color: Color | None = ...,
        end_color: Color | None = ...,
    ) -> None: ...
    def to_tree(self, tagname: Unused = ..., idx: Unused = ...): ...  # type: ignore[override]

DEFAULT_EMPTY_FILL: PatternFill
DEFAULT_GRAY_FILL: PatternFill

class Stop(Serialisable):
    tagname: str
    @property
    def position(self) -> float: ...
    @position.setter
    def position(self, __value: _FloatSetter) -> None: ...
    color: Color
    def __init__(self, color: Color, position: _FloatSetter) -> None: ...

class StopList(SequenceDescriptor):
    expected_type: type[Stop]
    def __set__(self, obj: GradientFill, values: Sequence[Stop]) -> None: ...

class GradientFill(Fill):
    tagname: str
    type: Literal["linear", "path"]
    fill_type = type
    @property
    def degree(self) -> float: ...
    @degree.setter
    def degree(self, __value: _FloatSetter) -> None: ...
    @property
    def left(self) -> float: ...
    @left.setter
    def left(self, __value: _FloatSetter) -> None: ...
    @property
    def right(self) -> float: ...
    @right.setter
    def right(self, __value: _FloatSetter) -> None: ...
    @property
    def top(self) -> float: ...
    @top.setter
    def top(self, __value: _FloatSetter) -> None: ...
    @property
    def bottom(self) -> float: ...
    @bottom.setter
    def bottom(self, __value: _FloatSetter) -> None: ...
    stop: _Sequence[Stop]
    def __init__(
        self,
        type: Literal["linear", "path"] = ...,
        degree: _FloatSetter = ...,
        left: _FloatSetter = ...,
        right: _FloatSetter = ...,
        top: _FloatSetter = ...,
        bottom: _FloatSetter = ...,
        stop: _Sequence[Stop] = ...,
    ) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...
    def to_tree(  # type: ignore[override]
        self, tagname: Unused = ..., namespace: Unused = ..., idx: Unused = ...
    ) -> _Element: ...
