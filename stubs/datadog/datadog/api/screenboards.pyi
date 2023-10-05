from datadog.api.resources import (
    ActionAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource,
)

class Screenboard(
    GetableAPIResource, CreateableAPIResource, UpdatableAPIResource, DeletableAPIResource, ActionAPIResource, ListableAPIResource
):
    @classmethod
    def share(cls, board_id): ...
    @classmethod
    def revoke(cls, board_id): ...
