from _typeshed import Incomplete

class DecimalPlaces:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, is_enforced: Incomplete | None = ..., digits: Incomplete | None = ...) -> None: ...
    @property
    def is_enforced(self): ...
    @is_enforced.setter
    def is_enforced(self, is_enforced) -> None: ...
    @property
    def digits(self): ...
    @digits.setter
    def digits(self, digits) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
