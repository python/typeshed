from _typeshed import Incomplete
from typing import Dict, Optional, Union

from sagemaker.estimator import Framework
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class MXNet(Framework):
    framework_version: Incomplete
    py_version: Incomplete
    def __init__(
        self,
        entry_point: str | PipelineVariable,
        framework_version: Optional[str] = None,
        py_version: Optional[str] = None,
        source_dir: Optional[str | PipelineVariable] = None,
        hyperparameters: Optional[Dict[str, str | PipelineVariable]] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        distribution: Optional[Dict[str, str]] = None,
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
