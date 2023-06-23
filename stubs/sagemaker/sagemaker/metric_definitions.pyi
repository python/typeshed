from _typeshed import Incomplete
from typing import Dict, List, Optional

logger: Incomplete

def retrieve_default(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> Optional[List[Dict[str, str]]]: ...
