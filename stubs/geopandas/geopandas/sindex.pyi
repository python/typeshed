from typing import Literal, overload

import numpy as np
from numpy.typing import ArrayLike, NDArray
from shapely import Geometry

PREDICATES: set[str | None]

class SpatialIndex:
    geometries: NDArray[np.object_]
    def __init__(self, geometry: NDArray[np.object_]) -> None: ...
    @property
    def valid_query_predicates(self) -> set[str | None]: ...
    def query(
        self,
        geometry: Geometry | ArrayLike,
        predicate: str | None = None,
        sort: bool = False,
        distance: float | ArrayLike | None = None,
        output_format: Literal["sparse", "dense", "tuple"] = "tuple",
    ) -> NDArray[np.int_]: ...
    @overload
    def nearest(
        self,
        geometry,
        return_all: bool = True,
        max_distance: float | None = None,
        return_distance: Literal[False] = False,
        exclusive: bool = False,
    ) -> NDArray[np.int_]: ...
    @overload
    def nearest(
        self,
        geometry,
        return_all: bool = True,
        max_distance: float | None = None,
        *,
        return_distance: Literal[True],
        exclusive: bool = False,
    ) -> tuple[NDArray[np.int_], NDArray[np.float64]]: ...
    @overload
    def nearest(
        self,
        geometry,
        return_all: bool = True,
        max_distance: float | None = None,
        return_distance: bool = False,
        exclusive: bool = False,
    ) -> NDArray[np.int_] | tuple[NDArray[np.int_], NDArray[np.float64]]: ...
    def intersection(self, coordinates) -> NDArray[np.int_]: ...
    @property
    def size(self) -> int: ...
    @property
    def is_empty(self) -> bool: ...
    def __len__(self) -> int: ...
