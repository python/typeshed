from typing import Any, Dict, Optional

from sagemaker.jumpstart.enums import HyperparameterValidationMode

def validate_hyperparameters(
    model_id: str,
    model_version: str,
    hyperparameters: Dict[str, Any],
    validation_mode: HyperparameterValidationMode = ...,
    region: Optional[str] = "eu-west-1",
) -> None: ...
