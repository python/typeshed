from _typeshed import Incomplete

class MeasurementSchema:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        bucket_id: Incomplete | None = ...,
        name: Incomplete | None = ...,
        columns: Incomplete | None = ...,
        created_at: Incomplete | None = ...,
        updated_at: Incomplete | None = ...,
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
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def columns(self): ...
    @columns.setter
    def columns(self, columns) -> None: ...
    @property
    def created_at(self): ...
    @created_at.setter
    def created_at(self, created_at) -> None: ...
    @property
    def updated_at(self): ...
    @updated_at.setter
    def updated_at(self, updated_at) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
