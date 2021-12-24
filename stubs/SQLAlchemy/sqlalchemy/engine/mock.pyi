from _typeshed import Self
from abc import abstractmethod
from collections.abc import Mapping
from typing import Any, overload

from ..sql.compiler import Compiled
from ..sql.ddl import DDLElement
from ..sql.elements import ClauseElement
from ..sql.functions import FunctionElement
from ..sql.schema import DefaultGenerator
from .cursor import CursorResult
from .interfaces import Connectable, Dialect
from .url import URL

class MockConnection(Connectable):
    def __init__(self, dialect: Dialect, execute) -> None: ...
    @property
    def engine(self: Self) -> Self: ...  # type: ignore[override]
    @property
    def dialect(self) -> Dialect: ...
    @property
    def name(self) -> str: ...
    def schema_for_object(self, obj): ...
    def connect(self, **kwargs): ...
    def execution_options(self, **kw): ...
    def compiler(self, statement, parameters, **kwargs): ...
    def create(self, entity, **kwargs) -> None: ...
    def drop(self, entity, **kwargs) -> None: ...
    @abstractmethod
    @overload
    def execute(
        self,
        object_: ClauseElement | FunctionElement | DDLElement | DefaultGenerator | Compiled,
        *multiparams: Mapping[str, Any],
        **params: Any,
    ) -> CursorResult: ...
    @abstractmethod
    @overload
    def execute(self, object_: str, *multiparams: Any | tuple[Any, ...] | Mapping[str, Any], **params: Any) -> CursorResult: ...

def create_mock_engine(url: URL | str, executor, **kw) -> MockConnection: ...
