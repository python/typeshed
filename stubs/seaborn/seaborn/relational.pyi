from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Sequence
from typing import Any
from typing_extensions import Literal

import numpy as np
from matplotlib.axes import Axes
from matplotlib.typing import ColorType

from .axisgrid import FacetGrid

__all__ = ["relplot", "scatterplot", "lineplot"]

# The docs of these functions say that the palette argument accepts `matplotlib.colors.Colormap`
# as well but it doesn't

def lineplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    size: Incomplete | None = None,
    style: Incomplete | None = None,
    units: Incomplete | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    hue_order: Iterable[Any] | None = None,
    hue_norm: Incomplete | None = None,
    sizes: list[float] | dict[str, float] | tuple[float, float] | None = None,
    size_order: Iterable[Any] | None = None,
    size_norm: Incomplete | None = None,
    dashes: bool | list[Incomplete] | dict[str, Incomplete] = True,
    markers: Incomplete | None = None,
    style_order: Iterable[Any] | None = None,
    estimator: str | Callable[..., Incomplete] | None = "mean",
    errorbar: str | tuple[str, float] | Callable[[Iterable[float]], tuple[float, float]] | None = ("ci", 95),
    n_boot: int = 1000,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
    orient: Literal["x", "y"] = "x",
    sort: bool = True,
    err_style: Literal["band", "bars"] = "band",
    err_kws: dict[str, Any] | None = None,
    legend: Literal["auto", "brief", "full"] | bool = "auto",
    ci: str | int | None = "deprecated",  # deprecated
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def scatterplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    size: Incomplete | None = None,
    style: Incomplete | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    hue_order: Iterable[Any] | None = None,
    hue_norm: Incomplete | None = None,
    sizes: list[float] | dict[str, float] | tuple[float, float] | None = None,
    size_order: Iterable[Any] | None = None,
    size_norm: Incomplete | None = None,
    markers: Incomplete = True,
    style_order: Iterable[Any] | None = None,
    legend: Literal["auto", "brief", "full"] | bool = "auto",
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def relplot(
    data: Incomplete | None = None,
    *,
    x: Incomplete | None = None,
    y: Incomplete | None = None,
    hue: Incomplete | None = None,
    size: Incomplete | None = None,
    style: Incomplete | None = None,
    units: Incomplete | None = None,
    row: Incomplete | None = None,
    col: Incomplete | None = None,
    col_wrap: int | None = None,
    row_order: Iterable[Any] | None = None,
    col_order: Iterable[Any] | None = None,
    palette: str | Sequence[ColorType] | dict[Incomplete, ColorType] | None = None,
    hue_order: Iterable[Any] | None = None,
    hue_norm: Incomplete | None = None,
    sizes: list[float] | dict[str, float] | tuple[float, float] | None = None,
    size_order: Iterable[Any] | None = None,
    size_norm: Incomplete | None = None,
    markers: Incomplete | None = None,
    dashes: Incomplete | None = None,
    style_order: Iterable[Any] | None = None,
    legend: Literal["auto", "brief", "full"] | bool = "auto",
    kind: Literal["scatter", "line"] = "scatter",
    height: float = 5,
    aspect: float = 1,
    facet_kws: dict[str, Any] | None = None,
    **kwargs: Any,
) -> FacetGrid: ...
