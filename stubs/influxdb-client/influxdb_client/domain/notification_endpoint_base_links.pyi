from _typeshed import Incomplete

class NotificationEndpointBaseLinks:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        _self: Incomplete | None = ...,
        labels: Incomplete | None = ...,
        members: Incomplete | None = ...,
        owners: Incomplete | None = ...,
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
    def owners(self): ...
    @owners.setter
    def owners(self, owners) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
