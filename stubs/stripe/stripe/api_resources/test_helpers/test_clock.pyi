from _typeshed import Self
from typing import Any, Literal
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource

class TestClock(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME: Literal["test_helpers.test_clock"]

    @classmethod
    def advance(cls, idempotency_key: str | None = None, **params: Any) -> Self: ...
    def advance(self, idempotency_key: str | None = None, **params: Any) -> Self: ...
