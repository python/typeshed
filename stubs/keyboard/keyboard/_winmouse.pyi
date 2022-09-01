from _typeshed import Incomplete
from collections.abc import Callable
from ctypes import (
    Structure,
    WinDLL,
    c_char as c_char,
    c_int,
    c_int32,
    c_long,
    c_short as c_short,
    c_uint as c_uint,
    c_uint8 as c_uint8,
    c_uint32 as c_uint32,
)
from ctypes.wintypes import BOOL, DWORD, HHOOK, LPARAM, LPMSG as LPMSG, LPWSTR as LPWSTR, WCHAR as WCHAR, WPARAM
from queue import Queue
from typing_extensions import Literal, TypeAlias

from ._mouse_event import (
    DOUBLE as DOUBLE,
    DOWN as DOWN,
    HORIZONTAL as HORIZONTAL,
    LEFT as LEFT,
    MIDDLE as MIDDLE,
    RIGHT as RIGHT,
    UP as UP,
    VERTICAL as VERTICAL,
    WHEEL as WHEEL,
    X2 as X2,
    ButtonEvent as ButtonEvent,
    MoveEvent as MoveEvent,
    WheelEvent as WheelEvent,
    X as X,
    _MouseButton,
)

user32: WinDLL

class MSLLHOOKSTRUCT(Structure):
    x: c_long
    y: c_long
    data: c_int32
    reserved: c_int32
    flags: DWORD
    time: c_int

_POINTER_MSLLHOOKSTRUCT: TypeAlias = Incomplete  # POINTER(MSLLHOOKSTRUCT)
_LRESULT: TypeAlias = Incomplete
LowLevelMouseProc: TypeAlias = Callable[[Callable[[c_int, WPARAM, LPARAM], c_int]], _POINTER_MSLLHOOKSTRUCT]
SetWindowsHookEx: Callable[[c_int, LowLevelMouseProc, c_int, c_int], HHOOK]
CallNextHookEx: Callable[[c_int, c_int, WPARAM, LPARAM], c_int]
UnhookWindowsHookEx: Callable[[HHOOK], BOOL]
GetMessage: Callable[[LPMSG, c_int, c_int, c_int], BOOL]
TranslateMessage: Callable[[LPMSG], BOOL]
DispatchMessage: Callable[[LPMSG], _LRESULT]
WM_MOUSEMOVE: Literal[512]
WM_LBUTTONDOWN: Literal[513]
WM_LBUTTONUP: Literal[514]
WM_LBUTTONDBLCLK: Literal[515]
WM_RBUTTONDOWN: Literal[516]
WM_RBUTTONUP: Literal[517]
WM_RBUTTONDBLCLK: Literal[518]
WM_MBUTTONDOWN: Literal[519]
WM_MBUTTONUP: Literal[520]
WM_MBUTTONDBLCLK: Literal[521]
WM_MOUSEWHEEL: Literal[522]
WM_XBUTTONDOWN: Literal[523]
WM_XBUTTONUP: Literal[524]
WM_XBUTTONDBLCLK: Literal[525]
WM_NCXBUTTONDOWN: Literal[171]
WM_NCXBUTTONUP: Literal[172]
WM_NCXBUTTONDBLCLK: Literal[173]
WM_MOUSEHWHEEL: Literal[526]
buttons_by_wm_code: dict[
    int,
    tuple[Literal["down"], Literal["left"]]
    | tuple[Literal["up"], Literal["left"]]
    | tuple[Literal["double"], Literal["left"]]
    | tuple[Literal["down"], Literal["right"]]
    | tuple[Literal["up"], Literal["right"]]
    | tuple[Literal["double"], Literal["right"]]
    | tuple[Literal["down"], Literal["middle"]]
    | tuple[Literal["up"], Literal["middle"]]
    | tuple[Literal["double"], Literal["middle"]]
    | tuple[Literal["down"], Literal["x"]]
    | tuple[Literal["up"], Literal["x"]]
    | tuple[Literal["double"], Literal["x"]],
]
MOUSEEVENTF_ABSOLUTE: Literal[32768]
MOUSEEVENTF_MOVE: Literal[1]
MOUSEEVENTF_WHEEL: Literal[2048]
MOUSEEVENTF_HWHEEL: Literal[4096]
MOUSEEVENTF_LEFTDOWN: Literal[2]
MOUSEEVENTF_LEFTUP: Literal[4]
MOUSEEVENTF_RIGHTDOWN: Literal[8]
MOUSEEVENTF_RIGHTUP: Literal[16]
MOUSEEVENTF_MIDDLEDOWN: Literal[32]
MOUSEEVENTF_MIDDLEUP: Literal[64]
MOUSEEVENTF_XDOWN: Literal[128]
MOUSEEVENTF_XUP: Literal[256]
simulated_mouse_codes: dict[
    tuple[Literal["wheel"], Literal["horizontal"]]
    | tuple[Literal["wheel"], Literal["vertical"]]
    | tuple[Literal["down"], Literal["left"]]
    | tuple[Literal["up"], Literal["left"]]
    | tuple[Literal["down"], Literal["right"]]
    | tuple[Literal["up"], Literal["right"]]
    | tuple[Literal["down"], Literal["middle"]]
    | tuple[Literal["up"], Literal["middle"]]
    | tuple[Literal["down"], Literal["x"]]
    | tuple[Literal["up"], Literal["x"]],
    int,
]
NULL: c_long
WHEEL_DELTA: Literal[120]
init: Callable[[], None]

def listen(queue: Queue[MoveEvent | WheelEvent | ButtonEvent]): ...
def press(button: _MouseButton = ...) -> None: ...
def release(button: _MouseButton = ...) -> None: ...
def wheel(delta: int = ...) -> None: ...
def move_to(x: int | c_long, y: int | c_long) -> None: ...
def move_relative(x: int | c_long, y: int | c_long) -> None: ...

class POINT(Structure):
    x: c_long
    y: c_long

def get_position() -> tuple[c_long, c_long]: ...
