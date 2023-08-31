from _typeshed import Incomplete

from sagemaker.jumpstart.enums import HyperparameterValidationMode

logger: Incomplete

def retrieve_default(
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    include_container_hyperparameters: bool = False,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> dict[str, str]: ...
def validate(
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    hyperparameters: dict | None = None,
    validation_mode: HyperparameterValidationMode = ...,
) -> None: ...
