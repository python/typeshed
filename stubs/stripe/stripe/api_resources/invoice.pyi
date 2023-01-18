from _typeshed import Incomplete, Self

from stripe import api_requestor as api_requestor
from stripe.api_resources.abstract import (
    CreateableAPIResource as CreateableAPIResource,
    DeletableAPIResource as DeletableAPIResource,
    ListableAPIResource as ListableAPIResource,
    SearchableAPIResource as SearchableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
    custom_method as custom_method,
)

class Invoice(CreateableAPIResource, DeletableAPIResource, ListableAPIResource, SearchableAPIResource, UpdateableAPIResource):
    OBJECT_NAME: str
    def finalize_invoice(self: Self, idempotency_key: str | None = ..., **params) -> Self: ...
    def mark_uncollectible(self: Self, idempotency_key: str | None = ..., **params) -> Self: ...
    def pay(self: Self, idempotency_key: str | None = ..., **params) -> Self: ...
    def send_invoice(self: Self, idempotency_key: str | None = ..., **params) -> Self: ...
    def void_invoice(self: Self, idempotency_key: str | None = ..., **params) -> Self: ...
    @classmethod
    def upcoming(
        cls,
        api_key: Incomplete | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ) -> Invoice: ...
