from _typeshed import FloatInt
from collections.abc import Sequence
from typing import Literal, SupportsIndex, TypeAlias, overload
from typing_extensions import Unpack

import numpy as np
from numpy.typing import NDArray

from ._enum import ParamEnum
from ._geometry import GeometryType
from ._typing import ArrayLike, ArrayLikeSeq, GeoArray, OptGeoArrayLike, OptGeoArrayLikeSeq, UFuncKwargsNoOut
from .geometry import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon
from .lib import Geometry

__all__ = [
    "box",
    "destroy_prepared",
    "empty",
    "geometrycollections",
    "linearrings",
    "linestrings",
    "multilinestrings",
    "multipoints",
    "multipolygons",
    "points",
    "polygons",
    "prepare",
]

class HandleNaN(ParamEnum):
    allow = 0
    skip = 1
    error = 2

_HandleNaN: TypeAlias = Literal["allow", "skip", "error"] | HandleNaN

@overload
def points(
    coords: FloatInt,
    y: FloatInt,
    z: FloatInt | None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],  # acts as x
) -> Point: ...
@overload
def points(
    coords: Sequence[FloatInt],
    y: None = None,
    z: None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],  # acts as x, y[, z]
) -> Point: ...
@overload
def points(
    coords: Sequence[FloatInt],  # acts as (x1, x2, ...)
    y: Sequence[FloatInt],  # must be (y1, y2, ...)
    z: Sequence[FloatInt] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def points(
    coords: Sequence[Sequence[FloatInt]],  # acts as (x1, x2, ...), (y1, y2, ...)[, (z1, z2, ...)]
    y: None = None,
    z: None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def points(
    coords: ArrayLike[FloatInt],
    y: ArrayLike[FloatInt],
    z: ArrayLike[FloatInt] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> Point | GeoArray: ...
@overload
def points(
    coords: ArrayLikeSeq[FloatInt],
    y: ArrayLike[FloatInt] | None = None,
    z: ArrayLike[FloatInt] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> Point | GeoArray: ...

@overload
def linestrings(
    coords: Sequence[FloatInt],  # acts as (x1, x2, ...)
    y: Sequence[FloatInt],
    z: Sequence[FloatInt] | None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> LineString: ...
@overload
def linestrings(
    coords: Sequence[Sequence[FloatInt]],  # acts as (x1, y1[, z1]), (x2, y2[, z2]), ...
    y: None = None,
    z: None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> LineString: ...
@overload
def linestrings(
    coords: Sequence[Sequence[Sequence[FloatInt]]],  # acts as seq of (x1, y1[, z1]), (x2, y2[, z2]), ...
    y: None = None,
    z: None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def linestrings(
    coords: ArrayLikeSeq[FloatInt],
    y: ArrayLikeSeq[FloatInt] | None = None,
    z: ArrayLikeSeq[FloatInt] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> LineString | GeoArray: ...

@overload
def linearrings(
    coords: Sequence[FloatInt],  # acts as (x1, x2, ...)
    y: Sequence[FloatInt],
    z: Sequence[FloatInt] | None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> LinearRing: ...
@overload
def linearrings(
    coords: Sequence[Sequence[FloatInt]],  # acts as (x1, y1[, z1]), (x2, y2[, z2]), ...
    y: None = None,
    z: None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> LinearRing: ...
@overload
def linearrings(
    coords: Sequence[Sequence[Sequence[FloatInt]]],  # acts as seq of (x1, y1[, z1]), (x2, y2[, z2]), ...
    y: None = None,
    z: None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def linearrings(
    coords: ArrayLikeSeq[FloatInt],
    y: ArrayLikeSeq[FloatInt] | None = None,
    z: ArrayLikeSeq[FloatInt] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = ...,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> LinearRing | GeoArray: ...

@overload
def polygons(
    geometries: LinearRing | Sequence[Sequence[FloatInt]] | None,
    holes: ArrayLikeSeq[FloatInt] | OptGeoArrayLikeSeq | None = None,
    indices: None = None,
    *,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> Polygon: ...
@overload
def polygons(
    geometries: Sequence[LinearRing | Sequence[Sequence[FloatInt]] | None],
    holes: ArrayLikeSeq[FloatInt] | OptGeoArrayLikeSeq | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def polygons(
    geometries: ArrayLikeSeq[FloatInt] | OptGeoArrayLikeSeq,
    holes: ArrayLikeSeq[FloatInt] | OptGeoArrayLikeSeq | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> Polygon | GeoArray: ...

@overload
def box(xmin: FloatInt, ymin: FloatInt, xmax: FloatInt, ymax: FloatInt, ccw: bool = True, **kwargs: Unpack[UFuncKwargsNoOut]) -> Polygon: ...
@overload
def box(
    xmin: ArrayLikeSeq[FloatInt],
    ymin: ArrayLikeSeq[FloatInt],
    xmax: ArrayLikeSeq[FloatInt],
    ymax: ArrayLikeSeq[FloatInt],
    ccw: bool = True,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...

@overload
def multipoints(
    geometries: Sequence[Point | Sequence[FloatInt] | None],
    indices: None = None,
    *,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> MultiPoint: ...
@overload
def multipoints(
    geometries: Sequence[Sequence[Point | Sequence[FloatInt] | None]],
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def multipoints(
    geometries: OptGeoArrayLikeSeq,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> MultiPoint | GeoArray: ...

@overload
def multilinestrings(
    geometries: Sequence[LineString | Sequence[Sequence[FloatInt]] | None],
    indices: None = None,
    *,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> MultiLineString: ...
@overload
def multilinestrings(
    geometries: Sequence[Sequence[LineString | Sequence[Sequence[FloatInt]] | None]],
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def multilinestrings(
    geometries: OptGeoArrayLikeSeq,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> MultiLineString | GeoArray: ...

@overload
def multipolygons(
    geometries: Sequence[Polygon | Sequence[Sequence[FloatInt]] | None],
    indices: None = None,
    *,
    out: None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> MultiPolygon: ...
@overload
def multipolygons(
    geometries: Sequence[Sequence[Polygon | Sequence[Sequence[FloatInt]] | None]],
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def multipolygons(
    geometries: OptGeoArrayLikeSeq,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> MultiPolygon | GeoArray: ...

@overload
def geometrycollections(
    geometries: Sequence[Geometry | None], indices: None = None, out: None = None, **kwargs: Unpack[UFuncKwargsNoOut]
) -> GeometryCollection: ...
@overload
def geometrycollections(
    geometries: Sequence[Sequence[Geometry | None]],
    indices: ArrayLikeSeq[int] | None = None,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeoArray: ...
@overload
def geometrycollections(
    geometries: OptGeoArrayLikeSeq,
    indices: ArrayLikeSeq[int] | None = None,
    out: NDArray[np.object_] | None = None,
    **kwargs: Unpack[UFuncKwargsNoOut],
) -> GeometryCollection | GeoArray: ...

def prepare(geometry: OptGeoArrayLike, **kwargs: Unpack[UFuncKwargsNoOut]) -> None: ...
def destroy_prepared(geometry: OptGeoArrayLike, **kwargs: Unpack[UFuncKwargsNoOut]) -> None: ...
def empty(
    shape: SupportsIndex | Sequence[SupportsIndex], geom_type: GeometryType | int | None = None, order: Literal["C", "F"] = "C"
) -> NDArray[np.object_]: ...
