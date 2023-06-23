from _typeshed import Incomplete

class CheckJobConfig:
    role: Incomplete
    instance_count: Incomplete
    instance_type: Incomplete
    volume_size_in_gb: Incomplete
    volume_kms_key: Incomplete
    output_kms_key: Incomplete
    max_runtime_in_seconds: Incomplete
    base_job_name: Incomplete
    sagemaker_session: Incomplete
    env: Incomplete
    tags: Incomplete
    network_config: Incomplete
    def __init__(
        self,
        role,
        instance_count: int = 1,
        instance_type: str = "ml.m5.xlarge",
        volume_size_in_gb: int = 30,
        volume_kms_key: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        max_runtime_in_seconds: Incomplete | None = None,
        base_job_name: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
        env: Incomplete | None = None,
        tags: Incomplete | None = None,
        network_config: Incomplete | None = None,
    ) -> None: ...
