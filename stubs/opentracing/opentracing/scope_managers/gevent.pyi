from typing import Any
from ..scope_manager import ScopeManager

class GeventScopeManager(ScopeManager):
    def activate(self, span, finish_on_close: bool) -> Any: ...
    @property
    def active(self) -> Any: ...
