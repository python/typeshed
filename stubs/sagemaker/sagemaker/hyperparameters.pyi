from _typeshed import Incomplete
from typing import Dict, Optional

from sagemaker.jumpstart.enums import HyperparameterValidationMode

logger: Incomplete

def retrieve_default(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    include_container_hyperparameters: bool = False,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> Dict[str, str]: ...
def validate(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    hyperparameters: Optional[dict] = None,
    validation_mode: HyperparameterValidationMode = ...,
) -> None: ...
