from _typeshed import Incomplete
from typing import List, Optional, Union

from sagemaker import PipelineModel
from sagemaker.estimator import EstimatorBase
from sagemaker.model import Model
from sagemaker.workflow.entities import RequestType as RequestType
from sagemaker.workflow.retry import RetryPolicy
from sagemaker.workflow.steps import Step

class StepCollection:
    name: str
    steps: List[Step]
    def request_dicts(self) -> List[RequestType]: ...
    @property
    def properties(self): ...
    def __init__(self, name, steps) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class RegisterModel(StepCollection):
    name: Incomplete
    model_list: Incomplete
    container_def_list: Incomplete
    steps: Incomplete
    def __init__(
        self,
        name: str,
        content_types,
        response_types,
        inference_instances: Incomplete | None = None,
        transform_instances: Incomplete | None = None,
        estimator: EstimatorBase = None,
        model_data: Incomplete | None = None,
        depends_on: Optional[List[str | Step | StepCollection]] = None,
        repack_model_step_retry_policies: List[RetryPolicy] = None,
        register_model_step_retry_policies: List[RetryPolicy] = None,
        model_package_group_name: Incomplete | None = None,
        model_metrics: Incomplete | None = None,
        approval_status: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        compile_model_family: Incomplete | None = None,
        display_name: Incomplete | None = None,
        description: Incomplete | None = None,
        tags: Incomplete | None = None,
        model: Model | PipelineModel = None,
        drift_check_baselines: Incomplete | None = None,
        customer_metadata_properties: Incomplete | None = None,
        domain: Incomplete | None = None,
        sample_payload_url: Incomplete | None = None,
        task: Incomplete | None = None,
        framework: Incomplete | None = None,
        framework_version: Incomplete | None = None,
        nearest_model_name: Incomplete | None = None,
        data_input_configuration: Incomplete | None = None,
        **kwargs,
    ) -> None: ...

class EstimatorTransformer(StepCollection):
    name: Incomplete
    steps: Incomplete
    def __init__(
        self,
        name: str,
        estimator: EstimatorBase,
        model_data,
        model_inputs,
        instance_count,
        instance_type,
        transform_inputs,
        description: str = None,
        display_name: str = None,
        image_uri: Incomplete | None = None,
        predictor_cls: Incomplete | None = None,
        env: Incomplete | None = None,
        strategy: Incomplete | None = None,
        assemble_with: Incomplete | None = None,
        output_path: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        accept: Incomplete | None = None,
        max_concurrent_transforms: Incomplete | None = None,
        max_payload: Incomplete | None = None,
        tags: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        depends_on: Optional[List[str | Step | StepCollection]] = None,
        repack_model_step_retry_policies: List[RetryPolicy] = None,
        model_step_retry_policies: List[RetryPolicy] = None,
        transform_step_retry_policies: List[RetryPolicy] = None,
        **kwargs,
    ) -> None: ...
