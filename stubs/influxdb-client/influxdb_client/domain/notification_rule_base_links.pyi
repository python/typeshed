from _typeshed import Incomplete

class NotificationRuleBaseLinks:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        _self: Incomplete | None = None,
        labels: Incomplete | None = None,
        members: Incomplete | None = None,
        owners: Incomplete | None = None,
        query: Incomplete | None = None,
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
    @property
    def query(self): ...
    @query.setter
    def query(self, query) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
