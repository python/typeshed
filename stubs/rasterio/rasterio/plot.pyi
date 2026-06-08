import logging
from collections.abc import Mapping, Sequence
from typing import Any, Final, Literal

from numpy.typing import NDArray
from rasterio._affine_types import Affine
from rasterio.io import DatasetReader as DatasetReader
from rasterio.transform import guard_transform as guard_transform

logger: Final[logging.Logger]

def get_plt() -> Any: ...
def show(
    source: NDArray[Any] | DatasetReader | tuple[DatasetReader, int],
    with_bounds: bool = True,
    contour: bool = False,
    contour_label_kws: Mapping[str, Any] | None = None,
    indexes: Sequence[int] | None = None,
    ax: Any | None = None,
    title: str | None = None,
    transform: Affine | None = None,
    percent_range: tuple[float, float] | None = None,
    adjust: bool = True,
    **kwargs: Any,
) -> Any: ...
def plotting_extent(
    source: NDArray[Any] | DatasetReader, transform: Affine | None = None
) -> tuple[float, float, float, float]: ...
def reshape_as_image(arr: NDArray[Any]) -> NDArray[Any]: ...
def reshape_as_raster(arr: NDArray[Any]) -> NDArray[Any]: ...
def show_hist(
    source: NDArray[Any] | DatasetReader,
    bins: int = 10,
    masked: bool = True,
    title: str = "Histogram",
    ax: Any | None = None,
    label: str | Sequence[str] | None = None,
    range: tuple[float, float] | None = None,
    **kwargs: Any,
) -> None: ...
def adjust_band(band: NDArray[Any], kind: Literal["linear", "log"] | None = None) -> NDArray[Any]: ...
def contrast_strech(arr: NDArray[Any], percent_range: tuple[float, float] = (2.0, 98.0)) -> NDArray[Any]: ...
