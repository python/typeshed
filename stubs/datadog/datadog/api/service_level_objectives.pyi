from _typeshed import Incomplete

from datadog.api.resources import (
    ActionAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    GetableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource,
)

class ServiceLevelObjective(
    GetableAPIResource, CreateableAPIResource, UpdatableAPIResource, ListableAPIResource, DeletableAPIResource, ActionAPIResource
):
    @classmethod
    def create(
        cls,
        attach_host_name: bool = False,
        method: str = "POST",
        id: Incomplete | None = None,
        params: Incomplete | None = None,
        **body,
    ): ...
    @classmethod
    def get(cls, id, **params): ...
    @classmethod
    def get_all(
        cls,
        query: Incomplete | None = None,
        tags_query: Incomplete | None = None,
        metrics_query: Incomplete | None = None,
        ids: Incomplete | None = None,
        offset: int = 0,
        limit: int = 100,
        **params,
    ): ...
    @classmethod
    def update(cls, id, params: Incomplete | None = None, **body): ...
    @classmethod
    def delete(cls, id, **params): ...
    @classmethod
    def bulk_delete(cls, ops, **params): ...
    @classmethod
    def delete_many(cls, ids, **params): ...
    @classmethod
    def can_delete(cls, ids, **params): ...
    @classmethod
    def history(cls, id, from_ts, to_ts, **params): ...
    @classmethod
    def search(cls, **params): ...
