import _curses
from _curses import *  # noqa: F403
from typing import Callable, Any, Sequence, Mapping

LINES: int
COLS: int

LINES: int
COLS: int

def initscr() -> _curses._CursesWindow: ...
def start_color() -> None: ...
def wrapper(func: Callable, *args: Sequence[Any], **kwds: Mapping[Any, Any]) -> None: ...
