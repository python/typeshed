"""Verify the deprecated-overload routing on `rasterio.warp.transform_geom`."""

from __future__ import annotations

from rasterio.crs import CRS
from rasterio.warp import transform_geom

src = CRS.from_epsg(4326)
dst = CRS.from_epsg(3857)
geom: dict[str, object] = {"type": "Point", "coordinates": [0.0, 0.0]}

transform_geom(src, dst, geom)
transform_geom(src, dst, geom, precision=2)

transform_geom(src, dst, geom, antimeridian_cutting=True)  # pyright: ignore[reportDeprecated]
transform_geom(src, dst, geom, antimeridian_offset=10.0)  # pyright: ignore[reportDeprecated]
