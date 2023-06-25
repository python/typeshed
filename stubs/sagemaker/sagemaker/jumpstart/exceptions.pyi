from _typeshed import Incomplete
from typing import List, Optional

from sagemaker.jumpstart.constants import JumpStartScriptScope

NO_AVAILABLE_INSTANCES_ERROR_MSG: str
INVALID_MODEL_ID_ERROR_MSG: Incomplete

class JumpStartHyperparametersError(ValueError):
    message: Incomplete
    def __init__(self, message: str | None = None) -> None: ...

class VulnerableJumpStartModelError(ValueError):
    message: Incomplete
    def __init__(
        self,
        model_id: str | None = None,
        version: str | None = None,
        vulnerabilities: list[str] | None = None,
        scope: JumpStartScriptScope | None = None,
        message: str | None = None,
    ) -> None: ...

class DeprecatedJumpStartModelError(ValueError):
    message: Incomplete
    def __init__(self, model_id: str | None = None, version: str | None = None, message: str | None = None) -> None: ...
