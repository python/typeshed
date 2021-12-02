from typing import Any

from .tracer import Tracer

class SpanContext:
    EMPTY_BAGGAGE: Any
    @property
    def baggage(self): ...

class Span:
    def __init__(self, tracer: Tracer, context: SpanContext) -> None: ...
    @property
    def context(self): ...
    @property
    def tracer(self): ...
    def set_operation_name(self, operation_name: str): ...
    def finish(self, finish_time: Any | None = ...) -> None: ...
    def set_tag(self, key: Any, value: Any): ...
    def log_kv(self, key_values: Any, timestamp: Any | None = ...): ...
    def set_baggage_item(self, key: Any, value: Any): ...
    def get_baggage_item(self, key: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def log_event(self, event: Any, payload: Any | None = ...): ...
    def log(self, **kwargs: Any): ...
