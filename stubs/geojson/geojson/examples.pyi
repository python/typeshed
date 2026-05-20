from typing import Any, Literal

from geojson.geometry import Geometry

from geojson import GeoJSON

class SimpleWebFeature:
    id: None | int | str
    geometry: None | Geometry
    properties: dict[Literal["title", "summary", "link"], str]
    __geo_interface__: dict[str, Any]
    def __init__(
        self,
        id: None | int | str = None,
        geometry: None | dict[str, Any] = None,
        title: None | str = None,
        summary: None | str = None,
        link: None | str = None,
    ) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

def create_simple_web_feature(o: dict[str, Any]) -> GeoJSON: ...
