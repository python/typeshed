# TODO: DONE!

from collections.abc import Callable, Iterator
from typing import Any, NoReturn

class _StatsProperty:
    name: str
    func: Callable[..., Any]
    internal_name: str
    __doc__: str | None
    def __init__(self, name: str, func: Callable[..., Any]) -> NoReturn: ...
    def __get__(self, obj: object, objtype: Any | None = ...) -> Any: ...

class Stats:
    data: list[float]
    default: float
    def __init__(self, data: list[float], default: float = ..., use_copy: bool = ..., is_sorted: bool = ...) -> NoReturn: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...
    def clear_cache(self) -> NoReturn: ...
    count: _StatsProperty
    mean: _StatsProperty
    max: _StatsProperty
    min: _StatsProperty
    median: _StatsProperty
    iqr: _StatsProperty
    trimean: _StatsProperty
    variance: _StatsProperty
    std_dev: _StatsProperty
    median_abs_dev: _StatsProperty
    mad: _StatsProperty
    rel_std_dev: _StatsProperty
    skewness: _StatsProperty
    kurtosis: _StatsProperty
    pearson_type: _StatsProperty
    def get_quantile(self, q: float) -> float: ...
    def get_zscore(self, value: float) -> float: ...
    def trim_relative(self, amount: float = ...) -> NoReturn: ...
    def get_histogram_counts(self, bins: int | None = ..., **kw) -> int: ...
    def format_histogram(self, bins: int | None = ..., **kw) -> str: ...
    def describe(self, quantiles: list[float] | None = ..., format: str | None = ...) -> dict[str, float] | list[float] | str: ...

def describe(
    data: list[float], quantiles: list[float] | None = ..., format: str | None = ...
) -> dict[str, float] | list[float] | str: ...

# func: Incomplete
mean: Any
median: Any
iqr: Any
trimean: Any
variance: Any
std_dev: Any
median_abs_dev: Any
rel_std_dev: Any
skewness: Any
kurtosis: Any
pearson_type: Any

def format_histogram_counts(
    bin_counts: list[float], width: int | None = ..., format_bin: Callable[..., Any] | None = ...
) -> str: ...
