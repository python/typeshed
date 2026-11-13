from _typeshed import FloatInt
import logging
import os
from collections.abc import Sequence
from typing import Any, Final

from affine import Affine as Affine
from numpy.typing import DTypeLike, NDArray
from rasterio.enums import Resampling
from rasterio.io import DatasetReaderBase

logger: Final[logging.Logger]

def stack(
    sources: Sequence[DatasetReaderBase | str | os.PathLike[str]],
    bounds: tuple[FloatInt, FloatInt, FloatInt, FloatInt] | None = None,
    res: FloatInt | tuple[FloatInt, FloatInt] | None = None,
    nodata: FloatInt | None = None,
    dtype: DTypeLike | None = None,
    indexes: int | Sequence[int] | None = None,
    output_count: int | None = None,
    resampling: Resampling = ...,
    target_aligned_pixels: bool = False,
    mem_limit: int = 64,
    use_highest_res: bool = False,
    masked: bool = False,
    dst_path: str | os.PathLike[str] | None = None,
    dst_kwds: dict[str, Any] | None = None,
) -> tuple[NDArray[Any], Affine]: ...
