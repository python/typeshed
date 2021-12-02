from typing import Any

from ..scope_manager import ScopeManager
from ..span import SpanContext
from ..tracer import Tracer
from .propagator import Propagator

class MockTracer(Tracer):
    def __init__(self, scope_manager: ScopeManager | None = ...) -> None: ...
    def register_propagator(self, format: Any, propagator: Propagator) -> None: ...
    def finished_spans(self) -> Any: ...
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
    ) -> Any: ...
    def start_span(
        self,
        operation_name: Any | None = ...,
        child_of: Any | None = ...,
        references: Any | None = ...,
        tags: Any | None = ...,
        start_time: Any | None = ...,
        ignore_active_span: bool = ...,
    ) -> Any: ...
    def inject(self, span_context: SpanContext, format: Any, carrier: Any) -> None: ...
    def extract(self, format: Any, carrier: Any) -> Any: ...
