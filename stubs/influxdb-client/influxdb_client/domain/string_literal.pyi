from _typeshed import Incomplete

from influxdb_client.domain.property_key import PropertyKey

class StringLiteral(PropertyKey):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, type: Incomplete | None = None, value: Incomplete | None = None) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
