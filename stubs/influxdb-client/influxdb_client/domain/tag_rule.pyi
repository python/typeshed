from _typeshed import Incomplete

class TagRule:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, key: Incomplete | None = ..., value: Incomplete | None = ..., operator: Incomplete | None = ...
    ) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    @property
    def operator(self): ...
    @operator.setter
    def operator(self, operator) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
