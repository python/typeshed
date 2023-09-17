from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any
from typing_extensions import Literal

from matplotlib.axes import Axes

from .axisgrid import FacetGrid

__all__ = ["displot", "histplot", "kdeplot", "ecdfplot", "rugplot", "distplot"]

def histplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    weights: Incomplete | None = None,
    stat: str = "count",
    bins: Incomplete = "auto",
    binwidth: float | tuple[float, float] | None = None,
    binrange: Incomplete | None = None,
    discrete: bool | None = None,
    cumulative: bool = False,
    common_bins: bool = True,
    common_norm: bool = True,
    multiple: Literal["layer", "dodge", "stack", "fill"] = "layer",
    element: Literal["bars", "step", "poly"] = "bars",
    fill: bool = True,
    shrink: float = 1,
    kde: bool = False,
    kde_kws: dict[str, Any] | None = None,
    line_kws: dict[str, Any] | None = None,
    thresh: float | None = 0,
    pthresh: float | None = None,
    pmax: float | None = None,
    cbar: bool = False,
    cbar_ax: Axes | None = None,
    cbar_kws: dict[str, Any] | None = None,
    palette: Incomplete | None = None,
    hue_order: Iterable[str] | None = None,
    hue_norm: Incomplete | None = None,
    color: Incomplete | None = None,
    log_scale: bool | float | tuple[bool | float, bool | float] | None = None,
    legend: bool = True,
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def kdeplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    weights: Incomplete | None = None,
    palette: Incomplete | None = None,
    hue_order: Iterable[str] | None = None,
    hue_norm: Incomplete | None = None,
    color: Incomplete | None = None,
    fill: bool | None = None,
    multiple: Literal["layer", "stack", "fill"] = "layer",
    common_norm: bool = True,
    common_grid: bool = False,
    cumulative: bool = False,
    bw_method: str = "scott",
    bw_adjust: float = 1,
    warn_singular: bool = True,
    log_scale: bool | float | tuple[bool | float, bool | float] | None = None,
    levels: int | Iterable[int] = 10,
    thresh: float = 0.05,
    gridsize: int = 200,
    cut: float = 3,
    clip: Incomplete | None = None,
    legend: bool = True,
    cbar: bool = False,
    cbar_ax: Axes | None = None,
    cbar_kws: dict[str, Any] | None = None,
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def ecdfplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    weights: Incomplete | None = None,
    stat: Literal["proportion", "count"] = "proportion",
    complementary: bool = False,
    palette: Incomplete | None = None,
    hue_order: Iterable[str] | None = None,
    hue_norm: Incomplete | None = None,
    log_scale: bool | float | tuple[bool | float, bool | float] | None = None,
    legend: bool = True,
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def rugplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    height: float = 0.025,
    expand_margins: bool = True,
    palette: Incomplete | None = None,
    hue_order: Iterable[str] | None = None,
    hue_norm: Incomplete | None = None,
    legend: bool = True,
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def displot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    row: Incomplete | None = None,
    col: Incomplete | None = None,
    weights: Incomplete | None = None,
    kind: Literal["hist", "kde", "ecdf"] = "hist",
    rug: bool = False,
    rug_kws: dict[str, Any] | None = None,
    log_scale: bool | float | tuple[bool | float, bool | float] | None = None,
    legend: bool = True,
    palette: Incomplete | None = None,
    hue_order: Iterable[str] | None = None,
    hue_norm: Incomplete | None = None,
    color: Incomplete | None = None,
    col_wrap: int | None = None,
    row_order: Iterable[str] | None = None,
    col_order: Iterable[str] | None = None,
    height: float = 5,
    aspect: float = 1,
    facet_kws: dict[str, Any] | None = None,
    **kwargs: Any,
) -> FacetGrid: ...
def distplot(  # deprecated
    a: Incomplete | None = None,
    bins: Incomplete | None = None,
    hist: bool = True,
    kde: bool = True,
    rug: bool = False,
    fit: Incomplete | None = None,
    hist_kws: dict[str, Any] | None = None,
    kde_kws: dict[str, Any] | None = None,
    rug_kws: dict[str, Any] | None = None,
    fit_kws: dict[str, Any] | None = None,
    color: Incomplete | None = None,
    vertical: bool = False,
    norm_hist: bool = False,
    axlabel: str | Literal[False] | None = None,
    label: Incomplete | None = None,
    ax: Axes | None = None,
    x: Incomplete | None = None,
) -> Axes: ...
