from _typeshed import Incomplete
from threading import Thread

CONTAINER_PREFIX: str
DOCKER_COMPOSE_FILENAME: str
DOCKER_COMPOSE_HTTP_TIMEOUT_ENV: str
DOCKER_COMPOSE_HTTP_TIMEOUT: str
REGION_ENV_NAME: str
TRAINING_JOB_NAME_ENV_NAME: str
S3_ENDPOINT_URL_ENV_NAME: str
SELINUX_ENABLED: Incomplete
logger: Incomplete

class _SageMakerContainer:
    sagemaker_session: Incomplete
    instance_type: Incomplete
    instance_count: Incomplete
    image: Incomplete
    container_entrypoint: Incomplete
    container_arguments: Incomplete
    hosts: Incomplete
    container_root: Incomplete
    container: Incomplete
    def __init__(
        self,
        instance_type,
        instance_count,
        image,
        sagemaker_session: Incomplete | None = None,
        container_entrypoint: Incomplete | None = None,
        container_arguments: Incomplete | None = None,
    ) -> None: ...
    def process(self, processing_inputs, processing_output_config, environment, processing_job_name) -> None: ...
    def train(self, input_data_config, output_data_config, hyperparameters, environment, job_name): ...
    def serve(self, model_dir, environment) -> None: ...
    def stop_serving(self) -> None: ...
    def retrieve_artifacts(self, compose_data, output_data_config, job_name): ...
    def write_processing_config_files(
        self, host, environment, processing_inputs, processing_output_config, processing_job_name
    ) -> None: ...
    def write_config_files(self, host, hyperparameters, input_data_config) -> None: ...

class _HostingContainer(Thread):
    command: Incomplete
    process: Incomplete
    def __init__(self, command) -> None: ...
    def run(self) -> None: ...
    def down(self) -> None: ...

class _Volume:
    container_dir: Incomplete
    host_dir: Incomplete
    map: Incomplete
    def __init__(self, host_dir, container_dir: Incomplete | None = None, channel: Incomplete | None = None) -> None: ...
