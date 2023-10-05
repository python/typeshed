from datadog.api.resources import (
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource,
)

class Timeboard(GetableAPIResource, CreateableAPIResource, UpdatableAPIResource, ListableAPIResource, DeletableAPIResource): ...
