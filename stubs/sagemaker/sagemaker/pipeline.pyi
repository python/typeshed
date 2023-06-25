from _typeshed import Incomplete
from typing import Dict, List, Optional

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
        models: list[Model],
        role: str | None = None,
        predictor_cls: callable | None = None,
        name: str | None = None,
        vpc_config: dict[str, list[str | PipelineVariable]] | None = None,
        sagemaker_session: Session | None = None,
        enable_network_isolation: bool | PipelineVariable | None = None,
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
