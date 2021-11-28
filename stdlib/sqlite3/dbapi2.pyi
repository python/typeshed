import sys
from _typeshed import Self, StrOrBytesPath
from datetime import date, datetime, time
from typing import Any, Callable, Generator, Iterable, Iterator, Protocol, Type, TypeVar

_T = TypeVar("_T")

paramstyle: str
threadsafety: int
apilevel: str
Date = date
Time = time
Timestamp = datetime

def DateFromTicks(ticks: float) -> Date: ...
def TimeFromTicks(ticks: float) -> Time: ...
def TimestampFromTicks(ticks: float) -> Timestamp: ...

version_info: tuple[int, int, int]
sqlite_version_info: tuple[int, int, int]
Binary = memoryview

# The remaining definitions are imported from _sqlite3.

PARSE_COLNAMES: int
PARSE_DECLTYPES: int
SQLITE_ALTER_TABLE: int
SQLITE_ANALYZE: int
SQLITE_ATTACH: int
SQLITE_CREATE_INDEX: int
SQLITE_CREATE_TABLE: int
SQLITE_CREATE_TEMP_INDEX: int
SQLITE_CREATE_TEMP_TABLE: int
SQLITE_CREATE_TEMP_TRIGGER: int
SQLITE_CREATE_TEMP_VIEW: int
SQLITE_CREATE_TRIGGER: int
SQLITE_CREATE_VIEW: int
if sys.version_info >= (3, 7):
    SQLITE_CREATE_VTABLE: int
SQLITE_DELETE: int
SQLITE_DENY: int
SQLITE_DETACH: int
SQLITE_DROP_INDEX: int
SQLITE_DROP_TABLE: int
SQLITE_DROP_TEMP_INDEX: int
SQLITE_DROP_TEMP_TABLE: int
SQLITE_DROP_TEMP_TRIGGER: int
SQLITE_DROP_TEMP_VIEW: int
SQLITE_DROP_TRIGGER: int
SQLITE_DROP_VIEW: int
if sys.version_info >= (3, 7):
    SQLITE_DROP_VTABLE: int
    SQLITE_FUNCTION: int
SQLITE_IGNORE: int
SQLITE_INSERT: int
SQLITE_OK: int
if sys.version_info >= (3, 11):
    SQLITE_LIMIT_LENGTH: int
    SQLITE_LIMIT_SQL_LENGTH: int
    SQLITE_LIMIT_COLUMN: int
    SQLITE_LIMIT_EXPR_DEPTH: int
    SQLITE_LIMIT_COMPOUND_SELECT: int
    SQLITE_LIMIT_VDBE_OP: int
    SQLITE_LIMIT_FUNCTION_ARG: int
    SQLITE_LIMIT_ATTACHED: int
    SQLITE_LIMIT_LIKE_PATTERN_LENGTH: int
    SQLITE_LIMIT_VARIABLE_NUMBER: int
    SQLITE_LIMIT_TRIGGER_DEPTH: int
    SQLITE_LIMIT_WORKER_THREADS: int
SQLITE_PRAGMA: int
SQLITE_READ: int
SQLITE_REINDEX: int
if sys.version_info >= (3, 7):
    SQLITE_RECURSIVE: int
    SQLITE_SAVEPOINT: int
SQLITE_SELECT: int
SQLITE_TRANSACTION: int
SQLITE_UPDATE: int
adapters: Any
converters: Any
sqlite_version: str
version: str

# TODO: adapt needs to get probed
def adapt(obj, protocol, alternate): ...
def complete_statement(sql: str) -> bool: ...

if sys.version_info >= (3, 7):
    def connect(
        database: StrOrBytesPath,
        timeout: float = ...,
        detect_types: int = ...,
        isolation_level: str | None = ...,
        check_same_thread: bool = ...,
        factory: Type[Connection] | None = ...,
        cached_statements: int = ...,
        uri: bool = ...,
    ) -> Connection: ...

else:
    def connect(
        database: bytes | str,
        timeout: float = ...,
        detect_types: int = ...,
        isolation_level: str | None = ...,
        check_same_thread: bool = ...,
        factory: Type[Connection] | None = ...,
        cached_statements: int = ...,
        uri: bool = ...,
    ) -> Connection: ...

def enable_callback_tracebacks(__enable: bool) -> None: ...
def enable_shared_cache(enable: int) -> None: ...
def register_adapter(__type: Type[_T], __caster: Callable[[_T], int | float | str | bytes]) -> None: ...
def register_converter(__name: str, __converter: Callable[[bytes], Any]) -> None: ...

if sys.version_info < (3, 8):
    class Cache(object):
        def __init__(self, *args, **kwargs) -> None: ...
        def display(self, *args, **kwargs) -> None: ...
        def get(self, *args, **kwargs) -> None: ...

class _AggregateProtocol(Protocol):
    def step(self, value: int) -> None: ...
    def finalize(self) -> int: ...

class Connection(object):
    DataError: Any
    DatabaseError: Any
    Error: Any
    IntegrityError: Any
    InterfaceError: Any
    InternalError: Any
    NotSupportedError: Any
    OperationalError: Any
    ProgrammingError: Any
    Warning: Any
    in_transaction: Any
    isolation_level: Any
    row_factory: Any
    text_factory: Any
    total_changes: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def create_aggregate(self, name: str, n_arg: int, aggregate_class: Callable[[], _AggregateProtocol]) -> None: ...
    def create_collation(self, __name: str, __callback: Any) -> None: ...
    if sys.version_info >= (3, 8):
        def create_function(self, name: str, narg: int, func: Any, *, deterministic: bool = ...) -> None: ...
    else:
        def create_function(self, name: str, num_params: int, func: Any) -> None: ...
    def cursor(self, cursorClass: type | None = ...) -> Cursor: ...
    def execute(self, sql: str, parameters: Iterable[Any] = ...) -> Cursor: ...
    # TODO: please check in executemany() if seq_of_parameters type is possible like this
    def executemany(self, __sql: str, __parameters: Iterable[Iterable[Any]]) -> Cursor: ...
    def executescript(self, __sql_script: bytes | str) -> Cursor: ...
    def interrupt(self, *args: Any, **kwargs: Any) -> None: ...
    def iterdump(self, *args: Any, **kwargs: Any) -> Generator[str, None, None]: ...
    def rollback(self, *args: Any, **kwargs: Any) -> None: ...
    # TODO: set_authorizer(authorzer_callback)
    # see https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.set_authorizer
    # returns [SQLITE_OK, SQLITE_DENY, SQLITE_IGNORE] so perhaps int
    def set_authorizer(self, *args: Any, **kwargs: Any) -> None: ...
    # set_progress_handler(handler, n) -> see https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.set_progress_handler
    def set_progress_handler(self, *args: Any, **kwargs: Any) -> None: ...
    def set_trace_callback(self, *args: Any, **kwargs: Any) -> None: ...
    # enable_load_extension and load_extension is not available on python distributions compiled
    # without sqlite3 loadable extension support. see footnotes https://docs.python.org/3/library/sqlite3.html#f1
    def enable_load_extension(self, enabled: bool) -> None: ...
    def load_extension(self, path: str) -> None: ...
    if sys.version_info >= (3, 7):
        def backup(
            self,
            target: Connection,
            *,
            pages: int = ...,
            progress: Callable[[int, int, int], object] | None = ...,
            name: str = ...,
            sleep: float = ...,
        ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, t: type | None, exc: BaseException | None, tb: Any | None) -> None: ...

class Cursor(Iterator[Any]):
    arraysize: Any
    connection: Any
    description: Any
    lastrowid: Any
    row_factory: Any
    rowcount: int
    # TODO: Cursor class accepts exactly 1 argument
    # required type is sqlite3.Connection (which is imported as _Connection)
    # however, the name of the __init__ variable is unknown
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def close(self, *args: Any, **kwargs: Any) -> None: ...
    def execute(self, __sql: str, __parameters: Iterable[Any] = ...) -> Cursor: ...
    def executemany(self, __sql: str, __seq_of_parameters: Iterable[Iterable[Any]]) -> Cursor: ...
    def executescript(self, __sql_script: bytes | str) -> Cursor: ...
    def fetchall(self) -> list[Any]: ...
    def fetchmany(self, size: int | None = ...) -> list[Any]: ...
    def fetchone(self) -> Any: ...
    def setinputsizes(self, *args: Any, **kwargs: Any) -> None: ...
    def setoutputsize(self, *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self) -> Cursor: ...
    def __next__(self) -> Any: ...

class DataError(DatabaseError): ...
class DatabaseError(Error): ...

class Error(Exception):
    if sys.version_info >= (3, 11):
        sqlite_errorcode: int
        sqlite_errorname: str

class IntegrityError(DatabaseError): ...
class InterfaceError(Error): ...
class InternalError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...
class OperationalError(DatabaseError): ...

OptimizedUnicode = str

class PrepareProtocol(object):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class ProgrammingError(DatabaseError): ...

class Row(object):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def keys(self, *args: Any, **kwargs: Any): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __iter__(self): ...
    def __le__(self, other): ...
    def __len__(self): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...

if sys.version_info < (3, 8):
    class Statement(object):
        def __init__(self, *args, **kwargs): ...

class Warning(Exception): ...
