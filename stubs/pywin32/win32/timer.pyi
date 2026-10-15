from _typeshed import Incomplete
from collections.abc import Callable
from typing import Final

from win32.lib.pywintypes import error as error

def set_timer(Elapse: int, TimerFunc: Callable[..., Incomplete], /) -> int: ...
def kill_timer(timer_id: int, /) -> bool: ...

__version__: Final[bytes]
