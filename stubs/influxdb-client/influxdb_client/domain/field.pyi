from _typeshed import Incomplete

class Field:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        value: Incomplete | None = ...,
        type: Incomplete | None = ...,
        alias: Incomplete | None = ...,
        args: Incomplete | None = ...,
    ) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def alias(self): ...
    @alias.setter
    def alias(self, alias) -> None: ...
    @property
    def args(self): ...
    @args.setter
    def args(self, args) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
