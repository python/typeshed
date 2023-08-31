from _typeshed import Incomplete

from sagemaker.training_compiler.config import TrainingCompilerConfig as BaseConfig

logger: Incomplete

class TrainingCompilerConfig(BaseConfig):
    SUPPORTED_INSTANCE_CLASS_PREFIXES: Incomplete
    MIN_SUPPORTED_VERSION: str
    MAX_SUPPORTED_VERSION: str
    def __init__(self, enabled: bool = True, debug: bool = False) -> None: ...
    @classmethod
    def validate(cls, estimator) -> None: ...
