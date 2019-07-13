from _curses import *  # noqa: F403
from typing import TypeVar, Callable, Any

_T = TypeVar('_T')

# available after calling `curses.initscr()`
LINES: int
COLS: int

# available after calling `curses.init_colors()`
COLORS: int
COLOR_PAIRS: int

def wrapper(func: Callable[..., _T], *arg: Any, **kwds: Any) -> _T: ...
