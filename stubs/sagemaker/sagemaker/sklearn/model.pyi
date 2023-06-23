from _typeshed import Incomplete
from typing import Dict, List, Optional, Union

from sagemaker import ModelMetrics
from sagemaker.drift_check_baselines import DriftCheckBaselines
from sagemaker.metadata_properties import MetadataProperties
from sagemaker.model import FrameworkModel
from sagemaker.predictor import Predictor
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class SKLearnPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class SKLearnModel(FrameworkModel):
    framework_version: Incomplete
    py_version: Incomplete
    model_server_workers: Incomplete
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: Optional[str] = None,
        entry_point: Optional[str] = None,
        framework_version: Optional[str] = None,
        py_version: str = "py3",
        image_uri: Optional[str | PipelineVariable] = None,
        predictor_cls: callable = ...,
        model_server_workers: Optional[int | PipelineVariable] = None,
        **kwargs,
    ) -> None: ...
    image_uri: Incomplete
    def register(
        self,
        content_types: List[str | PipelineVariable],
        response_types: List[str | PipelineVariable],
        inference_instances: Optional[List[str | PipelineVariable]] = None,
        transform_instances: Optional[List[str | PipelineVariable]] = None,
        model_package_name: Optional[str | PipelineVariable] = None,
        model_package_group_name: Optional[str | PipelineVariable] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        model_metrics: Optional[ModelMetrics] = None,
        metadata_properties: Optional[MetadataProperties] = None,
        marketplace_cert: bool = False,
        approval_status: Optional[str | PipelineVariable] = None,
        description: Optional[str] = None,
        drift_check_baselines: Optional[DriftCheckBaselines] = None,
        customer_metadata_properties: Optional[Dict[str, str | PipelineVariable]] = None,
        domain: Optional[str | PipelineVariable] = None,
        sample_payload_url: Optional[str | PipelineVariable] = None,
        task: Optional[str | PipelineVariable] = None,
        framework: Optional[str | PipelineVariable] = None,
        framework_version: Optional[str | PipelineVariable] = None,
        nearest_model_name: Optional[str | PipelineVariable] = None,
        data_input_configuration: Optional[str | PipelineVariable] = None,
    ): ...
    def prepare_container_def(
        self,
        instance_type: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
    ): ...
    def serving_image_uri(self, region_name, instance_type, serverless_inference_config: Incomplete | None = None): ...
