from _typeshed import Incomplete, SupportsGetItem
from collections.abc import Iterable, Mapping, Sequence
from typing import Any, TypeVar, overload

import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.legend import Legend
from matplotlib.text import Text
from matplotlib.ticker import Locator
from matplotlib.typing import ColorType
from numpy.typing import ArrayLike, NDArray
from pandas import DataFrame
from seaborn.axisgrid import Grid

__all__ = [
    "desaturate",
    "saturate",
    "set_hls_values",
    "move_legend",
    "despine",
    "get_dataset_names",
    "get_data_home",
    "load_dataset",
]

_VectorT = TypeVar("_VectorT", bound=SupportsGetItem[Any, Any])

def ci_to_errsize(cis: ArrayLike, heights: ArrayLike) -> NDArray[np.float64]: ...
def desaturate(color: ColorType, prop: float) -> tuple[float, float, float]: ...
def saturate(color: ColorType) -> tuple[float, float, float]: ...
def set_hls_values(
    color: ColorType, h: float | None = None, l: float | None = None, s: float | None = None
) -> tuple[float, float, float]: ...
def axlabel(xlabel: str, ylabel: str, **kwargs: Any) -> None: ...  # deprecated
def remove_na(vector: _VectorT) -> _VectorT: ...
def get_color_cycle() -> list[str]: ...
def despine(
    fig: Figure | None = None,
    ax: Axes | None = None,
    top: bool = True,
    right: bool = True,
    left: bool = False,
    bottom: bool = False,
    offset: int | Mapping[str, int] | None = None,
    trim: bool = False,
) -> None: ...
def move_legend(obj: Grid | Axes | Figure, loc: str | int, **kwargs: Any) -> None: ...
def ci(a: ArrayLike, which: float | ArrayLike = 95, axis: int | tuple[int, ...] | None = None) -> Incomplete: ...
def get_dataset_names() -> list[str]: ...
def get_data_home(data_home: str | None = None) -> str: ...
def load_dataset(name: str, cache: bool = True, data_home: str | None = None, **kws: Any) -> DataFrame: ...
def axis_ticklabels_overlap(labels: Iterable[Text]) -> bool: ...
def axes_ticklabels_overlap(ax: Axes) -> tuple[bool, bool]: ...
def locator_to_legend_entries(
    locator: Locator, limits: Iterable[float], dtype: Incomplete
) -> tuple[list[Incomplete], list[str]]: ...
@overload
def relative_luminance(color: ColorType) -> float: ...  # type: ignore[misc]
@overload
def relative_luminance(color: Sequence[ColorType]) -> NDArray[np.float64]: ...
@overload
def relative_luminance(color: ColorType | Sequence[ColorType] | ArrayLike) -> float | NDArray[np.float64]: ...
def to_utf8(obj: object) -> str: ...
def adjust_legend_subtitles(legend: Legend) -> None: ...  # not public API
