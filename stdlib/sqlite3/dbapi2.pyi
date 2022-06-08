import sqlite3
import sys
from _typeshed import ReadableBuffer, Self, StrOrBytesPath, SupportsLenAndGetItem
from collections.abc import Callable, Generator, Iterable, Iterator, Mapping
from datetime import date, datetime, time
from types import TracebackType
from typing import Any, Generic, Protocol, TypeVar, overload
from typing_extensions import Literal, SupportsIndex, TypeAlias, final

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_CursorT = TypeVar("_CursorT", bound=Cursor)
_SqliteData: TypeAlias = str | ReadableBuffer | int | float | None
# Data that is passed through adapters can be of any type accepted by an adapter.
_AdaptedInputData: TypeAlias = _SqliteData | Any
# The Mapping must really be a dict, but making it invariant is too annoying.
_Parameters: TypeAlias = SupportsLenAndGetItem[_AdaptedInputData] | Mapping[str, _AdaptedInputData]
_SqliteOutputData: TypeAlias = str | bytes | int | float | None
_Adapter: TypeAlias = Callable[[_T], _SqliteData]
_Converter: TypeAlias = Callable[[bytes], Any]

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
if sys.version_info >= (3, 7):
    SQLITE_DONE: int
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
adapters: dict[tuple[type[Any], type[Any]], _Adapter[Any]]
converters: dict[str, _Converter]
sqlite_version: str
version: str

if sys.version_info >= (3, 11):
    SQLITE_ABORT: int
    SQLITE_ABORT_ROLLBACK: int
    SQLITE_AUTH: int
    SQLITE_AUTH_USER: int
    SQLITE_BUSY: int
    SQLITE_BUSY_RECOVERY: int
    SQLITE_BUSY_SNAPSHOT: int
    SQLITE_BUSY_TIMEOUT: int
    SQLITE_CANTOPEN: int
    SQLITE_CANTOPEN_CONVPATH: int
    SQLITE_CANTOPEN_DIRTYWAL: int
    SQLITE_CANTOPEN_FULLPATH: int
    SQLITE_CANTOPEN_ISDIR: int
    SQLITE_CANTOPEN_NOTEMPDIR: int
    SQLITE_CANTOPEN_SYMLINK: int
    SQLITE_CONSTRAINT: int
    SQLITE_CONSTRAINT_CHECK: int
    SQLITE_CONSTRAINT_COMMITHOOK: int
    SQLITE_CONSTRAINT_FOREIGNKEY: int
    SQLITE_CONSTRAINT_FUNCTION: int
    SQLITE_CONSTRAINT_NOTNULL: int
    SQLITE_CONSTRAINT_PINNED: int
    SQLITE_CONSTRAINT_PRIMARYKEY: int
    SQLITE_CONSTRAINT_ROWID: int
    SQLITE_CONSTRAINT_TRIGGER: int
    SQLITE_CONSTRAINT_UNIQUE: int
    SQLITE_CONSTRAINT_VTAB: int
    SQLITE_CORRUPT: int
    SQLITE_CORRUPT_INDEX: int
    SQLITE_CORRUPT_SEQUENCE: int
    SQLITE_CORRUPT_VTAB: int
    SQLITE_EMPTY: int
    SQLITE_ERROR: int
    SQLITE_ERROR_MISSING_COLLSEQ: int
    SQLITE_ERROR_RETRY: int
    SQLITE_ERROR_SNAPSHOT: int
    SQLITE_FORMAT: int
    SQLITE_FULL: int
    SQLITE_INTERNAL: int
    SQLITE_INTERRUPT: int
    SQLITE_IOERR: int
    SQLITE_IOERR_ACCESS: int
    SQLITE_IOERR_AUTH: int
    SQLITE_IOERR_BEGIN_ATOMIC: int
    SQLITE_IOERR_BLOCKED: int
    SQLITE_IOERR_CHECKRESERVEDLOCK: int
    SQLITE_IOERR_CLOSE: int
    SQLITE_IOERR_COMMIT_ATOMIC: int
    SQLITE_IOERR_CONVPATH: int
    SQLITE_IOERR_CORRUPTFS: int
    SQLITE_IOERR_DATA: int
    SQLITE_IOERR_DELETE: int
    SQLITE_IOERR_DELETE_NOENT: int
    SQLITE_IOERR_DIR_CLOSE: int
    SQLITE_IOERR_DIR_FSYNC: int
    SQLITE_IOERR_FSTAT: int
    SQLITE_IOERR_FSYNC: int
    SQLITE_IOERR_GETTEMPPATH: int
    SQLITE_IOERR_LOCK: int
    SQLITE_IOERR_MMAP: int
    SQLITE_IOERR_NOMEM: int
    SQLITE_IOERR_RDLOCK: int
    SQLITE_IOERR_READ: int
    SQLITE_IOERR_ROLLBACK_ATOMIC: int
    SQLITE_IOERR_SEEK: int
    SQLITE_IOERR_SHMLOCK: int
    SQLITE_IOERR_SHMMAP: int
    SQLITE_IOERR_SHMOPEN: int
    SQLITE_IOERR_SHMSIZE: int
    SQLITE_IOERR_SHORT_READ: int
    SQLITE_IOERR_TRUNCATE: int
    SQLITE_IOERR_UNLOCK: int
    SQLITE_IOERR_VNODE: int
    SQLITE_IOERR_WRITE: int
    SQLITE_LOCKED: int
    SQLITE_LOCKED_SHAREDCACHE: int
    SQLITE_LOCKED_VTAB: int
    SQLITE_MISMATCH: int
    SQLITE_MISUSE: int
    SQLITE_NOLFS: int
    SQLITE_NOMEM: int
    SQLITE_NOTADB: int
    SQLITE_NOTFOUND: int
    SQLITE_NOTICE: int
    SQLITE_NOTICE_RECOVER_ROLLBACK: int
    SQLITE_NOTICE_RECOVER_WAL: int
    SQLITE_OK_LOAD_PERMANENTLY: int
    SQLITE_OK_SYMLINK: int
    SQLITE_PERM: int
    SQLITE_PROTOCOL: int
    SQLITE_RANGE: int
    SQLITE_READONLY: int
    SQLITE_READONLY_CANTINIT: int
    SQLITE_READONLY_CANTLOCK: int
    SQLITE_READONLY_DBMOVED: int
    SQLITE_READONLY_DIRECTORY: int
    SQLITE_READONLY_RECOVERY: int
    SQLITE_READONLY_ROLLBACK: int
    SQLITE_ROW: int
    SQLITE_SCHEMA: int
    SQLITE_TOOBIG: int
    SQLITE_WARNING: int
    SQLITE_WARNING_AUTOINDEX: int

# Can take or return anything depending on what's in the registry.
@overload
def adapt(__obj: Any, __proto: Any) -> Any: ...
@overload
def adapt(__obj: Any, __proto: Any, __alt: _T) -> Any | _T: ...
def complete_statement(statement: str) -> bool: ...

if sys.version_info >= (3, 7):
    _DatabaseArg: TypeAlias = StrOrBytesPath
else:
    _DatabaseArg: TypeAlias = bytes | str

def connect(
    database: _DatabaseArg,
    timeout: float = ...,
    detect_types: int = ...,
    isolation_level: str | None = ...,
    check_same_thread: bool = ...,
    factory: type[Connection] | None = ...,
    cached_statements: int = ...,
    uri: bool = ...,
) -> Connection: ...
def enable_callback_tracebacks(__enable: bool) -> None: ...

# takes a pos-or-keyword argument because there is a C wrapper
def enable_shared_cache(enable: int) -> None: ...
def register_adapter(__type: type[_T], __caster: _Adapter[_T]) -> None: ...
def register_converter(__name: str, __converter: _Converter) -> None: ...

if sys.version_info < (3, 8):
    class Cache:
        def __init__(self, *args, **kwargs) -> None: ...
        def display(self, *args, **kwargs) -> None: ...
        def get(self, *args, **kwargs) -> None: ...

class _AggregateProtocol(Protocol):
    def step(self, __value: int) -> object: ...
    def finalize(self) -> int: ...

class _SingleParamWindowAggregateClass(Protocol):
    def step(self, __param: Any) -> object: ...
    def inverse(self, __param: Any) -> object: ...
    def value(self) -> _SqliteData: ...
    def finalize(self) -> _SqliteData: ...

class _AnyParamWindowAggregateClass(Protocol):
    def step(self, *args: Any) -> object: ...
    def inverse(self, *args: Any) -> object: ...
    def value(self) -> _SqliteData: ...
    def finalize(self) -> _SqliteData: ...

class _WindowAggregateClass(Protocol):
    step: Callable[..., object]
    inverse: Callable[..., object]
    def value(self) -> _SqliteData: ...
    def finalize(self) -> _SqliteData: ...

class Connection:
    @property
    def DataError(self) -> type[sqlite3.DataError]: ...
    @property
    def DatabaseError(self) -> type[sqlite3.DatabaseError]: ...
    @property
    def Error(self) -> type[sqlite3.Error]: ...
    @property
    def IntegrityError(self) -> type[sqlite3.IntegrityError]: ...
    @property
    def InterfaceError(self) -> type[sqlite3.InterfaceError]: ...
    @property
    def InternalError(self) -> type[sqlite3.InternalError]: ...
    @property
    def NotSupportedError(self) -> type[sqlite3.NotSupportedError]: ...
    @property
    def OperationalError(self) -> type[sqlite3.OperationalError]: ...
    @property
    def ProgrammingError(self) -> type[sqlite3.ProgrammingError]: ...
    @property
    def Warning(self) -> type[sqlite3.Warning]: ...
    @property
    def in_transaction(self) -> bool: ...
    isolation_level: str | None  # one of '', 'DEFERRED', 'IMMEDIATE' or 'EXCLUSIVE'
    @property
    def total_changes(self) -> int: ...
    row_factory: Any
    text_factory: Any
    def __init__(
        self,
        database: _DatabaseArg,
        timeout: float = ...,
        detect_types: int = ...,
        isolation_level: str | None = ...,
        check_same_thread: bool = ...,
        factory: type[Connection] | None = ...,
        cached_statements: int = ...,
        uri: bool = ...,
    ) -> None: ...
    def close(self) -> None: ...
    if sys.version_info >= (3, 11):
        def blobopen(self, __table: str, __column: str, __row: int, *, readonly: bool = ..., name: str = ...) -> Blob: ...

    def commit(self) -> None: ...
    def create_aggregate(self, name: str, n_arg: int, aggregate_class: Callable[[], _AggregateProtocol]) -> None: ...
    if sys.version_info >= (3, 11):
        # num_params determines how many params will be passed to the aggregate class. We provide an overload
        # for the case where num_params = 1, which is expected to be the common case.
        @overload
        def create_window_function(
            self, __name: str, __num_params: Literal[1], __aggregate_class: Callable[[], _SingleParamWindowAggregateClass] | None
        ) -> None: ...
        # And for num_params = -1, which means the aggregate must accept any number of parameters.
        @overload
        def create_window_function(
            self, __name: str, __num_params: Literal[-1], __aggregate_class: Callable[[], _AnyParamWindowAggregateClass] | None
        ) -> None: ...
        @overload
        def create_window_function(
            self, __name: str, __num_params: int, __aggregate_class: Callable[[], _WindowAggregateClass] | None
        ) -> None: ...

    def create_collation(self, __name: str, __callback: Callable[[str, str], int | SupportsIndex] | None) -> None: ...
    if sys.version_info >= (3, 8):
        def create_function(
            self, name: str, narg: int, func: Callable[..., _SqliteData], *, deterministic: bool = ...
        ) -> None: ...
    else:
        def create_function(self, name: str, num_params: int, func: Callable[..., _SqliteData]) -> None: ...

    @overload
    def cursor(self, cursorClass: None = ...) -> Cursor: ...
    @overload
    def cursor(self, cursorClass: Callable[[], _CursorT]) -> _CursorT: ...
    def execute(self, sql: str, parameters: _Parameters = ...) -> Cursor: ...
    def executemany(self, __sql: str, __parameters: Iterable[_Parameters]) -> Cursor: ...
    def executescript(self, __sql_script: str) -> Cursor: ...
    def interrupt(self) -> None: ...
    def iterdump(self) -> Generator[str, None, None]: ...
    def rollback(self) -> None: ...
    def set_authorizer(
        self, authorizer_callback: Callable[[int, str | None, str | None, str | None, str | None], int] | None
    ) -> None: ...
    def set_progress_handler(self, progress_handler: Callable[[], bool | None] | None, n: int) -> None: ...
    def set_trace_callback(self, trace_callback: Callable[[str], object] | None) -> None: ...
    # enable_load_extension and load_extension is not available on python distributions compiled
    # without sqlite3 loadable extension support. see footnotes https://docs.python.org/3/library/sqlite3.html#f1
    def enable_load_extension(self, __enabled: bool) -> None: ...
    def load_extension(self, __name: str) -> None: ...
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
    if sys.version_info >= (3, 11):
        def setlimit(self, __category: int, __limit: int) -> int: ...
        def getlimit(self, __category: int) -> int: ...
        def serialize(self, *, name: str = ...) -> bytes: ...
        def deserialize(self, __data: ReadableBuffer, *, name: str = ...) -> None: ...

    def __call__(self, __sql: str) -> _Statement: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, __type: type[BaseException] | None, __value: BaseException | None, __traceback: TracebackType | None
    ) -> Literal[False]: ...

class Cursor(Iterator[Any]):
    arraysize: int
    @property
    def connection(self) -> Connection: ...
    # May be None, but using | Any instead to avoid slightly annoying false positives.
    @property
    def description(self) -> tuple[tuple[str, None, None, None, None, None, None], ...] | Any: ...
    @property
    def lastrowid(self) -> int | None: ...
    row_factory: Callable[[Cursor, Row], object] | None
    @property
    def rowcount(self) -> int: ...
    def __init__(self, __cursor: Connection) -> None: ...
    def close(self) -> None: ...
    def execute(self: Self, __sql: str, __parameters: _Parameters = ...) -> Self: ...
    def executemany(self: Self, __sql: str, __seq_of_parameters: Iterable[_Parameters]) -> Self: ...
    def executescript(self, __sql_script: str) -> Cursor: ...
    def fetchall(self) -> list[Any]: ...
    def fetchmany(self, size: int | None = ...) -> list[Any]: ...
    # Returns either a row (as created by the row_factory) or None, but
    # putting None in the return annotation causes annoying false positives.
    def fetchone(self) -> Any: ...
    def setinputsizes(self, __sizes: object) -> None: ...  # does nothing
    def setoutputsize(self, __size: object, __column: object = ...) -> None: ...  # does nothing
    def __iter__(self: Self) -> Self: ...
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

if sys.version_info < (3, 10):
    OptimizedUnicode = str

@final
class PrepareProtocol:
    def __init__(self, *args: object, **kwargs: object) -> None: ...

class ProgrammingError(DatabaseError): ...

class Row:
    def __init__(self, __cursor: Cursor, __data: tuple[Any]) -> None: ...
    def keys(self) -> list[str]: ...
    @overload
    def __getitem__(self, __index: int | str) -> Any: ...
    @overload
    def __getitem__(self, __index: slice) -> tuple[Any, ...]: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    # These return NotImplemented for anything that is not a Row.
    def __eq__(self, __other: object) -> bool: ...
    def __ge__(self, __other: object) -> bool: ...
    def __gt__(self, __other: object) -> bool: ...
    def __le__(self, __other: object) -> bool: ...
    def __lt__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...

if sys.version_info >= (3, 8):
    @final
    class _Statement: ...

else:
    @final
    class Statement:
        def __init__(self, *args, **kwargs): ...
    _Statement: TypeAlias = Statement

class Warning(Exception): ...

if sys.version_info >= (3, 11):
    @final
    class Blob:
        def close(self) -> None: ...
        def read(self, __length: int = ...) -> bytes: ...
        def write(self, __data: bytes) -> None: ...
        def tell(self) -> int: ...
        # whence must be one of os.SEEK_SET, os.SEEK_CUR, os.SEEK_END
        def seek(self, __offset: int, __origin: int = ...) -> None: ...
        def __len__(self) -> int: ...
        def __enter__(self: Self) -> Self: ...
        def __exit__(self, __typ: object, __val: object, __tb: object) -> Literal[False]: ...
        def __getitem__(self, __item: SupportsIndex | slice) -> int: ...
        def __setitem__(self, __item: SupportsIndex | slice, __value: int) -> None: ...
