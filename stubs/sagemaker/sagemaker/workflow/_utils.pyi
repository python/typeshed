from _typeshed import Incomplete
from typing import List, Optional

from sagemaker.estimator import EstimatorBase
from sagemaker.workflow.entities import RequestType as RequestType
from sagemaker.workflow.retry import RetryPolicy
from sagemaker.workflow.steps import ConfigurableRetryStep, Step, TrainingStep

logger: Incomplete
FRAMEWORK_VERSION: str
INSTANCE_TYPE: str
REPACK_SCRIPT: str
REPACK_SCRIPT_LAUNCHER: str
LAUNCH_REPACK_SCRIPT_CMD: str

class _RepackModelStep(TrainingStep):
    sagemaker_session: Incomplete
    role: Incomplete
    def __init__(
        self,
        name: str,
        sagemaker_session,
        role,
        model_data: str,
        entry_point: str,
        display_name: str = None,
        description: str = None,
        source_dir: str = None,
        dependencies: List = None,
        depends_on: Optional[List[str | Step | "StepCollection"]] = None,
        retry_policies: List[RetryPolicy] = None,
        subnets: Incomplete | None = None,
        security_group_ids: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...

class _RegisterModelStep(ConfigurableRetryStep):
    step_args: Incomplete
    estimator: Incomplete
    model_data: Incomplete
    content_types: Incomplete
    response_types: Incomplete
    inference_instances: Incomplete
    transform_instances: Incomplete
    model_package_group_name: Incomplete
    tags: Incomplete
    model_metrics: Incomplete
    drift_check_baselines: Incomplete
    customer_metadata_properties: Incomplete
    domain: Incomplete
    sample_payload_url: Incomplete
    task: Incomplete
    metadata_properties: Incomplete
    approval_status: Incomplete
    image_uri: Incomplete
    compile_model_family: Incomplete
    description: Incomplete
    kwargs: Incomplete
    container_def_list: Incomplete
    def __init__(
        self,
        name: str,
        step_args: Optional[dict] = None,
        content_types: Optional[list] = None,
        response_types: Optional[list] = None,
        inference_instances: Optional[list] = None,
        transform_instances: Optional[list] = None,
        estimator: EstimatorBase = None,
        model_data: Incomplete | None = None,
        model_package_group_name: Incomplete | None = None,
        model_metrics: Incomplete | None = None,
        metadata_properties: Incomplete | None = None,
        approval_status: str = "PendingManualApproval",
        image_uri: Incomplete | None = None,
        compile_model_family: Incomplete | None = None,
        display_name: str = None,
        description: Incomplete | None = None,
        depends_on: Optional[List[str | Step | "StepCollection"]] = None,
        retry_policies: Optional[List[RetryPolicy]] = None,
        tags: Incomplete | None = None,
        container_def_list: Incomplete | None = None,
        drift_check_baselines: Incomplete | None = None,
        customer_metadata_properties: Incomplete | None = None,
        domain: Incomplete | None = None,
        sample_payload_url: Incomplete | None = None,
        task: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
