from _typeshed import Incomplete
from enum import Enum
from typing import Dict, List, Optional, Union

from sagemaker.network import NetworkConfig
from sagemaker.processing import ProcessingInput, ProcessingOutput, ScriptProcessor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class _SparkProcessorBase(ScriptProcessor):
    configuration_location: Incomplete
    dependency_location: Incomplete
    history_server: Incomplete
    image_uri: Incomplete
    def __init__(
        self,
        role: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        instance_count: Incomplete | None = None,
        framework_version: Incomplete | None = None,
        py_version: Incomplete | None = None,
        container_version: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        volume_size_in_gb: int = 30,
        volume_kms_key: Incomplete | None = None,
        output_kms_key: Incomplete | None = None,
        configuration_location: Optional[str] = None,
        dependency_location: Optional[str] = None,
        max_runtime_in_seconds: Incomplete | None = None,
        base_job_name: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
        env: Incomplete | None = None,
        tags: Incomplete | None = None,
        network_config: Incomplete | None = None,
    ) -> None: ...
    def get_run_args(
        self, code, inputs: Incomplete | None = None, outputs: Incomplete | None = None, arguments: Incomplete | None = None
    ): ...
    def run(
        self,
        submit_app,
        inputs: Incomplete | None = None,
        outputs: Incomplete | None = None,
        arguments: Incomplete | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Incomplete | None = None,
        experiment_config: Incomplete | None = None,
        kms_key: Incomplete | None = None,
    ): ...
    def start_history_server(self, spark_event_logs_s3_uri: Incomplete | None = None) -> None: ...
    def terminate_history_server(self) -> None: ...

class PySparkProcessor(_SparkProcessorBase):
    def __init__(
        self,
        role: str = None,
        instance_type: str | PipelineVariable = None,
        instance_count: int | PipelineVariable = None,
        framework_version: Optional[str] = None,
        py_version: Optional[str] = None,
        container_version: Optional[str] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        volume_size_in_gb: int | PipelineVariable = 30,
        volume_kms_key: Optional[str | PipelineVariable] = None,
        output_kms_key: Optional[str | PipelineVariable] = None,
        configuration_location: Optional[str] = None,
        dependency_location: Optional[str] = None,
        max_runtime_in_seconds: Optional[int | PipelineVariable] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        env: Optional[Dict[str, str | PipelineVariable]] = None,
        tags: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        network_config: Optional[NetworkConfig] = None,
    ) -> None: ...
    def get_run_args(
        self,
        submit_app,
        submit_py_files: Incomplete | None = None,
        submit_jars: Incomplete | None = None,
        submit_files: Incomplete | None = None,
        inputs: Incomplete | None = None,
        outputs: Incomplete | None = None,
        arguments: Incomplete | None = None,
        job_name: Incomplete | None = None,
        configuration: Incomplete | None = None,
        spark_event_logs_s3_uri: Incomplete | None = None,
    ): ...
    def run(
        self,
        submit_app: str,
        submit_py_files: Optional[List[str | PipelineVariable]] = None,
        submit_jars: Optional[List[str | PipelineVariable]] = None,
        submit_files: Optional[List[str | PipelineVariable]] = None,
        inputs: Optional[List[ProcessingInput]] = None,
        outputs: Optional[List[ProcessingOutput]] = None,
        arguments: Optional[List[str | PipelineVariable]] = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
        configuration: Optional[List[Dict, Dict]] = None,
        spark_event_logs_s3_uri: Optional[str | PipelineVariable] = None,
        kms_key: Optional[str] = None,
    ): ...

class SparkJarProcessor(_SparkProcessorBase):
    def __init__(
        self,
        role: str = None,
        instance_type: str | PipelineVariable = None,
        instance_count: int | PipelineVariable = None,
        framework_version: Optional[str] = None,
        py_version: Optional[str] = None,
        container_version: Optional[str] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        volume_size_in_gb: int | PipelineVariable = 30,
        volume_kms_key: Optional[str | PipelineVariable] = None,
        output_kms_key: Optional[str | PipelineVariable] = None,
        configuration_location: Optional[str] = None,
        dependency_location: Optional[str] = None,
        max_runtime_in_seconds: Optional[int | PipelineVariable] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        env: Optional[Dict[str, str | PipelineVariable]] = None,
        tags: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        network_config: Optional[NetworkConfig] = None,
    ) -> None: ...
    def get_run_args(
        self,
        submit_app,
        submit_class: Incomplete | None = None,
        submit_jars: Incomplete | None = None,
        submit_files: Incomplete | None = None,
        inputs: Incomplete | None = None,
        outputs: Incomplete | None = None,
        arguments: Incomplete | None = None,
        job_name: Incomplete | None = None,
        configuration: Incomplete | None = None,
        spark_event_logs_s3_uri: Incomplete | None = None,
    ): ...
    def run(
        self,
        submit_app: str,
        submit_class: str | PipelineVariable,
        submit_jars: Optional[List[str | PipelineVariable]] = None,
        submit_files: Optional[List[str | PipelineVariable]] = None,
        inputs: Optional[List[ProcessingInput]] = None,
        outputs: Optional[List[ProcessingOutput]] = None,
        arguments: Optional[List[str | PipelineVariable]] = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
        configuration: Optional[List[Dict, Dict]] = None,
        spark_event_logs_s3_uri: Optional[str | PipelineVariable] = None,
        kms_key: Optional[str] = None,
    ): ...

class _HistoryServer:
    arg_event_logs_s3_uri: str
    arg_remote_domain_name: str
    cli_args: Incomplete
    image_uri: Incomplete
    network_config: Incomplete
    run_history_server_command: Incomplete
    def __init__(self, cli_args, image_uri, network_config) -> None: ...
    def run(self) -> None: ...
    def down(self) -> None: ...

class FileType(Enum):
    JAR: int
    PYTHON: int
    FILE: int

class SparkConfigUtils:
    @staticmethod
    def validate_configuration(configuration: Dict): ...
    @staticmethod
    def validate_s3_uri(spark_output_s3_path) -> None: ...
