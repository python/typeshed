from _typeshed import Incomplete
from typing import Dict, Optional, Union

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
        entry_point: Union[str, PipelineVariable],
        use_mpi: Optional[Union[bool, PipelineVariable]] = None,
        num_processes: Optional[Union[int, PipelineVariable]] = None,
        process_slots_per_host: Optional[Union[int, PipelineVariable]] = None,
        additional_mpi_options: Optional[Union[str, PipelineVariable]] = None,
        source_dir: Optional[Union[str, PipelineVariable]] = None,
        hyperparameters: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
        framework_version: Optional[str] = None,
        py_version: Optional[str] = None,
        image_uri: Optional[Union[str, PipelineVariable]] = None,
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
