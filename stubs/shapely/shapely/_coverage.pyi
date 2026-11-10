from typing import Literal, overload

import numpy as np

from ._typing import ArrayLike, GeoArray, GeoArrayLikeSeq, OptGeoArrayLike
from ._enum import ParamEnum
from .geometry import Polygon

__all__ = ["coverage_clean", "coverage_invalid_edges", "coverage_is_valid", "coverage_simplify"]

class CoverageCleanMergeStrategy(ParamEnum):
    longest_border = 0
    max_area = 1
    min_area = 2
    min_index = 3

def coverage_clean(
    geometry: OptGeoArrayLike,
    *,
    gap_width: float = 0.0,
    snapping_distance: float = -1,
    merge_strategy: Literal["longest_border", "max_area", "min_area", "min_index"] | int = "longest_border",
) -> GeoArray: ...
def coverage_is_valid(geometry: OptGeoArrayLike, gap_width: float = 0.0, **kwargs) -> np.bool_: ...
def coverage_invalid_edges(geometry: OptGeoArrayLike, gap_width: float = 0.0, **kwargs) -> GeoArray: ...

@overload
def coverage_simplify(geometry: Polygon, tolerance: ArrayLike[float], *, simplify_boundary: bool = True) -> Polygon: ...
@overload
def coverage_simplify(geometry: GeoArrayLikeSeq, tolerance: ArrayLike[float], *, simplify_boundary: bool = True) -> GeoArray: ...
