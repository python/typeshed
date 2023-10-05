from datadog.api.resources import (
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource,
)

class Tag(CreateableAPIResource, UpdatableAPIResource, GetableAPIResource, ListableAPIResource, DeletableAPIResource):
    @classmethod
    def create(cls, host, **body): ...
    @classmethod
    def update(cls, host, **body): ...
