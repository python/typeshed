import datetime
from typing import Optional, List, Dict, Tuple, Set, Any, Union

__version__: str

def parse(
    date_string: str,
    date_formats: Optional[Union[List[str], Tuple[str], Set[str]]] = None,
    languages: Optional[Union[List[str], Tuple[str], Set[str]]] = None,
    locales: Optional[Union[List[str], Tuple[str], Set[str]]] = None,
    region: Optional[str] = None,
    settings: Optional[Dict] = None,
) -> Optional[datetime.datetime]: ...

def __getattr__(name: str) -> Any: ...  # incomplete
