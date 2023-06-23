from _typeshed import Incomplete
from typing import Optional

logger: Incomplete

def retrieve(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    model_scope: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> str: ...
