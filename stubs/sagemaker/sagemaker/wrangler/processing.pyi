from _typeshed import Incomplete
from typing import Dict, List

from sagemaker.network import NetworkConfig
from sagemaker.processing import Processor
from sagemaker.session import Session

class DataWranglerProcessor(Processor):
    data_wrangler_flow_source: Incomplete
    sagemaker_session: Incomplete
    def __init__(
        self,
        role: str = None,
        data_wrangler_flow_source: str = None,
        instance_count: int = None,
        instance_type: str = None,
        volume_size_in_gb: int = 30,
        volume_kms_key: str = None,
        output_kms_key: str = None,
        max_runtime_in_seconds: int = None,
        base_job_name: str = None,
        sagemaker_session: Session = None,
        env: Dict[str, str] = None,
        tags: List[dict] = None,
        network_config: NetworkConfig = None,
    ) -> None: ...
