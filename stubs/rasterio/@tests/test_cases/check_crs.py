"""Verify `rasterio.crs.CRS` factory return types and arg validation."""

from __future__ import annotations

from typing_extensions import assert_type

from rasterio.crs import CRS

# All factory staticmethods return `CRS`.
assert_type(CRS.from_epsg(4326), CRS)
assert_type(CRS.from_string("EPSG:4326"), CRS)
assert_type(CRS.from_wkt("..."), CRS)
assert_type(CRS.from_authority("EPSG", 4326), CRS)
assert_type(CRS.from_user_input(4326), CRS)

# from_epsg expects int | str, not float.
CRS.from_epsg(4326.0)  # type: ignore[arg-type]
