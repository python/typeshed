"""Verify `rasterio.open` overloads route to the right return type."""

from __future__ import annotations

from typing_extensions import assert_type

import rasterio
from rasterio.io import DatasetReader, DatasetWriter

# Default mode is "r" → DatasetReader
assert_type(rasterio.open("foo.tif"), DatasetReader)
assert_type(rasterio.open("foo.tif", "r"), DatasetReader)

# Write/update modes → DatasetWriter
assert_type(rasterio.open("foo.tif", "w", driver="GTiff"), DatasetWriter)
assert_type(rasterio.open("foo.tif", "r+"), DatasetWriter)
assert_type(rasterio.open("foo.tif", "w+"), DatasetWriter)


def _opaque_mode(mode: str) -> None:
    # When `mode` is opaque str, the union overload is picked.
    assert_type(rasterio.open("foo.tif", mode), DatasetReader | DatasetWriter)


# An int path is not a valid `fp`; the overload check rejects it.
rasterio.open(123)  # type: ignore[call-overload]
