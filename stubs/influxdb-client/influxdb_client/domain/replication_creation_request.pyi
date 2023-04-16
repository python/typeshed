from _typeshed import Incomplete

class ReplicationCreationRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        org_id: Incomplete | None = None,
        remote_id: Incomplete | None = None,
        local_bucket_id: Incomplete | None = None,
        remote_bucket_id: Incomplete | None = None,
        max_queue_size_bytes: int = 67108860,
        drop_non_retryable_data: bool = False,
    ) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def remote_id(self): ...
    @remote_id.setter
    def remote_id(self, remote_id) -> None: ...
    @property
    def local_bucket_id(self): ...
    @local_bucket_id.setter
    def local_bucket_id(self, local_bucket_id) -> None: ...
    @property
    def remote_bucket_id(self): ...
    @remote_bucket_id.setter
    def remote_bucket_id(self, remote_bucket_id) -> None: ...
    @property
    def max_queue_size_bytes(self): ...
    @max_queue_size_bytes.setter
    def max_queue_size_bytes(self, max_queue_size_bytes) -> None: ...
    @property
    def drop_non_retryable_data(self): ...
    @drop_non_retryable_data.setter
    def drop_non_retryable_data(self, drop_non_retryable_data) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
