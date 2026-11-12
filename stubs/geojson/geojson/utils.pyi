from collections.abc import Callable, Generator, Iterable, Sequence
from typing import Any, Literal

from geojson.base import GeoJSON
from geojson.geometry import Geometry, LineString, Point, Polygon

def coords(obj: GeoJSON | dict[str, Any]) -> Generator[tuple[float, ...]]: ...
def map_coords(func: Callable[[float], float], obj: GeoJSON | dict[str, Any]) -> dict[str, Any]: ...
def map_tuples(func: Callable[[Sequence[float]], Iterable[float]], obj: GeoJSON | dict[str, Any]) -> dict[str, Any]: ...
def map_geometries(
    func: Callable[[Geometry | dict[str, Any]], Geometry | dict[str, Any]], obj: GeoJSON | dict[str, Any]
) -> dict[str, Any]: ...
def generate_random(
    featureType: Literal["Point", "LineString", "Polygon"],
    numberVertices: int = 3,
    boundingBox: list[float] = [-180.0, -90.0, 180.0, 90.0],
) -> Point | LineString | Polygon: ...
