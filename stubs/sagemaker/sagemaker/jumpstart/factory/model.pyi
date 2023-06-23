from _typeshed import Incomplete
from typing import Dict, List, Optional, Union

from sagemaker.async_inference.async_inference_config import AsyncInferenceConfig
from sagemaker.base_deserializers import BaseDeserializer
from sagemaker.base_predictor import Predictor
from sagemaker.base_serializers import BaseSerializer
from sagemaker.explainer.explainer_config import ExplainerConfig
from sagemaker.jumpstart.types import JumpStartModelDeployKwargs, JumpStartModelInitKwargs
from sagemaker.model_monitor.data_capture_config import DataCaptureConfig
from sagemaker.serverless.serverless_inference_config import ServerlessInferenceConfig
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

def get_default_predictor(
    predictor: Predictor,
    model_id: str,
    model_version: str,
    region: str,
    tolerate_vulnerable_model: bool,
    tolerate_deprecated_model: bool,
) -> Predictor: ...
def get_deploy_kwargs(
    model_id: str,
    model_version: Optional[str] = None,
    region: Optional[str] = None,
    initial_instance_count: Optional[int] = None,
    instance_type: Optional[str] = None,
    serializer: Optional[BaseSerializer] = None,
    deserializer: Optional[BaseDeserializer] = None,
    accelerator_type: Optional[str] = None,
    endpoint_name: Optional[str] = None,
    tags: List[Dict[str, str]] = None,
    kms_key: Optional[str] = None,
    wait: Optional[bool] = None,
    data_capture_config: Optional[DataCaptureConfig] = None,
    async_inference_config: Optional[AsyncInferenceConfig] = None,
    serverless_inference_config: Optional[ServerlessInferenceConfig] = None,
    volume_size: Optional[int] = None,
    model_data_download_timeout: Optional[int] = None,
    container_startup_health_check_timeout: Optional[int] = None,
    inference_recommendation_id: Optional[str] = None,
    explainer_config: Optional[ExplainerConfig] = None,
    tolerate_vulnerable_model: Optional[bool] = None,
    tolerate_deprecated_model: Optional[bool] = None,
) -> JumpStartModelDeployKwargs: ...
def get_init_kwargs(
    model_id: str,
    model_from_estimator: bool = False,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: Optional[bool] = None,
    tolerate_deprecated_model: Optional[bool] = None,
    instance_type: Optional[str] = None,
    region: Optional[str] = None,
    image_uri: Optional[str | PipelineVariable] = None,
    model_data: Optional[str | PipelineVariable] = None,
    role: Optional[str] = None,
    predictor_cls: Optional[callable] = None,
    env: Optional[Dict[str, str | PipelineVariable]] = None,
    name: Optional[str] = None,
    vpc_config: Optional[Dict[str, List[str | PipelineVariable]]] = None,
    sagemaker_session: Optional[Session] = None,
    enable_network_isolation: bool | PipelineVariable = None,
    model_kms_key: Optional[str] = None,
    image_config: Optional[Dict[str, str | PipelineVariable]] = None,
    source_dir: Optional[str] = None,
    code_location: Optional[str] = None,
    entry_point: Optional[str] = None,
    container_log_level: Optional[int | PipelineVariable] = None,
    dependencies: Optional[List[str]] = None,
    git_config: Optional[Dict[str, str]] = None,
) -> JumpStartModelInitKwargs: ...
