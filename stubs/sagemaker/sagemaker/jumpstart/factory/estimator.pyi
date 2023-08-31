from _typeshed import Incomplete

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
    model_version: str | None = None,
    tolerate_vulnerable_model: bool | None = None,
    tolerate_deprecated_model: bool | None = None,
    region: str | None = None,
    image_uri: str | PipelineVariable | None = None,
    role: str | None = None,
    instance_count: int | PipelineVariable | None = None,
    instance_type: str | PipelineVariable | None = None,
    keep_alive_period_in_seconds: int | PipelineVariable | None = None,
    volume_size: int | PipelineVariable | None = None,
    volume_kms_key: str | PipelineVariable | None = None,
    max_run: int | PipelineVariable | None = None,
    input_mode: str | PipelineVariable | None = None,
    output_path: str | PipelineVariable | None = None,
    output_kms_key: str | PipelineVariable | None = None,
    base_job_name: str | None = None,
    sagemaker_session: Session | None = None,
    hyperparameters: dict[str, str | PipelineVariable] | None = None,
    tags: list[dict[str, str | PipelineVariable]] | None = None,
    subnets: list[str | PipelineVariable] | None = None,
    security_group_ids: list[str | PipelineVariable] | None = None,
    model_uri: str | None = None,
    model_channel_name: str | PipelineVariable | None = None,
    metric_definitions: list[dict[str, str | PipelineVariable]] | None = None,
    encrypt_inter_container_traffic: bool | PipelineVariable | None = None,
    use_spot_instances: bool | PipelineVariable | None = None,
    max_wait: int | PipelineVariable | None = None,
    checkpoint_s3_uri: str | PipelineVariable | None = None,
    checkpoint_local_path: str | PipelineVariable | None = None,
    enable_network_isolation: bool | PipelineVariable | None = None,
    rules: list[RuleBase] | None = None,
    debugger_hook_config: DebuggerHookConfig | bool | None = None,
    tensorboard_output_config: TensorBoardOutputConfig | None = None,
    enable_sagemaker_metrics: bool | PipelineVariable | None = None,
    profiler_config: ProfilerConfig | None = None,
    disable_profiler: bool | None = None,
    environment: dict[str, str | PipelineVariable] | None = None,
    max_retry_attempts: int | PipelineVariable | None = None,
    source_dir: str | PipelineVariable | None = None,
    git_config: dict[str, str] | None = None,
    container_log_level: int | PipelineVariable | None = None,
    code_location: str | None = None,
    entry_point: str | PipelineVariable | None = None,
    dependencies: list[str] | None = None,
    instance_groups: list[InstanceGroup] | None = None,
    training_repository_access_mode: str | PipelineVariable | None = None,
    training_repository_credentials_provider_arn: str | PipelineVariable | None = None,
) -> JumpStartEstimatorInitKwargs: ...
def get_fit_kwargs(
    model_id: str,
    model_version: str | None = None,
    region: str | None = None,
    inputs: str | dict | TrainingInput | FileSystemInput | None = None,
    wait: bool | None = None,
    logs: str | None = None,
    job_name: str | None = None,
    experiment_config: dict[str, str] | None = None,
    tolerate_vulnerable_model: bool | None = None,
    tolerate_deprecated_model: bool | None = None,
) -> JumpStartEstimatorFitKwargs: ...
def get_deploy_kwargs(
    model_id: str,
    model_version: str | None = None,
    region: str | None = None,
    initial_instance_count: int | None = None,
    instance_type: str | None = None,
    serializer: BaseSerializer | None = None,
    deserializer: BaseDeserializer | None = None,
    accelerator_type: str | None = None,
    endpoint_name: str | None = None,
    tags: list[dict[str, str]] | None = None,
    kms_key: str | None = None,
    wait: bool | None = None,
    data_capture_config: DataCaptureConfig | None = None,
    async_inference_config: AsyncInferenceConfig | None = None,
    serverless_inference_config: ServerlessInferenceConfig | None = None,
    volume_size: int | None = None,
    model_data_download_timeout: int | None = None,
    container_startup_health_check_timeout: int | None = None,
    inference_recommendation_id: str | None = None,
    explainer_config: ExplainerConfig | None = None,
    image_uri: str | PipelineVariable | None = None,
    role: str | None = None,
    predictor_cls: callable | None = None,
    env: dict[str, str | PipelineVariable] | None = None,
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
    tolerate_deprecated_model: bool | None = None,
    tolerate_vulnerable_model: bool | None = None,
    use_compiled_model: bool | None = None,
    model_name: str | None = None,
) -> JumpStartEstimatorDeployKwargs: ...
