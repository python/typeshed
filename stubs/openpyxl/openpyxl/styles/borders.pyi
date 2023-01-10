from _typeshed import Incomplete
from collections.abc import Generator
from typing_extensions import Final, Literal, TypeAlias

from openpyxl.descriptors.serialisable import Serialisable

from .colors import Color

BORDER_NONE: None
BORDER_DASHDOT: Final = "dashDot"
BORDER_DASHDOTDOT: Final = "dashDotDot"
BORDER_DASHED: Final = "dashed"
BORDER_DOTTED: Final = "dotted"
BORDER_DOUBLE: Final = "double"
BORDER_HAIR: Final = "hair"
BORDER_MEDIUM: Final = "medium"
BORDER_MEDIUMDASHDOT: Final = "mediumDashDot"
BORDER_MEDIUMDASHDOTDOT: Final = "mediumDashDotDot"
BORDER_MEDIUMDASHED: Final = "mediumDashed"
BORDER_SLANTDASHDOT: Final = "slantDashDot"
BORDER_THICK: Final = "thick"
BORDER_THIN: Final = "thin"
_StyleType: TypeAlias = Literal[
    "dashDot",
    "dashDotDot",
    "dashed",
    "dotted",
    "double",
    "hair",
    "medium",
    "mediumDashDot",
    "mediumDashDotDot",
    "mediumDashed",
    "slantDashDot",
    "thick",
    "thin",
]

class Side(Serialisable):  # type: ignore[misc]
    __fields__: tuple[str, ...]
    color: Color | None
    style: _StyleType | None = ...
    border_style = style
    def __init__(
        self, style: _StyleType | None = ..., color: Color | None = ..., border_style: _StyleType | None = ...
    ) -> None: ...

class Border(Serialisable):
    tagname: str
    __fields__: tuple[str, ...]
    __elements__: tuple[str, ...]
    start: Side | None
    end: Side | None
    left: Side | None
    right: Side | None
    top: Side | None
    bottom: Side | None
    diagonal: Side | None
    vertical: Side | None
    horizontal: Side | None
    outline: bool
    diagonalUp: bool
    diagonalDown: bool
    diagonal_direction: Incomplete | None
    def __init__(
        self,
        left: Side | None = ...,
        right: Side | None = ...,
        top: Side | None = ...,
        bottom: Side | None = ...,
        diagonal: Side | None = ...,
        diagonal_direction: Incomplete | None = ...,
        vertical: Side | None = ...,
        horizontal: Side | None = ...,
        diagonalUp: bool = ...,
        diagonalDown: bool = ...,
        outline: bool = ...,
        start: Side | None = ...,
        end: Side | None = ...,
    ) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...

DEFAULT_BORDER: Border
