from _typeshed import Incomplete

from sagemaker.network import NetworkConfig
from sagemaker.processing import Processor
from sagemaker.session import Session

class DataWranglerProcessor(Processor):
    data_wrangler_flow_source: Incomplete
    sagemaker_session: Incomplete
    def __init__(
        self,
        role: str | None = None,
        data_wrangler_flow_source: str | None = None,
        instance_count: int | None = None,
        instance_type: str | None = None,
        volume_size_in_gb: int = 30,
        volume_kms_key: str | None = None,
        output_kms_key: str | None = None,
        max_runtime_in_seconds: int | None = None,
        base_job_name: str | None = None,
        sagemaker_session: Session | None = None,
        env: dict[str, str] | None = None,
        tags: list[dict] | None = None,
        network_config: NetworkConfig | None = None,
    ) -> None: ...
