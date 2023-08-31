from _typeshed import Incomplete
from collections.abc import Callable
from enum import Enum
from typing import Any

from sagemaker import Predictor

class JumpStartDataHolderType:
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class JumpStartS3FileType(str, Enum):
    MANIFEST: str
    SPECS: str

class JumpStartLaunchedRegionInfo(JumpStartDataHolderType):
    content_bucket: Incomplete
    region_name: Incomplete
    def __init__(self, content_bucket: str, region_name: str) -> None: ...

class JumpStartModelHeader(JumpStartDataHolderType):
    def __init__(self, header: dict[str, str]) -> None: ...
    def to_json(self) -> dict[str, str]: ...
    model_id: Incomplete
    version: Incomplete
    min_version: Incomplete
    spec_key: Incomplete
    def from_json(self, json_obj: dict[str, str]) -> None: ...

class JumpStartECRSpecs(JumpStartDataHolderType):
    def __init__(self, spec: dict[str, Any]) -> None: ...
    framework: Incomplete
    framework_version: Incomplete
    py_version: Incomplete
    huggingface_transformers_version: Incomplete
    def from_json(self, json_obj: dict[str, Any]) -> None: ...
    def to_json(self) -> dict[str, Any]: ...

class JumpStartHyperparameter(JumpStartDataHolderType):
    def __init__(self, spec: dict[str, Any]) -> None: ...
    name: Incomplete
    type: Incomplete
    default: Incomplete
    scope: Incomplete
    options: Incomplete
    min: Incomplete
    max: Incomplete
    exclusive_min: Incomplete
    exclusive_max: Incomplete
    def from_json(self, json_obj: dict[str, Any]) -> None: ...
    def to_json(self) -> dict[str, Any]: ...

class JumpStartEnvironmentVariable(JumpStartDataHolderType):
    def __init__(self, spec: dict[str, Any]) -> None: ...
    name: Incomplete
    type: Incomplete
    default: Incomplete
    scope: Incomplete
    required_for_model_class: Incomplete
    def from_json(self, json_obj: dict[str, Any]) -> None: ...
    def to_json(self) -> dict[str, Any]: ...

class JumpStartPredictorSpecs(JumpStartDataHolderType):
    def __init__(self, spec: dict[str, Any] | None) -> None: ...
    default_content_type: Incomplete
    supported_content_types: Incomplete
    default_accept_type: Incomplete
    supported_accept_types: Incomplete
    def from_json(self, json_obj: dict[str, Any] | None) -> None: ...
    def to_json(self) -> dict[str, Any]: ...

class JumpStartModelSpecs(JumpStartDataHolderType):
    def __init__(self, spec: dict[str, Any]) -> None: ...
    model_id: Incomplete
    url: Incomplete
    version: Incomplete
    min_sdk_version: Incomplete
    incremental_training_supported: Incomplete
    hosting_ecr_specs: Incomplete
    hosting_artifact_key: Incomplete
    hosting_script_key: Incomplete
    training_supported: Incomplete
    inference_environment_variables: Incomplete
    inference_vulnerable: Incomplete
    inference_dependencies: Incomplete
    inference_vulnerabilities: Incomplete
    training_vulnerable: Incomplete
    training_dependencies: Incomplete
    training_vulnerabilities: Incomplete
    deprecated: Incomplete
    default_inference_instance_type: Incomplete
    default_training_instance_type: Incomplete
    supported_inference_instance_types: Incomplete
    supported_training_instance_types: Incomplete
    metrics: Incomplete
    training_prepacked_script_key: Incomplete
    hosting_prepacked_artifact_key: Incomplete
    model_kwargs: Incomplete
    deploy_kwargs: Incomplete
    predictor_specs: Incomplete
    inference_volume_size: Incomplete
    inference_enable_network_isolation: Incomplete
    resource_name_base: Incomplete
    training_ecr_specs: Incomplete
    training_artifact_key: Incomplete
    training_script_key: Incomplete
    hyperparameters: Incomplete
    estimator_kwargs: Incomplete
    fit_kwargs: Incomplete
    training_volume_size: Incomplete
    training_enable_network_isolation: Incomplete
    def from_json(self, json_obj: dict[str, Any]) -> None: ...
    def to_json(self) -> dict[str, Any]: ...
    def supports_prepacked_inference(self) -> bool: ...
    def supports_incremental_training(self) -> bool: ...

class JumpStartVersionedModelId(JumpStartDataHolderType):
    model_id: Incomplete
    version: Incomplete
    def __init__(self, model_id: str, version: str) -> None: ...

class JumpStartCachedS3ContentKey(JumpStartDataHolderType):
    file_type: Incomplete
    s3_key: Incomplete
    def __init__(self, file_type: JumpStartS3FileType, s3_key: str) -> None: ...

class JumpStartCachedS3ContentValue(JumpStartDataHolderType):
    formatted_content: Incomplete
    md5_hash: Incomplete
    def __init__(
        self,
        formatted_content: dict[JumpStartVersionedModelId | JumpStartModelHeader, JumpStartModelSpecs],
        md5_hash: str | None = None,
    ) -> None: ...

class JumpStartKwargs(JumpStartDataHolderType):
    SERIALIZATION_EXCLUSION_SET: set[str]
    def to_kwargs_dict(self): ...

class JumpStartModelInitKwargs(JumpStartKwargs):
    SERIALIZATION_EXCLUSION_SET: Incomplete
    model_id: Incomplete
    model_version: Incomplete
    instance_type: Incomplete
    region: Incomplete
    image_uri: Incomplete
    model_data: Incomplete
    source_dir: Incomplete
    entry_point: Incomplete
    env: Incomplete
    predictor_cls: Incomplete
    role: Incomplete
    name: Incomplete
    vpc_config: Incomplete
    sagemaker_session: Incomplete
    enable_network_isolation: Incomplete
    model_kms_key: Incomplete
    image_config: Incomplete
    code_location: Incomplete
    container_log_level: Incomplete
    dependencies: Incomplete
    git_config: Incomplete
    tolerate_deprecated_model: Incomplete
    tolerate_vulnerable_model: Incomplete
    def __init__(
        self,
        model_id: str,
        model_version: str | None = None,
        region: str | None = None,
        instance_type: str | None = None,
        image_uri: str | Any | None = None,
        model_data: str | Any | None = None,
        role: str | None = None,
        predictor_cls: Callable[..., Predictor] | Predictor | None = None,
        env: dict[str, str | Any] | None = None,
        name: str | None = None,
        vpc_config: dict[str, list[str | Any]] | None = None,
        sagemaker_session: Any | None = None,
        enable_network_isolation: bool | Any = None,
        model_kms_key: str | None = None,
        image_config: dict[str, str | Any] | None = None,
        source_dir: str | None = None,
        code_location: str | None = None,
        entry_point: str | None = None,
        container_log_level: int | Any | None = None,
        dependencies: list[str] | None = None,
        git_config: dict[str, str] | None = None,
        tolerate_vulnerable_model: bool | None = None,
        tolerate_deprecated_model: bool | None = None,
    ) -> None: ...

class JumpStartModelDeployKwargs(JumpStartKwargs):
    SERIALIZATION_EXCLUSION_SET: Incomplete
    model_id: Incomplete
    model_version: Incomplete
    initial_instance_count: Incomplete
    instance_type: Incomplete
    region: Incomplete
    serializer: Incomplete
    deserializer: Incomplete
    accelerator_type: Incomplete
    endpoint_name: Incomplete
    tags: Incomplete
    kms_key: Incomplete
    wait: Incomplete
    data_capture_config: Incomplete
    async_inference_config: Incomplete
    serverless_inference_config: Incomplete
    volume_size: Incomplete
    model_data_download_timeout: Incomplete
    container_startup_health_check_timeout: Incomplete
    inference_recommendation_id: Incomplete
    explainer_config: Incomplete
    tolerate_vulnerable_model: Incomplete
    tolerate_deprecated_model: Incomplete
    def __init__(
        self,
        model_id: str,
        model_version: str | None = None,
        region: str | None = None,
        initial_instance_count: int | None = None,
        instance_type: str | None = None,
        serializer: Any | None = None,
        deserializer: Any | None = None,
        accelerator_type: str | None = None,
        endpoint_name: str | None = None,
        tags: list[dict[str, str]] | None = None,
        kms_key: str | None = None,
        wait: bool | None = None,
        data_capture_config: Any | None = None,
        async_inference_config: Any | None = None,
        serverless_inference_config: Any | None = None,
        volume_size: int | None = None,
        model_data_download_timeout: int | None = None,
        container_startup_health_check_timeout: int | None = None,
        inference_recommendation_id: str | None = None,
        explainer_config: Any | None = None,
        tolerate_deprecated_model: bool | None = None,
        tolerate_vulnerable_model: bool | None = None,
    ) -> None: ...

class JumpStartEstimatorInitKwargs(JumpStartKwargs):
    SERIALIZATION_EXCLUSION_SET: Incomplete
    model_id: Incomplete
    model_version: Incomplete
    instance_type: Incomplete
    instance_count: Incomplete
    region: Incomplete
    image_uri: Incomplete
    model_uri: Incomplete
    source_dir: Incomplete
    entry_point: Incomplete
    hyperparameters: Incomplete
    metric_definitions: Incomplete
    role: Incomplete
    keep_alive_period_in_seconds: Incomplete
    volume_size: Incomplete
    volume_kms_key: Incomplete
    max_run: Incomplete
    input_mode: Incomplete
    output_path: Incomplete
    output_kms_key: Incomplete
    base_job_name: Incomplete
    sagemaker_session: Incomplete
    tags: Incomplete
    subnets: Incomplete
    security_group_ids: Incomplete
    model_channel_name: Incomplete
    encrypt_inter_container_traffic: Incomplete
    use_spot_instances: Incomplete
    max_wait: Incomplete
    checkpoint_s3_uri: Incomplete
    checkpoint_local_path: Incomplete
    enable_network_isolation: Incomplete
    rules: Incomplete
    debugger_hook_config: Incomplete
    tensorboard_output_config: Incomplete
    enable_sagemaker_metrics: Incomplete
    profiler_config: Incomplete
    disable_profiler: Incomplete
    environment: Incomplete
    max_retry_attempts: Incomplete
    git_config: Incomplete
    container_log_level: Incomplete
    code_location: Incomplete
    dependencies: Incomplete
    instance_groups: Incomplete
    training_repository_access_mode: Incomplete
    training_repository_credentials_provider_arn: Incomplete
    tolerate_vulnerable_model: Incomplete
    tolerate_deprecated_model: Incomplete
    def __init__(
        self,
        model_id: str,
        model_version: str | None = None,
        region: str | None = None,
        image_uri: str | Any | None = None,
        role: str | None = None,
        instance_count: int | Any | None = None,
        instance_type: str | Any | None = None,
        keep_alive_period_in_seconds: int | Any | None = None,
        volume_size: int | Any | None = None,
        volume_kms_key: str | Any | None = None,
        max_run: int | Any | None = None,
        input_mode: str | Any | None = None,
        output_path: str | Any | None = None,
        output_kms_key: str | Any | None = None,
        base_job_name: str | None = None,
        sagemaker_session: Any | None = None,
        hyperparameters: dict[str, str | Any] | None = None,
        tags: list[dict[str, str | Any]] | None = None,
        subnets: list[str | Any] | None = None,
        security_group_ids: list[str | Any] | None = None,
        model_uri: str | None = None,
        model_channel_name: str | Any | None = None,
        metric_definitions: list[dict[str, str | Any]] | None = None,
        encrypt_inter_container_traffic: bool | Any = None,
        use_spot_instances: bool | Any | None = None,
        max_wait: int | Any | None = None,
        checkpoint_s3_uri: str | Any | None = None,
        checkpoint_local_path: str | Any | None = None,
        enable_network_isolation: bool | Any = None,
        rules: list[Any] | None = None,
        debugger_hook_config: Any | bool | None = None,
        tensorboard_output_config: Any | None = None,
        enable_sagemaker_metrics: bool | Any | None = None,
        profiler_config: Any | None = None,
        disable_profiler: bool | None = None,
        environment: dict[str, str | Any] | None = None,
        max_retry_attempts: int | Any | None = None,
        source_dir: str | Any | None = None,
        git_config: dict[str, str] | None = None,
        container_log_level: int | Any | None = None,
        code_location: str | None = None,
        entry_point: str | Any | None = None,
        dependencies: list[str] | None = None,
        instance_groups: list[Any] | None = None,
        training_repository_access_mode: str | Any | None = None,
        training_repository_credentials_provider_arn: str | Any | None = None,
        tolerate_vulnerable_model: bool | None = None,
        tolerate_deprecated_model: bool | None = None,
    ) -> None: ...

class JumpStartEstimatorFitKwargs(JumpStartKwargs):
    SERIALIZATION_EXCLUSION_SET: Incomplete
    model_id: Incomplete
    model_version: Incomplete
    region: Incomplete
    inputs: Incomplete
    wait: Incomplete
    logs: Incomplete
    job_name: Incomplete
    experiment_config: Incomplete
    tolerate_deprecated_model: Incomplete
    tolerate_vulnerable_model: Incomplete
    def __init__(
        self,
        model_id: str,
        model_version: str | None = None,
        region: str | None = None,
        inputs: str | dict[Any, Any] | None = None,
        wait: bool | None = None,
        logs: str | None = None,
        job_name: str | None = None,
        experiment_config: dict[str, str] | None = None,
        tolerate_deprecated_model: bool | None = None,
        tolerate_vulnerable_model: bool | None = None,
    ) -> None: ...

class JumpStartEstimatorDeployKwargs(JumpStartKwargs):
    SERIALIZATION_EXCLUSION_SET: Incomplete
    model_id: Incomplete
    model_version: Incomplete
    instance_type: Incomplete
    initial_instance_count: Incomplete
    region: Incomplete
    image_uri: Incomplete
    source_dir: Incomplete
    entry_point: Incomplete
    env: Incomplete
    predictor_cls: Incomplete
    serializer: Incomplete
    deserializer: Incomplete
    accelerator_type: Incomplete
    endpoint_name: Incomplete
    tags: Incomplete
    kms_key: Incomplete
    wait: Incomplete
    data_capture_config: Incomplete
    async_inference_config: Incomplete
    serverless_inference_config: Incomplete
    volume_size: Incomplete
    model_data_download_timeout: Incomplete
    container_startup_health_check_timeout: Incomplete
    inference_recommendation_id: Incomplete
    explainer_config: Incomplete
    role: Incomplete
    model_name: Incomplete
    vpc_config: Incomplete
    sagemaker_session: Incomplete
    enable_network_isolation: Incomplete
    model_kms_key: Incomplete
    image_config: Incomplete
    code_location: Incomplete
    container_log_level: Incomplete
    dependencies: Incomplete
    git_config: Incomplete
    tolerate_deprecated_model: Incomplete
    tolerate_vulnerable_model: Incomplete
    use_compiled_model: Incomplete
    def __init__(
        self,
        model_id: str,
        model_version: str | None = None,
        region: str | None = None,
        initial_instance_count: int | None = None,
        instance_type: str | None = None,
        serializer: Any | None = None,
        deserializer: Any | None = None,
        accelerator_type: str | None = None,
        endpoint_name: str | None = None,
        tags: list[dict[str, str]] | None = None,
        kms_key: str | None = None,
        wait: bool | None = None,
        data_capture_config: Any | None = None,
        async_inference_config: Any | None = None,
        serverless_inference_config: Any | None = None,
        volume_size: int | None = None,
        model_data_download_timeout: int | None = None,
        container_startup_health_check_timeout: int | None = None,
        inference_recommendation_id: str | None = None,
        explainer_config: Any | None = None,
        image_uri: str | Any | None = None,
        role: str | None = None,
        predictor_cls: Callable[..., Predictor] | Predictor | None = None,
        env: dict[str, str | Any] | None = None,
        model_name: str | None = None,
        vpc_config: dict[str, list[str | Any]] | None = None,
        sagemaker_session: Any | None = None,
        enable_network_isolation: bool | Any = None,
        model_kms_key: str | None = None,
        image_config: dict[str, str | Any] | None = None,
        source_dir: str | None = None,
        code_location: str | None = None,
        entry_point: str | None = None,
        container_log_level: int | Any | None = None,
        dependencies: list[str] | None = None,
        git_config: dict[str, str] | None = None,
        tolerate_deprecated_model: bool | None = None,
        tolerate_vulnerable_model: bool | None = None,
        use_compiled_model: bool = False,
    ) -> None: ...
