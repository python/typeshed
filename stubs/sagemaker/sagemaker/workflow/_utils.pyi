from _typeshed import Incomplete
from typing import Any

from sagemaker.estimator import EstimatorBase
from sagemaker.workflow.entities import RequestType as RequestType
from sagemaker.workflow.retry import RetryPolicy
from sagemaker.workflow.step_collections import StepCollection
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
        display_name: str | None = None,
        description: str | None = None,
        source_dir: str | None = None,
        dependencies: list[str] | None = None,
        depends_on: list[str | Step | StepCollection] | None = None,
        retry_policies: list[RetryPolicy] | None = None,
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
        step_args: dict[Any, Any] | None = None,
        content_types: list[Any] | None = None,
        response_types: list[Any] | None = None,
        inference_instances: list[Any] | None = None,
        transform_instances: list[Any] | None = None,
        estimator: EstimatorBase | None = None,
        model_data: Incomplete | None = None,
        model_package_group_name: Incomplete | None = None,
        model_metrics: Incomplete | None = None,
        metadata_properties: Incomplete | None = None,
        approval_status: str = "PendingManualApproval",
        image_uri: Incomplete | None = None,
        compile_model_family: Incomplete | None = None,
        display_name: str | None = None,
        description: Incomplete | None = None,
        depends_on: list[str | Step | StepCollection] | None = None,
        retry_policies: list[RetryPolicy] | None = None,
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
