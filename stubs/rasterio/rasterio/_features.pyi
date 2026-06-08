from collections.abc import Iterator
from typing import Any, Final

from rasterio.enums import MergeAlg as MergeAlg

GEOMETRY_TYPES: Final[dict[int, str]]
GEOJSON2OGR_GEOMETRY_TYPES: Final[dict[str, int]]

bool_: Final[str]
int8: Final[str]
int16: Final[str]
int32: Final[str]
int64: Final[str]
uint8: Final[str]
uint16: Final[str]
uint32: Final[str]
uint64: Final[str]
float16: Final[str]
float32: Final[str]
float64: Final[str]

class GeomBuilder:
    def build(self, geom: Any) -> dict[str, Any]: ...

class OGRGeomBuilder:
    def build(self, geom: dict[str, Any]) -> Any: ...

class ShapeIterator:
    def __iter__(self) -> Iterator[tuple[dict[str, Any], float]]: ...
    def __next__(self) -> tuple[dict[str, Any], float]: ...
