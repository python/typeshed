from typing import Any

class Tracer:
    def __init__(self, scope_manager: Any | None = ...) -> None: ...
    @property
    def scope_manager(self): ...
    @property
    def active_span(self): ...
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

class ReferenceType:
    CHILD_OF: str
    FOLLOWS_FROM: str

class Reference: ...

def child_of(referenced_context: Any | None = ...): ...
def follows_from(referenced_context: Any | None = ...): ...
def start_child_span(parent_span, operation_name, tags: Any | None = ..., start_time: Any | None = ...): ...
