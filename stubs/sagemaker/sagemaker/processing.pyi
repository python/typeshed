from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.apiutils._base_types import ApiObject
from sagemaker.dataset_definition.inputs import DatasetDefinition, S3Input
from sagemaker.job import _Job
from sagemaker.network import NetworkConfig
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class Processor:
    JOB_CLASS_NAME: str
    image_uri: Incomplete
    instance_count: Incomplete
    instance_type: Incomplete
    entrypoint: Incomplete
    volume_size_in_gb: Incomplete
    max_runtime_in_seconds: Incomplete
    base_job_name: Incomplete
    tags: Incomplete
    jobs: Incomplete
    latest_job: Incomplete
    arguments: Incomplete
    sagemaker_session: Incomplete
    output_kms_key: Incomplete
    volume_kms_key: Incomplete
    network_config: Incomplete
    role: Incomplete
    env: Incomplete
    def __init__(
        self,
        role: str | None = None,
        image_uri: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        entrypoint: list[str | PipelineVariable] | None = None,
        volume_size_in_gb: int | PipelineVariable = 30,
        volume_kms_key: str | PipelineVariable | None = None,
        output_kms_key: str | PipelineVariable | None = None,
        max_runtime_in_seconds: int | PipelineVariable | None = None,
        base_job_name: str | None = None,
        sagemaker_session: Session | None = None,
        env: dict[str, str | PipelineVariable] | None = None,
        tags: list[dict[str, str | PipelineVariable]] | None = None,
        network_config: NetworkConfig | None = None,
    ) -> None: ...
    def run(
        self,
        inputs: list["ProcessingInput"] | None = None,
        outputs: list["ProcessingOutput"] | None = None,
        arguments: list[str | PipelineVariable] | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
        experiment_config: dict[str, str] | None = None,
        kms_key: str | None = None,
    ): ...

class ScriptProcessor(Processor):
    command: Incomplete
    def __init__(
        self,
        role: str | PipelineVariable | None = None,
        image_uri: str | PipelineVariable | None = None,
        command: list[str] | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        volume_size_in_gb: int | PipelineVariable = 30,
        volume_kms_key: str | PipelineVariable | None = None,
        output_kms_key: str | PipelineVariable | None = None,
        max_runtime_in_seconds: int | PipelineVariable | None = None,
        base_job_name: str | None = None,
        sagemaker_session: Session | None = None,
        env: dict[str, str | PipelineVariable] | None = None,
        tags: list[dict[str, str | PipelineVariable]] | None = None,
        network_config: NetworkConfig | None = None,
    ) -> None: ...
    def get_run_args(
        self, code, inputs: Incomplete | None = None, outputs: Incomplete | None = None, arguments: Incomplete | None = None
    ): ...
    latest_job: Incomplete
    def run(
        self,
        code: str,
        inputs: list["ProcessingInput"] | None = None,
        outputs: list["ProcessingOutput"] | None = None,
        arguments: list[str | PipelineVariable] | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
        experiment_config: dict[str, str] | None = None,
        kms_key: str | None = None,
    ): ...

class ProcessingJob(_Job):
    inputs: Incomplete
    outputs: Incomplete
    output_kms_key: Incomplete
    def __init__(self, sagemaker_session, job_name, inputs, outputs, output_kms_key: Incomplete | None = None) -> None: ...
    @classmethod
    def start_new(cls, processor, inputs, outputs, experiment_config): ...
    @classmethod
    def from_processing_name(cls, sagemaker_session, processing_job_name): ...
    @classmethod
    def from_processing_arn(cls, sagemaker_session, processing_job_arn): ...
    def wait(self, logs: bool = True) -> None: ...
    def describe(self): ...
    def stop(self) -> None: ...
    @staticmethod
    def prepare_app_specification(container_arguments, container_entrypoint, image_uri): ...
    @staticmethod
    def prepare_output_config(kms_key_id, outputs): ...
    @staticmethod
    def prepare_processing_resources(instance_count, instance_type, volume_kms_key_id, volume_size_in_gb): ...
    @staticmethod
    def prepare_stopping_condition(max_runtime_in_seconds): ...

class ProcessingInput:
    source: Incomplete
    destination: Incomplete
    input_name: Incomplete
    s3_data_type: Incomplete
    s3_input_mode: Incomplete
    s3_data_distribution_type: Incomplete
    s3_compression_type: Incomplete
    s3_input: Incomplete
    dataset_definition: Incomplete
    app_managed: Incomplete
    def __init__(
        self,
        source: str | PipelineVariable | None = None,
        destination: str | PipelineVariable | None = None,
        input_name: str | PipelineVariable | None = None,
        s3_data_type: str | PipelineVariable = "S3Prefix",
        s3_input_mode: str | PipelineVariable = "File",
        s3_data_distribution_type: str | PipelineVariable = "FullyReplicated",
        s3_compression_type: str | PipelineVariable = "None",
        s3_input: S3Input | None = None,
        dataset_definition: DatasetDefinition | None = None,
        app_managed: bool | PipelineVariable = False,
    ) -> None: ...

class ProcessingOutput:
    source: Incomplete
    destination: Incomplete
    output_name: Incomplete
    s3_upload_mode: Incomplete
    app_managed: Incomplete
    feature_store_output: Incomplete
    def __init__(
        self,
        source: str | PipelineVariable | None = None,
        destination: str | PipelineVariable | None = None,
        output_name: str | PipelineVariable | None = None,
        s3_upload_mode: str | PipelineVariable = "EndOfJob",
        app_managed: bool | PipelineVariable = False,
        feature_store_output: Optional["FeatureStoreOutput"] = None,
    ) -> None: ...

class RunArgs:
    code: Incomplete
    inputs: Incomplete
    outputs: Incomplete
    arguments: Incomplete
    def __init__(self, code, inputs, outputs, arguments) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class FeatureStoreOutput(ApiObject):
    feature_group_name: Incomplete

class FrameworkProcessor(ScriptProcessor):
    framework_entrypoint_command: Incomplete
    estimator_cls: Incomplete
    framework_version: Incomplete
    py_version: Incomplete
    code_location: Incomplete
    image_uri: Incomplete
    base_job_name: Incomplete
    def __init__(
        self,
        estimator_cls: type,
        framework_version: str,
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        py_version: str = "py3",
        image_uri: str | PipelineVariable | None = None,
        command: list[str] | None = None,
        volume_size_in_gb: int | PipelineVariable = 30,
        volume_kms_key: str | PipelineVariable | None = None,
        output_kms_key: str | PipelineVariable | None = None,
        code_location: str | None = None,
        max_runtime_in_seconds: int | PipelineVariable | None = None,
        base_job_name: str | None = None,
        sagemaker_session: Session | None = None,
        env: dict[str, str | PipelineVariable] | None = None,
        tags: list[dict[str, str | PipelineVariable]] | None = None,
        network_config: NetworkConfig | None = None,
    ) -> None: ...
    def get_run_args(
        self,
        code,
        source_dir: Incomplete | None = None,
        dependencies: Incomplete | None = None,
        git_config: Incomplete | None = None,
        inputs: Incomplete | None = None,
        outputs: Incomplete | None = None,
        arguments: Incomplete | None = None,
        job_name: Incomplete | None = None,
    ): ...
    def run(
        self,
        code: str,
        source_dir: str | None = None,
        dependencies: list[str] | None = None,
        git_config: dict[str, str] | None = None,
        inputs: list[ProcessingInput] | None = None,
        outputs: list[ProcessingOutput] | None = None,
        arguments: list[str | PipelineVariable] | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
        experiment_config: dict[str, str] | None = None,
        kms_key: str | None = None,
    ): ...
