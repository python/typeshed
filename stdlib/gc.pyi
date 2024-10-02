import sys
from collections.abc import Callable
from typing import Any, Final, Literal
from typing_extensions import TypeAlias

DEBUG_COLLECTABLE: Final = 2
DEBUG_LEAK: Final = 38
DEBUG_SAVEALL: Final = 32
DEBUG_STATS: Final = 1
DEBUG_UNCOLLECTABLE: Final = 4

_CallbackType: TypeAlias = Callable[[Literal["start", "stop"], dict[str, int]], object]

callbacks: list[_CallbackType]
garbage: list[Any]

def collect(generation: int = 2) -> int: ...
def disable() -> None: ...
def enable() -> None: ...
def get_count() -> tuple[int, int, int]: ...
def get_debug() -> int: ...
def get_objects(generation: int | None = None) -> list[Any]: ...
def freeze() -> None: ...
def unfreeze() -> None: ...
def get_freeze_count() -> int: ...
def get_referents(*objs: Any) -> list[Any]: ...
def get_referrers(*objs: Any) -> list[Any]: ...
def get_stats() -> list[dict[str, Any]]: ...
def get_threshold() -> tuple[int, int, int]: ...
def is_tracked(obj: Any, /) -> bool: ...

if sys.version_info >= (3, 9):
    def is_finalized(obj: Any, /) -> bool: ...

def isenabled() -> bool: ...
def set_debug(flags: int, /) -> None: ...
def set_threshold(threshold0: int, threshold1: int = ..., threshold2: int = ..., /) -> None: ...
