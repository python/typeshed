from _typeshed import Incomplete
import ctypes
import ctypes.wintypes
from typing_extensions import TypeAlias
from pyautogui import LEFT as LEFT, MIDDLE as MIDDLE, RIGHT as RIGHT

_Pointer: TypeAlias = Incomplete


MOUSEEVENTF_MOVE: int
MOUSEEVENTF_LEFTDOWN: int
MOUSEEVENTF_LEFTUP: int
MOUSEEVENTF_LEFTCLICK: int
MOUSEEVENTF_RIGHTDOWN: int
MOUSEEVENTF_RIGHTUP: int
MOUSEEVENTF_RIGHTCLICK: int
MOUSEEVENTF_MIDDLEDOWN: int
MOUSEEVENTF_MIDDLEUP: int
MOUSEEVENTF_MIDDLECLICK: int
MOUSEEVENTF_ABSOLUTE: int
MOUSEEVENTF_WHEEL: int
MOUSEEVENTF_HWHEEL: int
KEYEVENTF_KEYDOWN: int
KEYEVENTF_KEYUP: int
INPUT_MOUSE: int
INPUT_KEYBOARD: int


class MOUSEINPUT(ctypes.Structure):
    dx: ctypes.wintypes.LONG
    dy: ctypes.wintypes.LONG
    mouseData: ctypes.wintypes.DWORD
    dwFlags: ctypes.wintypes.DWORD
    time: ctypes.wintypes.DWORD
    dwExtraInfo: _Pointer


class KEYBDINPUT(ctypes.Structure):
    wVk: ctypes.wintypes.WORD
    wScan: ctypes.wintypes.WORD
    dwFlags: ctypes.wintypes.DWORD
    time: ctypes.wintypes.DWORD
    dwExtraInfo: _Pointer


class HARDWAREINPUT(ctypes.Structure):
    uMsg: ctypes.wintypes.DWORD
    wParamL: ctypes.wintypes.WORD
    wParamH: ctypes.wintypes.DWORD


class INPUT(ctypes.Structure):
    class _I(ctypes.Union):
        mi: MOUSEINPUT
        ki: KEYBDINPUT
        hi: HARDWAREINPUT

    mi: MOUSEINPUT
    ki: KEYBDINPUT
    hi: HARDWAREINPUT
    type: ctypes.wintypes.DWORD
    i: _I


keyboardMapping: dict[str, int]
