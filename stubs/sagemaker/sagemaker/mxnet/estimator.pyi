from _typeshed import Incomplete
from typing import Dict, Optional

from sagemaker.estimator import Framework
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class MXNet(Framework):
    framework_version: Incomplete
    py_version: Incomplete
    def __init__(
        self,
        entry_point: str | PipelineVariable,
        framework_version: str | None = None,
        py_version: str | None = None,
        source_dir: str | PipelineVariable | None = None,
        hyperparameters: dict[str, str | PipelineVariable] | None = None,
        image_uri: str | PipelineVariable | None = None,
        distribution: dict[str, str] | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(
        self,
        model_server_workers: Incomplete | None = None,
        role: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        entry_point: Incomplete | None = None,
        source_dir: Incomplete | None = None,
        dependencies: Incomplete | None = None,
        image_uri: Incomplete | None = None,
        **kwargs,
    ): ...
