from typing import Any

from .propagator import Propagator

prefix_tracer_state: str
prefix_baggage: str
field_name_trace_id: Any
field_name_span_id: Any
field_count: int

class TextPropagator(Propagator):
    def inject(self, span_context, carrier) -> None: ...
    def extract(self, carrier): ...
