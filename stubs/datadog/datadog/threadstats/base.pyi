from _typeshed import Incomplete
from collections.abc import Generator

log: Incomplete
DD_ENV_TAGS_MAPPING: Incomplete

class ThreadStats:
    namespace: Incomplete
    constant_tags: Incomplete
    compress_payload: Incomplete
    def __init__(self, namespace: str = "", constant_tags: Incomplete | None = None, compress_payload: bool = False) -> None: ...
    flush_interval: Incomplete
    roll_up_interval: Incomplete
    device: Incomplete
    reporter: Incomplete
    flush_count: int
    def start(
        self,
        flush_interval: int = 10,
        roll_up_interval: int = 10,
        device: Incomplete | None = None,
        flush_in_thread: bool = True,
        flush_in_greenlet: bool = False,
        disabled: bool = False,
    ): ...
    def stop(self): ...
    def event(
        self,
        title,
        message,
        alert_type: Incomplete | None = None,
        aggregation_key: Incomplete | None = None,
        source_type_name: Incomplete | None = None,
        date_happened: Incomplete | None = None,
        priority: Incomplete | None = None,
        tags: Incomplete | None = None,
        hostname: Incomplete | None = None,
    ) -> None: ...
    def gauge(
        self,
        metric_name,
        value,
        timestamp: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        host: Incomplete | None = None,
    ) -> None: ...
    def set(
        self,
        metric_name,
        value,
        timestamp: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        host: Incomplete | None = None,
    ) -> None: ...
    def increment(
        self,
        metric_name,
        value: int = 1,
        timestamp: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        host: Incomplete | None = None,
    ) -> None: ...
    def decrement(
        self,
        metric_name,
        value: int = 1,
        timestamp: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        host: Incomplete | None = None,
    ) -> None: ...
    def histogram(
        self,
        metric_name,
        value,
        timestamp: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        host: Incomplete | None = None,
    ) -> None: ...
    def distribution(
        self,
        metric_name,
        value,
        timestamp: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        host: Incomplete | None = None,
    ) -> None: ...
    def timing(
        self,
        metric_name,
        value,
        timestamp: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: int = 1,
        host: Incomplete | None = None,
    ) -> None: ...
    def timer(
        self, metric_name, sample_rate: int = 1, tags: Incomplete | None = None, host: Incomplete | None = None
    ) -> Generator[None, None, None]: ...
    def timed(self, metric_name, sample_rate: int = 1, tags: Incomplete | None = None, host: Incomplete | None = None): ...
    def flush(self, timestamp: Incomplete | None = None): ...
