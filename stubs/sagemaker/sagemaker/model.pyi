import abc
from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.drift_check_baselines import DriftCheckBaselines
from sagemaker.inference_recommender.inference_recommender_mixin import InferenceRecommenderMixin
from sagemaker.metadata_properties import MetadataProperties
from sagemaker.model_metrics import ModelMetrics
from sagemaker.predictor import PredictorBase
from sagemaker.serverless import ServerlessInferenceConfig
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

LOGGER: Incomplete
NEO_ALLOWED_FRAMEWORKS: Incomplete
NEO_IOC_TARGET_DEVICES: Incomplete
NEO_MULTIVERSION_UNSUPPORTED: Incomplete

class ModelBase(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def deploy(self, *args, **kwargs) -> PredictorBase: ...
    @abc.abstractmethod
    def delete_model(self, *args, **kwargs) -> None: ...

SCRIPT_PARAM_NAME: str
DIR_PARAM_NAME: str
CONTAINER_LOG_LEVEL_PARAM_NAME: str
JOB_NAME_PARAM_NAME: str
MODEL_SERVER_WORKERS_PARAM_NAME: str
SAGEMAKER_REGION_PARAM_NAME: str
SAGEMAKER_OUTPUT_LOCATION: str

class Model(ModelBase, InferenceRecommenderMixin):
    model_data: Incomplete
    image_uri: Incomplete
    predictor_cls: Incomplete
    name: Incomplete
    sagemaker_session: Incomplete
    role: Incomplete
    vpc_config: Incomplete
    endpoint_name: Incomplete
    inference_recommender_job_results: Incomplete
    inference_recommendations: Incomplete
    env: Incomplete
    model_kms_key: Incomplete
    image_config: Incomplete
    entry_point: Incomplete
    source_dir: Incomplete
    dependencies: Incomplete
    git_config: Incomplete
    container_log_level: Incomplete
    uploaded_code: Incomplete
    repacked_model_data: Incomplete
    def __init__(
        self,
        image_uri: str | PipelineVariable,
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
        container_log_level: int | PipelineVariable = 20,
        dependencies: Optional[List[str]] = None,
        git_config: Optional[Dict[str, str]] = None,
    ) -> None: ...
    def register(
        self,
        content_types: List[str | PipelineVariable],
        response_types: List[str | PipelineVariable],
        inference_instances: Optional[List[str | PipelineVariable]] = None,
        transform_instances: Optional[List[str | PipelineVariable]] = None,
        model_package_name: Optional[str | PipelineVariable] = None,
        model_package_group_name: Optional[str | PipelineVariable] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        model_metrics: Optional[ModelMetrics] = None,
        metadata_properties: Optional[MetadataProperties] = None,
        marketplace_cert: bool = False,
        approval_status: Optional[str | PipelineVariable] = None,
        description: Optional[str] = None,
        drift_check_baselines: Optional[DriftCheckBaselines] = None,
        customer_metadata_properties: Optional[Dict[str, str | PipelineVariable]] = None,
        validation_specification: Optional[str | PipelineVariable] = None,
        domain: Optional[str | PipelineVariable] = None,
        task: Optional[str | PipelineVariable] = None,
        sample_payload_url: Optional[str | PipelineVariable] = None,
        framework: Optional[str | PipelineVariable] = None,
        framework_version: Optional[str | PipelineVariable] = None,
        nearest_model_name: Optional[str | PipelineVariable] = None,
        data_input_configuration: Optional[str | PipelineVariable] = None,
    ): ...
    def create(
        self,
        instance_type: Optional[str] = None,
        accelerator_type: Optional[str] = None,
        serverless_inference_config: Optional[ServerlessInferenceConfig] = None,
        tags: Optional[List[Dict[str, str | PipelineVariable]]] = None,
    ): ...
    def prepare_container_def(
        self,
        instance_type: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
    ): ...
    def enable_network_isolation(self): ...
    def package_for_edge(
        self,
        output_path,
        model_name,
        model_version,
        role: Incomplete | None = None,
        job_name: Incomplete | None = None,
        resource_key: Incomplete | None = None,
        s3_kms_key: Incomplete | None = None,
        tags: Incomplete | None = None,
    ): ...
    def compile(
        self,
        target_instance_family,
        input_shape,
        output_path,
        role: Incomplete | None = None,
        tags: Incomplete | None = None,
        job_name: Incomplete | None = None,
        compile_max_run=900,
        framework: Incomplete | None = None,
        framework_version: Incomplete | None = None,
        target_platform_os: Incomplete | None = None,
        target_platform_arch: Incomplete | None = None,
        target_platform_accelerator: Incomplete | None = None,
        compiler_options: Incomplete | None = None,
    ): ...
    def deploy(
        self,
        initial_instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        serializer: Incomplete | None = None,
        deserializer: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        endpoint_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        wait: bool = True,
        data_capture_config: Incomplete | None = None,
        async_inference_config: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
        volume_size: Incomplete | None = None,
        model_data_download_timeout: Incomplete | None = None,
        container_startup_health_check_timeout: Incomplete | None = None,
        inference_recommendation_id: Incomplete | None = None,
        explainer_config: Incomplete | None = None,
        **kwargs,
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

class FrameworkModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        image_uri: str | PipelineVariable,
        role: Optional[str] = None,
        entry_point: Optional[str] = None,
        source_dir: Optional[str] = None,
        predictor_cls: Optional[callable] = None,
        env: Optional[Dict[str, str | PipelineVariable]] = None,
        name: Optional[str] = None,
        container_log_level: int | PipelineVariable = 20,
        code_location: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        dependencies: Optional[List[str]] = None,
        git_config: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> None: ...

MODEL_PACKAGE_ARN_PATTERN: str

class ModelPackage(Model):
    algorithm_arn: Incomplete
    model_data: Incomplete
    model_package_arn: Incomplete
    def __init__(
        self,
        role: Incomplete | None = None,
        model_data: Incomplete | None = None,
        algorithm_arn: Incomplete | None = None,
        model_package_arn: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def enable_network_isolation(self): ...
