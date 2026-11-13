from _typeshed import FloatInt
import contextlib
from _typeshed import ConvertibleToInt
from collections.abc import Callable, Iterable, Sequence
from datetime import datetime
from typing import Final, NamedTuple, ParamSpec, SupportsIndex, SupportsInt, TypeAlias, TypeVar

from pyscreeze import (
    center as center,
    locate as locate,
    locateAll as locateAll,
    locateAllOnScreen as locateAllOnScreen,
    locateCenterOnScreen as locateCenterOnScreen,
    locateOnScreen as locateOnScreen,
    locateOnWindow as locateOnWindow,
    pixel as pixel,
    pixelMatchesColor as pixelMatchesColor,
    screenshot as screenshot,
)

_P = ParamSpec("_P")
_R = TypeVar("_R")
# Explicitly mentioning str despite being in the ConvertibleToInt Alias because it has a different meaning (filename on screen)
# Specifying non-None Y arg when X is a string or sequence raises an error
# TODO: This could be better represented through overloads
_NormalizeableXArg: TypeAlias = str | ConvertibleToInt | Sequence[ConvertibleToInt]

# Constants
KEY_NAMES: list[str]
KEYBOARD_KEYS: list[str]
LEFT: Final = "left"
MIDDLE: Final = "middle"
RIGHT: Final = "right"
PRIMARY: Final = "primary"
SECONDARY: Final = "secondary"
G_LOG_SCREENSHOTS_FILENAMES: list[str]
# Implementation details
QWERTY: Final[str]
QWERTZ: Final[str]
MINIMUM_SLEEP: Final[FloatInt]

# These are meant to be overridable
LOG_SCREENSHOTS: bool
LOG_SCREENSHOTS_LIMIT: int | None
# https://pyautogui.readthedocs.io/en/latest/index.html#fail-safes
FAILSAFE: bool
PAUSE: FloatInt
DARWIN_CATCH_UP_TIME: FloatInt
FAILSAFE_POINTS: list[tuple[int, int]]
# https://pyautogui.readthedocs.io/en/latest/mouse.htmln#mouse-movement
MINIMUM_DURATION: FloatInt

class PyAutoGUIException(Exception): ...
class FailSafeException(PyAutoGUIException): ...
class ImageNotFoundException(PyAutoGUIException): ...

def raisePyAutoGUIImageNotFoundException(wrappedFunction: Callable[_P, _R]) -> Callable[_P, _R]: ...
def mouseInfo() -> None: ...
def useImageNotFoundException(value: bool | None = None) -> None: ...
def isShiftCharacter(character: str) -> bool: ...

class Point(NamedTuple):
    x: int
    y: int

class Size(NamedTuple):
    width: int
    height: int

def getPointOnLine(x1: FloatInt, y1: FloatInt, x2: FloatInt, y2: FloatInt, n: FloatInt) -> tuple[float, float]: ...
def linear(n: FloatInt) -> float: ...
def position(x: int | None = None, y: int | None = None) -> Point: ...
def size() -> Size: ...

resolution = size

def onScreen(x: _NormalizeableXArg | None, y: SupportsInt | None = None) -> bool: ...
def mouseDown(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    # Docstring says `button` can also be `int`, but `.lower()` is called unconditionally in `_normalizeButton()`
    button: str = "primary",
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def mouseUp(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    # Docstring says `button` can also be `int`, but `.lower()` is called unconditionally in `_normalizeButton()`
    button: str = "primary",
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def click(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    clicks: SupportsIndex = 1,
    interval: FloatInt = 0.0,
    # Docstring says `button` can also be `int`, but `.lower()` is called unconditionally in `_normalizeButton()`
    button: str = "primary",
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def leftClick(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    interval: FloatInt = 0.0,
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def rightClick(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    interval: FloatInt = 0.0,
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def middleClick(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    interval: FloatInt = 0.0,
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def doubleClick(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    interval: FloatInt = 0.0,
    # Docstring says `button` can also be `int`, but `.lower()` is called unconditionally in `_normalizeButton()`
    button: str = "left",
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def tripleClick(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    interval: FloatInt = 0.0,
    # Docstring says `button` can also be `int`, but `.lower()` is called unconditionally in `_normalizeButton()`
    button: str = "left",
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def scroll(
    clicks: FloatInt,
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def hscroll(
    clicks: FloatInt,
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def vscroll(
    clicks: FloatInt,
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def moveTo(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool = False,
    _pause: bool = True,
) -> None: ...
def moveRel(
    xOffset: _NormalizeableXArg | None = None,
    yOffset: SupportsInt | None = None,
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    logScreenshot: bool = False,
    _pause: bool = True,
) -> None: ...

move = moveRel

def dragTo(
    x: _NormalizeableXArg | None = None,
    y: SupportsInt | None = None,
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    # Docstring says `button` can also be `int`, but `.lower()` is called unconditionally in `_normalizeButton()`
    button: str = "primary",
    logScreenshot: bool | None = None,
    _pause: bool = True,
    mouseDownUp: bool = True,
) -> None: ...
def dragRel(
    xOffset: _NormalizeableXArg | None = 0,
    yOffset: SupportsInt | None = 0,
    duration: FloatInt = 0.0,
    tween: Callable[[FloatInt], float] = ...,
    # Docstring says `button` can also be `int`, but `.lower()` is called unconditionally in `_normalizeButton()`
    button: str = "primary",
    logScreenshot: bool | None = None,
    _pause: bool = True,
    mouseDownUp: bool = True,
) -> None: ...

drag = dragRel

def isValidKey(key: str) -> bool: ...
def keyDown(key: str, logScreenshot: bool | None = None, _pause: bool = True) -> None: ...
def keyUp(key: str, logScreenshot: bool | None = None, _pause: bool = True) -> None: ...
def press(
    keys: str | Iterable[str],
    presses: SupportsIndex = 1,
    interval: FloatInt = 0.0,
    logScreenshot: bool | None = None,
    _pause: bool = True,
) -> None: ...
def hold(
    keys: str | Iterable[str], logScreenshot: bool | None = None, _pause: bool = True
) -> contextlib._GeneratorContextManager[None]: ...
def typewrite(
    message: str | Sequence[str], interval: FloatInt = 0.0, logScreenshot: bool | None = None, _pause: bool = True
) -> None: ...

write = typewrite

def hotkey(*args: str, logScreenshot: bool | None = None, interval: FloatInt = 0.0) -> None: ...

shortcut = hotkey

def failSafeCheck() -> None: ...
def displayMousePosition(xOffset: FloatInt = 0, yOffset: FloatInt = 0) -> None: ...
def sleep(seconds: FloatInt) -> None: ...
def countdown(seconds: SupportsIndex) -> None: ...
def run(commandStr: str, _ssCount: Sequence[int] | None = None) -> None: ...
def printInfo(dontPrint: bool = False) -> str: ...
def getInfo() -> tuple[str, str, str, str, Size, datetime]: ...
