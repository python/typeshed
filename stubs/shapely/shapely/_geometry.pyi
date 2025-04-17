from enum import IntEnum
from typing import Any, Literal, SupportsIndex, overload
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import NDArray

from ._enum import ParamEnum
from ._typing import ArrayLike, ArrayLikeSeq, GeoArray, OptGeoArrayLike, OptGeoArrayLikeSeq, OptGeoT
from .geometry import LinearRing, LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon
from .geometry.base import BaseGeometry, BaseMultipartGeometry
from .lib import Geometry

__all__ = [
    "GeometryType",
    "force_2d",
    "force_3d",
    "get_coordinate_dimension",
    "get_dimensions",
    "get_exterior_ring",
    "get_geometry",
    "get_interior_ring",
    "get_m",
    "get_num_coordinates",
    "get_num_geometries",
    "get_num_interior_rings",
    "get_num_points",
    "get_parts",
    "get_point",
    "get_precision",
    "get_rings",
    "get_srid",
    "get_type_id",
    "get_x",
    "get_y",
    "get_z",
    "set_precision",
    "set_srid",
]

_PrecisionMode: TypeAlias = Literal["valid_output", "pointwise", "keep_collapsed", 0, 1, 2]

class GeometryType(IntEnum):
    MISSING = -1
    POINT = 0
    LINESTRING = 1
    LINEARRING = 2
    POLYGON = 3
    MULTIPOINT = 4
    MULTILINESTRING = 5
    MULTIPOLYGON = 6
    GEOMETRYCOLLECTION = 7

@overload
def get_type_id(geometry: Geometry | None, **kwargs) -> int: ...
@overload
def get_type_id(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]: ...
@overload
def get_dimensions(geometry: Geometry | None, **kwargs) -> int: ...
@overload
def get_dimensions(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]: ...
@overload
def get_coordinate_dimension(geometry: Geometry | None, **kwargs) -> int: ...
@overload
def get_coordinate_dimension(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]: ...
@overload
def get_num_coordinates(geometry: Geometry | None, **kwargs) -> int: ...
@overload
def get_num_coordinates(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]: ...
@overload
def get_srid(geometry: Geometry | None, **kwargs) -> int: ...
@overload
def get_srid(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]: ...
@overload
def set_srid(geometry: OptGeoT, srid: SupportsIndex, **kwargs) -> OptGeoT: ...
@overload
def set_srid(geometry: OptGeoArrayLikeSeq, srid: ArrayLike[SupportsIndex], **kwargs) -> GeoArray: ...
@overload
def set_srid(geometry: OptGeoArrayLike, srid: ArrayLikeSeq[SupportsIndex], **kwargs) -> GeoArray: ...
@overload
def get_x(point: Geometry | None, **kwargs) -> float: ...
@overload
def get_x(point: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]: ...
@overload
def get_y(point: Geometry | None, **kwargs) -> float: ...
@overload
def get_y(point: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]: ...
@overload
def get_z(point: Geometry | None, **kwargs) -> float: ...
@overload
def get_z(point: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]: ...
@overload
def get_m(point: Geometry | None, **kwargs) -> float: ...
@overload
def get_m(point: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]: ...
@overload
def get_point(geometry: LineString, index: SupportsIndex, **kwargs) -> Point | Any: ...
@overload
def get_point(geometry: Point | Polygon | BaseMultipartGeometry | None, index: SupportsIndex, **kwargs) -> None: ...
@overload
def get_point(geometry: Geometry, index: SupportsIndex, **kwargs) -> Point | None: ...
@overload
def get_point(geometry: OptGeoArrayLikeSeq, index: ArrayLike[SupportsIndex], **kwargs) -> GeoArray: ...
@overload
def get_point(geometry: OptGeoArrayLike, index: ArrayLikeSeq[SupportsIndex], **kwargs) -> GeoArray: ...
@overload
def get_num_points(geometry: Geometry | None, **kwargs) -> int: ...
@overload
def get_num_points(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]: ...
@overload
def get_exterior_ring(geometry: Polygon, **kwargs) -> LinearRing: ...
@overload
def get_exterior_ring(geometry: Point | LineString | BaseMultipartGeometry | None, **kwargs) -> None: ...
@overload
def get_exterior_ring(geometry: Geometry, **kwargs) -> LinearRing | None: ...
@overload
def get_exterior_ring(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray: ...
@overload
def get_interior_ring(geometry: Polygon, index: SupportsIndex, **kwargs) -> LinearRing | Any: ...
@overload
def get_interior_ring(geometry: Point | LineString | BaseMultipartGeometry | None, index: SupportsIndex, **kwargs) -> None: ...
@overload
def get_interior_ring(geometry: Geometry, index: SupportsIndex, **kwargs) -> LinearRing | None: ...
@overload
def get_interior_ring(geometry: OptGeoArrayLikeSeq, index: ArrayLike[SupportsIndex], **kwargs) -> GeoArray: ...
@overload
def get_interior_ring(geometry: OptGeoArrayLike, index: ArrayLikeSeq[SupportsIndex], **kwargs) -> GeoArray: ...
@overload
def get_num_interior_rings(geometry: Geometry | None, **kwargs) -> int: ...
@overload
def get_num_interior_rings(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]: ...
@overload
def get_geometry(geometry: MultiPoint, index: SupportsIndex, **kwargs) -> Point | Any: ...
@overload
def get_geometry(geometry: MultiLineString, index: SupportsIndex, **kwargs) -> LineString | Any: ...
@overload
def get_geometry(geometry: MultiPolygon, index: SupportsIndex, **kwargs) -> Polygon | Any: ...
@overload
def get_geometry(geometry: BaseMultipartGeometry, index: SupportsIndex, **kwargs) -> BaseGeometry | Any: ...
@overload
def get_geometry(geometry: None, index: SupportsIndex, **kwargs) -> None: ...
@overload
def get_geometry(geometry: Geometry | None, index: SupportsIndex, **kwargs) -> BaseGeometry | None: ...
@overload
def get_geometry(geometry: OptGeoArrayLikeSeq, index: ArrayLike[SupportsIndex], **kwargs) -> GeoArray: ...
@overload
def get_geometry(geometry: OptGeoArrayLike, index: ArrayLikeSeq[SupportsIndex], **kwargs) -> GeoArray: ...
@overload
def get_parts(geometry: OptGeoArrayLike, return_index: Literal[False] = False) -> GeoArray: ...
@overload
def get_parts(geometry: OptGeoArrayLike, return_index: Literal[True]) -> tuple[GeoArray, NDArray[np.int64]]: ...
@overload
def get_parts(geometry: OptGeoArrayLike, return_index: bool) -> GeoArray | tuple[GeoArray, NDArray[np.int64]]: ...
@overload
def get_rings(geometry: OptGeoArrayLike, return_index: Literal[False] = False) -> GeoArray: ...
@overload
def get_rings(geometry: OptGeoArrayLike, return_index: Literal[True]) -> tuple[GeoArray, NDArray[np.int64]]: ...
@overload
def get_rings(geometry: OptGeoArrayLike, return_index: bool) -> GeoArray | tuple[GeoArray, NDArray[np.int64]]: ...
@overload
def get_num_geometries(geometry: Geometry | None, **kwargs) -> int: ...
@overload
def get_num_geometries(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]: ...
@overload
def get_precision(geometry: Geometry | None, **kwargs) -> float: ...
@overload
def get_precision(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]: ...

class SetPrecisionMode(ParamEnum):
    valid_output = 0
    pointwise = 1
    keep_collapsed = 2

@overload
def set_precision(geometry: OptGeoT, grid_size: float, mode: _PrecisionMode = "valid_output", **kwargs) -> OptGeoT: ...
@overload
def set_precision(
    geometry: OptGeoArrayLikeSeq, grid_size: float, mode: _PrecisionMode = "valid_output", **kwargs
) -> GeoArray: ...
@overload
def force_2d(geometry: OptGeoT, **kwargs) -> OptGeoT: ...
@overload
def force_2d(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray: ...
@overload
def force_3d(geometry: OptGeoT, z: float = 0.0, **kwargs) -> OptGeoT: ...
@overload
def force_3d(geometry: OptGeoArrayLikeSeq, z: ArrayLike[float] = 0.0, **kwargs) -> GeoArray: ...
@overload
def force_3d(geometry: OptGeoArrayLike, z: ArrayLikeSeq[float], **kwargs) -> GeoArray: ...
