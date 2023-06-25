import enum
from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.estimator import Framework
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete
SAGEMAKER_ESTIMATOR: str
SAGEMAKER_ESTIMATOR_VALUE: str
PYTHON_VERSION: str
TOOLKIT_FRAMEWORK_VERSION_MAP: Incomplete

class RLToolkit(enum.Enum):
    COACH: str
    RAY: str

class RLFramework(enum.Enum):
    TENSORFLOW: str
    MXNET: str
    PYTORCH: str

class RLEstimator(Framework):
    COACH_LATEST_VERSION_TF: str
    COACH_LATEST_VERSION_MXNET: str
    RAY_LATEST_VERSION: str
    toolkit: Incomplete
    toolkit_version: Incomplete
    framework: Incomplete
    framework_version: Incomplete
    def __init__(
        self,
        entry_point: str | PipelineVariable,
        toolkit: RLToolkit | None = None,
        toolkit_version: str | None = None,
        framework: Framework | None = None,
        source_dir: str | PipelineVariable | None = None,
        hyperparameters: dict[str, str | PipelineVariable] | None = None,
        image_uri: str | PipelineVariable | None = None,
        metric_definitions: list[dict[str, str | PipelineVariable]] | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(
        self,
        role: Incomplete | None = None,
        vpc_config_override="VPC_CONFIG_DEFAULT",
        entry_point: Incomplete | None = None,
        source_dir: Incomplete | None = None,
        dependencies: Incomplete | None = None,
        **kwargs,
    ): ...
    def training_image_uri(self): ...
    def hyperparameters(self): ...
    @classmethod
    def default_metric_definitions(cls, toolkit): ...
