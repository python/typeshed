from _typeshed import Incomplete
from typing import List, Optional

logger: Incomplete

def retrieve_default(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    scope: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> str: ...
def retrieve(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    scope: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> List[str]: ...
