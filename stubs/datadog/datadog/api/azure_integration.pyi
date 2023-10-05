from datadog.api.resources import (
    AddableAPISubResource,
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    UpdatableAPIResource,
)

class AzureIntegration(
    GetableAPIResource, CreateableAPIResource, DeletableAPIResource, UpdatableAPIResource, AddableAPISubResource
):
    @classmethod
    def list(cls, **params): ...
    @classmethod
    def create(cls, **params): ...
    @classmethod
    def delete(cls, **body): ...
    @classmethod
    def update_host_filters(cls, **params): ...
    @classmethod
    def update(cls, **body): ...
