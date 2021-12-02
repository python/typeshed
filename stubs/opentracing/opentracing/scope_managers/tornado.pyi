from typing import Any

from ..scope_managers import ThreadLocalScopeManager
from ..span import Span

class TornadoScopeManager(ThreadLocalScopeManager):
    def activate(self, span: Span, finish_on_close: bool) -> Any: ...
    @property
    def active(self) -> Any: ...

class ThreadSafeStackContext:
    contexts: Any
    def __init__(self, *args: Any) -> None: ...

def tracer_stack_context() -> Any: ...
