from _typeshed import Incomplete

class TelegrafPluginRequestPlugins:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: Incomplete | None = ...,
        name: Incomplete | None = ...,
        alias: Incomplete | None = ...,
        description: Incomplete | None = ...,
        config: Incomplete | None = ...,
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def alias(self): ...
    @alias.setter
    def alias(self, alias) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def config(self): ...
    @config.setter
    def config(self, config) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
