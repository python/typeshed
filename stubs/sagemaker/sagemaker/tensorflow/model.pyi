from _typeshed import Incomplete
from typing import Dict, List, Optional, Union

import sagemaker
from sagemaker import ModelMetrics
from sagemaker.drift_check_baselines import DriftCheckBaselines
from sagemaker.metadata_properties import MetadataProperties
from sagemaker.predictor import Predictor
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class TensorFlowPredictor(Predictor):
    def __init__(
        self,
        endpoint_name,
        sagemaker_session: Incomplete | None = None,
        serializer=...,
        deserializer=...,
        model_name: Incomplete | None = None,
        model_version: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def classify(self, data): ...
    def regress(self, data): ...
    def predict(self, data, initial_args: Incomplete | None = None): ...

class TensorFlowModel(sagemaker.model.FrameworkModel):
    LOG_LEVEL_PARAM_NAME: str
    LOG_LEVEL_MAP: Incomplete
    LATEST_EIA_VERSION: Incomplete
    framework_version: Incomplete
    inference_framework_version: Incomplete
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: str = None,
        entry_point: Optional[str] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        framework_version: Optional[str] = None,
        container_log_level: Optional[int] = None,
        predictor_cls: callable = ...,
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
    def deploy(
        self,
        initial_instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        serializer: Incomplete | None = None,
        deserializer: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        endpoint_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        wait: bool = True,
        data_capture_config: Incomplete | None = None,
        async_inference_config: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
        volume_size: Incomplete | None = None,
        model_data_download_timeout: Incomplete | None = None,
        container_startup_health_check_timeout: Incomplete | None = None,
        inference_recommendation_id: Incomplete | None = None,
        explainer_config: Incomplete | None = None,
        **kwargs,
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
