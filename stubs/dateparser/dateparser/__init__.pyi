import datetime
from typing import Any, List, Mapping, Optional, Set, Tuple, Union

__version__: str

def parse(
    date_string: str,
    date_formats: Optional[Union[List[str], Tuple[str], Set[str]]] = ...,
    languages: Optional[Union[List[str], Tuple[str], Set[str]]] = ...,
    locales: Optional[Union[List[str], Tuple[str], Set[str]]] = ...,
    region: str | None = ...,
    settings: Optional[Mapping[str, Any]] = ...,
) -> Optional[datetime.datetime]: ...
