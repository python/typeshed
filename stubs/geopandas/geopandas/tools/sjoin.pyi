from _typeshed import FloatInt
from typing import Literal

from numpy.typing import ArrayLike

from ..geodataframe import GeoDataFrame

def sjoin(
    left_df: GeoDataFrame,
    right_df: GeoDataFrame,
    how: Literal["left", "right", "inner"] = "inner",
    predicate: str = "intersects",
    lsuffix: str = "left",
    rsuffix: str = "right",
    distance: FloatInt | ArrayLike | None = None,
    on_attribute: str | tuple[str, ...] | list[str] | None = None,
) -> GeoDataFrame: ...
def sjoin_nearest(
    left_df: GeoDataFrame,
    right_df: GeoDataFrame,
    how: Literal["left", "right", "inner"] = "inner",
    max_distance: FloatInt | None = None,
    lsuffix: str = "left",
    rsuffix: str = "right",
    distance_col: str | None = None,
    exclusive: bool = False,
) -> GeoDataFrame: ...
