from typing import overload

from stripe.api_resources.abstract import (
    CreateableAPIResource as CreateableAPIResource,
    ListableAPIResource as ListableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
)

class PaymentLink(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME: str

    @overload
    @classmethod
    def list_line_items(cls, payment_link, api_key=None, stripe_version=None, stripe_account=None, **params): ...
    @overload
    @classmethod
    def list_line_items(cls, idempotency_key=None, **params): ...
