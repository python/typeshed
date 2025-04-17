from typing import Any, Literal, overload
from typing_extensions import TypeGuard

import numpy as np
from numpy.typing import NDArray

from ._typing import ArrayLike, ArrayLikeSeq, OptGeoArrayLike, OptGeoArrayLikeSeq
from .geometry.base import BaseGeometry
from .lib import Geometry

__all__ = [
    "contains",
    "contains_properly",
    "contains_xy",
    "covered_by",
    "covers",
    "crosses",
    "disjoint",
    "dwithin",
    "equals",
    "equals_exact",
    "equals_identical",
    "has_m",
    "has_z",
    "intersects",
    "intersects_xy",
    "is_ccw",
    "is_closed",
    "is_empty",
    "is_geometry",
    "is_missing",
    "is_prepared",
    "is_ring",
    "is_simple",
    "is_valid",
    "is_valid_input",
    "is_valid_reason",
    "overlaps",
    "relate",
    "relate_pattern",
    "touches",
    "within",
]

@overload
def has_z(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def has_z(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def has_m(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def has_m(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def is_ccw(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def is_ccw(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def is_closed(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def is_closed(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def is_empty(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def is_empty(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def is_geometry(geometry: Geometry, **kwargs) -> Literal[True]: ...
@overload
def is_geometry(geometry: ArrayLikeSeq[Any], **kwargs) -> NDArray[np.bool_]: ...  # type: ignore[overload-overlap]
@overload
def is_geometry(geometry: object, **kwargs) -> TypeGuard[BaseGeometry]: ...
@overload
def is_missing(geometry: Geometry, **kwargs) -> Literal[True]: ...
@overload
def is_missing(geometry: ArrayLikeSeq[Any], **kwargs) -> NDArray[np.bool_]: ...  # type: ignore[overload-overlap]
@overload
def is_missing(geometry: object, **kwargs) -> TypeGuard[BaseGeometry]: ...
@overload
def is_prepared(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def is_prepared(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def is_valid_input(geometry: Geometry | None, **kwargs) -> Literal[True]: ...
@overload
def is_valid_input(geometry: ArrayLikeSeq[Any], **kwargs) -> NDArray[np.bool_]: ...  # type: ignore[overload-overlap]
@overload
def is_valid_input(geometry: object, **kwargs) -> TypeGuard[BaseGeometry | None]: ...
@overload
def is_ring(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def is_ring(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def is_simple(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def is_simple(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def is_valid(geometry: Geometry | None, **kwargs) -> bool: ...
@overload
def is_valid(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def is_valid_reason(geometry: None, **kwargs) -> None: ...
@overload
def is_valid_reason(geometry: Geometry, **kwargs) -> str: ...
@overload
def is_valid_reason(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.object_]: ...
@overload
def crosses(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def crosses(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def crosses(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def contains(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def contains(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def contains(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def contains_properly(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def contains_properly(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def contains_properly(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def covered_by(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def covered_by(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def covered_by(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def covers(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def covers(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def covers(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def disjoint(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def disjoint(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def disjoint(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def equals(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def equals(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def equals(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def intersects(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def intersects(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def intersects(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def overlaps(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def overlaps(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def overlaps(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def touches(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def touches(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def touches(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def within(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def within(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def within(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def equals_exact(
    a: Geometry | None, b: Geometry | None, tolerance: float = 0.0, *, normalize: bool = False, **kwargs
) -> bool: ...
@overload
def equals_exact(
    a: OptGeoArrayLike, b: OptGeoArrayLike, tolerance: ArrayLikeSeq[float], *, normalize: bool = False, **kwargs
) -> NDArray[np.bool_]: ...
@overload
def equals_exact(
    a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, tolerance: ArrayLike[float] = 0.0, *, normalize: bool = False, **kwargs
) -> NDArray[np.bool_]: ...
@overload
def equals_exact(
    a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, tolerance: ArrayLike[float] = 0.0, *, normalize: bool = False, **kwargs
) -> NDArray[np.bool_]: ...
@overload
def equals_identical(a: Geometry | None, b: Geometry | None, **kwargs) -> bool: ...
@overload
def equals_identical(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.bool_]: ...
@overload
def equals_identical(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.bool_]: ...
@overload
def relate(a: Geometry | None, b: None, **kwargs) -> None: ...
@overload
def relate(a: None, b: Geometry | None, **kwargs) -> None: ...
@overload
def relate(a: Geometry, b: Geometry, **kwargs) -> str: ...
@overload
def relate(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.object_]: ...
@overload
def relate(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.object_]: ...
@overload
def relate_pattern(a: Geometry | None, b: Geometry | None, pattern: str, **kwargs) -> bool: ...
@overload
def relate_pattern(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, pattern: str, **kwargs) -> NDArray[np.bool_]: ...
@overload
def relate_pattern(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, pattern: str, **kwargs) -> NDArray[np.bool_]: ...
@overload
def dwithin(a: Geometry | None, b: Geometry | None, distance: float, **kwargs) -> bool: ...
@overload
def dwithin(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, distance: float, **kwargs) -> NDArray[np.bool_]: ...
@overload
def dwithin(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, distance: float, **kwargs) -> NDArray[np.bool_]: ...
@overload
def contains_xy(geom: Geometry | None, x: float, y: float, **kwargs) -> bool: ...
@overload
def contains_xy(geom: OptGeoArrayLike, x: ArrayLikeSeq[float], y: None = None, **kwargs) -> NDArray[np.bool_]: ...
@overload
def contains_xy(geom: Geometry | None, x: ArrayLike[float], y: ArrayLikeSeq[float], **kwargs) -> NDArray[np.bool_]: ...
@overload
def contains_xy(geom: Geometry | None, x: ArrayLikeSeq[float], y: ArrayLike[float], **kwargs) -> NDArray[np.bool_]: ...
@overload
def contains_xy(geom: OptGeoArrayLikeSeq, x: ArrayLike[float], y: ArrayLike[float], **kwargs) -> NDArray[np.bool_]: ...
@overload
def intersects_xy(geom: Geometry | None, x: float, y: float, **kwargs) -> bool: ...
@overload
def intersects_xy(geom: OptGeoArrayLike, x: ArrayLikeSeq[float], y: None = None, **kwargs) -> NDArray[np.bool_]: ...
@overload
def intersects_xy(geom: Geometry | None, x: ArrayLike[float], y: ArrayLikeSeq[float], **kwargs) -> NDArray[np.bool_]: ...
@overload
def intersects_xy(geom: Geometry | None, x: ArrayLikeSeq[float], y: ArrayLike[float], **kwargs) -> NDArray[np.bool_]: ...
@overload
def intersects_xy(geom: OptGeoArrayLikeSeq, x: ArrayLike[float], y: ArrayLike[float], **kwargs) -> NDArray[np.bool_]: ...
