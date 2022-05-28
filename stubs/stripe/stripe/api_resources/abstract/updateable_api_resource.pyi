from _typeshed import Self
from typing import Any

from stripe.api_resources.abstract.api_resource import APIResource as APIResource

class UpdateableAPIResource(APIResource):
    @classmethod
    def modify(cls: type[Self], sid, **params) -> Self: ...
    def save(self, idempotency_key: Any | None = ...): ...
