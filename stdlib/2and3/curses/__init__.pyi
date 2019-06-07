from _curses import *  # noqa: F403
from typing import TypeVar, Callable, Any

_T = TypeVar('_T')

LINES: int
COLS: int

def wrapper(func: Callable[..., _T], *arg: Any, **kwds: Any) -> _T: ...
