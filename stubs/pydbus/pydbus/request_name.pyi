from typing import Generic, TypeVar

from .bus import Bus
from .exitable import Exitable

_T = TypeVar("_T")

class NameOwner(Exitable, Generic[_T]):
    def __init__(self, bus: Bus[_T], name: str, allow_replacement: bool, replace: bool) -> None: ...
    def unown(self) -> None: ...  # added by ExitableWithAliases('unown')

class RequestNameMixin(Generic[_T]):
    def request_name(self, name: str, allow_replacement: bool = True, replace: bool = False) -> NameOwner[_T]: ...
