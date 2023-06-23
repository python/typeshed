from _typeshed import Incomplete
from typing import Dict, List, Optional, Union

from sagemaker import Model, ModelMetrics
from sagemaker.drift_check_baselines import DriftCheckBaselines
from sagemaker.metadata_properties import MetadataProperties
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class PipelineModel:
    models: Incomplete
    predictor_cls: Incomplete
    name: Incomplete
    endpoint_name: Incomplete
    sagemaker_session: Incomplete
    role: Incomplete
    vpc_config: Incomplete
    enable_network_isolation: Incomplete
    def __init__(
        self,
        models: List[Model],
        role: str = None,
        predictor_cls: Optional[callable] = None,
        name: Optional[str] = None,
        vpc_config: Optional[Dict[str, List[Union[str, PipelineVariable]]]] = None,
        sagemaker_session: Optional[Session] = None,
        enable_network_isolation: Union[bool, PipelineVariable] = None,
    ) -> None: ...
    def pipeline_container_def(self, instance_type: Incomplete | None = None): ...
    def deploy(
        self,
        initial_instance_count,
        instance_type,
        serializer: Incomplete | None = None,
        deserializer: Incomplete | None = None,
        endpoint_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        wait: bool = True,
        update_endpoint: bool = False,
        data_capture_config: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        volume_size: Incomplete | None = None,
        model_data_download_timeout: Incomplete | None = None,
        container_startup_health_check_timeout: Incomplete | None = None,
    ): ...
    def create(self, instance_type: str): ...
    def register(
        self,
        content_types: List[Union[str, PipelineVariable]],
        response_types: List[Union[str, PipelineVariable]],
        inference_instances: Optional[List[Union[str, PipelineVariable]]] = None,
        transform_instances: Optional[List[Union[str, PipelineVariable]]] = None,
        model_package_name: Optional[Union[str, PipelineVariable]] = None,
        model_package_group_name: Optional[Union[str, PipelineVariable]] = None,
        image_uri: Optional[Union[str, PipelineVariable]] = None,
        model_metrics: Optional[ModelMetrics] = None,
        metadata_properties: Optional[MetadataProperties] = None,
        marketplace_cert: bool = False,
        approval_status: Optional[Union[str, PipelineVariable]] = None,
        description: Optional[str] = None,
        drift_check_baselines: Optional[DriftCheckBaselines] = None,
        customer_metadata_properties: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
        domain: Optional[Union[str, PipelineVariable]] = None,
        sample_payload_url: Optional[Union[str, PipelineVariable]] = None,
        task: Optional[Union[str, PipelineVariable]] = None,
        framework: Optional[Union[str, PipelineVariable]] = None,
        framework_version: Optional[Union[str, PipelineVariable]] = None,
        nearest_model_name: Optional[Union[str, PipelineVariable]] = None,
        data_input_configuration: Optional[Union[str, PipelineVariable]] = None,
    ): ...
    def transformer(
        self,
        instance_count,
        instance_type,
        strategy: Incomplete | None = None,
        assemble_with: Incomplete | None = None,
        output_path: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        accept: Incomplete | None = None,
        env: Incomplete | None = None,
        max_concurrent_transforms: Incomplete | None = None,
        max_payload: Incomplete | None = None,
        tags: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
    ): ...
    def delete_model(self) -> None: ...
