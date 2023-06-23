from _typeshed import Incomplete
from typing import Union

from sagemaker.training_compiler.config import TrainingCompilerConfig as BaseConfig
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class TrainingCompilerConfig(BaseConfig):
    SUPPORTED_INSTANCE_CLASS_PREFIXES: Incomplete
    SUPPORTED_INSTANCE_TYPES_WITH_EFA: Incomplete
    def __init__(self, enabled: bool | PipelineVariable = True, debug: bool | PipelineVariable = False) -> None: ...
    @classmethod
    def validate(cls, estimator) -> None: ...
