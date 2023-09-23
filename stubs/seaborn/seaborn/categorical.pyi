from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Sequence
from typing import Any, TypeVar
from typing_extensions import Literal

import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection
from matplotlib.typing import ColorType
from numpy.typing import NDArray
from seaborn.axisgrid import FacetGrid

__all__ = ["catplot", "stripplot", "swarmplot", "boxplot", "violinplot", "boxenplot", "pointplot", "barplot", "countplot"]

_T = TypeVar("_T")

def boxplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    orient: Literal["v", "h"] | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    dodge: bool = True,
    fliersize: float = 5,
    linewidth: Incomplete | None = None,
    whis: float = 1.5,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def violinplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    bw: str = "scott",
    cut: int = 2,
    scale: str = "area",
    scale_hue: bool = True,
    gridsize: int = 100,
    width: float = 0.8,
    inner: str = "box",
    split: bool = False,
    dodge: bool = True,
    orient: Literal["v", "h"] | None = None,
    linewidth: Incomplete | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    saturation: float = 0.75,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def boxenplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    orient: Literal["v", "h"] | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    dodge: bool = True,
    k_depth: str = "tukey",
    linewidth: Incomplete | None = None,
    scale: str = "exponential",
    outlier_prop: float = 0.007,
    trust_alpha: float = 0.05,
    showfliers: bool = True,
    ax: Axes | None = None,
    box_kws: dict[str, Any] | None = None,
    flier_kws: dict[str, Any] | None = None,
    line_kws: dict[str, Any] | None = None,
) -> Axes: ...
def stripplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    jitter: bool = True,
    dodge: bool = False,
    orient: Literal["v", "h"] | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    size: float = 5,
    edgecolor: ColorType = "gray",
    linewidth: float = 0,
    hue_norm: Incomplete | None = None,
    native_scale: bool = False,
    formatter: Incomplete | None = None,
    legend: str = "auto",
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def swarmplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    dodge: bool = False,
    orient: Literal["v", "h"] | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    size: float = 5,
    edgecolor: ColorType = "gray",
    linewidth: float = 0,
    hue_norm: Incomplete | None = None,
    native_scale: bool = False,
    formatter: Incomplete | None = None,
    legend: str = "auto",
    warn_thresh: float = 0.05,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def barplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Iterable[str] | None = None,
    hue_order: Iterable[str] | None = None,
    estimator: str | Callable[..., Incomplete] = "mean",
    errorbar: str | tuple[str, float] | Callable[[Iterable[float]], tuple[float, float]] | None = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    orient: Literal["v", "h"] | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    errcolor: ColorType = ".26",
    errwidth: float | None = None,
    capsize: float | None = None,
    dodge: bool = True,
    ci: str = "deprecated",
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def pointplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    estimator: str | Callable[..., Incomplete] = "mean",
    errorbar: str | tuple[str, float] | Callable[[Iterable[float]], tuple[float, float]] | None = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    markers: str = "o",
    linestyles: str = "-",
    dodge: bool = False,
    join: bool = True,
    scale: float = 1,
    orient: Literal["v", "h"] | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    errwidth: Incomplete | None = None,
    ci: str = "deprecated",
    capsize: Incomplete | None = None,
    label: Incomplete | None = None,
    ax: Axes | None = None,
) -> Axes: ...
def countplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    orient: Literal["v", "h"] | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    saturation: float = 0.75,
    width: float = 0.8,
    dodge: bool = True,
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def catplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    row: Incomplete | None = None,
    col: Incomplete | None = None,
    col_wrap: int | None = None,
    estimator: str | Callable[..., Incomplete] = "mean",
    errorbar: str | tuple[str, float] | Callable[[Iterable[float]], tuple[float, float]] | None = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    order: Iterable[str] | None = None,
    hue_order: Iterable[str] | None = None,
    row_order: Iterable[str] | None = None,
    col_order: Iterable[str] | None = None,
    height: float = 5,
    aspect: float = 1,
    kind: str = "strip",
    native_scale: bool = False,
    formatter: Callable[..., str] | None = None,
    orient: Literal["v", "h"] | None = None,
    color: ColorType | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    hue_norm: Incomplete | None = None,
    legend: str | bool = "auto",
    legend_out: bool = True,
    sharex: bool = True,
    sharey: bool = True,
    margin_titles: bool = False,
    facet_kws: dict[str, Any] | None = None,
    ci: str = "deprecated",
    **kwargs,
) -> FacetGrid: ...

class Beeswarm:
    orient: Literal["v", "h"]
    width: float
    warn_thresh: float
    def __init__(self, orient: str = "v", width: float = 0.8, warn_thresh: float = 0.05) -> None: ...
    def __call__(self, points: PathCollection, center: float) -> None: ...
    def beeswarm(self, orig_xyr) -> NDArray[np.float64]: ...
    def could_overlap(self, xyr_i, swarm) -> NDArray[np.float64]: ...
    def position_candidates(self, xyr_i, neighbors) -> NDArray[np.float64]: ...
    def first_non_overlapping_candidate(self, candidates, neighbors) -> Incomplete: ...
    def add_gutters(self, points: _T, center: float, log_scale: bool = False) -> _T: ...
