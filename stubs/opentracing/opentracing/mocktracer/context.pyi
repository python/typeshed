from typing import Any

import opentracing

class SpanContext(opentracing.SpanContext):
    trace_id: Any
    span_id: Any
    def __init__(self, trace_id=..., span_id=..., baggage=...) -> None: ...
    @property
    def baggage(self): ...
    def with_baggage_item(self, key, value): ...
