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
        use_mpi: Optional[bool | PipelineVariable] = None,
        num_processes: Optional[int | PipelineVariable] = None,
        process_slots_per_host: Optional[int | PipelineVariable] = None,
        additional_mpi_options: Optional[str | PipelineVariable] = None,
        source_dir: Optional[str | PipelineVariable] = None,
        hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
        framework_version: Optional[str] = None,
        py_version: Optional[str] = None,
        image_uri: Optional[str | PipelineVariable] = None,
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
