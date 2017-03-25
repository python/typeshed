# Stubs for sqlalchemy.engine.strategies (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from sqlalchemy import pool as poollib
from . import base

strategies = ...  # type: Any

class EngineStrategy:
    def __init__(self) -> None: ...
    def create(self, *args, **kwargs): ...

class DefaultEngineStrategy(EngineStrategy):
    def create(self, name_or_url, **kwargs): ...

class PlainEngineStrategy(DefaultEngineStrategy):
    name = ...  # type: str
    engine_cls = ...  # type: Any

class ThreadLocalEngineStrategy(DefaultEngineStrategy):
    name = ...  # type: str
    engine_cls = ...  # type: Any

class MockEngineStrategy(EngineStrategy):
    name = ...  # type: str
    def create(self, name_or_url, executor, **kwargs): ...
    class MockConnection(base.Connectable):
        execute = ...  # type: Any
        def __init__(self, dialect, execute) -> None: ...
        engine = ...  # type: Any
        dialect = ...  # type: Any
        name = ...  # type: Any
        schema_for_object = ...  # type: Any
        def contextual_connect(self, **kwargs): ...
        def execution_options(self, **kw): ...
        def compiler(self, statement, parameters, **kwargs): ...
        def create(self, entity, **kwargs): ...
        def drop(self, entity, **kwargs): ...
