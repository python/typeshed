from typing import Self
from typing_extensions import TypeAlias

from .anchor import Anchor

__all__ = ["ScalarInt", "BinaryInt", "OctalInt", "HexInt", "HexCapsInt", "DecimalInt"]

_Underscore: TypeAlias = list[int | bool]  # [int, bool, bool]

class ScalarInt(int):
    _width: int | None
    _underscore: _Underscore | None
    def __new__(
        cls, value: int, /, *, width: int | None = None, underscore: _Underscore | None = None, anchor: str | None = None
    ) -> Self: ...
    def __iadd__(self, a: int, /) -> Self: ...
    def __ifloordiv__(self, a: int, /) -> Self: ...
    def __imul__(self, a: int, /) -> Self: ...
    def __ipow__(self, a: int, /) -> Self: ...
    def __isub__(self, a: int, /) -> Self: ...
    @property
    def anchor(self) -> Anchor: ...
    def yaml_anchor(self, *, any: bool = False) -> Anchor | None: ...
    def yaml_set_anchor(self, value: str, /, *, always_dump: bool = False) -> None: ...

class BinaryInt(ScalarInt):
    def __new__(
        cls, value: int, /, *, width: int | None = None, underscore: _Underscore | None = None, anchor: str | None = None
    ) -> Self: ...

class OctalInt(ScalarInt):
    def __new__(
        cls, value: int, /, *, width: int | None = None, underscore: _Underscore | None = None, anchor: str | None = None
    ) -> Self: ...

class HexInt(ScalarInt):
    def __new__(
        cls, value: int, /, *, width: int | None = None, underscore: _Underscore | None = None, anchor: str | None = None
    ) -> Self: ...

class HexCapsInt(ScalarInt):
    def __new__(
        cls, value: int, /, *, width: int | None = None, underscore: _Underscore | None = None, anchor: str | None = None
    ) -> Self: ...

class DecimalInt(ScalarInt):
    def __new__(
        cls, value: int, /, *, width: int | None = None, underscore: _Underscore | None = None, anchor: str | None = None
    ) -> Self: ...
