from typing import Any

from ..span import SpanContext

class Propagator:
    def inject(self, span_context: SpanContext, carrier: Any) -> None: ...
    def extract(self, carrier: Any) -> None: ...
