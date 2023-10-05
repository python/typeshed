from datadog.api.resources import (
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource,
)

class Dashboard(GetableAPIResource, CreateableAPIResource, UpdatableAPIResource, DeletableAPIResource, ListableAPIResource): ...
