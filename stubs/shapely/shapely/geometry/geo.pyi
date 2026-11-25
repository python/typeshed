from _typeshed import FloatInt
from typing import Any

from .._typing import SupportsGeoInterface
from .base import BaseGeometry
from .polygon import Polygon

def box(minx: FloatInt, miny: FloatInt, maxx: FloatInt, maxy: FloatInt, ccw: bool = True) -> Polygon: ...
def shape(context: dict[str, Any] | SupportsGeoInterface) -> BaseGeometry: ...
def mapping(ob: SupportsGeoInterface) -> dict[str, Any]: ...
