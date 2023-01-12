from _typeshed import Incomplete

class RetentionPolicyManifest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        replica_n: Incomplete | None = ...,
        duration: Incomplete | None = ...,
        shard_group_duration: Incomplete | None = ...,
        shard_groups: Incomplete | None = ...,
        subscriptions: Incomplete | None = ...,
    ) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def replica_n(self): ...
    @replica_n.setter
    def replica_n(self, replica_n) -> None: ...
    @property
    def duration(self): ...
    @duration.setter
    def duration(self, duration) -> None: ...
    @property
    def shard_group_duration(self): ...
    @shard_group_duration.setter
    def shard_group_duration(self, shard_group_duration) -> None: ...
    @property
    def shard_groups(self): ...
    @shard_groups.setter
    def shard_groups(self, shard_groups) -> None: ...
    @property
    def subscriptions(self): ...
    @subscriptions.setter
    def subscriptions(self, subscriptions) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
