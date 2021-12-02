from typing import Any

from .scope_manager import ScopeManager
from .span import Span, SpanContext

class Tracer:
    def __init__(self, scope_manager: ScopeManager | None = ...) -> None: ...
    @property
    def scope_manager(self): ...
    @property
    def active_span(self): ...
    def start_active_span(
        self,
        operation_name: str,
        child_of: Any | None = ...,
        references: Any | None = ...,
        tags: Any | None = ...,
        start_time: Any | None = ...,
        ignore_active_span: bool = ...,
        finish_on_close: bool = ...,
    ): ...
    def start_span(
        self,
        operation_name: str | None = ...,
        child_of: Any | None = ...,
        references: Any | None = ...,
        tags: Any | None = ...,
        start_time: Any | None = ...,
        ignore_active_span: bool = ...,
    ): ...
    def inject(self, span_context: SpanContext, format: Any, carrier: Any) -> None: ...
    def extract(self, format: Any, carrier: Any): ...

class ReferenceType:
    CHILD_OF: str
    FOLLOWS_FROM: str

class Reference: ...

def child_of(referenced_context: Any | None = ...): ...
def follows_from(referenced_context: Any | None = ...): ...
def start_child_span(parent_span: Span, operation_name: str, tags: Any | None = ..., start_time: Any | None = ...): ...
