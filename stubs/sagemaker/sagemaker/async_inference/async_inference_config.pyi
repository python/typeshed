from _typeshed import Incomplete

class AsyncInferenceConfig:
    output_path: Incomplete
    max_concurrent_invocations_per_instance: Incomplete
    kms_key_id: Incomplete
    notification_config: Incomplete
    failure_path: Incomplete
    def __init__(
        self,
        output_path: Incomplete | None = None,
        max_concurrent_invocations_per_instance: Incomplete | None = None,
        kms_key_id: Incomplete | None = None,
        notification_config: Incomplete | None = None,
        failure_path: Incomplete | None = None,
    ) -> None: ...
