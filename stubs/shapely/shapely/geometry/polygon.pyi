from collections.abc import Collection
from typing import NoReturn, overload
from typing_extensions import Self, TypeAlias

from .base import BaseGeometry
from .linestring import LineString, _ConvertibleToLineString
from .multilinestring import MultiLineString

__all__ = ["LinearRing", "Polygon", "orient"]

_ConvertibleToLinearRing: TypeAlias = _ConvertibleToLineString  # same alias but with better name for doc purposes
_PolygonShellLike: TypeAlias = Polygon | _ConvertibleToLinearRing | None
_PolygonHolesLike: TypeAlias = Collection[_ConvertibleToLinearRing | None] | None

class LinearRing(LineString):
    def __new__(self, coordinates: _ConvertibleToLinearRing | None = None) -> Self: ...
    @property
    def is_ccw(self) -> bool: ...

class InteriorRingSequence:
    def __init__(self, parent: Polygon) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> LinearRing: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: int) -> LinearRing: ...
    @overload
    def __getitem__(self, key: slice) -> list[LinearRing]: ...

class Polygon(BaseGeometry):
    def __new__(self, shell: _PolygonShellLike = None, holes: _PolygonHolesLike = None) -> Self: ...
    @property
    def exterior(self) -> LinearRing: ...
    @property
    def interiors(self) -> list[LinearRing] | InteriorRingSequence: ...
    @property
    def coords(self) -> NoReturn: ...
    def svg(self, scale_factor: float = 1.0, fill_color: str | None = None, opacity: float | None = None) -> str: ...  # type: ignore[override]
    @classmethod
    def from_bounds(cls, xmin: float, ymin: float, xmax: float, ymax: float) -> Self: ...
    # more precise base overrides
    @property
    def boundary(self) -> MultiLineString: ...

def orient(polygon: Polygon, sign: float = 1.0) -> Polygon: ...
