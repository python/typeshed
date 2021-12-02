from typing import Any

from opentracing.scope_managers import ThreadLocalScopeManager

class TornadoScopeManager(ThreadLocalScopeManager):
    def activate(self, span, finish_on_close): ...
    @property
    def active(self): ...

class ThreadSafeStackContext:
    contexts: Any
    def __init__(self, *args, **kwargs): ...

def tracer_stack_context(): ...
