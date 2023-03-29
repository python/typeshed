from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import NoneSet, Typed
from openpyxl.descriptors.serialisable import Serialisable

BORDER_NONE: Incomplete
BORDER_DASHDOT: str
BORDER_DASHDOTDOT: str
BORDER_DASHED: str
BORDER_DOTTED: str
BORDER_DOUBLE: str
BORDER_HAIR: str
BORDER_MEDIUM: str
BORDER_MEDIUMDASHDOT: str
BORDER_MEDIUMDASHDOTDOT: str
BORDER_MEDIUMDASHED: str
BORDER_SLANTDASHDOT: str
BORDER_THICK: str
BORDER_THIN: str

class Side(Serialisable):  # type: ignore[misc]
    __fields__: Incomplete
    color: Incomplete
    style: NoneSet(
        values=(
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
        )
    )
    border_style: Incomplete
    def __init__(
        self, style: Incomplete | None = None, color: Incomplete | None = None, border_style: Incomplete | None = None
    ) -> None: ...

class Border(Serialisable):
    tagname: str
    __fields__: Incomplete
    __elements__: Incomplete
    start: Typed[Side, Literal[True]]
    end: Typed[Side, Literal[True]]
    left: Typed[Side, Literal[True]]
    right: Typed[Side, Literal[True]]
    top: Typed[Side, Literal[True]]
    bottom: Typed[Side, Literal[True]]
    diagonal: Typed[Side, Literal[True]]
    vertical: Typed[Side, Literal[True]]
    horizontal: Typed[Side, Literal[True]]
    outline: Incomplete
    diagonalUp: Incomplete
    diagonalDown: Incomplete
    diagonal_direction: Incomplete
    def __init__(
        self,
        left: Side | None = None,
        right: Side | None = None,
        top: Side | None = None,
        bottom: Side | None = None,
        diagonal: Side | None = None,
        diagonal_direction: Incomplete | None = None,
        vertical: Side | None = None,
        horizontal: Side | None = None,
        diagonalUp: bool = False,
        diagonalDown: bool = False,
        outline: bool = True,
        start: Side | None = None,
        end: Side | None = None,
    ) -> None: ...
    def __iter__(self): ...

DEFAULT_BORDER: Incomplete
