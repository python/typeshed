from datadog.api.resources import (
    ActionAPIResource,
    CreateableAPIResource,
    CustomUpdatableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
)

class Permissions(
    ActionAPIResource,
    CreateableAPIResource,
    CustomUpdatableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
): ...
