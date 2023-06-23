import abc
from _typeshed import Incomplete
from typing import Dict, List, Optional, Union

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
        model_name: Union[str, PipelineVariable],
        instance_count: Union[int, PipelineVariable],
        instance_type: Union[str, PipelineVariable],
        strategy: Optional[Union[str, PipelineVariable]] = None,
        assemble_with: Optional[Union[str, PipelineVariable]] = None,
        output_path: Optional[Union[str, PipelineVariable]] = None,
        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
        accept: Optional[Union[str, PipelineVariable]] = None,
        max_concurrent_transforms: Optional[Union[int, PipelineVariable]] = None,
        max_payload: Optional[Union[int, PipelineVariable]] = None,
        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
        env: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
        base_transform_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
    ) -> None: ...
    def transform(
        self,
        data: Union[str, PipelineVariable],
        data_type: Union[str, PipelineVariable] = "S3Prefix",
        content_type: Optional[Union[str, PipelineVariable]] = None,
        compression_type: Optional[Union[str, PipelineVariable]] = None,
        split_type: Optional[Union[str, PipelineVariable]] = None,
        job_name: Optional[str] = None,
        input_filter: Optional[Union[str, PipelineVariable]] = None,
        output_filter: Optional[Union[str, PipelineVariable]] = None,
        join_source: Optional[Union[str, PipelineVariable]] = None,
        experiment_config: Optional[Dict[str, str]] = None,
        model_client_config: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
        batch_data_capture_config: BatchDataCaptureConfig = None,
        wait: bool = True,
        logs: bool = True,
    ): ...
    def transform_with_monitoring(
        self,
        monitoring_config,
        monitoring_resource_config,
        data: str,
        data_type: str = "S3Prefix",
        content_type: str = None,
        compression_type: str = None,
        split_type: str = None,
        input_filter: str = None,
        output_filter: str = None,
        join_source: str = None,
        model_client_config: Dict[str, str] = None,
        batch_data_capture_config: BatchDataCaptureConfig = None,
        monitor_before_transform: bool = False,
        supplied_baseline_statistics: str = None,
        supplied_baseline_constraints: str = None,
        wait: bool = True,
        pipeline_name: str = None,
        role: str = None,
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
