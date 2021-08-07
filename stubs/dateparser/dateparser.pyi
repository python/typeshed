import datetime
from typing import Any, List, Mapping, Set, Tuple

__version__: str

def parse(
    date_string: str,
    date_formats: List[str] | Tuple[str] | Set[str] | None = ...,
    languages: List[str] | Tuple[str] | Set[str] | None = ...,
    locales: List[str] | Tuple[str] | Set[str] | None = ...,
    region: str | None = ...,
    settings: Mapping[str, Any] | None = ...,
) -> datetime.datetime | None: ...
def __getattr__(name: str) -> Any: ...  # incomplete
