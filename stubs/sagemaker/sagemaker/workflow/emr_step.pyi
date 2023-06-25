from _typeshed import Incomplete
from typing import Any, Dict, List, Optional

from sagemaker.workflow.entities import RequestType as RequestType
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import CacheConfig, Step

class EMRStepConfig:
    jar: Incomplete
    args: Incomplete
    main_class: Incomplete
    properties: Incomplete
    def __init__(self, jar, args: list[str] | None = None, main_class: str | None = None, properties: list[dict] | None = None) -> None: ...
    def to_request(self) -> RequestType: ...

INSTANCES: str
INSTANCEGROUPS: str
INSTANCEFLEETS: str
ERR_STR_WITH_NAME_AUTO_TERMINATION_OR_STEPS: str
ERR_STR_WITHOUT_INSTANCE: Incomplete
ERR_STR_WITH_KEEPJOBFLOW_OR_TERMINATIONPROTECTED: Incomplete
ERR_STR_BOTH_OR_NONE_INSTANCEGROUPS_OR_INSTANCEFLEETS: Incomplete
ERR_STR_WITH_BOTH_CLUSTER_ID_AND_CLUSTER_CFG: str
ERR_STR_WITH_EXEC_ROLE_ARN_AND_WITHOUT_CLUSTER_ID: str
ERR_STR_WITHOUT_CLUSTER_ID_AND_CLUSTER_CFG: str

class EMRStep(Step):
    args: Incomplete
    cache_config: Incomplete
    def __init__(
        self,
        name: str,
        display_name: str,
        description: str,
        cluster_id: str,
        step_config: EMRStepConfig,
        depends_on: list[str | Step | StepCollection] | None = None,
        cache_config: CacheConfig | None = None,
        cluster_config: dict[str, Any] | None = None,
        execution_role_arn: str | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self) -> RequestType: ...
    def to_request(self) -> RequestType: ...
