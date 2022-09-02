import sys
from collections.abc import Callable, Sequence
from ctypes import c_long
from typing import Tuple  # noqa: Y022 # Arbitrary length Tuple
from typing_extensions import Literal, ParamSpec, TypeAlias

from ._generic import GenericListener as _GenericListener
from ._mouse_event import (
    DOUBLE as DOUBLE,
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
    _MouseEvent,
)

_P = ParamSpec("_P")
_Callback: TypeAlias = Callable[[ButtonEvent | WheelEvent | MoveEvent], bool | None]

class _MouseListener(_GenericListener):
    def init(self) -> None: ...
    def pre_process_event(  # type: ignore[override]  # Mouse specific events and return
        self, event: ButtonEvent | MoveEvent | WheelEvent
    ) -> Literal[True]: ...
    def listen(self) -> None: ...

def is_pressed(button: _MouseButton = ...): ...
def press(button: _MouseButton = ...) -> None: ...
def release(button: _MouseButton = ...) -> None: ...
def click(button: _MouseButton = ...) -> None: ...
def double_click(button: _MouseButton = ...) -> None: ...
def right_click() -> None: ...
def wheel(delta: int = ...) -> None: ...
def move(x: int | c_long, y: int | c_long, absolute: bool = ..., duration: float = ...) -> None: ...
def drag(start_x: int, start_y: int, end_x: int, end_y: int, absolute: bool = ..., duration: float = ...) -> None: ...

# TODO: how to make args: _P.args ?
_P_args: TypeAlias = tuple[object, ...]

def on_button(
    callback: Callable[_P, None],
    args: _P_args = ...,
    buttons: list[_MouseButton] | Tuple[_MouseButton, ...] | _MouseButton = ...,
    types: list[_MouseEvent] | Tuple[_MouseEvent, ...] | _MouseEvent = ...,
) -> _Callback: ...
def on_click(callback: Callable[_P, None], args: _P_args = ...) -> _Callback: ...
def on_double_click(callback: Callable[_P, None], args: _P_args = ...) -> _Callback: ...
def on_right_click(callback: Callable[_P, None], args: _P_args = ...) -> _Callback: ...
def on_middle_click(callback: Callable[_P, None], args: _P_args = ...) -> _Callback: ...
def wait(button: _MouseButton = ..., target_types: tuple[_MouseEvent] = ...) -> None: ...

if sys.platform == "win32":
    def get_position() -> tuple[c_long, c_long]: ...

else:
    def get_position() -> tuple[int, int]: ...

def hook(callback: _Callback) -> _Callback: ...
def unhook(callback: _Callback) -> None: ...
def unhook_all() -> None: ...
def record(button: _MouseButton = ..., target_types: tuple[_MouseEvent] = ...) -> ButtonEvent | WheelEvent | MoveEvent: ...
def play(
    events: Sequence[ButtonEvent | WheelEvent | MoveEvent],
    speed_factor: float = ...,
    include_clicks: bool = ...,
    include_moves: bool = ...,
    include_wheel: bool = ...,
) -> None: ...

replay = play
hold = press
