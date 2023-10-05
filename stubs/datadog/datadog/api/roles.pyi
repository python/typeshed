from datadog.api.resources import (
    ActionAPIResource,
    CreateableAPIResource,
    CustomUpdatableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
)

class Roles(
    ActionAPIResource,
    CreateableAPIResource,
    CustomUpdatableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
):
    @classmethod
    def update(cls, id, **body): ...
    @classmethod
    def assign_permission(cls, id, **body): ...
    @classmethod
    def unassign_permission(cls, id, **body): ...
