import abc
from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.job import _Job
from sagemaker.session import Session

logger: Incomplete

class AutoMLInput:
    inputs: Incomplete
    target_attribute_name: Incomplete
    compression: Incomplete
    channel_type: Incomplete
    content_type: Incomplete
    s3_data_type: Incomplete
    sample_weight_attribute_name: Incomplete
    def __init__(
        self,
        inputs,
        target_attribute_name,
        compression: Incomplete | None = None,
        channel_type: Incomplete | None = None,
        content_type: Incomplete | None = None,
        s3_data_type: Incomplete | None = None,
        sample_weight_attribute_name: Incomplete | None = None,
    ) -> None: ...
    def to_request_dict(self): ...

class AutoML:
    output_path: Incomplete
    base_job_name: Incomplete
    compression_type: Incomplete
    encrypt_inter_container_traffic: Incomplete
    problem_type: Incomplete
    max_candidate: Incomplete
    max_runtime_per_training_job_in_seconds: Incomplete
    total_job_runtime_in_seconds: Incomplete
    target_attribute_name: Incomplete
    job_objective: Incomplete
    generate_candidate_definitions_only: Incomplete
    tags: Incomplete
    content_type: Incomplete
    s3_data_type: Incomplete
    feature_specification_s3_uri: Incomplete
    validation_fraction: Incomplete
    mode: Incomplete
    auto_generate_endpoint_name: Incomplete
    endpoint_name: Incomplete
    current_job_name: Incomplete
    sagemaker_session: Incomplete
    vpc_config: Incomplete
    volume_kms_key: Incomplete
    output_kms_key: Incomplete
    role: Incomplete
    sample_weight_attribute_name: Incomplete
    def __init__(
        self,
        role: Optional[str] = None,
        target_attribute_name: str = None,
        output_kms_key: Optional[str] = None,
        output_path: Optional[str] = None,
        base_job_name: Optional[str] = None,
        compression_type: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        volume_kms_key: Optional[str] = None,
        encrypt_inter_container_traffic: Optional[bool] = None,
        vpc_config: Optional[Dict[str, List]] = None,
        problem_type: Optional[str] = None,
        max_candidates: Optional[int] = None,
        max_runtime_per_training_job_in_seconds: Optional[int] = None,
        total_job_runtime_in_seconds: Optional[int] = None,
        job_objective: Optional[Dict[str, str]] = None,
        generate_candidate_definitions_only: Optional[bool] = False,
        tags: Optional[List[Dict[str, str]]] = None,
        content_type: Optional[str] = None,
        s3_data_type: Optional[str] = None,
        feature_specification_s3_uri: Optional[str] = None,
        validation_fraction: Optional[float] = None,
        mode: Optional[str] = None,
        auto_generate_endpoint_name: Optional[bool] = None,
        endpoint_name: Optional[str] = None,
        sample_weight_attribute_name: str = None,
    ) -> None: ...
    latest_auto_ml_job: Incomplete
    def fit(
        self, inputs: Incomplete | None = None, wait: bool = True, logs: bool = True, job_name: Incomplete | None = None
    ) -> None: ...
    @classmethod
    def attach(cls, auto_ml_job_name, sagemaker_session: Incomplete | None = None): ...
    def describe_auto_ml_job(self, job_name: Incomplete | None = None): ...
    def best_candidate(self, job_name: Incomplete | None = None): ...
    def list_candidates(
        self,
        job_name: Incomplete | None = None,
        status_equals: Incomplete | None = None,
        candidate_name: Incomplete | None = None,
        candidate_arn: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        max_results: Incomplete | None = None,
    ): ...
    def create_model(
        self,
        name,
        sagemaker_session: Incomplete | None = None,
        candidate: Incomplete | None = None,
        vpc_config: Incomplete | None = None,
        enable_network_isolation: bool = False,
        model_kms_key: Incomplete | None = None,
        predictor_cls: Incomplete | None = None,
        inference_response_keys: Incomplete | None = None,
    ): ...
    def deploy(
        self,
        initial_instance_count,
        instance_type,
        serializer: Incomplete | None = None,
        deserializer: Incomplete | None = None,
        candidate: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
        name: Incomplete | None = None,
        endpoint_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        wait: bool = True,
        vpc_config: Incomplete | None = None,
        enable_network_isolation: bool = False,
        model_kms_key: Incomplete | None = None,
        predictor_cls: Incomplete | None = None,
        inference_response_keys: Incomplete | None = None,
        volume_size: Incomplete | None = None,
        model_data_download_timeout: Incomplete | None = None,
        container_startup_health_check_timeout: Incomplete | None = None,
    ): ...
    @classmethod
    def validate_and_update_inference_response(cls, inference_containers, inference_response_keys) -> None: ...

class AutoMLJob(_Job, metaclass=abc.ABCMeta):
    inputs: Incomplete
    job_name: Incomplete
    def __init__(self, sagemaker_session, job_name, inputs) -> None: ...
    @classmethod
    def start_new(cls, auto_ml, inputs): ...
    def describe(self): ...
    def wait(self, logs: bool = True) -> None: ...
