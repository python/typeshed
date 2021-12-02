from typing import Any

from ..scope_managers import ThreadLocalScopeManager
from ..span import Span

class TornadoScopeManager(ThreadLocalScopeManager):
    def activate(self, span: Span, finish_on_close: bool): ...
    @property
    def active(self): ...

class ThreadSafeStackContext:
    contexts: Any
    def __init__(self, *args) -> None: ...

def tracer_stack_context(): ...
