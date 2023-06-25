from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.async_inference.async_inference_config import AsyncInferenceConfig
from sagemaker.base_deserializers import BaseDeserializer
from sagemaker.base_serializers import BaseSerializer
from sagemaker.explainer.explainer_config import ExplainerConfig
from sagemaker.model import Model
from sagemaker.model_monitor.data_capture_config import DataCaptureConfig
from sagemaker.predictor import PredictorBase
from sagemaker.serverless.serverless_inference_config import ServerlessInferenceConfig
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class JumpStartModel(Model):
    orig_predictor_cls: Incomplete
    model_id: Incomplete
    model_version: Incomplete
    instance_type: Incomplete
    tolerate_vulnerable_model: Incomplete
    tolerate_deprecated_model: Incomplete
    region: Incomplete
    def __init__(
        self,
        model_id: str | None = None,
        model_version: str | None = None,
        tolerate_vulnerable_model: bool | None = None,
        tolerate_deprecated_model: bool | None = None,
        region: str | None = None,
        instance_type: str | None = None,
        image_uri: str | PipelineVariable | None = None,
        model_data: str | PipelineVariable | None = None,
        role: str | None = None,
        predictor_cls: callable | None = None,
        env: dict[str, str | PipelineVariable] | None = None,
        name: str | None = None,
        vpc_config: dict[str, list[str | PipelineVariable]] | None = None,
        sagemaker_session: Session | None = None,
        enable_network_isolation: bool | PipelineVariable | None = None,
        model_kms_key: str | None = None,
        image_config: dict[str, str | PipelineVariable] | None = None,
        source_dir: str | None = None,
        code_location: str | None = None,
        entry_point: str | None = None,
        container_log_level: int | PipelineVariable | None = None,
        dependencies: list[str] | None = None,
        git_config: dict[str, str] | None = None,
    ) -> None: ...
    def deploy(
        self,
        initial_instance_count: int | None = None,
        instance_type: str | None = None,
        serializer: BaseSerializer | None = None,
        deserializer: BaseDeserializer | None = None,
        accelerator_type: str | None = None,
        endpoint_name: str | None = None,
        tags: list[dict[str, str]] | None = None,
        kms_key: str | None = None,
        wait: bool | None = True,
        data_capture_config: DataCaptureConfig | None = None,
        async_inference_config: AsyncInferenceConfig | None = None,
        serverless_inference_config: ServerlessInferenceConfig | None = None,
        volume_size: int | None = None,
        model_data_download_timeout: int | None = None,
        container_startup_health_check_timeout: int | None = None,
        inference_recommendation_id: str | None = None,
        explainer_config: ExplainerConfig | None = None,
    ) -> PredictorBase: ...
