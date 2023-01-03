from _typeshed import Incomplete

from influxdb_client.domain.check_discriminator import CheckDiscriminator

class ThresholdCheck(CheckDiscriminator):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: str = ...,
        thresholds: Incomplete | None = ...,
        every: Incomplete | None = ...,
        offset: Incomplete | None = ...,
        tags: Incomplete | None = ...,
        status_message_template: Incomplete | None = ...,
        id: Incomplete | None = ...,
        name: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        task_id: Incomplete | None = ...,
        owner_id: Incomplete | None = ...,
        created_at: Incomplete | None = ...,
        updated_at: Incomplete | None = ...,
        query: Incomplete | None = ...,
        status: Incomplete | None = ...,
        description: Incomplete | None = ...,
        latest_completed: Incomplete | None = ...,
        last_run_status: Incomplete | None = ...,
        last_run_error: Incomplete | None = ...,
        labels: Incomplete | None = ...,
        links: Incomplete | None = ...,
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def thresholds(self): ...
    @thresholds.setter
    def thresholds(self, thresholds) -> None: ...
    @property
    def every(self): ...
    @every.setter
    def every(self, every) -> None: ...
    @property
    def offset(self): ...
    @offset.setter
    def offset(self, offset) -> None: ...
    @property
    def tags(self): ...
    @tags.setter
    def tags(self, tags) -> None: ...
    @property
    def status_message_template(self): ...
    @status_message_template.setter
    def status_message_template(self, status_message_template) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
