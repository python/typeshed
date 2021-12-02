from typing import Any

from opentracing import Tracer

class MockTracer(Tracer):
    def __init__(self, scope_manager: Any | None = ...) -> None: ...
    def register_propagator(self, format, propagator) -> None: ...
    def finished_spans(self): ...
    def reset(self) -> None: ...
    def start_active_span(
        self,
        operation_name,
        child_of: Any | None = ...,
        references: Any | None = ...,
        tags: Any | None = ...,
        start_time: Any | None = ...,
        ignore_active_span: bool = ...,
        finish_on_close: bool = ...,
    ): ...
    def start_span(
        self,
        operation_name: Any | None = ...,
        child_of: Any | None = ...,
        references: Any | None = ...,
        tags: Any | None = ...,
        start_time: Any | None = ...,
        ignore_active_span: bool = ...,
    ): ...
    def inject(self, span_context, format, carrier) -> None: ...
    def extract(self, format, carrier): ...
