from stripe.api_resources.abstract import (
    CreateableAPIResource as CreateableAPIResource,
    ListableAPIResource as ListableAPIResource,
    nested_resource_class_methods as nested_resource_class_methods,
)

class Session(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME: str
    def expire(self, idempotency_key: str | None = ..., **params): ...
    def list_line_items(self, idempotency_key: str | None = ..., **params): ...
