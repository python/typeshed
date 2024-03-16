import sys
from collections.abc import Callable
from typing import TypeVar
from typing_extensions import Concatenate, ParamSpec

if sys.platform != "win32":
    from _curses import *
    from _curses import _CursesWindow as _CursesWindow

    _T = TypeVar("_T")
    _P = ParamSpec("_P")

    # available after calling `curses.initscr()`
    LINES: int
    COLS: int

    # available after calling `curses.start_color()`
    COLORS: int
    COLOR_PAIRS: int

    def wrapper(func: Callable[Concatenate[_CursesWindow, _P], _T], /, *arg: _P.args, **kwds: _P.kwargs) -> _T: ...
