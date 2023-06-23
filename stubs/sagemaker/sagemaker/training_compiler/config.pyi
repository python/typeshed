from _typeshed import Incomplete

logger: Incomplete

class TrainingCompilerConfig:
    DEBUG_PATH: str
    SUPPORTED_INSTANCE_CLASS_PREFIXES: Incomplete
    HP_ENABLE_COMPILER: str
    HP_ENABLE_DEBUG: str
    enabled: Incomplete
    debug: Incomplete
    def __init__(self, enabled: bool = True, debug: bool = False) -> None: ...
    def __nonzero__(self): ...
    def disclaimers_and_warnings(self) -> None: ...
    @classmethod
    def validate(cls, estimator) -> None: ...
