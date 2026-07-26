from collections.abc import Callable, Sequence
from enum import Enum
from typing import Any, BinaryIO, TypeAlias

from rasterio.crs import CRS
from rasterio.io import BufferedDatasetWriter, DatasetReader, DatasetWriter, MemoryFile
from rasterio.windows import Window

AnyDataset: TypeAlias = DatasetReader | DatasetWriter | BufferedDatasetWriter | MemoryFile
Colormap: TypeAlias = dict[int, tuple[int, int, int] | tuple[int, int, int, int]]
CRSInput: TypeAlias = str | dict[str, str] | CRS
FileOrBytes: TypeAlias = BinaryIO | bytes
Indexes: TypeAlias = int | Sequence[int]
NumType: TypeAlias = int | float
ShapeND: TypeAlias = Sequence[int]
WindowInput: TypeAlias = Window | tuple[tuple[int, int], tuple[int, int]]

# Scalar values accepted by every GDAL CSL-style option list: global
# config (`set_gdal_config` / `Env`), per-call warp options
# (NUM_THREADS, INIT_DEST, …), RPC/transformer options (RPC_HEIGHT,
# RPC_DEM, COORDINATE_OPERATION, …), and metadata tag values. The
# runtime stringifies each value at the C boundary and does not
# special-case Enum or tuple types here (use `_OpenOption` for those).
_GDALOption: TypeAlias = str | int | float | bool | None  # noqa: Y047

# GDAL driver-specific open/creation option values. The runtime coerces
# every value to a string at the C boundary; documented usage covers
# scalars, Enum members (encoded as `.name.upper()`), and tuples of
# scalars (joined with commas). Lists are not handled specially — pass
# a tuple if you need a multi-value option.
_OpenOption: TypeAlias = str | int | float | bool | Enum | tuple[str | int | float | bool, ...] | None  # noqa: Y047

# Opaque OGR geometry handle (a Cython-wrapped C object). Callers only
# pass it back to other Cython internals; the public API surfaces
# already-decoded GeoJSON-like dicts.
_OGRGeometry: TypeAlias = Any  # noqa: Y047

# Scalar or arbitrarily nested list of scalars; used by helpers that
# recurse into sequences while preserving the nesting depth.
_NestedScalar: TypeAlias = float | list[_NestedScalar]  # noqa: Y047

# fsspec-style opener forwarded to `rasterio.open(opener=...)`:
# `(path: str, mode: str) -> file-like`.
_Opener: TypeAlias = Callable[..., Any]  # noqa: Y047
