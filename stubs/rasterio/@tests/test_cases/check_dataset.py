"""Verify the inferred property types on a `DatasetReader`."""

from __future__ import annotations

from typing import Any
from typing_extensions import assert_type

from numpy.typing import NDArray
from rasterio.coords import BoundingBox
from rasterio.crs import CRS
from rasterio.io import DatasetReader
from rasterio.profiles import Profile


def check_props(reader: DatasetReader) -> None:
    assert_type(reader.crs, CRS)
    # NOTE: `reader.transform` is typed via the stubs-only
    # `rasterio._affine_types.Affine = Any` indirection until affine
    # ships its own `py.typed` (v3). No `assert_type` here because the
    # alias is `Any`; once affine v3 lands and the indirection swaps to
    # `from affine import Affine`, an `assert_type(reader.transform,
    # Affine)` line should be reinstated.
    assert_type(reader.bounds, BoundingBox)
    assert_type(reader.profile, Profile)
    assert_type(reader.count, int)
    assert_type(reader.width, int)
    assert_type(reader.height, int)
    assert_type(reader.shape, tuple[int, int])
    assert_type(reader.dtypes, tuple[str, ...])
    assert_type(reader.indexes, tuple[int, ...])
    assert_type(reader.nodata, float | None)
    assert_type(reader.read(1), NDArray[Any])
    assert_type(reader.read_crs(), CRS | None)
    assert_type(reader.tags(), dict[str, str])
