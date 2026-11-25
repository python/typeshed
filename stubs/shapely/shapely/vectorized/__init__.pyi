from _typeshed import FloatInt
from typing import overload
from typing_extensions import deprecated

import numpy as np
from numpy.typing import NDArray

from .._typing import ArrayLike, ArrayLikeSeq
from ..lib import Geometry
from ..prepared import PreparedGeometry

@overload
@deprecated("Use 'shapely.contains_xy' instead (available since shapely 2.0.0).")
def contains(geometry: Geometry | PreparedGeometry[Geometry], x: FloatInt, y: FloatInt) -> np.bool_: ...
@overload
@deprecated("Use 'shapely.contains_xy' instead (available since shapely 2.0.0).")
def contains(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLikeSeq[FloatInt], y: ArrayLike[FloatInt]
) -> NDArray[np.bool_]: ...
@overload
@deprecated("Use 'shapely.contains_xy' instead (available since shapely 2.0.0).")
def contains(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLike[FloatInt], y: ArrayLikeSeq[FloatInt]
) -> NDArray[np.bool_]: ...
@overload
@deprecated("Use 'shapely.contains_xy' instead (available since shapely 2.0.0).")
def contains(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLike[FloatInt], y: ArrayLike[FloatInt]
) -> np.bool_ | NDArray[np.bool_]: ...

@overload
@deprecated("Use 'shapely.intersects_xy' instead (available since shapely 2.0.0).")
def touches(geometry: Geometry | PreparedGeometry[Geometry], x: FloatInt, y: FloatInt) -> np.bool_: ...
@overload
@deprecated("Use 'shapely.intersects_xy' instead (available since shapely 2.0.0).")
def touches(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLikeSeq[FloatInt], y: ArrayLike[FloatInt]
) -> NDArray[np.bool_]: ...
@overload
@deprecated("Use 'shapely.intersects_xy' instead (available since shapely 2.0.0).")
def touches(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLike[FloatInt], y: ArrayLikeSeq[FloatInt]
) -> NDArray[np.bool_]: ...
@overload
@deprecated("Use 'shapely.intersects_xy' instead (available since shapely 2.0.0).")
def touches(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLike[FloatInt], y: ArrayLike[FloatInt]
) -> np.bool_ | NDArray[np.bool_]: ...
