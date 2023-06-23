from typing import List, Optional

def retrieve_options(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> List[str]: ...
def retrieve_default(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> str: ...

CONTENT_TYPE_JSON: str
CONTENT_TYPE_CSV: str
CONTENT_TYPE_OCTET_STREAM: str
CONTENT_TYPE_NPY: str
