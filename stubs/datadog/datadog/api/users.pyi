from datadog.api.resources import (
    ActionAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource,
)

class User(
    ActionAPIResource, GetableAPIResource, CreateableAPIResource, UpdatableAPIResource, ListableAPIResource, DeletableAPIResource
):
    @classmethod
    def invite(cls, emails): ...
