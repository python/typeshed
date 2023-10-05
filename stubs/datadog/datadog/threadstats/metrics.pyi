from _typeshed import Incomplete

class Metric:
    def add_point(self, value) -> None: ...
    def flush(self, timestamp, interval) -> None: ...

class Set(Metric):
    stats_tag: str
    name: Incomplete
    tags: Incomplete
    host: Incomplete
    set: Incomplete
    def __init__(self, name, tags, host) -> None: ...
    def add_point(self, value) -> None: ...
    def flush(self, timestamp, interval): ...

class Gauge(Metric):
    stats_tag: str
    name: Incomplete
    tags: Incomplete
    host: Incomplete
    value: Incomplete
    def __init__(self, name, tags, host) -> None: ...
    def add_point(self, value) -> None: ...
    def flush(self, timestamp, interval): ...

class Counter(Metric):
    stats_tag: str
    name: Incomplete
    tags: Incomplete
    host: Incomplete
    count: Incomplete
    def __init__(self, name, tags, host) -> None: ...
    def add_point(self, value) -> None: ...
    def flush(self, timestamp, interval): ...

class Distribution(Metric):
    stats_tag: str
    name: Incomplete
    tags: Incomplete
    host: Incomplete
    value: Incomplete
    def __init__(self, name, tags, host) -> None: ...
    def add_point(self, value) -> None: ...
    def flush(self, timestamp, interval): ...

class Histogram(Metric):
    stats_tag: str
    name: Incomplete
    tags: Incomplete
    host: Incomplete
    max: Incomplete
    min: Incomplete
    sum: Incomplete
    iter_counter: Incomplete
    count: Incomplete
    sample_size: int
    samples: Incomplete
    percentiles: Incomplete
    def __init__(self, name, tags, host) -> None: ...
    def add_point(self, value) -> None: ...
    def flush(self, timestamp, interval): ...
    def average(self): ...

class Timing(Histogram):
    stats_tag: str

class MetricsAggregator:
    def __init__(self, roll_up_interval: int = 10) -> None: ...
    def add_point(
        self, metric, tags, timestamp, value, metric_class, sample_rate: int = 1, host: Incomplete | None = None
    ) -> None: ...
    def flush(self, timestamp): ...
