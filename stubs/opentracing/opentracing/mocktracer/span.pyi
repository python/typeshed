from typing import Any

from opentracing import Span

class MockSpan(Span):
    operation_name: Any
    start_time: Any
    parent_id: Any
    tags: Any
    finish_time: int
    finished: bool
    logs: Any
    def __init__(
        self,
        tracer,
        operation_name: Any | None = ...,
        context: Any | None = ...,
        parent_id: Any | None = ...,
        tags: Any | None = ...,
        start_time: Any | None = ...,
    ) -> None: ...
    def set_operation_name(self, operation_name: str) -> Any: ...
    def set_tag(self, key: Any, value: Any) -> Any: ...
    def log_kv(self, key_values: Any, timestamp: Any | None = ...) -> Any: ...
    def finish(self, finish_time: Any | None = ...) -> None: ...
    def set_baggage_item(self, key: Any, value: Any) -> Any: ...
    def get_baggage_item(self, key: Any) -> Any: ...

class LogData:
    key_values: Any
    timestamp: Any
    def __init__(self, key_values: Any, timestamp: Any | None = ...) -> None: ...
