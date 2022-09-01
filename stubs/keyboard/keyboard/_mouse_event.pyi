import sys
from typing import NamedTuple
from typing_extensions import Literal, TypeAlias

LEFT: Literal["left"]
RIGHT: Literal["right"]
MIDDLE: Literal["middle"]
X: Literal["x"]
X2: Literal["x2"]

UP: Literal["up"]
DOWN: Literal["down"]
DOUBLE: Literal["double"]
WHEEL: Literal["wheel"]

VERTICAL: Literal["vertical"]
HORIZONTAL: Literal["horizontal"]

if sys.platform == "linux" or sys.platform == "win32":
    _MouseButton: TypeAlias = Literal["left", "right", "middle", "x", "x2"]
else:
    _MouseButton: TypeAlias = Literal["left", "right", "middle"]

if sys.platform == "win32":
    _MouseEvent: TypeAlias = Literal["up", "down", "double", "wheel"]
else:
    _MouseEvent: TypeAlias = Literal["up", "down"]

class ButtonEvent(NamedTuple):
    event_type: _MouseEvent
    button: _MouseButton
    time: float

class WheelEvent(NamedTuple):
    delta: int
    time: float

class MoveEvent(NamedTuple):
    x: int
    y: int
    time: float
