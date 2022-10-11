from typing_extensions import TypeAlias

from cv2.cv2 import _Mat

_Unused: TypeAlias = object

__all__: list[str] = []

class Mat(_Mat):
    wrap_channels: bool | None
    def __new__(cls, arr: _Mat, wrap_channels: bool = ..., **kwargs: _Unused) -> _Mat: ...
    def __init__(self, arr: _Mat, wrap_channels: bool = ...) -> None: ...
    def __array_finalize__(self, obj: _Mat | None) -> None: ...
