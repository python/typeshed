from _typeshed import Incomplete
from typing import List, Optional

from sagemaker.workflow.entities import PipelineVariable

class NetworkConfig:
    enable_network_isolation: Incomplete
    security_group_ids: Incomplete
    subnets: Incomplete
    encrypt_inter_container_traffic: Incomplete
    def __init__(
        self,
        enable_network_isolation: bool | PipelineVariable | None = None,
        security_group_ids: list[str | PipelineVariable] | None = None,
        subnets: list[str | PipelineVariable] | None = None,
        encrypt_inter_container_traffic: bool | PipelineVariable | None = None,
    ) -> None: ...
