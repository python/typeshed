import abc
from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.inputs import BatchDataCaptureConfig
from sagemaker.job import _Job
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class Transformer:
    JOB_CLASS_NAME: str
    model_name: Incomplete
    strategy: Incomplete
    output_path: Incomplete
    accept: Incomplete
    assemble_with: Incomplete
    instance_count: Incomplete
    instance_type: Incomplete
    max_concurrent_transforms: Incomplete
    max_payload: Incomplete
    tags: Incomplete
    base_transform_job_name: Incomplete
    latest_transform_job: Incomplete
    sagemaker_session: Incomplete
    volume_kms_key: Incomplete
    output_kms_key: Incomplete
    env: Incomplete
    def __init__(
        self,
        model_name: str | PipelineVariable,
        instance_count: int | PipelineVariable,
        instance_type: str | PipelineVariable,
        strategy: str | PipelineVariable | None = None,
        assemble_with: str | PipelineVariable | None = None,
        output_path: str | PipelineVariable | None = None,
        output_kms_key: str | PipelineVariable | None = None,
        accept: str | PipelineVariable | None = None,
        max_concurrent_transforms: int | PipelineVariable | None = None,
        max_payload: int | PipelineVariable | None = None,
        tags: list[dict[str, str | PipelineVariable]] | None = None,
        env: dict[str, str | PipelineVariable] | None = None,
        base_transform_job_name: str | None = None,
        sagemaker_session: Session | None = None,
        volume_kms_key: str | PipelineVariable | None = None,
    ) -> None: ...
    def transform(
        self,
        data: str | PipelineVariable,
        data_type: str | PipelineVariable = "S3Prefix",
        content_type: str | PipelineVariable | None = None,
        compression_type: str | PipelineVariable | None = None,
        split_type: str | PipelineVariable | None = None,
        job_name: str | None = None,
        input_filter: str | PipelineVariable | None = None,
        output_filter: str | PipelineVariable | None = None,
        join_source: str | PipelineVariable | None = None,
        experiment_config: dict[str, str] | None = None,
        model_client_config: dict[str, str | PipelineVariable] | None = None,
        batch_data_capture_config: BatchDataCaptureConfig | None = None,
        wait: bool = True,
        logs: bool = True,
    ): ...
    def transform_with_monitoring(
        self,
        monitoring_config,
        monitoring_resource_config,
        data: str,
        data_type: str = "S3Prefix",
        content_type: str | None = None,
        compression_type: str | None = None,
        split_type: str | None = None,
        input_filter: str | None = None,
        output_filter: str | None = None,
        join_source: str | None = None,
        model_client_config: dict[str, str] | None = None,
        batch_data_capture_config: BatchDataCaptureConfig | None = None,
        monitor_before_transform: bool = False,
        supplied_baseline_statistics: str | None = None,
        supplied_baseline_constraints: str | None = None,
        wait: bool = True,
        pipeline_name: str | None = None,
        role: str | None = None,
    ): ...
    def delete_model(self) -> None: ...
    def wait(self, logs: bool = True) -> None: ...
    def stop_transform_job(self, wait: bool = True) -> None: ...
    @classmethod
    def attach(cls, transform_job_name, sagemaker_session: Incomplete | None = None): ...

class _TransformJob(_Job, metaclass=abc.ABCMeta):
    @classmethod
    def start_new(
        cls,
        transformer,
        data,
        data_type,
        content_type,
        compression_type,
        split_type,
        input_filter,
        output_filter,
        join_source,
        experiment_config,
        model_client_config,
        batch_data_capture_config,
    ): ...
    def wait(self, logs: bool = True) -> None: ...
    def stop(self) -> None: ...
