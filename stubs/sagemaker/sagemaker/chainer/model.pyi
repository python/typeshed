from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker import ModelMetrics
from sagemaker.drift_check_baselines import DriftCheckBaselines
from sagemaker.metadata_properties import MetadataProperties
from sagemaker.model import FrameworkModel
from sagemaker.predictor import Predictor
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class ChainerPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class ChainerModel(FrameworkModel):
    framework_version: Incomplete
    py_version: Incomplete
    model_server_workers: Incomplete
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: str | None = None,
        entry_point: str | None = None,
        image_uri: str | PipelineVariable | None = None,
        framework_version: str | None = None,
        py_version: str | None = None,
        predictor_cls: callable = ...,
        model_server_workers: int | PipelineVariable | None = None,
        **kwargs,
    ) -> None: ...
    image_uri: Incomplete
    def register(
        self,
        content_types: list[str | PipelineVariable],
        response_types: list[str | PipelineVariable],
        inference_instances: list[str | PipelineVariable] | None = None,
        transform_instances: list[str | PipelineVariable] | None = None,
        model_package_name: str | PipelineVariable | None = None,
        model_package_group_name: str | PipelineVariable | None = None,
        image_uri: str | PipelineVariable | None = None,
        model_metrics: ModelMetrics | None = None,
        metadata_properties: MetadataProperties | None = None,
        marketplace_cert: bool = False,
        approval_status: str | PipelineVariable | None = None,
        description: str | None = None,
        drift_check_baselines: DriftCheckBaselines | None = None,
        customer_metadata_properties: dict[str, str | PipelineVariable] | None = None,
        domain: str | PipelineVariable | None = None,
        sample_payload_url: str | PipelineVariable | None = None,
        task: str | PipelineVariable | None = None,
        framework: str | PipelineVariable | None = None,
        framework_version: str | PipelineVariable | None = None,
        nearest_model_name: str | PipelineVariable | None = None,
        data_input_configuration: str | PipelineVariable | None = None,
    ): ...
    def prepare_container_def(
        self,
        instance_type: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
    ): ...
    def serving_image_uri(
        self,
        region_name,
        instance_type,
        accelerator_type: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
    ): ...
