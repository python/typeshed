from _typeshed import Incomplete
from typing import Optional

logger: Incomplete

def retrieve(
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    script_scope: str | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> str: ...
