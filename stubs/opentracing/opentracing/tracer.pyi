from .scope_manager import ScopeManager
from .span import Span, SpanContext

class Tracer:
    def __init__(self, scope_manager: ScopeManager | None = ...) -> None: ...
    @property
    def scope_manager(self) -> ScopeManager: ...
    @property
    def active_span(self) -> Span: ...
    def start_active_span(
        self,
        operation_name: str,
        child_of=...,
        references=...,
        tags=...,
        start_time=...,
        ignore_active_span: bool = ...,
        finish_on_close: bool = ...,
    ): ...
    def start_span(
        self,
        operation_name: str | None = ...,
        child_of=...,
        references=...,
        tags=...,
        start_time=...,
        ignore_active_span: bool = ...,
    ): ...
    def inject(self, span_context: SpanContext, format, carrier) -> None: ...
    def extract(self, format, carrier): ...

class ReferenceType:
    CHILD_OF: str
    FOLLOWS_FROM: str

class Reference: ...

def child_of(referenced_context=...): ...
def follows_from(referenced_context=...): ...
def start_child_span(parent_span: Span, operation_name: str, tags=..., start_time=...): ...
