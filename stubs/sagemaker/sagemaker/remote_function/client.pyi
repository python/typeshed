from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Dict, List, Tuple

from sagemaker.remote_function.job import _JobSettings
from sagemaker.remote_function.spark_config import SparkConfig
from sagemaker.session import Session

logger: Incomplete

def remote(
    _func: Incomplete | None = None,
    *,
    dependencies: str = None,
    pre_execution_commands: List[str] = None,
    pre_execution_script: str = None,
    environment_variables: Dict[str, str] = None,
    image_uri: str = None,
    include_local_workdir: bool = False,
    instance_count: int = 1,
    instance_type: str = None,
    job_conda_env: str = None,
    job_name_prefix: str = None,
    keep_alive_period_in_seconds: int = 0,
    max_retry_attempts: int = 1,
    max_runtime_in_seconds: int = 86400,
    role: str = None,
    s3_kms_key: str = None,
    s3_root_uri: str = None,
    sagemaker_session: Session = None,
    security_group_ids: List[str] = None,
    subnets: List[str] = None,
    tags: List[Tuple[str, str]] = None,
    volume_kms_key: str = None,
    volume_size: int = 30,
    encrypt_inter_container_traffic: bool = None,
    spark_config: SparkConfig = None,
): ...

class _SubmitRequest:
    future: Incomplete
    job_settings: Incomplete
    func: Incomplete
    args: Incomplete
    kwargs: Incomplete
    run_info: Incomplete
    def __init__(
        self, future, job_settings: _JobSettings, func, func_args, func_kwargs, run_info: Incomplete | None = None
    ) -> None: ...

class RemoteExecutor:
    max_parallel_jobs: Incomplete
    job_settings: Incomplete
    def __init__(
        self,
        *,
        dependencies: str = None,
        pre_execution_commands: List[str] = None,
        pre_execution_script: str = None,
        environment_variables: Dict[str, str] = None,
        image_uri: str = None,
        include_local_workdir: bool = False,
        instance_count: int = 1,
        instance_type: str = None,
        job_conda_env: str = None,
        job_name_prefix: str = None,
        keep_alive_period_in_seconds: int = 0,
        max_parallel_jobs: int = 1,
        max_retry_attempts: int = 1,
        max_runtime_in_seconds: int = 86400,
        role: str = None,
        s3_kms_key: str = None,
        s3_root_uri: str = None,
        sagemaker_session: Session = None,
        security_group_ids: List[str] = None,
        subnets: List[str] = None,
        tags: List[Tuple[str, str]] = None,
        volume_kms_key: str = None,
        volume_size: int = 30,
        encrypt_inter_container_traffic: bool = None,
        spark_config: SparkConfig = None,
    ) -> None: ...
    def submit(self, func, *args, **kwargs): ...
    def map(self, func, *iterables): ...
    def shutdown(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...

class Future:
    def __init__(self) -> None: ...
    @staticmethod
    def from_describe_response(describe_training_job_response, sagemaker_session): ...
    def result(self, timeout: float = None) -> Any: ...
    def wait(self, timeout: int = None) -> None: ...
    def cancel(self) -> bool: ...
    def running(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...

def get_future(job_name, sagemaker_session: Incomplete | None = None) -> Future: ...
def list_futures(job_name_prefix, sagemaker_session: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
