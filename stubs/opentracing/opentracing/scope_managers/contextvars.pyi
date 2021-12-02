from typing import Any
from ..scope_manager import ScopeManager
from ..span import Span

class ContextVarsScopeManager(ScopeManager):
    def activate(self, span: Span, finish_on_close: bool) -> Any: ...
    @property
    def active(self) -> Any: ...

def no_parent_scope() -> None: ...
