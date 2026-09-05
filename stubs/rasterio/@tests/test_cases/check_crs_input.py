from __future__ import annotations

from typing_extensions import assert_type

import rasterio.warp
from rasterio.crs import CRS
from rasterio.io import MemoryFile


class ForeignCRS:
    def to_wkt(self) -> str:
        return ""


assert_type(rasterio.warp.transform_bounds(4326, 3857, 0.0, 0.0, 1.0, 1.0), tuple[float, float, float, float])
rasterio.warp.transform_bounds(ForeignCRS(), ForeignCRS(), 0.0, 0.0, 1.0, 1.0)
rasterio.warp.transform_bounds(CRS.from_epsg(4326), "EPSG:3857", 0.0, 0.0, 1.0, 1.0)
rasterio.warp.transform_bounds({"init": "EPSG:4326"}, CRS.from_epsg(3857), 0.0, 0.0, 1.0, 1.0)
rasterio.warp.transform_bounds(object(), 3857, 0.0, 0.0, 1.0, 1.0)  # type: ignore
rasterio.warp.transform(4326, ForeignCRS(), [0.0], [0.0])
rasterio.warp.calculate_default_transform(4326, ForeignCRS(), 10, 10, left=0.0, bottom=0.0, right=1.0, top=1.0)
MemoryFile().open(driver="GTiff", width=1, height=1, count=1, dtype="uint8", crs=4326)
MemoryFile().open(driver="GTiff", width=1, height=1, count=1, dtype="uint8", crs=ForeignCRS())
