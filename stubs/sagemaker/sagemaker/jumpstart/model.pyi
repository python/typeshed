from _typeshed import Incomplete
from typing import Dict, List, Optional, Union

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
        model_id: Optional[str] = None,
        model_version: Optional[str] = None,
        tolerate_vulnerable_model: Optional[bool] = None,
        tolerate_deprecated_model: Optional[bool] = None,
        region: Optional[str] = None,
        instance_type: Optional[str] = None,
        image_uri: Optional[Union[str, PipelineVariable]] = None,
        model_data: Optional[Union[str, PipelineVariable]] = None,
        role: Optional[str] = None,
        predictor_cls: Optional[callable] = None,
        env: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
        name: Optional[str] = None,
        vpc_config: Optional[Dict[str, List[Union[str, PipelineVariable]]]] = None,
        sagemaker_session: Optional[Session] = None,
        enable_network_isolation: Union[bool, PipelineVariable] = None,
        model_kms_key: Optional[str] = None,
        image_config: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
        source_dir: Optional[str] = None,
        code_location: Optional[str] = None,
        entry_point: Optional[str] = None,
        container_log_level: Optional[Union[int, PipelineVariable]] = None,
        dependencies: Optional[List[str]] = None,
        git_config: Optional[Dict[str, str]] = None,
    ) -> None: ...
    def deploy(
        self,
        initial_instance_count: Optional[int] = None,
        instance_type: Optional[str] = None,
        serializer: Optional[BaseSerializer] = None,
        deserializer: Optional[BaseDeserializer] = None,
        accelerator_type: Optional[str] = None,
        endpoint_name: Optional[str] = None,
        tags: List[Dict[str, str]] = None,
        kms_key: Optional[str] = None,
        wait: Optional[bool] = True,
        data_capture_config: Optional[DataCaptureConfig] = None,
        async_inference_config: Optional[AsyncInferenceConfig] = None,
        serverless_inference_config: Optional[ServerlessInferenceConfig] = None,
        volume_size: Optional[int] = None,
        model_data_download_timeout: Optional[int] = None,
        container_startup_health_check_timeout: Optional[int] = None,
        inference_recommendation_id: Optional[str] = None,
        explainer_config: Optional[ExplainerConfig] = None,
    ) -> PredictorBase: ...
