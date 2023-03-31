from _typeshed import Incomplete, Self
from _typeshed.dbapi import DBAPIConnection
from abc import abstractmethod
from collections.abc import Callable, Mapping
from types import TracebackType
from typing import Any, TypeVar, overload
from typing_extensions import Concatenate, ParamSpec, TypeAlias

from ..log import Identified, _EchoFlag, echo_property
from ..pool import Pool
from ..sql.compiler import Compiled
from ..sql.ddl import DDLElement
from ..sql.elements import ClauseElement
from ..sql.functions import FunctionElement
from ..sql.schema import DefaultGenerator
from .cursor import CursorResult
from .interfaces import Connectable as Connectable, Dialect, ExceptionContext
from .url import URL
from .util import TransactionalContext

_T = TypeVar("_T")
_P = ParamSpec("_P")

_Executable: TypeAlias = ClauseElement | FunctionElement | DDLElement | DefaultGenerator | Compiled

class Connection(Connectable):
    engine: Engine
    dialect: Dialect
    should_close_with_result: bool
    dispatch: Any
    def __init__(
        self,
        engine: Engine,
        connection: DBAPIConnection | None = None,
        close_with_result: bool = False,
        _branch_from: Incomplete | None = None,
        _execution_options: Incomplete | None = None,
        _dispatch: Incomplete | None = None,
        _has_events: Incomplete | None = None,
        _allow_revalidate: bool = True,
    ) -> None: ...
    def schema_for_object(self, obj) -> str | None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, type_: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def execution_options(self, **opt): ...
    def get_execution_options(self): ...
    @property
    def closed(self) -> bool: ...
    @property
    def invalidated(self) -> bool: ...
    @property
    def connection(self) -> DBAPIConnection: ...
    def get_isolation_level(self): ...
    @property
    def default_isolation_level(self): ...
    @property
    def info(self): ...
    def connect(self, close_with_result: bool = False): ...  # type: ignore[override]
    def invalidate(self, exception: Exception | None = None) -> None: ...
    def detach(self) -> None: ...
    def begin(self) -> Transaction: ...
    def begin_nested(self) -> Transaction | None: ...
    def begin_twophase(self, xid: Incomplete | None = None) -> TwoPhaseTransaction: ...
    def recover_twophase(self): ...
    def rollback_prepared(self, xid, recover: bool = False) -> None: ...
    def commit_prepared(self, xid, recover: bool = False) -> None: ...
    def in_transaction(self) -> bool: ...
    def in_nested_transaction(self) -> bool: ...
    def get_transaction(self) -> Transaction | None: ...
    def get_nested_transaction(self) -> Transaction | None: ...
    def close(self) -> None: ...
    @overload
    def scalar(self, object_: _Executable, *multiparams: Mapping[str, Any], **params: Any) -> Any: ...
    @overload
    def scalar(self, object_: str, *multiparams: Any | tuple[Any, ...] | Mapping[str, Any], **params: Any) -> Any: ...
    def scalars(self, object_, *multiparams, **params): ...
    @overload  # type: ignore[override]
    def execute(self, statement: _Executable, *multiparams: Mapping[str, Any], **params) -> CursorResult: ...
    @overload
    def execute(self, statement: str, *multiparams: Any | tuple[Any, ...] | Mapping[str, Any], **params) -> CursorResult: ...
    def exec_driver_sql(
        self, statement: str, parameters: Incomplete | None = None, execution_options: Incomplete | None = None
    ): ...
    def transaction(self, callable_: Callable[Concatenate[Connection, _P], _T], *args: _P.args, **kwargs: _P.kwargs) -> _T: ...
    def run_callable(self, callable_: Callable[Concatenate[Connection, _P], _T], *args: _P.args, **kwargs: _P.kwargs) -> _T: ...

class ExceptionContextImpl(ExceptionContext):
    engine: Any
    connection: Any
    sqlalchemy_exception: Any
    original_exception: Any
    execution_context: Any
    statement: Any
    parameters: Any
    is_disconnect: Any
    invalidate_pool_on_disconnect: Any
    def __init__(
        self,
        exception,
        sqlalchemy_exception,
        engine,
        connection,
        cursor,
        statement,
        parameters,
        context,
        is_disconnect,
        invalidate_pool_on_disconnect,
    ) -> None: ...

class Transaction(TransactionalContext):
    def __init__(self, connection: Connection) -> None: ...
    @property
    def is_valid(self) -> bool: ...
    def close(self) -> None: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    # The following field are technically not defined on Transaction, but on
    # all sub-classes.
    @property
    @abstractmethod
    def connection(self) -> Connection: ...
    @property
    @abstractmethod
    def is_active(self) -> bool: ...

class MarkerTransaction(Transaction):
    connection: Connection
    @property
    def is_active(self) -> bool: ...

class RootTransaction(Transaction):
    connection: Connection
    is_active: bool

class NestedTransaction(Transaction):
    connection: Connection
    is_active: bool

class TwoPhaseTransaction(RootTransaction):
    xid: Any
    def __init__(self, connection: Connection, xid) -> None: ...
    def prepare(self) -> None: ...

class Engine(Connectable, Identified):
    pool: Pool
    url: URL
    dialect: Dialect
    logging_name: str  # only exists if not None during initialization
    echo: echo_property
    hide_parameters: bool
    def __init__(
        self,
        pool: Pool,
        dialect: Dialect,
        url: str | URL,
        logging_name: str | None = None,
        echo: _EchoFlag = None,
        query_cache_size: int = 500,
        execution_options: Mapping[str, Any] | None = None,
        hide_parameters: bool = False,
    ) -> None: ...
    @property
    def engine(self) -> Engine: ...
    def clear_compiled_cache(self) -> None: ...
    def update_execution_options(self, **opt) -> None: ...
    def execution_options(self, **opt): ...
    def get_execution_options(self): ...
    @property
    def name(self) -> str: ...
    @property
    def driver(self): ...
    def dispose(self, close: bool = True) -> None: ...

    class _trans_ctx:
        conn: Connection
        transaction: Transaction
        close_with_result: bool
        def __init__(self, conn: Connection, transaction: Transaction, close_with_result: bool) -> None: ...
        def __enter__(self) -> Connection: ...
        def __exit__(
            self, type_: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
        ) -> None: ...

    def begin(self, close_with_result: bool = False) -> _trans_ctx: ...
    def transaction(
        self, callable_: Callable[Concatenate[Connection, _P], _T], *args: _P.args, **kwargs: _P.kwargs
    ) -> _T | None: ...
    def run_callable(self, callable_: Callable[Concatenate[Connection, _P], _T], *args: _P.args, **kwargs: _P.kwargs) -> _T: ...
    @overload  # type: ignore[override]
    def execute(self, statement: _Executable, *multiparams: Mapping[str, Any], **params: Any) -> CursorResult: ...
    @overload
    def execute(self, statement: str, *multiparams: Any | tuple[Any, ...] | Mapping[str, Any], **params: Any) -> CursorResult: ...
    @overload  # type: ignore[override]
    def scalar(self, statement: _Executable, *multiparams: Mapping[str, Any], **params: Any) -> Any: ...
    @overload
    def scalar(self, statement: str, *multiparams: Any | tuple[Any, ...] | Mapping[str, Any], **params: Any) -> Any: ...
    def connect(self, close_with_result: bool = False) -> Connection: ...  # type: ignore[override]
    def table_names(self, schema: Incomplete | None = None, connection: Connection | None = None): ...
    def has_table(self, table_name: str, schema: Incomplete | None = None) -> bool: ...
    def raw_connection(self, _connection: Connection | None = None) -> DBAPIConnection: ...

class OptionEngineMixin:
    url: URL
    dialect: Dialect
    logging_name: str
    echo: bool
    hide_parameters: bool
    dispatch: Any
    def __init__(self, proxied, execution_options) -> None: ...
    pool: Pool

class OptionEngine(OptionEngineMixin, Engine): ...  # type: ignore[misc]
