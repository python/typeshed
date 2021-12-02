from ..scope_manager import ScopeManager
from ..span import Span

class ContextVarsScopeManager(ScopeManager):
    def activate(self, span: Span, finish_on_close: bool): ...
    @property
    def active(self): ...

def no_parent_scope() -> None: ...
