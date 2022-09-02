from _typeshed import Incomplete
from collections.abc import Callable
from queue import Queue
from typing import TypeVar
from typing_extensions import TypeAlias

from ._keyboard_event import KeyboardEvent
from ._mouse_event import (
    DOWN as DOWN,
    LEFT as LEFT,
    MIDDLE as MIDDLE,
    RIGHT as RIGHT,
    UP as UP,
    X2 as X2,
    ButtonEvent as ButtonEvent,
    MoveEvent as MoveEvent,
    WheelEvent as WheelEvent,
    X as X,
    _MouseButton,
)

_Unused: TypeAlias = object

# https://github.com/ronaldoussoren/pyobjc/milestone/3
_CGEventTap: TypeAlias = Incomplete  # Quartz.CGEventTap
_KCGEventKey: TypeAlias = Incomplete  # Quartz.kCGEventKey
_T = TypeVar("_T")

class MouseEventListener:
    blocking: bool
    callback: Callable[[KeyboardEvent], None]
    listening: bool
    def __init__(self, callback: Callable[[KeyboardEvent], None], blocking: bool = ...) -> None: ...
    tap: _CGEventTap
    def run(self) -> None: ...
    def handler(self, proxy: _Unused, e_type: _KCGEventKey, event: _T, refcon: _Unused) -> _T: ...

def init() -> None: ...
def listen(queue: Queue[KeyboardEvent]) -> None: ...
def press(button: _MouseButton = ...) -> None: ...
def release(button: _MouseButton = ...) -> None: ...
def wheel(delta: int = ...) -> None: ...
def move_to(x: int, y: int) -> None: ...
def get_position() -> tuple[int, int]: ...
