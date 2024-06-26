from array import array
from collections.abc import Iterator
from typing import Any, Generic, Literal, NoReturn, overload
from typing_extensions import Self, TypeVar, deprecated

import numpy as np
from numpy.typing import NDArray

from .._typing import ArrayLikeSeq, GeoArray, GeoT, OptGeoArrayLike, OptGeoArrayLikeSeq
from ..constructive import BufferCapStyle, BufferJoinStyle
from ..coords import CoordinateSequence
from ..lib import Geometry
from .collection import GeometryCollection
from .point import Point
from .polygon import Polygon

GEOMETRY_TYPES: list[str]

@deprecated("Function 'geom_factory' is deprecated.")
def geom_factory(g: int, parent: object | None = None) -> Any: ...
def dump_coords(geom: Geometry) -> list[tuple[float, float] | list[tuple[float, float]]]: ...

class CAP_STYLE:
    round: Literal[BufferCapStyle.round]
    flat: Literal[BufferCapStyle.flat]
    square: Literal[BufferCapStyle.square]

class JOIN_STYLE:
    round: Literal[BufferJoinStyle.round]
    mitre: Literal[BufferJoinStyle.mitre]
    bevel: Literal[BufferJoinStyle.bevel]

class BaseGeometry(Geometry):
    @deprecated(
        "Directly calling 'BaseGeometry()' is deprecated. To create an empty geometry, "
        "use one of the subclasses instead, for example 'GeometryCollection()'."
    )
    def __new__(self) -> GeometryCollection: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __format__(self, format_spec: str) -> str: ...
    @overload
    def __and__(self, other: Geometry) -> BaseGeometry: ...
    @overload
    def __and__(self, other: OptGeoArrayLikeSeq) -> GeoArray: ...
    @overload
    def __and__(self, other: None) -> None: ...
    @overload
    def __or__(self, other: Geometry) -> BaseGeometry: ...
    @overload
    def __or__(self, other: OptGeoArrayLikeSeq) -> GeoArray: ...
    @overload
    def __or__(self, other: None) -> None: ...
    @overload
    def __sub__(self, other: Geometry) -> BaseGeometry: ...
    @overload
    def __sub__(self, other: OptGeoArrayLikeSeq) -> GeoArray: ...
    @overload
    def __sub__(self, other: None) -> None: ...
    @overload
    def __xor__(self, other: Geometry) -> BaseGeometry: ...
    @overload
    def __xor__(self, other: OptGeoArrayLikeSeq) -> GeoArray: ...
    @overload
    def __xor__(self, other: None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def coords(self) -> CoordinateSequence: ...
    @property
    def xy(self) -> tuple[array[float], array[float]]: ...
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...
    @deprecated("Method 'geometryType()' is deprecated. Use attribute 'geom_type' instead.")
    def geometryType(self) -> str: ...
    @property
    @deprecated("Attribute 'type' is deprecated. Use attribute 'geom_type' instead.")
    def type(self) -> str: ...
    @property
    def wkt(self) -> str: ...
    @property
    def wkb(self) -> bytes: ...
    @property
    def wkb_hex(self) -> str: ...
    def svg(self, scale_factor: float = 1.0, **kwargs) -> str: ...
    def _repr_svg_(self) -> str: ...
    @property
    def geom_type(self) -> str: ...
    @property
    def area(self) -> float: ...
    @overload
    def distance(self, other: Geometry | None) -> float: ...
    @overload
    def distance(self, other: OptGeoArrayLikeSeq) -> NDArray[np.float64]: ...
    @overload
    def hausdorff_distance(self, other: Geometry | None) -> float: ...
    @overload
    def hausdorff_distance(self, other: OptGeoArrayLikeSeq) -> NDArray[np.float64]: ...
    @property
    def length(self) -> float: ...
    @property
    def minimum_clearance(self) -> float: ...
    @property
    def boundary(self) -> BaseMultipartGeometry | Any: ...  # is None for GeometryCollection
    @property
    def bounds(self) -> tuple[float, float, float, float]: ...
    @property
    def centroid(self) -> Point: ...
    def point_on_surface(self) -> Point: ...
    def representative_point(self) -> Point: ...
    @property
    def convex_hull(self) -> BaseGeometry: ...
    @property
    def envelope(self) -> BaseGeometry: ...
    @property
    def oriented_envelope(self) -> BaseGeometry: ...
    @property
    def minimum_rotated_rectangle(self) -> BaseGeometry: ...
    def buffer(
        self,
        distance: float,
        quad_segs: int = 16,
        cap_style: BufferCapStyle | Literal["round", "square", "flat"] = "round",
        join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
        mitre_limit: float = 5.0,
        single_sided: bool = False,
        *,
        quadsegs: int | None = None,  # deprecated
        resolution: int | None = None,  # to be deprecated
    ) -> Polygon: ...
    def simplify(self, tolerance: float, preserve_topology: bool = True) -> BaseGeometry: ...
    def normalize(self) -> BaseGeometry: ...
    @overload
    def difference(self, other: Geometry, grid_size: float | None = None) -> BaseGeometry: ...
    @overload
    def difference(self, other: OptGeoArrayLikeSeq, grid_size: float | None = None) -> GeoArray: ...
    @overload
    def difference(self, other: None, grid_size: float | None = None) -> None: ...
    @overload
    def intersection(self, other: Geometry, grid_size: float | None = None) -> BaseGeometry: ...
    @overload
    def intersection(self, other: OptGeoArrayLikeSeq, grid_size: float | None = None) -> GeoArray: ...
    @overload
    def intersection(self, other: None, grid_size: float | None = None) -> None: ...
    @overload
    def symmetric_difference(self, other: Geometry, grid_size: float | None = None) -> BaseGeometry: ...
    @overload
    def symmetric_difference(self, other: OptGeoArrayLikeSeq, grid_size: float | None = None) -> GeoArray: ...
    @overload
    def symmetric_difference(self, other: None, grid_size: float | None = None) -> None: ...
    @overload
    def union(self, other: Geometry, grid_size: float | None = None) -> BaseGeometry: ...
    @overload
    def union(self, other: OptGeoArrayLikeSeq, grid_size: float | None = None) -> GeoArray: ...
    @overload
    def union(self, other: None, grid_size: float | None = None) -> None: ...
    @property
    def has_z(self) -> bool: ...
    @property
    def is_empty(self) -> bool: ...
    @property
    def is_ring(self) -> bool: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_simple(self) -> bool: ...
    @property
    def is_valid(self) -> bool: ...
    @overload
    def relate(self, other: Geometry) -> str: ...
    @overload
    def relate(self, other: OptGeoArrayLikeSeq) -> NDArray[np.str_]: ...
    @overload
    def relate(self, other: None) -> None: ...
    @overload
    def covers(self, other: Geometry | None) -> bool: ...
    @overload
    def covers(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def covered_by(self, other: Geometry | None) -> bool: ...
    @overload
    def covered_by(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def contains(self, other: Geometry | None) -> bool: ...
    @overload
    def contains(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def contains_properly(self, other: Geometry | None) -> bool: ...
    @overload
    def contains_properly(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def crosses(self, other: Geometry | None) -> bool: ...
    @overload
    def crosses(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def disjoint(self, other: Geometry | None) -> bool: ...
    @overload
    def disjoint(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def equals(self, other: Geometry | None) -> bool: ...
    @overload
    def equals(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def intersects(self, other: Geometry | None) -> bool: ...
    @overload
    def intersects(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def overlaps(self, other: Geometry | None) -> bool: ...
    @overload
    def overlaps(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def touches(self, other: Geometry | None) -> bool: ...
    @overload
    def touches(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def within(self, other: Geometry | None) -> bool: ...
    @overload
    def within(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]: ...
    @overload
    def dwithin(self, other: Geometry | None, distance: float) -> bool: ...
    @overload
    def dwithin(self, other: OptGeoArrayLikeSeq, distance: float) -> NDArray[np.bool_]: ...
    @overload
    def dwithin(self, other: OptGeoArrayLike, distance: ArrayLikeSeq[float]) -> NDArray[np.bool_]: ...
    @overload
    def equals_exact(self, other: Geometry | None, tolerance: float) -> bool: ...
    @overload
    def equals_exact(self, other: OptGeoArrayLikeSeq, tolerance: float) -> NDArray[np.bool_]: ...
    @overload
    def equals_exact(self, other: OptGeoArrayLike, tolerance: ArrayLikeSeq[float]) -> NDArray[np.bool_]: ...
    @deprecated("Method 'almost_equals()' is deprecated. Use method 'equals_exact()' instead.")
    def almost_equals(self, other: OptGeoArrayLike, decimal: int = 6) -> bool | NDArray[np.bool_]: ...
    @overload
    def relate_pattern(self, other: Geometry | None, pattern: str) -> bool: ...
    @overload
    def relate_pattern(self, other: OptGeoArrayLikeSeq, pattern: str) -> NDArray[np.bool_]: ...
    @overload
    def line_locate_point(self, other: Point | None, normalized: bool = False) -> float: ...
    @overload
    def line_locate_point(self, other: OptGeoArrayLikeSeq, normalized: bool = False) -> NDArray[np.float64]: ...
    @overload
    def project(self, other: Point | None, normalized: bool = False) -> float: ...
    @overload
    def project(self, other: OptGeoArrayLikeSeq, normalized: bool = False) -> NDArray[np.float64]: ...
    @overload
    def line_interpolate_point(self, distance: float, normalized: bool = False) -> Point: ...
    @overload
    def line_interpolate_point(self, distance: ArrayLikeSeq[float], normalized: bool = False) -> GeoArray: ...
    @overload
    def interpolate(self, distance: float, normalized: bool = False) -> Point: ...
    @overload
    def interpolate(self, distance: ArrayLikeSeq[float], normalized: bool = False) -> GeoArray: ...
    @overload
    def segmentize(self, max_segment_length: float) -> Self: ...
    @overload
    def segmentize(self, max_segment_length: ArrayLikeSeq[float]) -> GeoArray: ...
    def reverse(self) -> Self: ...

_GeoT_co = TypeVar("_GeoT_co", bound=Geometry, default=BaseGeometry, covariant=True)

class BaseMultipartGeometry(BaseGeometry, Generic[_GeoT_co]):
    @property
    def coords(self) -> NoReturn: ...
    @property
    def geoms(self) -> GeometrySequence[Self]: ...
    def svg(self, scale_factor: float = 1.0, color: str | None = None) -> str: ...  # type: ignore[override]

_P_co = TypeVar("_P_co", covariant=True, bound=BaseMultipartGeometry[Geometry])

class GeometrySequence(Generic[_P_co]):
    def __init__(self, parent: _P_co) -> None: ...
    def __iter__(self: GeometrySequence[BaseMultipartGeometry[GeoT]]) -> Iterator[GeoT]: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self: GeometrySequence[BaseMultipartGeometry[GeoT]], key: int | np.integer[Any]) -> GeoT: ...
    @overload
    def __getitem__(self, key: slice) -> _P_co: ...

class EmptyGeometry(BaseGeometry):
    @deprecated(
        "The 'EmptyGeometry()' constructor is deprecated. Use one of the "
        "geometry subclasses instead, for example 'GeometryCollection()'."
    )
    def __new__(self) -> GeometryCollection: ...  # type: ignore[misc]
