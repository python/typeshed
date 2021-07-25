from datetime import datetime
from typing import Any, List, Literal, Mapping, Optional, Set, Tuple, Union, overload

from dateparser.search.search import DateSearchWithDetection as DateSearchWithDetection

@overload
def search_dates(
    text: str,
    languages: Optional[Union[List[str], Tuple[str], Set[str]]],
    settings: Optional[Mapping[Any, Any]],
    add_detected_language: Literal[True],
) -> List[Tuple[str, datetime, str]]: ...
@overload
def search_dates(
    text: str,
    languages: Optional[Union[List[str], Tuple[str], Set[str]]] = ...,
    settings: Optional[Mapping[Any, Any]] = ...,
    add_detected_language: Literal[False] = ...,
) -> List[Tuple[str, datetime]]: ...
