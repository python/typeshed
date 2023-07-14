from stripe.api_resources.abstract import (
    CreateableAPIResource as CreateableAPIResource,
    ListableAPIResource as ListableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
)

class PaymentLink(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME: str

    def list_line_items(self, idempotency_key=None, **params): ...
