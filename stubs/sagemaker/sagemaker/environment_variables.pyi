from _typeshed import Incomplete
from typing import Dict, Optional

logger: Incomplete

def retrieve_default(
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
    include_aws_sdk_env_vars: bool = True,
) -> dict[str, str]: ...
