from typing import Any

from ..span import Span
from ..tracer import Tracer
from .context import SpanContext
from .tracer import MockTracer

class MockSpan(Span):
    operation_name: str | None
    start_time: Any
    parent_id: int | None
    tags: dict[str, Any]
    finish_time: float
    finished: bool
    logs: list[LogData]
    def __init__(
        self,
        tracer: Tracer,
        operation_name: str | None = ...,
        context: SpanContext | None = ...,
        parent_id: int | None = ...,
        tags: dict[str, Any] | None = ...,
        start_time: float | None = ...,
    ) -> None: ...
    @property
    def tracer(self) -> MockTracer: ...
    def set_operation_name(self, operation_name: str) -> MockSpan: ...
    def set_tag(self, key: str, value: str | bool | int | float) -> MockSpan: ...
    def log_kv(self, key_values: dict[str, Any], timestamp: float | None = ...) -> MockSpan: ...
    def set_baggage_item(self, key: str, value: str) -> MockSpan: ...
    def __enter__(self) -> MockSpan: ...
    def log_event(self, event: Any, payload: Any | None = ...) -> MockSpan: ...
    def log(self, **kwargs: Any) -> MockSpan: ...

class LogData:
    key_values: dict[str, Any]
    timestamp: float | None
    def __init__(self, key_values: dict[str, Any], timestamp: float | None = ...) -> None: ...
