from _typeshed import Incomplete
from typing import List, Optional, Union

from sagemaker.workflow.entities import PipelineVariable

class NetworkConfig:
    enable_network_isolation: Incomplete
    security_group_ids: Incomplete
    subnets: Incomplete
    encrypt_inter_container_traffic: Incomplete
    def __init__(
        self,
        enable_network_isolation: Union[bool, PipelineVariable] = None,
        security_group_ids: Optional[List[Union[str, PipelineVariable]]] = None,
        subnets: Optional[List[Union[str, PipelineVariable]]] = None,
        encrypt_inter_container_traffic: Optional[Union[bool, PipelineVariable]] = None,
    ) -> None: ...
