from _typeshed import Incomplete
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Union

class JumpStartDataHolderType:
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class JumpStartS3FileType(str, Enum):
    MANIFEST: str
    SPECS: str

class JumpStartLaunchedRegionInfo(JumpStartDataHolderType):
    content_bucket: Incomplete
    region_name: Incomplete
    def __init__(self, content_bucket: str, region_name: str) -> None: ...

class JumpStartModelHeader(JumpStartDataHolderType):
    def __init__(self, header: Dict[str, str]) -> None: ...
    def to_json(self) -> Dict[str, str]: ...
    model_id: Incomplete
    version: Incomplete
    min_version: Incomplete
    spec_key: Incomplete
    def from_json(self, json_obj: Dict[str, str]) -> None: ...

class JumpStartECRSpecs(JumpStartDataHolderType):
    def __init__(self, spec: Dict[str, Any]) -> None: ...
    framework: Incomplete
    framework_version: Incomplete
    py_version: Incomplete
    huggingface_transformers_version: Incomplete
    def from_json(self, json_obj: Dict[str, Any]) -> None: ...
    def to_json(self) -> Dict[str, Any]: ...

class JumpStartHyperparameter(JumpStartDataHolderType):
    def __init__(self, spec: Dict[str, Any]) -> None: ...
    name: Incomplete
    type: Incomplete
    default: Incomplete
    scope: Incomplete
    options: Incomplete
    min: Incomplete
    max: Incomplete
    exclusive_min: Incomplete
    exclusive_max: Incomplete
    def from_json(self, json_obj: Dict[str, Any]) -> None: ...
    def to_json(self) -> Dict[str, Any]: ...

class JumpStartEnvironmentVariable(JumpStartDataHolderType):
    def __init__(self, spec: Dict[str, Any]) -> None: ...
    name: Incomplete
    type: Incomplete
    default: Incomplete
    scope: Incomplete
    required_for_model_class: Incomplete
    def from_json(self, json_obj: Dict[str, Any]) -> None: ...
    def to_json(self) -> Dict[str, Any]: ...

class JumpStartPredictorSpecs(JumpStartDataHolderType):
    def __init__(self, spec: Optional[Dict[str, Any]]) -> None: ...
    default_content_type: Incomplete
    supported_content_types: Incomplete
    default_accept_type: Incomplete
    supported_accept_types: Incomplete
    def from_json(self, json_obj: Optional[Dict[str, Any]]) -> None: ...
    def to_json(self) -> Dict[str, Any]: ...

class JumpStartModelSpecs(JumpStartDataHolderType):
    def __init__(self, spec: Dict[str, Any]) -> None: ...
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
    def from_json(self, json_obj: Dict[str, Any]) -> None: ...
    def to_json(self) -> Dict[str, Any]: ...
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
        formatted_content: Dict[JumpStartVersionedModelId | JumpStartModelHeader, JumpStartModelSpecs],
        md5_hash: Optional[str] = None,
    ) -> None: ...

class JumpStartKwargs(JumpStartDataHolderType):
    SERIALIZATION_EXCLUSION_SET: Set[str]
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
        model_version: Optional[str] = None,
        region: Optional[str] = None,
        instance_type: Optional[str] = None,
        image_uri: Optional[str | Any] = None,
        model_data: Optional[str | Any] = None,
        role: Optional[str] = None,
        predictor_cls: Optional[callable] = None,
        env: Optional[Dict[str, str | Any]] = None,
        name: Optional[str] = None,
        vpc_config: Optional[Dict[str, List[str | Any]]] = None,
        sagemaker_session: Optional[Any] = None,
        enable_network_isolation: bool | Any = None,
        model_kms_key: Optional[str] = None,
        image_config: Optional[Dict[str, str | Any]] = None,
        source_dir: Optional[str] = None,
        code_location: Optional[str] = None,
        entry_point: Optional[str] = None,
        container_log_level: Optional[int | Any] = None,
        dependencies: Optional[List[str]] = None,
        git_config: Optional[Dict[str, str]] = None,
        tolerate_vulnerable_model: Optional[bool] = None,
        tolerate_deprecated_model: Optional[bool] = None,
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
        model_version: Optional[str] = None,
        region: Optional[str] = None,
        initial_instance_count: Optional[int] = None,
        instance_type: Optional[str] = None,
        serializer: Optional[Any] = None,
        deserializer: Optional[Any] = None,
        accelerator_type: Optional[str] = None,
        endpoint_name: Optional[str] = None,
        tags: List[Dict[str, str]] = None,
        kms_key: Optional[str] = None,
        wait: Optional[bool] = None,
        data_capture_config: Optional[Any] = None,
        async_inference_config: Optional[Any] = None,
        serverless_inference_config: Optional[Any] = None,
        volume_size: Optional[int] = None,
        model_data_download_timeout: Optional[int] = None,
        container_startup_health_check_timeout: Optional[int] = None,
        inference_recommendation_id: Optional[str] = None,
        explainer_config: Optional[Any] = None,
        tolerate_deprecated_model: Optional[bool] = None,
        tolerate_vulnerable_model: Optional[bool] = None,
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
        model_version: Optional[str] = None,
        region: Optional[str] = None,
        image_uri: Optional[str | Any] = None,
        role: Optional[str] = None,
        instance_count: Optional[int | Any] = None,
        instance_type: Optional[str | Any] = None,
        keep_alive_period_in_seconds: Optional[int | Any] = None,
        volume_size: Optional[int | Any] = None,
        volume_kms_key: Optional[str | Any] = None,
        max_run: Optional[int | Any] = None,
        input_mode: Optional[str | Any] = None,
        output_path: Optional[str | Any] = None,
        output_kms_key: Optional[str | Any] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Any] = None,
        hyperparameters: Optional[Dict[str, str | Any]] = None,
        tags: Optional[List[Dict[str, str | Any]]] = None,
        subnets: Optional[List[str | Any]] = None,
        security_group_ids: Optional[List[str | Any]] = None,
        model_uri: Optional[str] = None,
        model_channel_name: Optional[str | Any] = None,
        metric_definitions: Optional[List[Dict[str, str | Any]]] = None,
        encrypt_inter_container_traffic: bool | Any = None,
        use_spot_instances: Optional[bool | Any] = None,
        max_wait: Optional[int | Any] = None,
        checkpoint_s3_uri: Optional[str | Any] = None,
        checkpoint_local_path: Optional[str | Any] = None,
        enable_network_isolation: bool | Any = None,
        rules: Optional[List[Any]] = None,
        debugger_hook_config: Optional[Any | bool] = None,
        tensorboard_output_config: Optional[Any] = None,
        enable_sagemaker_metrics: Optional[bool | Any] = None,
        profiler_config: Optional[Any] = None,
        disable_profiler: Optional[bool] = None,
        environment: Optional[Dict[str, str | Any]] = None,
        max_retry_attempts: Optional[int | Any] = None,
        source_dir: Optional[str | Any] = None,
        git_config: Optional[Dict[str, str]] = None,
        container_log_level: Optional[int | Any] = None,
        code_location: Optional[str] = None,
        entry_point: Optional[str | Any] = None,
        dependencies: Optional[List[str]] = None,
        instance_groups: Optional[List[Any]] = None,
        training_repository_access_mode: Optional[str | Any] = None,
        training_repository_credentials_provider_arn: Optional[str | Any] = None,
        tolerate_vulnerable_model: Optional[bool] = None,
        tolerate_deprecated_model: Optional[bool] = None,
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
        model_version: Optional[str] = None,
        region: Optional[str] = None,
        inputs: Optional[str | Dict | Any | Any] = None,
        wait: Optional[bool] = None,
        logs: Optional[str] = None,
        job_name: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
        tolerate_deprecated_model: Optional[bool] = None,
        tolerate_vulnerable_model: Optional[bool] = None,
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
        model_version: Optional[str] = None,
        region: Optional[str] = None,
        initial_instance_count: Optional[int] = None,
        instance_type: Optional[str] = None,
        serializer: Optional[Any] = None,
        deserializer: Optional[Any] = None,
        accelerator_type: Optional[str] = None,
        endpoint_name: Optional[str] = None,
        tags: List[Dict[str, str]] = None,
        kms_key: Optional[str] = None,
        wait: Optional[bool] = None,
        data_capture_config: Optional[Any] = None,
        async_inference_config: Optional[Any] = None,
        serverless_inference_config: Optional[Any] = None,
        volume_size: Optional[int] = None,
        model_data_download_timeout: Optional[int] = None,
        container_startup_health_check_timeout: Optional[int] = None,
        inference_recommendation_id: Optional[str] = None,
        explainer_config: Optional[Any] = None,
        image_uri: Optional[str | Any] = None,
        role: Optional[str] = None,
        predictor_cls: Optional[callable] = None,
        env: Optional[Dict[str, str | Any]] = None,
        model_name: Optional[str] = None,
        vpc_config: Optional[Dict[str, List[str | Any]]] = None,
        sagemaker_session: Optional[Any] = None,
        enable_network_isolation: bool | Any = None,
        model_kms_key: Optional[str] = None,
        image_config: Optional[Dict[str, str | Any]] = None,
        source_dir: Optional[str] = None,
        code_location: Optional[str] = None,
        entry_point: Optional[str] = None,
        container_log_level: Optional[int | Any] = None,
        dependencies: Optional[List[str]] = None,
        git_config: Optional[Dict[str, str]] = None,
        tolerate_deprecated_model: Optional[bool] = None,
        tolerate_vulnerable_model: Optional[bool] = None,
        use_compiled_model: bool = False,
    ) -> None: ...
