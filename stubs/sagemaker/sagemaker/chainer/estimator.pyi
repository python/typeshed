from _typeshed import Incomplete
from typing import Dict, Optional

from sagemaker.estimator import Framework
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class Chainer(Framework):
    framework_version: Incomplete
    py_version: Incomplete
    use_mpi: Incomplete
    num_processes: Incomplete
    process_slots_per_host: Incomplete
    additional_mpi_options: Incomplete
    def __init__(
        self,
        entry_point: str | PipelineVariable,
        use_mpi: bool | PipelineVariable | None = None,
        num_processes: int | PipelineVariable | None = None,
        process_slots_per_host: int | PipelineVariable | None = None,
        additional_mpi_options: str | PipelineVariable | None = None,
        source_dir: str | PipelineVariable | None = None,
        hyperparameters: dict[str, str | PipelineVariable] | None = None,
        framework_version: str | None = None,
        py_version: str | None = None,
        image_uri: str | PipelineVariable | None = None,
        **kwargs,
    ) -> None: ...
    def hyperparameters(self): ...
    def create_model(
        self,
        model_server_workers: Incomplete | None = None,
        role: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        entry_point: Incomplete | None = None,
        source_dir: Incomplete | None = None,
        dependencies: Incomplete | None = None,
        **kwargs,
    ): ...
