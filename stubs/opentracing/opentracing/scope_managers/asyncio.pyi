from ..scope_managers import ThreadLocalScopeManager
from ..span import Span

class AsyncioScopeManager(ThreadLocalScopeManager):
    def activate(self, span: Span, finish_on_close: bool): ...
    @property
    def active(self): ...
