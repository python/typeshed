from _typeshed import Incomplete

from sagemaker.remote_function.spark_config import SparkConfig
from sagemaker.session import Session

BOOTSTRAP_SCRIPT_NAME: str
ENTRYPOINT_SCRIPT_NAME: str
PRE_EXECUTION_SCRIPT_NAME: str
RUNTIME_MANAGER_SCRIPT_NAME: str
SPARK_APP_SCRIPT_NAME: str
RUNTIME_SCRIPTS_CHANNEL_NAME: str
REMOTE_FUNCTION_WORKSPACE: str
JOB_REMOTE_FUNCTION_WORKSPACE: str
SPARK_CONF_CHANNEL_NAME: str
SPARK_CONF_FILE_NAME: str
SPARK_SUBMIT_JARS_WORKSPACE: str
SPARK_SUBMIT_PY_FILES_WORKSPACE: str
SPARK_SUBMIT_FILES_WORKSPACE: str
SPARK_CONF_WORKSPACE: str
DEFAULT_SPARK_VERSION: str
DEFAULT_SPARK_CONTAINER_VERSION: str
KEY_EXPERIMENT_NAME: str
KEY_RUN_NAME: str
JOBS_CONTAINER_ENTRYPOINT: Incomplete
SPARK_APP_SCRIPT_PATH: Incomplete
ENTRYPOINT_SCRIPT: Incomplete
SPARK_ENTRYPOINT_SCRIPT: Incomplete
logger: Incomplete

class _JobSettings:
    sagemaker_session: Incomplete
    environment_variables: Incomplete
    image_uri: Incomplete
    dependencies: Incomplete
    pre_execution_commands: Incomplete
    pre_execution_script: Incomplete
    include_local_workdir: Incomplete
    instance_type: Incomplete
    instance_count: Incomplete
    volume_size: Incomplete
    max_runtime_in_seconds: Incomplete
    max_retry_attempts: Incomplete
    keep_alive_period_in_seconds: Incomplete
    spark_config: Incomplete
    job_conda_env: Incomplete
    job_name_prefix: Incomplete
    encrypt_inter_container_traffic: Incomplete
    enable_network_isolation: bool
    role: Incomplete
    s3_root_uri: Incomplete
    s3_kms_key: Incomplete
    volume_kms_key: Incomplete
    vpc_config: Incomplete
    tags: Incomplete
    def __init__(
        self,
        *,
        dependencies: str | None = None,
        pre_execution_commands: list[str] | None = None,
        pre_execution_script: str | None = None,
        environment_variables: dict[str, str] | None = None,
        image_uri: str | None = None,
        include_local_workdir: bool | None = None,
        instance_count: int = 1,
        instance_type: str | None = None,
        job_conda_env: str | None = None,
        job_name_prefix: str | None = None,
        keep_alive_period_in_seconds: int = 0,
        max_retry_attempts: int = 1,
        max_runtime_in_seconds: int = 86400,
        role: str | None = None,
        s3_kms_key: str | None = None,
        s3_root_uri: str | None = None,
        sagemaker_session: Session | None = None,
        security_group_ids: list[str] | None = None,
        subnets: list[str] | None = None,
        tags: list[tuple[str, str]] | None = None,
        volume_kms_key: str | None = None,
        volume_size: int = 30,
        encrypt_inter_container_traffic: bool | None = None,
        spark_config: SparkConfig | None = None,
    ) -> None: ...

class _Job:
    job_name: Incomplete
    s3_uri: Incomplete
    sagemaker_session: Incomplete
    hmac_key: Incomplete
    def __init__(self, job_name: str, s3_uri: str, sagemaker_session: Session, hmac_key: str) -> None: ...
    @staticmethod
    def from_describe_response(describe_training_job_response, sagemaker_session): ...
    @staticmethod
    def start(job_settings: _JobSettings, func, func_args, func_kwargs, run_info: Incomplete | None = None): ...
    def describe(self): ...
    def stop(self) -> None: ...
    def wait(self, timeout: int | None = None): ...

class _RunInfo:
    experiment_name: str
    run_name: str
    def __init__(self, experiment_name, run_name) -> None: ...
