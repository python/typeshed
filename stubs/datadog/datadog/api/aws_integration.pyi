from datadog.api.resources import (
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPISubResource,
    UpdatableAPIResource,
    UpdatableAPISubResource,
)

class AwsIntegration(
    GetableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPISubResource,
    UpdatableAPIResource,
    UpdatableAPISubResource,
):
    @classmethod
    def list(cls, **params): ...
    @classmethod
    def create(cls, **params): ...
    @classmethod
    def update(cls, **body): ...
    @classmethod
    def delete(cls, **body): ...
    @classmethod
    def list_namespace_rules(cls, **params): ...
    @classmethod
    def generate_new_external_id(cls, **params): ...
