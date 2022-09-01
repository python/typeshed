from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Callable, Generator, Sequence
from ctypes import (
    Array,
    Structure,
    Union,
    WinDLL,
    c_char as c_char,
    c_int,
    c_int32 as c_int32,
    c_long,
    c_short,
    c_uint,
    c_uint8,
    c_uint32 as c_uint32,
    c_wchar,
)
from ctypes.wintypes import (
    BOOL,
    DWORD,
    HHOOK,
    HMODULE,
    LONG,
    LPARAM,
    LPCWSTR,
    LPDWORD,
    LPMSG as LPMSG,
    LPWSTR,
    WCHAR,
    WORD,
    WPARAM,
)
from threading import Lock
from typing import Tuple
from typing_extensions import Literal, TypeAlias

from ._canonical_names import normalize_name as normalize_name
from ._keyboard_event import KEY_DOWN as KEY_DOWN, KEY_UP as KEY_UP, KeyboardEvent as KeyboardEvent

ULONG_PTR: TypeAlias = LPDWORD
kernel32: WinDLL
GetModuleHandleW: Callable[[LPCWSTR | None], HMODULE]
user32: WinDLL
VK_PACKET: Literal[231]
INPUT_MOUSE: Literal[0]
INPUT_KEYBOARD: Literal[1]
INPUT_HARDWARE: Literal[2]
KEYEVENTF_KEYUP: Literal[2]
KEYEVENTF_UNICODE: Literal[4]

class KBDLLHOOKSTRUCT(Structure):
    vk_code: DWORD
    scan_code: DWORD
    flags: DWORD
    time: c_int
    dwExtraInfo: ULONG_PTR

class MOUSEINPUT(Structure):
    dx: LONG
    dy: LONG
    mouseData: DWORD
    dwFlags: DWORD
    time: DWORD
    dwExtraInfo: ULONG_PTR

class KEYBDINPUT(Structure):
    wVk: WORD
    wScan: WORD
    dwFlags: DWORD
    time: DWORD
    dwExtraInfo: ULONG_PTR

class HARDWAREINPUT(Structure):
    uMsg: DWORD
    wParamL: WORD
    wParamH: WORD

class _INPUTunion(Union):
    mi: MOUSEINPUT
    ki: KEYBDINPUT
    hi: HARDWAREINPUT

class INPUT(Structure):
    type: DWORD
    union: _INPUTunion

_POINTER_KBDLLHOOKSTRUCT: TypeAlias = Incomplete  # POINTER(KBDLLHOOKSTRUCT)
_LRESULT: TypeAlias = Incomplete
_POINTER_INPUT: TypeAlias = Incomplete  # POINTER(INPUT)
_LowLevelKeyboardProc: TypeAlias = Callable[[Callable[[c_int, WPARAM, LPARAM], c_int]], _POINTER_KBDLLHOOKSTRUCT]
LowLevelKeyboardProc: _LowLevelKeyboardProc
SetWindowsHookEx: Callable[[c_int, _LowLevelKeyboardProc, c_int, c_int], HHOOK]
CallNextHookEx: Callable[[c_int, c_int, WPARAM, LPARAM], c_int]
UnhookWindowsHookEx: Callable[[HHOOK], BOOL]
GetMessage: Callable[[LPMSG, c_int, c_int, c_int], BOOL]
TranslateMessage: Callable[[LPMSG], BOOL]
DispatchMessage: Callable[[LPMSG], _LRESULT]
_keyboard_state_type: TypeAlias = Array[c_uint8]
keyboard_state_type: _keyboard_state_type
GetKeyboardState: Callable[[_keyboard_state_type], BOOL]
GetKeyNameText: Callable[[c_long, LPWSTR, c_int], c_int]
MapVirtualKey: Callable[[c_uint, c_uint], c_uint]
ToUnicode: Callable[[c_uint, c_uint, _keyboard_state_type, LPWSTR, c_int, c_uint], c_int]
SendInput: Callable[[c_uint, _POINTER_INPUT, c_int], c_uint]
MAPVK_VK_TO_CHAR: Literal[2]
MAPVK_VK_TO_VSC: Literal[0]
MAPVK_VSC_TO_VK: Literal[1]
MAPVK_VK_TO_VSC_EX: Literal[4]
MAPVK_VSC_TO_VK_EX: Literal[3]
VkKeyScan: Callable[[WCHAR], c_short]
LLKHF_INJECTED: Literal[16]

WM_KEYDOWN: Literal[256]
WM_KEYUP: Literal[257]
WM_SYSKEYDOWN: Literal[260]
WM_SYSKEYUP: Literal[261]
keyboard_event_types: dict[int, str]
official_virtual_keys: dict[
    int,
    tuple[Literal["control-break processing"], Literal[False]]
    | tuple[Literal["backspace"], Literal[False]]
    | tuple[Literal["tab"], Literal[False]]
    | tuple[Literal["clear"], Literal[False]]
    | tuple[Literal["enter"], Literal[False]]
    | tuple[Literal["shift"], Literal[False]]
    | tuple[Literal["ctrl"], Literal[False]]
    | tuple[Literal["alt"], Literal[False]]
    | tuple[Literal["pause"], Literal[False]]
    | tuple[Literal["caps lock"], Literal[False]]
    | tuple[Literal["ime kana mode"], Literal[False]]
    | tuple[Literal["ime hanguel mode"], Literal[False]]
    | tuple[Literal["ime hangul mode"], Literal[False]]
    | tuple[Literal["ime junja mode"], Literal[False]]
    | tuple[Literal["ime final mode"], Literal[False]]
    | tuple[Literal["ime hanja mode"], Literal[False]]
    | tuple[Literal["ime kanji mode"], Literal[False]]
    | tuple[Literal["esc"], Literal[False]]
    | tuple[Literal["ime convert"], Literal[False]]
    | tuple[Literal["ime nonconvert"], Literal[False]]
    | tuple[Literal["ime accept"], Literal[False]]
    | tuple[Literal["ime mode change request"], Literal[False]]
    | tuple[Literal["spacebar"], Literal[False]]
    | tuple[Literal["page up"], Literal[False]]
    | tuple[Literal["page down"], Literal[False]]
    | tuple[Literal["end"], Literal[False]]
    | tuple[Literal["home"], Literal[False]]
    | tuple[Literal["left"], Literal[False]]
    | tuple[Literal["up"], Literal[False]]
    | tuple[Literal["right"], Literal[False]]
    | tuple[Literal["down"], Literal[False]]
    | tuple[Literal["select"], Literal[False]]
    | tuple[Literal["print"], Literal[False]]
    | tuple[Literal["execute"], Literal[False]]
    | tuple[Literal["print screen"], Literal[False]]
    | tuple[Literal["insert"], Literal[False]]
    | tuple[Literal["delete"], Literal[False]]
    | tuple[Literal["help"], Literal[False]]
    | tuple[Literal["0"], Literal[False]]
    | tuple[Literal["1"], Literal[False]]
    | tuple[Literal["2"], Literal[False]]
    | tuple[Literal["3"], Literal[False]]
    | tuple[Literal["4"], Literal[False]]
    | tuple[Literal["5"], Literal[False]]
    | tuple[Literal["6"], Literal[False]]
    | tuple[Literal["7"], Literal[False]]
    | tuple[Literal["8"], Literal[False]]
    | tuple[Literal["9"], Literal[False]]
    | tuple[Literal["a"], Literal[False]]
    | tuple[Literal["b"], Literal[False]]
    | tuple[Literal["c"], Literal[False]]
    | tuple[Literal["d"], Literal[False]]
    | tuple[Literal["e"], Literal[False]]
    | tuple[Literal["f"], Literal[False]]
    | tuple[Literal["g"], Literal[False]]
    | tuple[Literal["h"], Literal[False]]
    | tuple[Literal["i"], Literal[False]]
    | tuple[Literal["j"], Literal[False]]
    | tuple[Literal["k"], Literal[False]]
    | tuple[Literal["l"], Literal[False]]
    | tuple[Literal["m"], Literal[False]]
    | tuple[Literal["n"], Literal[False]]
    | tuple[Literal["o"], Literal[False]]
    | tuple[Literal["p"], Literal[False]],
]
tables_lock: Lock
to_name: defaultdict[tuple[int, int, int, str | int | Tuple[str, ...]] | tuple[int, int, int, int, int], list[str]]
from_name: defaultdict[str, list[tuple[int, Tuple[str | int | Tuple[str, ...], ...]]]]
scan_code_to_vk: dict[int, int]
distinct_modifiers: list[
    tuple[()]
    | tuple[Literal["shift"]]
    | tuple[Literal["alt gr"]]
    | tuple[Literal["num lock"]]
    | tuple[Literal["shift"], Literal["num lock"]]
    | tuple[Literal["caps lock"]]
    | tuple[Literal["shift"], Literal["caps lock"]]
    | tuple[Literal["alt gr"], Literal["num lock"]]
]
name_buffer: Array[c_wchar]
unicode_buffer: Array[c_wchar]
keyboard_state: _keyboard_state_type

def get_event_names(
    scan_code: int, vk: int, is_extended: Literal[0, 1], modifiers: Sequence[str]
) -> Generator[str, None, None]: ...

init: Callable[[], None]
keypad_keys: list[
    tuple[Literal[126], Literal[194], Literal[0]]
    | tuple[Literal[28], Literal[13], Literal[1]]
    | tuple[Literal[53], Literal[111], Literal[1]]
    | tuple[Literal[55], Literal[106], Literal[0]]
    | tuple[Literal[69], Literal[144], Literal[1]]
    | tuple[Literal[71], Literal[103], Literal[0]]
    | tuple[Literal[71], Literal[36], Literal[0]]
    | tuple[Literal[72], Literal[104], Literal[0]]
    | tuple[Literal[72], Literal[38], Literal[0]]
    | tuple[Literal[73], Literal[105], Literal[0]]
    | tuple[Literal[73], Literal[33], Literal[0]]
    | tuple[Literal[74], Literal[109], Literal[0]]
    | tuple[Literal[75], Literal[100], Literal[0]]
    | tuple[Literal[75], Literal[37], Literal[0]]
    | tuple[Literal[76], Literal[101], Literal[0]]
    | tuple[Literal[76], Literal[12], Literal[0]]
    | tuple[Literal[77], Literal[102], Literal[0]]
    | tuple[Literal[77], Literal[39], Literal[0]]
    | tuple[Literal[78], Literal[107], Literal[0]]
    | tuple[Literal[79], Literal[35], Literal[0]]
    | tuple[Literal[79], Literal[97], Literal[0]]
    | tuple[Literal[80], Literal[40], Literal[0]]
    | tuple[Literal[80], Literal[98], Literal[0]]
    | tuple[Literal[81], Literal[34], Literal[0]]
    | tuple[Literal[81], Literal[99], Literal[0]]
    | tuple[Literal[82], Literal[45], Literal[0]]
    | tuple[Literal[82], Literal[96], Literal[0]]
    | tuple[Literal[83], Literal[110], Literal[0]]
    | tuple[Literal[83], Literal[46], Literal[0]]
]
shift_is_pressed: bool
altgr_is_pressed: bool
ignore_next_right_alt: bool
shift_vks: set[int]

def prepare_intercept(callback: Callable[[KeyboardEvent], bool]) -> None: ...
def listen(callback: Callable[[KeyboardEvent], bool]) -> None: ...
def map_name(name: str) -> Generator[tuple[int, str | int | Tuple[str, ...]], None, None]: ...
def press(code: int) -> None: ...
def release(code: int) -> None: ...
def type_unicode(character: str) -> None: ...
