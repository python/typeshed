from _typeshed import Incomplete

class _StatsProperty:
    name: Incomplete
    func: Incomplete
    internal_name: Incomplete
    __doc__: Incomplete
    def __init__(self, name, func) -> None: ...
    def __get__(self, obj, objtype: Incomplete | None = ...): ...

class Stats:
    data: Incomplete
    default: Incomplete
    def __init__(self, data, default: float = ..., use_copy: bool = ..., is_sorted: bool = ...) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def clear_cache(self) -> None: ...
    count: Incomplete
    mean: Incomplete
    max: Incomplete
    min: Incomplete
    median: Incomplete
    iqr: Incomplete
    trimean: Incomplete
    variance: Incomplete
    std_dev: Incomplete
    median_abs_dev: Incomplete
    mad: Incomplete
    rel_std_dev: Incomplete
    skewness: Incomplete
    kurtosis: Incomplete
    pearson_type: Incomplete
    def get_quantile(self, q): ...
    def get_zscore(self, value): ...
    def trim_relative(self, amount: float = ...) -> None: ...
    def get_histogram_counts(self, bins: Incomplete | None = ..., **kw): ...
    def format_histogram(self, bins: Incomplete | None = ..., **kw): ...
    def describe(self, quantiles: Incomplete | None = ..., format: Incomplete | None = ...): ...

def describe(data, quantiles: Incomplete | None = ..., format: Incomplete | None = ...): ...

# func: Incomplete
mean: Incomplete
median: Incomplete
iqr: Incomplete
trimean: Incomplete
variance: Incomplete
std_dev: Incomplete
median_abs_dev: Incomplete
rel_std_dev: Incomplete
skewness: Incomplete
kurtosis: Incomplete
pearson_type: Incomplete

def format_histogram_counts(bin_counts, width: Incomplete | None = ..., format_bin: Incomplete | None = ...): ...
