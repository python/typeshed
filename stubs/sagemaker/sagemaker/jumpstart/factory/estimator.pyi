from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.async_inference.async_inference_config import AsyncInferenceConfig
from sagemaker.base_deserializers import BaseDeserializer
from sagemaker.base_serializers import BaseSerializer
from sagemaker.debugger.debugger import DebuggerHookConfig, RuleBase, TensorBoardOutputConfig
from sagemaker.debugger.profiler_config import ProfilerConfig
from sagemaker.explainer.explainer_config import ExplainerConfig
from sagemaker.inputs import FileSystemInput, TrainingInput
from sagemaker.instance_group import InstanceGroup
from sagemaker.jumpstart.types import JumpStartEstimatorDeployKwargs, JumpStartEstimatorFitKwargs, JumpStartEstimatorInitKwargs
from sagemaker.model_monitor.data_capture_config import DataCaptureConfig
from sagemaker.serverless.serverless_inference_config import ServerlessInferenceConfig
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

def get_init_kwargs(
    model_id: str,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: Optional[bool] = None,
    tolerate_deprecated_model: Optional[bool] = None,
    region: Optional[str] = None,
    image_uri: Optional[str | PipelineVariable] = None,
    role: Optional[str] = None,
    instance_count: Optional[int | PipelineVariable] = None,
    instance_type: Optional[str | PipelineVariable] = None,
    keep_alive_period_in_seconds: Optional[int | PipelineVariable] = None,
    volume_size: Optional[int | PipelineVariable] = None,
    volume_kms_key: Optional[str | PipelineVariable] = None,
    max_run: Optional[int | PipelineVariable] = None,
    input_mode: Optional[str | PipelineVariable] = None,
    output_path: Optional[str | PipelineVariable] = None,
    output_kms_key: Optional[str | PipelineVariable] = None,
    base_job_name: Optional[str] = None,
    sagemaker_session: Optional[Session] = None,
    hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
    tags: Optional[List[Dict[str, str | PipelineVariable]]] = None,
    subnets: Optional[List[str | PipelineVariable]] = None,
    security_group_ids: Optional[List[str | PipelineVariable]] = None,
    model_uri: Optional[str] = None,
    model_channel_name: Optional[str | PipelineVariable] = None,
    metric_definitions: Optional[List[Dict[str, str | PipelineVariable]]] = None,
    encrypt_inter_container_traffic: bool | PipelineVariable = None,
    use_spot_instances: Optional[bool | PipelineVariable] = None,
    max_wait: Optional[int | PipelineVariable] = None,
    checkpoint_s3_uri: Optional[str | PipelineVariable] = None,
    checkpoint_local_path: Optional[str | PipelineVariable] = None,
    enable_network_isolation: bool | PipelineVariable = None,
    rules: Optional[List[RuleBase]] = None,
    debugger_hook_config: Optional[DebuggerHookConfig | bool] = None,
    tensorboard_output_config: Optional[TensorBoardOutputConfig] = None,
    enable_sagemaker_metrics: Optional[bool | PipelineVariable] = None,
    profiler_config: Optional[ProfilerConfig] = None,
    disable_profiler: Optional[bool] = None,
    environment: Optional[Dict[str, str | PipelineVariable]] = None,
    max_retry_attempts: Optional[int | PipelineVariable] = None,
    source_dir: Optional[str | PipelineVariable] = None,
    git_config: Optional[Dict[str, str]] = None,
    container_log_level: Optional[int | PipelineVariable] = None,
    code_location: Optional[str] = None,
    entry_point: Optional[str | PipelineVariable] = None,
    dependencies: Optional[List[str]] = None,
    instance_groups: Optional[List[InstanceGroup]] = None,
    training_repository_access_mode: Optional[str | PipelineVariable] = None,
    training_repository_credentials_provider_arn: Optional[str | PipelineVariable] = None,
) -> JumpStartEstimatorInitKwargs: ...
def get_fit_kwargs(
    model_id: str,
    model_version: Optional[str] = None,
    region: Optional[str] = None,
    inputs: Optional[str | Dict | TrainingInput | FileSystemInput] = None,
    wait: Optional[bool] = None,
    logs: Optional[str] = None,
    job_name: Optional[str] = None,
    experiment_config: Optional[Dict[str, str]] = None,
    tolerate_vulnerable_model: Optional[bool] = None,
    tolerate_deprecated_model: Optional[bool] = None,
) -> JumpStartEstimatorFitKwargs: ...
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
    image_uri: Optional[str | PipelineVariable] = None,
    role: Optional[str] = None,
    predictor_cls: Optional[callable] = None,
    env: Optional[Dict[str, str | PipelineVariable]] = None,
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
    tolerate_deprecated_model: Optional[bool] = None,
    tolerate_vulnerable_model: Optional[bool] = None,
    use_compiled_model: Optional[bool] = None,
    model_name: Optional[str] = None,
) -> JumpStartEstimatorDeployKwargs: ...
