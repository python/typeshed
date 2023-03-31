from _typeshed import Incomplete

class DBRP:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        org_id: Incomplete | None = None,
        bucket_id: Incomplete | None = None,
        database: Incomplete | None = None,
        retention_policy: Incomplete | None = None,
        default: Incomplete | None = None,
        links: Incomplete | None = None,
    ) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def bucket_id(self): ...
    @bucket_id.setter
    def bucket_id(self, bucket_id) -> None: ...
    @property
    def database(self): ...
    @database.setter
    def database(self, database) -> None: ...
    @property
    def retention_policy(self): ...
    @retention_policy.setter
    def retention_policy(self, retention_policy) -> None: ...
    @property
    def default(self): ...
    @default.setter
    def default(self, default) -> None: ...
    @property
    def links(self): ...
    @links.setter
    def links(self, links) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
