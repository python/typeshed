from typing import Any

from stripe import error as error, util as util

class Webhook:
    DEFAULT_TOLERANCE: int
    @staticmethod
    def construct_event(payload, sig_header, secret, tolerance=..., api_key: Any | None = ...): ...

class WebhookSignature:
    EXPECTED_SCHEME: str
    @classmethod
    def verify_header(cls, payload, header, secret, tolerance: Any | None = ...): ...
