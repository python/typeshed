from _typeshed import Incomplete

class TimedContextManagerDecorator:
    statsd: Incomplete
    timing_func: Incomplete
    metric: Incomplete
    tags: Incomplete
    sample_rate: Incomplete
    use_ms: Incomplete
    elapsed: Incomplete
    def __init__(
        self,
        statsd,
        metric: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        use_ms: Incomplete | None = None,
    ) -> None: ...
    def __call__(self, func): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class DistributedContextManagerDecorator(TimedContextManagerDecorator):
    timing_func: Incomplete
    def __init__(
        self,
        statsd,
        metric: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        use_ms: Incomplete | None = None,
    ) -> None: ...
