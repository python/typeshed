from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing import Any
from typing_extensions import Literal

from matplotlib.axes import Axes
from matplotlib.typing import ColorType

from ._core.typing import Default
from .axisgrid import FacetGrid
from .utils import _ErrorBar, _Estimator, _Legend, _LogScale, _Palette, _Seed

__all__ = ["catplot", "stripplot", "swarmplot", "boxplot", "violinplot", "boxenplot", "pointplot", "barplot", "countplot"]

def boxplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    orient: Literal["v", "h", "x", "h"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    dodge: bool | Literal["auto"] = "auto",
    width: float = 0.8,
    gap: float = 0,
    whis: float = 1.5,
    linecolor: ColorType = "auto",
    linewidth: float | None = None,
    fliersize: float | None = None,
    ax: Axes | None = None,
    hue_norm: Incomplete | None = None,
    native_scale: bool = False,
    log_scale: _LogScale | None = None,
    formatter: Callable[..., str] | None = None,
    legend: _Legend = "auto",
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
    orient: Literal["v", "h", "x", "h"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    inner: str = "box",
    split: bool = False,
    width: float = 0.8,
    dodge: bool | Literal["auto"] = "auto",
    gap: float = 0,
    linewidth: float | None = None,
    linecolor: ColorType = "auto",
    cut: float = 2,
    gridsize: int = 100,
    bw_method: str | float = "scott",
    bw_adjust: float = 1,
    density_norm: Literal["area", "count", "width"] = "area",
    common_norm: bool | None = False,
    hue_norm: Incomplete | None = None,
    formatter: Callable[..., str] | None = None,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    legend: _Legend = "auto",
    scale: Incomplete = ...,  # deprecated
    scale_hue: Incomplete = ...,  # deprecated
    bw: Incomplete = ...,  # deprecated
    inner_kws: dict[str, Any] | None = None,
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
    orient: Literal["v", "h", "x", "h"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    dodge: bool | Literal["auto"] = "auto",
    width: float = 0.8,
    gap: float = 0,
    linewidth: float | None = None,
    linecolor: ColorType | None = None,
    width_method: Literal["exponential", "linear", "area"] = "exponential",
    k_depth: Literal["tukey", "proportion", "trustworthy", "full"] | int = "tukey",
    outlier_prop: float = 0.007,
    trust_alpha: float = 0.05,
    showfliers: bool = True,
    hue_norm: Incomplete | None = None,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[..., str] | None = None,
    legend: _Legend = "auto",
    scale: Incomplete = ...,  # deprecated
    box_kws: dict[str, Any] | None = None,
    flier_kws: dict[str, Any] | None = None,
    line_kws: dict[str, Any] | None = None,
    ax: Axes | None = None,
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
    orient: Literal["v", "h", "x", "h"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    size: float = 5,
    edgecolor: ColorType | Default = ...,
    linewidth: float = 0,
    hue_norm: Incomplete | None = None,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[..., str] | None = None,
    legend: _Legend = "auto",
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
    orient: Literal["v", "h", "x", "h"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    size: float = 5,
    edgecolor: ColorType | None = None,
    linewidth: float = 0,
    hue_norm: Incomplete | None = None,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[..., str] | None = None,
    legend: _Legend = "auto",
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
    estimator: _Estimator = "mean",
    errorbar: _ErrorBar | None = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: _Seed | None = None,
    orient: Literal["v", "h", "x", "h"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    hue_norm: Incomplete | None = None,
    width: float = 0.8,
    dodge: bool | Literal["auto"] = "auto",
    gap: float = 0,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[..., str] | None = None,
    legend: _Legend = "auto",
    capsize: float = 0,
    err_kws: dict[str, Any] | None = None,
    ci: Incomplete = ...,  # deprecated
    errcolor: Incomplete = ...,  # deprecated
    errwidth: Incomplete = ...,  # deprecated
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
    estimator: _Estimator = "mean",
    errorbar: _ErrorBar | None = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: _Seed | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    hue_norm: Incomplete | None = None,
    markers: str | Incomplete = ...,  # string or list of strings
    linestyles: str | Incomplete = ...,  # string or list of strings
    dodge: bool = False,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    orient: Literal["v", "h", "x", "h"] | None = None,
    capsize: float = 0,
    formatter: Callable[..., str] | None = None,
    legend: _Legend = "auto",
    err_kws: dict[str, Any] | None = None,
    ci: Incomplete = ...,  # deprecated
    errwidth: Incomplete = ...,  # deprecated
    join: Incomplete = ...,  # deprecated
    scale: Incomplete = ...,  # deprecated
    ax: Axes | None = None,
    **kwargs,
) -> Axes: ...
def countplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    order: Incomplete | None = None,
    hue_order: Incomplete | None = None,
    orient: Literal["v", "h", "x", "h"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    hue_norm: Incomplete | None = None,
    stat: Literal["count", "percent", "proportion", "probability"] = "count",
    width: float = 0.8,
    dodge: bool | Literal["auto"] = "auto",
    gap: float = 0,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[..., str] | None = None,
    legend: _Legend = "auto",
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
    kind: Literal["strip", "swarm", "box", "violin", "boxen", "point", "bar", "count"] = "strip",
    estimator: _Estimator = "mean",
    errorbar: _ErrorBar | None = ("ci", 95),
    n_boot: int = 1000,
    units: Incomplete | None = None,
    seed: _Seed | None = None,
    order: Iterable[str] | None = None,
    hue_order: Iterable[str] | None = None,
    row_order: Iterable[str] | None = None,
    col_order: Iterable[str] | None = None,
    col_wrap: int | None = None,
    height: float = 5,
    aspect: float = 1,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[..., str] | None = None,
    orient: Literal["v", "h", "x", "h"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    hue_norm: Incomplete | None = None,
    legend: _Legend = "auto",
    legend_out: bool = True,
    sharex: bool = True,
    sharey: bool = True,
    margin_titles: bool = False,
    facet_kws: dict[str, Any] | None = None,
    ci: Incomplete = ...,  # deprecated
    **kwargs,
) -> FacetGrid: ...
