from typing import Any

from ..span import SpanContext
from .propagator import Propagator

class BinaryPropagator(Propagator):
    def inject(self, span_context: SpanContext, carrier: Any) -> None: ...
    def extract(self, carrier: Any): ...
