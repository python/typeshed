from _typeshed import FloatInt
from collections.abc import Sequence
from typing import Literal, TypedDict, type_check_only

@type_check_only
class GroundControlPointDict(TypedDict):
    id: str
    info: str | None
    row: FloatInt
    col: FloatInt
    x: FloatInt
    y: FloatInt
    z: FloatInt | None

@type_check_only
class GroundControlPointGeometry(TypedDict):
    type: Literal["Point"]
    coordinates: Sequence[FloatInt]

@type_check_only
class GroundControlPointFeature(TypedDict):
    id: str
    type: Literal["Feature"]
    geometry: GroundControlPointGeometry
    properties: GroundControlPointDict

class GroundControlPoint:
    id: str
    info: str | None
    row: FloatInt
    col: FloatInt
    x: FloatInt
    y: FloatInt
    z: FloatInt | None
    def __init__(
        self,
        row: FloatInt | None = None,
        col: FloatInt | None = None,
        x: FloatInt | None = None,
        y: FloatInt | None = None,
        z: FloatInt | None = None,
        id: str | None = None,
        info: str | None = None,
    ) -> None: ...
    def asdict(self) -> GroundControlPointDict: ...
    @property
    def __geo_interface__(self) -> GroundControlPointFeature: ...
