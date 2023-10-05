from datadog.api.resources import (
    ActionAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource,
)

class Downtime(
    GetableAPIResource, CreateableAPIResource, UpdatableAPIResource, ListableAPIResource, DeletableAPIResource, ActionAPIResource
):
    @classmethod
    def cancel_downtime_by_scope(cls, **body): ...
