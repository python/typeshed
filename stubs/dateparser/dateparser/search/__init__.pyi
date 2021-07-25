from datetime import datetime
from typing import Any, Dict, List, Mapping, Optional, Set, Tuple, Union

from dateparser.search.search import DateSearchWithDetection as DateSearchWithDetection

def search_dates(
    text: str,
    languages: Optional[Union[List[str], Tuple[str], Set[str]]] = ...,
    settings: Optional[Mapping[Any, Any]] = ...,
    add_detected_language: bool = ...,
) -> Union[List[Tuple[str, datetime]], List[Tuple[str, datetime, str]]]: ...
