from typing import Any

from stripe import util as util

class VerifyMixin:
    def verify(self, idempotency_key: Any | None = ..., **params): ...
