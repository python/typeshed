from typing import Any

from stripe.api_resources.abstract import (
    CreateableAPIResource as CreateableAPIResource,
    ListableAPIResource as ListableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
    custom_method as custom_method,
)

class Order(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME: str
    def cancel(self, idempotency_key: str | None = ..., **params): ...
    def list_line_items(self, idempotency_key: str | None = ..., **params): ...
    def reopen(self, idempotency_key: str | None = ..., **params): ...
    def submit(self, idempotency_key: str | None = ..., **params): ...
