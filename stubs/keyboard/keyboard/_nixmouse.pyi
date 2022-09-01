from _typeshed import Incomplete
from ctypes import CDLL
from queue import Queue
from subprocess import check_output as check_output
from typing_extensions import Literal, TypeAlias

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
from ._nixcommon import (
    EV_ABS as EV_ABS,
    EV_KEY as EV_KEY,
    EV_MSC as EV_MSC,
    EV_REL as EV_REL,
    EV_SYN as EV_SYN,
    AggregatedEventDevice,
    EventDevice,
    aggregate_devices as aggregate_devices,
    ensure_root as ensure_root,
)

x11: CDLL | None
display: TypeAlias = Incomplete  # x11.XOpenDisplay(None)
window: TypeAlias = Incomplete  # x11.XDefaultRootWindow(display)

def build_display() -> None: ...
def get_position() -> tuple[int, int]: ...
def move_to(x, y) -> None: ...

REL_X: Literal[0]
REL_Y: Literal[1]
REL_Z: Literal[2]
REL_HWHEEL: Literal[6]
REL_WHEEL: Literal[8]

ABS_X: Literal[0]
ABS_Y: Literal[1]

BTN_MOUSE: Literal[272]
BTN_LEFT: Literal[272]
BTN_RIGHT: Literal[273]
BTN_MIDDLE: Literal[274]
BTN_SIDE: Literal[275]
BTN_EXTRA: Literal[276]

button_by_code: dict[int, str]
code_by_button: dict[str, int]
device: AggregatedEventDevice | EventDevice | None

def build_device() -> None: ...

init = build_device

def listen(queue: Queue[ButtonEvent | WheelEvent | MoveEvent]) -> None: ...
def press(button: _MouseButton = ...) -> None: ...
def release(button: _MouseButton = ...) -> None: ...
def move_relative(x: int, y: int) -> None: ...
def wheel(delta: int = ...) -> None: ...
