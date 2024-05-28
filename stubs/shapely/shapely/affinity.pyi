from collections.abc import Collection
from typing import Literal, overload
from typing_extensions import TypeAlias

from ._typing import GeoT
from .geometry import Point
from .lib import Geometry

__all__ = ["affine_transform", "rotate", "scale", "skew", "translate"]

_Origin: TypeAlias = Literal["center", "centroid"] | Point | tuple[float, float] | tuple[float, float, float]

def affine_transform(geom: GeoT, matrix: Collection[float]) -> GeoT: ...
@overload
def interpret_origin(geom: Geometry, origin: _Origin, ndim: Literal[2]) -> tuple[float, float]: ...
@overload
def interpret_origin(geom: Geometry, origin: _Origin, ndim: Literal[3]) -> tuple[float, float, float]: ...
@overload
def interpret_origin(geom: Geometry, origin: _Origin, ndim: int) -> tuple[float, float] | tuple[float, float, float]: ...
def rotate(geom: GeoT, angle: float, origin: _Origin = "center", use_radians: bool = False) -> GeoT: ...
def scale(geom: GeoT, xfact: float = 1.0, yfact: float = 1.0, zfact: float = 1.0, origin: _Origin = "center") -> GeoT: ...
def skew(geom: GeoT, xs: float = 0.0, ys: float = 0.0, origin: _Origin = "center", use_radians: bool = False) -> GeoT: ...
def translate(geom: GeoT, xoff: float = 0.0, yoff: float = 0.0, zoff: float = 0.0) -> GeoT: ...
