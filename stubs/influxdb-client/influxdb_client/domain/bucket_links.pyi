from _typeshed import Incomplete

class BucketLinks:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        labels: Incomplete | None = ...,
        members: Incomplete | None = ...,
        org: Incomplete | None = ...,
        owners: Incomplete | None = ...,
        _self: Incomplete | None = ...,
        write: Incomplete | None = ...,
    ) -> None: ...
    @property
    def labels(self): ...
    @labels.setter
    def labels(self, labels) -> None: ...
    @property
    def members(self): ...
    @members.setter
    def members(self, members) -> None: ...
    @property
    def org(self): ...
    @org.setter
    def org(self, org) -> None: ...
    @property
    def owners(self): ...
    @owners.setter
    def owners(self, owners) -> None: ...
    @property
    def write(self): ...
    @write.setter
    def write(self, write) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
