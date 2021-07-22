from datetime import datetime
from typing import TYPE_CHECKING, Any, List, Optional
from dateparser.conf import Settings

def parse(
    date_string: str,
    date_formats: Optional[Any] = ...,
    languages: Optional[List[str]] = ...,
    locales: Optional[List[str]] = ...,
    region: Optional[str] = ...,
    settings: Optional[Settings] = ...,
) -> Optional[datetime]: ...
