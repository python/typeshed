import enum
import sys
from collections.abc import Callable
from types import TracebackType
from typing import Any
from typing_extensions import Self

from pynput._util import AbstractListener

class Button(enum.Enum):
    unknown = 0
    left = 1
    middle = 2
    right = 3
    if sys.platform == "linux":
        button8 = 0
        button9 = 0
        button10 = 0
        button11 = 0
        button12 = 0
        button13 = 0
        button14 = 0
        button15 = 0
        button16 = 0
        button17 = 0
        button18 = 0
        button19 = 0
        button20 = 0
        button21 = 0
        button22 = 0
        button23 = 0
        button24 = 0
        button25 = 0
        button26 = 0
        button27 = 0
        button28 = 0
        button29 = 0
        button30 = 0
        scroll_down = 0
        scroll_left = 0
        scroll_right = 0
        scroll_up = 0
    if sys.platform == "win32":
        x1 = 0
        x2 = 0

class Controller:
    def __init__(self) -> None: ...
    @property
    def position(self) -> tuple[int, int]: ...
    @position.setter
    def position(self, position: tuple[int, int]) -> None: ...
    def scroll(self, dx: int, dy: int) -> None: ...
    def press(self, button: Button) -> None: ...
    def release(self, button: Button) -> None: ...
    def move(self, dx: int, dy: int) -> None: ...
    def click(self, button: Button, count: int = 1) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class Listener(AbstractListener):
    if sys.platform == "win32":
        WM_LBUTTONDOWN: int
        WM_LBUTTONUP: int
        WM_MBUTTONDOWN: int
        WM_MBUTTONUP: int
        WM_MOUSEMOVE: int
        WM_MOUSEWHEEL: int
        WM_MOUSEHWHEEL: int
        WM_RBUTTONDOWN: int
        WM_RBUTTONUP: int
        WM_XBUTTONDOWN: int
        WM_XBUTTONUP: int

        MK_XBUTTON1: int
        MK_XBUTTON2: int

        XBUTTON1: int
        XBUTTON2: int

        CLICK_BUTTONS: dict[int, tuple[Button, bool]]
        X_BUTTONS: dict[int, dict[int, tuple[Button, bool]]]
        SCROLL_BUTTONS: dict[int, tuple[int, int]]

    def __init__(
        self,
        on_move: Callable[[int, int], bool | None] | None = None,
        on_click: Callable[[int, int, Button, bool], bool | None] | None = None,
        on_scroll: Callable[[int, int, int, int], bool | None] | None = None,
        suppress: bool = False,
        **kwargs: Any,
    ) -> None: ...
