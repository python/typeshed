from _typeshed import Incomplete

from sagemaker.estimator import Framework
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class SKLearn(Framework):
    framework_version: Incomplete
    py_version: Incomplete
    image_uri: Incomplete
    def __init__(
        self,
        entry_point: str | PipelineVariable,
        framework_version: str | None = None,
        py_version: str = "py3",
        source_dir: str | PipelineVariable | None = None,
        hyperparameters: dict[str, str | PipelineVariable] | None = None,
        image_uri: str | PipelineVariable | None = None,
        image_uri_region: str | None = None,
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
        **kwargs,
    ): ...
