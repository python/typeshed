"""Verify the deprecated-overload routing on `rasterio.warp.transform_geom`."""

from __future__ import annotations

from rasterio.crs import CRS
from rasterio.warp import transform_geom

src = CRS.from_epsg(4326)
dst = CRS.from_epsg(3857)
geom: dict[str, object] = {"type": "Point", "coordinates": [0.0, 0.0]}

# Modern overload — no deprecated kwargs.
transform_geom(src, dst, geom)
transform_geom(src, dst, geom, precision=2)

# Legacy overload — `antimeridian_*` kwargs are deprecated no-ops since
# GDAL 2.2. The @deprecated marker on the overload is carried in the stub;
# typeshed's regr_test does not opt into `enable_error_code = deprecated`
# so this call type-checks here, but downstream consumers see the warning.
transform_geom(src, dst, geom, antimeridian_cutting=True)
transform_geom(src, dst, geom, antimeridian_offset=10.0)
