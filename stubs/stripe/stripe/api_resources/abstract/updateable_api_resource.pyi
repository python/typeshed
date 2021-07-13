from typing import Any

from stripe import util as util
from stripe.api_resources.abstract.api_resource import APIResource as APIResource

class UpdateableAPIResource(APIResource):
    @classmethod
    def modify(cls, sid, **params): ...
    def save(self, idempotency_key: Any | None = ...): ...
