# Stubs for pytz.lazy (Python 3.5)

from typing import Any, Iterable, List, Dict  # NOQA
from collections import Mapping

class LazyDict(Mapping):
    data = ...  # type: Dict[str, Any]
    def __getitem__(self, key: str) -> Any: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterable: ...
    def __len__(self) -> int: ...
    def keys(self) -> List[str]: ...

class LazyList(list):
    pass
class LazySet(set):
    pass
