from datetime import datetime
from typing import Any, Optional, List, Dict

def parse(
    date_string: str,
    date_formats: Optional[Any] = ...,
    languages: Optional[List[str]] = ...,
    locales: Optional[List[str]] = ...,
    region: Optional[str] = ...,
    settings: Optional[Dict] = ...,
) -> Optional[datetime]: ...
