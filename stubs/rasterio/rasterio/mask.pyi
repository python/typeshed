import logging
from collections.abc import Iterable, Mapping
from typing import Any, Final

from numpy.typing import NDArray
from rasterio._affine_types import Affine
from rasterio.errors import WindowError as WindowError
from rasterio.features import geometry_mask as geometry_mask, geometry_window as geometry_window
from rasterio.io import DatasetReader

logger: Final[logging.Logger]

def raster_geometry_mask(
    dataset: DatasetReader,
    shapes: Iterable[Mapping[str, Any]],
    all_touched: bool = False,
    invert: bool = False,
    crop: bool = False,
    pad: bool = False,
    pad_width: float = 0.5,
) -> tuple[NDArray[Any], Affine, tuple[int, int, int, int]]: ...
def mask(
    dataset: DatasetReader,
    shapes: Iterable[Mapping[str, Any]],
    all_touched: bool = False,
    invert: bool = False,
    nodata: float | None = None,
    filled: bool = True,
    crop: bool = False,
    pad: bool = False,
    pad_width: float = 0.5,
    indexes: int | Iterable[int] | None = None,
) -> tuple[NDArray[Any], Affine]: ...
