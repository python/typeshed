from collections.abc import Callable
from ctypes.wintypes import PFLOAT
from typing import TypeVar
from typing_extensions import TypeAlias

from d3dshot.capture_output import _Frame

_ProcessFuncRegionArg = TypeVar("_ProcessFuncRegionArg", tuple[int, int, int, int], None)
_ProcessFuncReturn = TypeVar("_ProcessFuncReturn", _Frame, None)
_ProcessFunc: TypeAlias = Callable[[PFLOAT, int, int, int, int, _ProcessFuncRegionArg, int], _ProcessFuncReturn]  # noqa: Y047
