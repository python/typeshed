from typing import Any, Type, TypeVar

from stripe.api_resources.abstract.api_resource import APIResource as APIResource

_T = TypeVar("_T")

class UpdateableAPIResource(APIResource):
    @classmethod
    def modify(cls: Type[_T], sid, **params) -> _T: ...
    def save(self, idempotency_key: Any | None = ...): ...
