from _typeshed import Incomplete

from datadog.api.resources import (
    AddableAPISubResource,
    CreateableAPIResource,
    DeletableAPIResource,
    DeletableAPISubResource,
    GetableAPIResource,
    ListableAPIResource,
    ListableAPISubResource,
    UpdatableAPIResource,
    UpdatableAPISubResource,
)

class DashboardList(
    AddableAPISubResource,
    CreateableAPIResource,
    DeletableAPIResource,
    DeletableAPISubResource,
    GetableAPIResource,
    ListableAPIResource,
    ListableAPISubResource,
    UpdatableAPIResource,
    UpdatableAPISubResource,
):
    v2: Incomplete
