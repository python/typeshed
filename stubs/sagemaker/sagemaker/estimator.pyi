import abc
from _typeshed import Incomplete
from abc import abstractmethod
from typing import Dict, List, Optional, Union

from sagemaker.debugger import (
    DEBUGGER_FLAG as DEBUGGER_FLAG,
    DebuggerHookConfig,
    ProfilerConfig,
    RuleBase,
    TensorBoardOutputConfig,
    get_default_profiler_rule as get_default_profiler_rule,
)
from sagemaker.inputs import FileSystemInput, TrainingInput
from sagemaker.instance_group import InstanceGroup
from sagemaker.job import _Job
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class EstimatorBase(metaclass=abc.ABCMeta):
    LAUNCH_PT_XLA_ENV_NAME: str
    LAUNCH_PS_ENV_NAME: str
    LAUNCH_MPI_ENV_NAME: str
    LAUNCH_SM_DDP_ENV_NAME: str
    LAUNCH_MWMS_ENV_NAME: str
    INSTANCE_TYPE: str
    MPI_NUM_PROCESSES_PER_HOST: str
    MPI_CUSTOM_MPI_OPTIONS: str
    SM_DDP_CUSTOM_MPI_OPTIONS: str
    CONTAINER_CODE_CHANNEL_SOURCEDIR_PATH: str
    JOB_CLASS_NAME: str
    instance_count: Incomplete
    instance_type: Incomplete
    keep_alive_period_in_seconds: Incomplete
    instance_groups: Incomplete
    volume_size: Incomplete
    max_run: Incomplete
    input_mode: Incomplete
    metric_definitions: Incomplete
    model_uri: Incomplete
    model_channel_name: Incomplete
    code_uri: Incomplete
    code_channel_name: str
    source_dir: Incomplete
    git_config: Incomplete
    container_log_level: Incomplete
    code_location: Incomplete
    entry_point: Incomplete
    dependencies: Incomplete
    uploaded_code: Incomplete
    tags: Incomplete
    sagemaker_session: Incomplete
    base_job_name: Incomplete
    output_path: Incomplete
    latest_training_job: Incomplete
    jobs: Incomplete
    deploy_instance_type: Incomplete
    role: Incomplete
    output_kms_key: Incomplete
    volume_kms_key: Incomplete
    subnets: Incomplete
    security_group_ids: Incomplete
    training_repository_access_mode: Incomplete
    training_repository_credentials_provider_arn: Incomplete
    container_entry_point: Incomplete
    container_arguments: Incomplete
    encrypt_inter_container_traffic: Incomplete
    use_spot_instances: Incomplete
    max_wait: Incomplete
    checkpoint_s3_uri: Incomplete
    checkpoint_local_path: Incomplete
    rules: Incomplete
    debugger_hook_config: Incomplete
    tensorboard_output_config: Incomplete
    debugger_rule_configs: Incomplete
    collection_configs: Incomplete
    enable_sagemaker_metrics: Incomplete
    profiler_config: Incomplete
    disable_profiler: Incomplete
    environment: Incomplete
    max_retry_attempts: Incomplete
    profiler_rule_configs: Incomplete
    profiler_rules: Incomplete
    debugger_rules: Incomplete
    disable_output_compression: Incomplete
    def __init__(
        self,
        role: str = None,
        instance_count: Optional[int | PipelineVariable] = None,
        instance_type: Optional[str | PipelineVariable] = None,
        keep_alive_period_in_seconds: Optional[int | PipelineVariable] = None,
        volume_size: int | PipelineVariable = 30,
        volume_kms_key: Optional[str | PipelineVariable] = None,
        max_run: int | PipelineVariable = 86400,
        input_mode: str | PipelineVariable = "File",
        output_path: Optional[str | PipelineVariable] = None,
        output_kms_key: Optional[str | PipelineVariable] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        tags: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        subnets: Optional[List[str | PipelineVariable]] = None,
        security_group_ids: Optional[List[str | PipelineVariable]] = None,
        model_uri: Optional[str] = None,
        model_channel_name: str | PipelineVariable = "model",
        metric_definitions: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        encrypt_inter_container_traffic: bool | PipelineVariable = None,
        use_spot_instances: bool | PipelineVariable = False,
        max_wait: Optional[int | PipelineVariable] = None,
        checkpoint_s3_uri: Optional[str | PipelineVariable] = None,
        checkpoint_local_path: Optional[str | PipelineVariable] = None,
        rules: Optional[List[RuleBase]] = None,
        debugger_hook_config: Optional[bool | DebuggerHookConfig] = None,
        tensorboard_output_config: Optional[TensorBoardOutputConfig] = None,
        enable_sagemaker_metrics: Optional[bool | PipelineVariable] = None,
        enable_network_isolation: bool | PipelineVariable = None,
        profiler_config: Optional[ProfilerConfig] = None,
        disable_profiler: bool = None,
        environment: Optional[Dict[str, str | PipelineVariable]] = None,
        max_retry_attempts: Optional[int | PipelineVariable] = None,
        source_dir: Optional[str | PipelineVariable] = None,
        git_config: Optional[Dict[str, str]] = None,
        hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
        container_log_level: int | PipelineVariable = 20,
        code_location: Optional[str] = None,
        entry_point: Optional[str | PipelineVariable] = None,
        dependencies: Optional[List[str]] = None,
        instance_groups: Optional[List[InstanceGroup]] = None,
        training_repository_access_mode: Optional[str | PipelineVariable] = None,
        training_repository_credentials_provider_arn: Optional[str | PipelineVariable] = None,
        container_entry_point: Optional[List[str]] = None,
        container_arguments: Optional[List[str]] = None,
        disable_output_compression: bool = False,
        **kwargs,
    ) -> None: ...
    @abstractmethod
    def training_image_uri(self): ...
    @abstractmethod
    def hyperparameters(self): ...
    def enable_network_isolation(self): ...
    def prepare_workflow_for_training(self, job_name: Incomplete | None = None) -> None: ...
    def latest_job_debugger_artifacts_path(self): ...
    def latest_job_tensorboard_artifacts_path(self): ...
    def latest_job_profiler_artifacts_path(self): ...
    def fit(
        self,
        inputs: Optional[str | Dict | TrainingInput | FileSystemInput] = None,
        wait: bool = True,
        logs: str = "All",
        job_name: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
    ): ...
    def compile_model(
        self,
        target_instance_family,
        input_shape,
        output_path,
        framework: Incomplete | None = None,
        framework_version: Incomplete | None = None,
        compile_max_run=900,
        tags: Incomplete | None = None,
        target_platform_os: Incomplete | None = None,
        target_platform_arch: Incomplete | None = None,
        target_platform_accelerator: Incomplete | None = None,
        compiler_options: Incomplete | None = None,
        **kwargs,
    ): ...
    @classmethod
    def attach(cls, training_job_name, sagemaker_session: Incomplete | None = None, model_channel_name: str = "model"): ...
    def logs(self) -> None: ...
    def deploy(
        self,
        initial_instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        serializer: Incomplete | None = None,
        deserializer: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        endpoint_name: Incomplete | None = None,
        use_compiled_model: bool = False,
        wait: bool = True,
        model_name: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        data_capture_config: Incomplete | None = None,
        tags: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
        async_inference_config: Incomplete | None = None,
        volume_size: Incomplete | None = None,
        model_data_download_timeout: Incomplete | None = None,
        container_startup_health_check_timeout: Incomplete | None = None,
        inference_recommendation_id: Incomplete | None = None,
        explainer_config: Incomplete | None = None,
        **kwargs,
    ): ...
    def register(
        self,
        content_types,
        response_types,
        inference_instances: Incomplete | None = None,
        transform_instances: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        model_package_name: Incomplete | None = None,
        model_package_group_name: Incomplete | None = None,
        model_metrics: Incomplete | None = None,
        metadata_properties: Incomplete | None = None,
        marketplace_cert: bool = False,
        approval_status: Incomplete | None = None,
        description: Incomplete | None = None,
        compile_model_family: Incomplete | None = None,
        model_name: Incomplete | None = None,
        drift_check_baselines: Incomplete | None = None,
        customer_metadata_properties: Incomplete | None = None,
        domain: Incomplete | None = None,
        sample_payload_url: Incomplete | None = None,
        task: Incomplete | None = None,
        framework: Incomplete | None = None,
        framework_version: Incomplete | None = None,
        nearest_model_name: Incomplete | None = None,
        data_input_configuration: Incomplete | None = None,
        **kwargs,
    ): ...
    @property
    def model_data(self): ...
    @abstractmethod
    def create_model(self, **kwargs): ...
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
        role: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        enable_network_isolation: Incomplete | None = None,
        model_name: Incomplete | None = None,
    ): ...
    @property
    def training_job_analytics(self): ...
    def get_vpc_config(self, vpc_config_override="VPC_CONFIG_DEFAULT"): ...
    delete_endpoint: Incomplete
    def enable_default_profiling(self) -> None: ...
    def disable_profiling(self) -> None: ...
    def update_profiler(
        self,
        rules: Incomplete | None = None,
        system_monitor_interval_millis: Incomplete | None = None,
        s3_output_path: Incomplete | None = None,
        framework_profile_params: Incomplete | None = None,
        disable_framework_metrics: bool = False,
    ) -> None: ...

class _TrainingJob(_Job):
    @classmethod
    def start_new(cls, estimator, inputs, experiment_config): ...
    @classmethod
    def update(
        cls,
        estimator,
        profiler_rule_configs: Incomplete | None = None,
        profiler_config: Incomplete | None = None,
        resource_config: Incomplete | None = None,
    ): ...
    def wait(self, logs: str = "All") -> None: ...
    def describe(self): ...
    def rule_job_summary(self): ...
    def stop(self) -> None: ...

class Estimator(EstimatorBase):
    image_uri: Incomplete
    def __init__(
        self,
        image_uri: str | PipelineVariable,
        role: str = None,
        instance_count: Optional[int | PipelineVariable] = None,
        instance_type: Optional[str | PipelineVariable] = None,
        keep_alive_period_in_seconds: Optional[int | PipelineVariable] = None,
        volume_size: int | PipelineVariable = 30,
        volume_kms_key: Optional[str | PipelineVariable] = None,
        max_run: int | PipelineVariable = 86400,
        input_mode: str | PipelineVariable = "File",
        output_path: Optional[str | PipelineVariable] = None,
        output_kms_key: Optional[str | PipelineVariable] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
        tags: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        subnets: Optional[List[str | PipelineVariable]] = None,
        security_group_ids: Optional[List[str | PipelineVariable]] = None,
        model_uri: Optional[str] = None,
        model_channel_name: str | PipelineVariable = "model",
        metric_definitions: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        encrypt_inter_container_traffic: bool | PipelineVariable = None,
        use_spot_instances: bool | PipelineVariable = False,
        max_wait: Optional[int | PipelineVariable] = None,
        checkpoint_s3_uri: Optional[str | PipelineVariable] = None,
        checkpoint_local_path: Optional[str | PipelineVariable] = None,
        enable_network_isolation: bool | PipelineVariable = None,
        rules: Optional[List[RuleBase]] = None,
        debugger_hook_config: Optional[DebuggerHookConfig | bool] = None,
        tensorboard_output_config: Optional[TensorBoardOutputConfig] = None,
        enable_sagemaker_metrics: Optional[bool | PipelineVariable] = None,
        profiler_config: Optional[ProfilerConfig] = None,
        disable_profiler: bool = False,
        environment: Optional[Dict[str, str | PipelineVariable]] = None,
        max_retry_attempts: Optional[int | PipelineVariable] = None,
        source_dir: Optional[str | PipelineVariable] = None,
        git_config: Optional[Dict[str, str]] = None,
        container_log_level: int | PipelineVariable = 20,
        code_location: Optional[str] = None,
        entry_point: Optional[str | PipelineVariable] = None,
        dependencies: Optional[List[str]] = None,
        instance_groups: Optional[List[InstanceGroup]] = None,
        training_repository_access_mode: Optional[str | PipelineVariable] = None,
        training_repository_credentials_provider_arn: Optional[str | PipelineVariable] = None,
        container_entry_point: Optional[List[str]] = None,
        container_arguments: Optional[List[str]] = None,
        disable_output_compression: bool = False,
        **kwargs,
    ) -> None: ...
    def training_image_uri(self): ...
    def set_hyperparameters(self, **kwargs) -> None: ...
    def hyperparameters(self): ...
    def create_model(
        self,
        role: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        predictor_cls: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        **kwargs,
    ): ...

class Framework(EstimatorBase, metaclass=abc.ABCMeta):
    entry_point: Incomplete
    git_config: Incomplete
    source_dir: Incomplete
    dependencies: Incomplete
    uploaded_code: Incomplete
    container_log_level: Incomplete
    code_location: Incomplete
    image_uri: Incomplete
    checkpoint_s3_uri: Incomplete
    checkpoint_local_path: Incomplete
    enable_sagemaker_metrics: Incomplete
    def __init__(
        self,
        entry_point: str | PipelineVariable,
        source_dir: Optional[str | PipelineVariable] = None,
        hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
        container_log_level: int | PipelineVariable = 20,
        code_location: Optional[str] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        dependencies: Optional[List[str]] = None,
        enable_network_isolation: bool | PipelineVariable = None,
        git_config: Optional[Dict[str, str]] = None,
        checkpoint_s3_uri: Optional[str | PipelineVariable] = None,
        checkpoint_local_path: Optional[str | PipelineVariable] = None,
        enable_sagemaker_metrics: Optional[bool | PipelineVariable] = None,
        **kwargs,
    ) -> None: ...
    def set_hyperparameters(self, **kwargs) -> None: ...
    def hyperparameters(self): ...
    def training_image_uri(self, region: Incomplete | None = None): ...
    @classmethod
    def attach(cls, training_job_name, sagemaker_session: Incomplete | None = None, model_channel_name: str = "model"): ...
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
        role: Incomplete | None = None,
        model_server_workers: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        entry_point: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        enable_network_isolation: Incomplete | None = None,
        model_name: Incomplete | None = None,
    ): ...
