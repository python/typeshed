from _typeshed import SupportsWrite
from typing import Literal, Self

from .anchor import Anchor
from .scalarint import _Underscore

__all__ = ["ScalarFloat", "ExponentialFloat", "ExponentialCapsFloat"]

class ScalarFloat(float):
    _width: int
    _prec: int
    _m_sign: Literal[False, "+", "-"]
    _m_lead0: int
    _exp: Literal["e", "E"] | None
    _e_width: int | None
    _e_sign: bool | None
    _underscore: _Underscore | None
    def __new__(
        cls,
        value: float,
        /,
        *,
        width: int,
        prec: int,
        m_sign: Literal[False, "+", "-"],
        m_lead0: int,
        exp: Literal["e", "E"] | None = None,
        e_width: int | None = None,
        e_sign: bool | None = None,
        underscore: _Underscore | None = None,
        anchor: str | None = None,
    ) -> Self: ...
    # The following methods explicitly return floats
    def __iadd__(self, a: float, /) -> float: ...  # noqa: Y034
    def __ifloordiv__(self, a: float, /) -> float: ...  # noqa: Y034
    def __imul__(self, a: float, /) -> float: ...  # noqa: Y034
    def __ipow__(self, a: float, /) -> float: ...  # noqa: Y034
    def __isub__(self, a: float, /) -> float: ...  # noqa: Y034
    @property
    def anchor(self) -> Anchor: ...
    def yaml_anchor(self, *, any: bool = False) -> Anchor: ...
    def yaml_set_anchor(self, value: str, /, *, always_dump: bool = False) -> None: ...
    def dump(self, out: SupportsWrite[str] = ...) -> None: ...

class ExponentialFloat(ScalarFloat):
    def __new__(cls, value: float, /, *, width: int | None = None, underscore: _Underscore | None = None): ...

class ExponentialCapsFloat(ScalarFloat):
    def __new__(cls, value: float, /, *, width: int | None = None, underscore: _Underscore | None = None): ...
