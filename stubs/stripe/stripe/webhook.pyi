from typing import Any

from stripe import error as error

class Webhook:
    DEFAULT_TOLERANCE: int
    @staticmethod
    def construct_event(
        payload: bytes | str, sig_header: str, secret: str, tolerance: int = ..., api_key: str | None = ...
    ) -> stripe.Event: ...

class WebhookSignature:
    EXPECTED_SCHEME: str
    @classmethod
    def verify_header(cls, payload: bytes | str, header: str, secret: str, tolerance: int | None = ...) -> bool: ...
    @classmethod
    def _compute_signature(cls, payload: str, secret: str) -> str: ...
