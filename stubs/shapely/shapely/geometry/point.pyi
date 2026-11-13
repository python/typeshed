from _typeshed import FloatInt
from collections.abc import Iterable
from typing import Literal, TypeAlias, overload
from typing_extensions import Self

from .._typing import ArrayLikeSeq
from .base import BaseGeometry
from .collection import GeometryCollection

__all__ = ["Point"]

_PointLike: TypeAlias = Point | Iterable[FloatInt] | ArrayLikeSeq[FloatInt]

class Point(BaseGeometry):
    __slots__: list[str] = []

    @overload  # no args: empty point
    def __new__(self) -> Self: ...
    @overload  # one arg: (x, y[, z]) tuple or a Point instance
    def __new__(self, coords: _PointLike, /) -> Self: ...
    @overload  # two args: (x, y) tuple
    def __new__(self, x: FloatInt, y: FloatInt, /) -> Self: ...
    @overload  # three args: (x, y, z) tuple
    def __new__(self, x: FloatInt, y: FloatInt, z: FloatInt, /) -> Self: ...

    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def z(self) -> float: ...
    @property
    def m(self) -> float: ...
    def svg(self, scale_factor: FloatInt = 1.0, fill_color: str | None = None, opacity: FloatInt | None = None) -> str: ...  # type: ignore[override]
    # more precise base overrides
    @property
    def geom_type(self) -> Literal["Point"]: ...
    @property
    def boundary(self) -> GeometryCollection: ...  # empty geometry collection
    @property
    def convex_hull(self) -> Point: ...
    @property
    def envelope(self) -> Point: ...
    @property
    def oriented_envelope(self) -> Point: ...
    @property
    def minimum_rotated_rectangle(self) -> Point: ...
