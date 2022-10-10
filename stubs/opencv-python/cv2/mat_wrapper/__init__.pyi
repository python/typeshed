from _typeshed import Incomplete
from typing_extensions import TypeAlias

# import numpy

_NDArray: TypeAlias = Incomplete  # numpy.ndarray
_Unused: TypeAlias = object

__all__: list[str] = []

class Mat(_NDArray):
    wrap_channels: bool | None
    def __new__(cls, arr: _NDArray, wrap_channels: bool = ..., **kwargs: _Unused) -> _NDArray: ...
    def __init__(self, arr: _NDArray, wrap_channels: bool = ...) -> None: ...
    def __array_finalize__(self, obj: _NDArray | None) -> None: ...
