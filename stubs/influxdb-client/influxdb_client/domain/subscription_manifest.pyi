from _typeshed import Incomplete

class SubscriptionManifest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, name: Incomplete | None = ..., mode: Incomplete | None = ..., destinations: Incomplete | None = ...
    ) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def mode(self): ...
    @mode.setter
    def mode(self, mode) -> None: ...
    @property
    def destinations(self): ...
    @destinations.setter
    def destinations(self, destinations) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
