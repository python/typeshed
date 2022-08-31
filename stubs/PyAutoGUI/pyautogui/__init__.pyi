import collections.abc
from _typeshed import Incomplete
from collections.abc import Callable, Generator
from datetime import datetime
from typing import NamedTuple, TypeVar, overload
from typing_extensions import ParamSpec

# from pyscreeze import Box

class PyAutoGUIException(Exception): ...
class FailSafeException(PyAutoGUIException): ...
class ImageNotFoundException(PyAutoGUIException): ...

collectionsSequence = collections.abc.Sequence

_P = ParamSpec("_P")
_R = TypeVar("_R")

# TODO: Complete types with pyscreeze once we can import non-types dependencies
# See: https://github.com/python/typeshed/issues/5768

class _Box(NamedTuple):
    left: int
    top: int
    width: int
    height: int

def raisePyAutoGUIImageNotFoundException(wrappedFunction: Callable[_P, _R]) -> Callable[_P, _R]: ...
def locate(*args: Incomplete, **kwargs: Incomplete) -> _Box | None: ...
def locateAll(*args: Incomplete, **kwargs: Incomplete) -> Generator[_Box, None, None]: ...
def locateAllOnScreen(*args: Incomplete, **kwargs: Incomplete) -> Generator[_Box, None, None]: ...
def locateCenterOnScreen(*args: Incomplete, **kwargs: Incomplete) -> Point | None: ...
def locateOnScreen(*args: Incomplete, **kwargs: Incomplete) -> _Box | None: ...
def locateOnWindow(*args: Incomplete, **kwargs: Incomplete) -> _Box | None: ...
def mouseInfo() -> None: ...
def useImageNotFoundException(value: bool | None = ...) -> None: ...

KEY_NAMES: list[str]
KEYBOARD_KEYS: list[str]
LEFT: str
MIDDLE: str
RIGHT: str
PRIMARY: str
SECONDARY: str
QWERTY: str
QWERTZ: str

def isShiftCharacter(character: str) -> bool: ...

MINIMUM_DURATION: float
MINIMUM_SLEEP: float
PAUSE: float
DARWIN_CATCH_UP_TIME: float
FAILSAFE: bool
FAILSAFE_POINTS: list[tuple[int, int]]
LOG_SCREENSHOTS: bool
LOG_SCREENSHOTS_LIMIT: int
G_LOG_SCREENSHOTS_FILENAMES: list[str]

class Point(NamedTuple):
    x: float
    y: float

class Size(NamedTuple):
    width: int
    height: int

def getPointOnLine(x1: float, y1: float, x2: float, y2: float, n: float) -> tuple[float, float]: ...
def linear(n: float) -> float: ...
def position(x: int | None = ..., y: int | None = ...) -> Point: ...
def size() -> Size: ...
@overload
def onScreen(xy: tuple[float, float]) -> bool: ...
@overload
def onScreen(x: float, y: float) -> bool: ...
def mouseDown(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    button: str = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def mouseUp(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    button: str = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def click(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    clicks: int = ...,
    interval: float = ...,
    button: str = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def leftClick(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    interval: float = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def rightClick(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    interval: float = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def middleClick(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    interval: float = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def doubleClick(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    interval: float = ...,
    button: str = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def tripleClick(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    interval: float = ...,
    button: str = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def scroll(
    clicks: float,
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def hscroll(
    clicks: float,
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def vscroll(
    clicks: float,
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
) -> None: ...
def moveTo(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool = ...,
    _pause: bool = ...,
) -> None: ...
def moveRel(
    xOffset: float | collectionsSequence[int] | None = ...,
    yOffset: float | collectionsSequence[int] | None = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    logScreenshot: bool = ...,
    _pause: bool = ...,
) -> None: ...

move = moveRel

def dragTo(
    x: float | collectionsSequence[int] | None = ...,
    y: float | collectionsSequence[int] | None = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    button: str = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
    mouseDownUp: bool = ...,
) -> None: ...
def dragRel(
    xOffset: float | collectionsSequence[int] = ...,
    yOffset: float | collectionsSequence[int] = ...,
    duration: float = ...,
    tween: Callable[[float], float] = ...,
    button: str = ...,
    logScreenshot: bool | None = ...,
    _pause: bool = ...,
    mouseDownUp: bool = ...,
) -> None: ...

drag = dragRel

def isValidKey(key: str) -> bool: ...
def keyDown(key: str, logScreenshot: bool | None = ..., _pause: bool = ...) -> None: ...
def keyUp(key: str, logScreenshot: bool | None = ..., _pause: bool = ...) -> None: ...
def press(
    keys: str | list[str], presses: int = ..., interval: float = ..., logScreenshot: bool | None = ..., _pause: bool = ...
) -> None: ...
def hold(keys: str | list[str], logScreenshot: bool | None = ..., _pause: bool = ...) -> Generator[None, None, None]: ...
def typewrite(message: str | list[str], interval: float = ..., logScreenshot: bool | None = ..., _pause: bool = ...) -> None: ...

write = typewrite

def hotkey(*args: str, **kwargs: float | bool | None) -> None: ...
def failSafeCheck() -> None: ...
def displayMousePosition(xOffset: float = ..., yOffset: float = ...) -> None: ...
def sleep(seconds: int) -> None: ...
def countdown(seconds: int) -> None: ...
def run(commandStr: str, _ssCount: list[int] | None = ...) -> None: ...
def printInfo(dontPrint: bool = ...) -> str: ...
def getInfo() -> tuple[str, str, str, str, Size, datetime]: ...
