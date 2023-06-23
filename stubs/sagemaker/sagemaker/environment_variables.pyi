from _typeshed import Incomplete
from typing import Dict, Optional

logger: Incomplete

def retrieve_default(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
    include_aws_sdk_env_vars: bool = True,
) -> Dict[str, str]: ...
