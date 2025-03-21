import datetime as dt
from _typeshed import ConvertibleToInt, Incomplete, SupportsRead, SupportsReadline, SupportsWrite, Unused
from collections.abc import Callable, Iterable, Mapping, Sequence
from types import TracebackType
from typing import Any, Literal, NoReturn, Protocol, TextIO, TypeVar, overload, type_check_only
from typing_extensions import Self, TypeAlias

from psycopg2.extras import ReplicationCursor as extras_ReplicationCursor
from psycopg2.sql import Composable

_Vars: TypeAlias = Sequence[Any] | Mapping[str, Any] | None

@type_check_only
class _type:
    # The class doesn't exist at runtime but following attributes have type "psycopg2._psycopg.type"
    name: str
    values: tuple[int, ...]
    def __call__(self, value: str | bytes | None, cur: cursor | None, /) -> Any: ...

BINARY: _type
BINARYARRAY: _type
BOOLEAN: _type
BOOLEANARRAY: _type
BYTES: _type
BYTESARRAY: _type
CIDRARRAY: _type
DATE: _type
DATEARRAY: _type
DATETIME: _type
DATETIMEARRAY: _type
DATETIMETZ: _type
DATETIMETZARRAY: _type
DECIMAL: _type
DECIMALARRAY: _type
FLOAT: _type
FLOATARRAY: _type
INETARRAY: _type
INTEGER: _type
INTEGERARRAY: _type
INTERVAL: _type
INTERVALARRAY: _type
LONGINTEGER: _type
LONGINTEGERARRAY: _type
MACADDRARRAY: _type
NUMBER: _type
PYDATE: _type
PYDATEARRAY: _type
PYDATETIME: _type
PYDATETIMEARRAY: _type
PYDATETIMETZ: _type
PYDATETIMETZARRAY: _type
PYINTERVAL: _type
PYINTERVALARRAY: _type
PYTIME: _type
PYTIMEARRAY: _type
ROWID: _type
ROWIDARRAY: _type
STRING: _type
STRINGARRAY: _type
TIME: _type
TIMEARRAY: _type
UNICODE: _type
UNICODEARRAY: _type
UNKNOWN: _type

REPLICATION_LOGICAL: int
REPLICATION_PHYSICAL: int

class _ISQLQuoteProto(Protocol):
    # Objects conforming this protocol should implement a getquoted() and optionally a prepare() method.
    # The real ISQLQuote class is implemented below with more stuff.
    def getquoted(self) -> bytes: ...
    # def prepare(self, __conn: connection) -> None: ...  # optional

adapters: dict[tuple[type[Any], type[ISQLQuote]], Callable[[Any], _ISQLQuoteProto]]
apilevel: str
binary_types: dict[Any, Any]
encodings: dict[str, str]
paramstyle: str
sqlstate_errors: dict[str, type[Error]]
string_types: dict[int, _type]
threadsafety: int

__libpq_version__: int

_T_co = TypeVar("_T_co", covariant=True)

class _SupportsReadAndReadline(SupportsRead[_T_co], SupportsReadline[_T_co], Protocol[_T_co]): ...

class cursor:
    arraysize: int
    binary_types: Incomplete | None
    connection: _Connection
    itersize: int
    row_factory: Incomplete | None
    scrollable: bool | None
    string_types: Incomplete | None
    tzinfo_factory: Callable[..., dt.tzinfo]
    withhold: bool
    def __init__(self, conn: _Connection, name: str | bytes | None = None) -> None: ...
    @property
    def closed(self) -> bool: ...
    @property
    def lastrowid(self) -> int: ...
    @property
    def name(self) -> Incomplete | None: ...
    @property
    def query(self) -> bytes | None: ...
    @property
    def description(self) -> tuple[Column, ...] | None: ...
    @property
    def rowcount(self) -> int: ...
    @property
    def rownumber(self) -> int: ...
    @property
    def typecaster(self) -> Incomplete | None: ...
    @property
    def statusmessage(self) -> str | None: ...
    @property
    def pgresult_ptr(self) -> int | None: ...
    def callproc(self, procname: str | bytes, parameters: _Vars = None, /) -> None: ...
    def cast(self, oid: int, s: str | bytes, /) -> Any: ...
    def close(self) -> None: ...
    def copy_expert(
        self,
        sql: str | bytes | Composable,
        file: _SupportsReadAndReadline[bytes] | SupportsWrite[bytes] | TextIO,
        size: int = 8192,
    ) -> None: ...
    def copy_from(
        self,
        file: _SupportsReadAndReadline[bytes] | _SupportsReadAndReadline[str],
        table: str,
        sep: str = "\t",
        null: str = "\\N",
        size: int = 8192,
        columns: Iterable[str] | None = None,
    ) -> None: ...
    def copy_to(
        self,
        file: SupportsWrite[bytes] | TextIO,
        table: str,
        sep: str = "\t",
        null: str = "\\N",
        columns: Iterable[str] | None = None,
    ) -> None: ...
    def execute(self, query: str | bytes | Composable, vars: _Vars = None) -> None: ...
    def executemany(self, query: str | bytes | Composable, vars_list: Iterable[_Vars]) -> None: ...
    def fetchall(self) -> list[tuple[Any, ...]]: ...
    def fetchmany(self, size: int | None = None) -> list[tuple[Any, ...]]: ...
    def fetchone(self) -> tuple[Any, ...] | None: ...
    def mogrify(self, query: str | bytes | Composable, vars: _Vars | None = None) -> bytes: ...
    def nextset(self) -> NoReturn: ...  # not supported
    def scroll(self, value: int, mode: Literal["absolute", "relative"] = "relative") -> None: ...
    def setinputsizes(self, sizes: Unused) -> None: ...
    def setoutputsize(self, size: int, column: int = ..., /) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> tuple[Any, ...]: ...

_Cursor: TypeAlias = cursor

class AsIs:
    def __init__(self, obj: object, /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> Any: ...
    def getquoted(self) -> bytes: ...
    def __conform__(self, proto, /) -> Self | None: ...

class Binary:
    def __init__(self, str: object, /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> Any: ...
    @property
    def buffer(self) -> Any: ...
    def getquoted(self) -> bytes: ...
    def prepare(self, conn: connection, /) -> None: ...
    def __conform__(self, proto, /) -> Self | None: ...

class Boolean:
    def __init__(self, obj: object, /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> Any: ...
    def getquoted(self) -> bytes: ...
    def __conform__(self, proto, /) -> Self | None: ...

class Column:
    display_size: Any
    internal_size: Any
    name: Any
    null_ok: Any
    precision: Any
    scale: Any
    table_column: Any
    table_oid: Any
    type_code: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other, /): ...
    def __ge__(self, other, /): ...
    def __getitem__(self, index, /): ...
    def __getstate__(self): ...
    def __gt__(self, other, /): ...
    def __le__(self, other, /): ...
    def __len__(self) -> int: ...
    def __lt__(self, other, /): ...
    def __ne__(self, other, /): ...
    def __setstate__(self, state): ...

class ConnectionInfo:
    # Note: the following properties can be None if their corresponding libpq function
    # returns NULL. They're not annotated as such, because this is very unlikely in
    # practice---the psycopg2 docs [1] don't even mention this as a possibility!
    #
    # - db_name
    # - user
    # - password
    # - host
    # - port
    # - options
    #
    # (To prove this, one needs to inspect the psycopg2 source code [2], plus the
    # documentation [3] and source code [4] of the corresponding libpq calls.)
    #
    # [1]: https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo
    # [2]: https://github.com/psycopg/psycopg2/blob/1d3a89a0bba621dc1cc9b32db6d241bd2da85ad1/psycopg/conninfo_type.c#L52 and below
    # [3]: https://www.postgresql.org/docs/current/libpq-status.html
    # [4]: https://github.com/postgres/postgres/blob/b39838889e76274b107935fa8e8951baf0e8b31b/src/interfaces/libpq/fe-connect.c#L6754 and below  # noqa: E501
    @property
    def backend_pid(self) -> int: ...
    @property
    def dbname(self) -> str: ...
    @property
    def dsn_parameters(self) -> dict[str, str]: ...
    @property
    def error_message(self) -> str | None: ...
    @property
    def host(self) -> str: ...
    @property
    def needs_password(self) -> bool: ...
    @property
    def options(self) -> str: ...
    @property
    def password(self) -> str: ...
    @property
    def port(self) -> int: ...
    @property
    def protocol_version(self) -> int: ...
    @property
    def server_version(self) -> int: ...
    @property
    def socket(self) -> int: ...
    @property
    def ssl_attribute_names(self) -> list[str]: ...
    @property
    def ssl_in_use(self) -> bool: ...
    @property
    def status(self) -> int: ...
    @property
    def transaction_status(self) -> int: ...
    @property
    def used_password(self) -> bool: ...
    @property
    def user(self) -> str: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def parameter_status(self, name: str) -> str | None: ...
    def ssl_attribute(self, name: str) -> str | None: ...

class Error(Exception):
    cursor: _Cursor | None
    diag: Diagnostics
    pgcode: str | None
    pgerror: str | None
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __setstate__(self, state): ...

class DatabaseError(Error): ...
class DataError(DatabaseError): ...
class IntegrityError(DatabaseError): ...
class InternalError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...
class OperationalError(DatabaseError): ...
class ProgrammingError(DatabaseError): ...
class QueryCanceledError(OperationalError): ...
class TransactionRollbackError(OperationalError): ...
class InterfaceError(Error): ...
class Warning(Exception): ...

class ISQLQuote:
    _wrapped: Any
    def __init__(self, wrapped: object, /, **kwargs) -> None: ...
    def getbinary(self): ...
    def getbuffer(self): ...
    def getquoted(self) -> bytes: ...

class Decimal:
    def __init__(self, value: object, /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> Any: ...
    def getquoted(self) -> bytes: ...
    def __conform__(self, proto, /) -> Self | None: ...

class Diagnostics:
    column_name: str | None
    constraint_name: str | None
    context: str | None
    datatype_name: str | None
    internal_position: str | None
    internal_query: str | None
    message_detail: str | None
    message_hint: str | None
    message_primary: str | None
    schema_name: str | None
    severity: str | None
    severity_nonlocalized: str | None
    source_file: str | None
    source_function: str | None
    source_line: str | None
    sqlstate: str | None
    statement_position: str | None
    table_name: str | None
    def __init__(self, err: Error, /) -> None: ...

class Float:
    def __init__(self, value: float, /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> float: ...
    def getquoted(self) -> bytes: ...
    def __conform__(self, proto, /) -> Self | None: ...

class Int:
    def __init__(self, value: ConvertibleToInt, /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> Any: ...
    def getquoted(self) -> bytes: ...
    def __conform__(self, proto, /) -> Self | None: ...

class List:
    def __init__(self, objs: list[object], /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> list[Any]: ...
    def getquoted(self) -> bytes: ...
    def prepare(self, conn: connection, /) -> None: ...
    def __conform__(self, proto, /) -> Self | None: ...

class Notify:
    channel: Any
    payload: Any
    pid: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other, /): ...
    def __ge__(self, other, /): ...
    def __getitem__(self, index, /): ...
    def __gt__(self, other, /): ...
    def __hash__(self) -> int: ...
    def __le__(self, other, /): ...
    def __len__(self) -> int: ...
    def __lt__(self, other, /): ...
    def __ne__(self, other, /): ...

class QuotedString:
    encoding: str
    def __init__(self, str: object, /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> Any: ...
    @property
    def buffer(self) -> Any: ...
    def getquoted(self) -> bytes: ...
    def prepare(self, conn: connection, /) -> None: ...
    def __conform__(self, proto, /) -> Self | None: ...

class ReplicationCursor(cursor):
    feedback_timestamp: Any
    io_timestamp: Any
    wal_end: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def consume_stream(self, consumer, keepalive_interval=...): ...
    def read_message(self) -> Incomplete | None: ...
    def send_feedback(self, write_lsn=..., flush_lsn=..., apply_lsn=..., reply=..., force=...): ...
    def start_replication_expert(self, command, decode=..., status_interval=...): ...

class ReplicationMessage:
    cursor: Any
    data_size: Any
    data_start: Any
    payload: Any
    send_time: Any
    wal_end: Any
    def __init__(self, *args, **kwargs) -> None: ...

class Xid:
    bqual: Any
    database: Any
    format_id: Any
    gtrid: Any
    owner: Any
    prepared: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def from_string(self, *args, **kwargs): ...
    def __getitem__(self, index, /): ...
    def __len__(self) -> int: ...

_T_cur = TypeVar("_T_cur", bound=cursor)

class connection:
    DataError: type[DataError]
    DatabaseError: type[DatabaseError]
    Error: type[Error]
    IntegrityError: type[IntegrityError]
    InterfaceError: type[InterfaceError]
    InternalError: type[InternalError]
    NotSupportedError: type[NotSupportedError]
    OperationalError: type[OperationalError]
    ProgrammingError: type[ProgrammingError]
    Warning: type[Warning]
    @property
    def async_(self) -> int: ...
    autocommit: bool
    @property
    def binary_types(self) -> dict[Incomplete, Incomplete]: ...
    @property
    def closed(self) -> int: ...
    cursor_factory: Callable[[connection, str | bytes | None], cursor]
    @property
    def dsn(self) -> str: ...
    @property
    def encoding(self) -> str: ...
    @property
    def info(self) -> ConnectionInfo: ...
    @property
    def isolation_level(self) -> int | None: ...
    @isolation_level.setter
    def isolation_level(self, value: str | bytes | int | None, /) -> None: ...
    notices: list[str]
    notifies: list[Notify]
    @property
    def pgconn_ptr(self) -> int | None: ...
    @property
    def protocol_version(self) -> int: ...
    @property
    def deferrable(self) -> bool | None: ...
    @deferrable.setter
    def deferrable(self, value: Literal["default"] | bool | None, /) -> None: ...
    @property
    def readonly(self) -> bool | None: ...
    @readonly.setter
    def readonly(self, value: Literal["default"] | bool | None, /) -> None: ...
    @property
    def server_version(self) -> int: ...
    @property
    def status(self) -> int: ...
    @property
    def string_types(self) -> dict[Incomplete, Incomplete]: ...
    # Really it's dsn: str, async: int = 0, async_: int = 0, but
    # that would be a syntax error.
    def __init__(self, dsn: str, *, async_: int = 0) -> None: ...
    def cancel(self) -> None: ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
    @overload
    def cursor(
        self, name: str | bytes | None = None, cursor_factory: None = None, withhold: bool = False, scrollable: bool | None = None
    ) -> cursor: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None = None,
        *,
        cursor_factory: Callable[[connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None,
        cursor_factory: Callable[[connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...
    def fileno(self) -> int: ...
    def get_backend_pid(self) -> int: ...
    def get_dsn_parameters(self) -> dict[str, str]: ...
    def get_native_connection(self): ...
    def get_parameter_status(self, parameter: str) -> str | None: ...
    def get_transaction_status(self) -> int: ...
    def isexecuting(self) -> bool: ...
    def lobject(
        self,
        oid: int = ...,
        mode: str | None = ...,
        new_oid: int = ...,
        new_file: str | None = ...,
        lobject_factory: type[lobject] = ...,
    ) -> lobject: ...
    def poll(self) -> int: ...
    def reset(self) -> None: ...
    def rollback(self) -> None: ...
    def set_client_encoding(self, encoding: str) -> None: ...
    def set_isolation_level(self, level: int | None) -> None: ...
    def set_session(
        self,
        isolation_level: str | bytes | int | None = ...,
        readonly: bool | Literal["default", b"default"] | None = ...,
        deferrable: bool | Literal["default", b"default"] | None = ...,
        autocommit: bool = ...,
    ) -> None: ...
    def tpc_begin(self, xid: str | bytes | Xid) -> None: ...
    def tpc_commit(self, xid: str | bytes | Xid = ..., /) -> None: ...
    def tpc_prepare(self) -> None: ...
    def tpc_recover(self) -> list[Xid]: ...
    def tpc_rollback(self, xid: str | bytes | Xid = ..., /) -> None: ...
    def xid(self, format_id, gtrid, bqual) -> Xid: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, type: type[BaseException] | None, name: BaseException | None, tb: TracebackType | None, /) -> None: ...

_Connection: TypeAlias = connection

class ReplicationConnection(connection):
    autocommit: Any
    isolation_level: Any
    replication_type: Any
    reset: Any
    set_isolation_level: Any
    set_session: Any
    def __init__(self, *args, **kwargs) -> None: ...
    # https://github.com/python/typeshed/issues/11282
    # The return type should be exactly extras.ReplicationCursor (not _psycopg.ReplicationCursor)
    # See the C code: replicationConnection_init(), psyco_conn_cursor()
    @overload
    def cursor(
        self, name: str | bytes | None = None, cursor_factory: None = None, withhold: bool = False, scrollable: bool | None = None
    ) -> extras_ReplicationCursor: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None = None,
        *,
        cursor_factory: Callable[[connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None,
        cursor_factory: Callable[[connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...

class lobject:
    closed: Any
    mode: Any
    oid: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def close(self): ...
    def export(self, filename): ...
    def read(self, size=...): ...
    def seek(self, offset, whence=...): ...
    def tell(self): ...
    def truncate(self, len=...): ...
    def unlink(self): ...
    def write(self, str): ...

@type_check_only
class _datetime:
    # The class doesn't exist at runtime but functions below return "psycopg2._psycopg.datetime" objects
    # XXX: This and other classes that implement the `ISQLQuote` protocol could be made generic
    # in the return type of their `adapted` property if someone asks for it.
    def __init__(self, obj: object, type: int = -1, /, **kwargs: Unused) -> None: ...
    @property
    def adapted(self) -> Any: ...
    @property
    def type(self) -> int: ...
    def getquoted(self) -> bytes: ...
    def __conform__(self, proto, /) -> Self | None: ...

def Date(year: int, month: int, day: int, /) -> _datetime: ...
def DateFromPy(date: dt.date, /) -> _datetime: ...
def DateFromTicks(ticks: float, /) -> _datetime: ...
def IntervalFromPy(interval: dt.timedelta, /) -> _datetime: ...
def Time(hour: int, minutes: int, seconds: float, tzinfo: dt.tzinfo | None = None, /) -> _datetime: ...
def TimeFromPy(time: dt.time, /) -> _datetime: ...
def TimeFromTicks(ticks: float, /) -> _datetime: ...
def Timestamp(
    year: int, month: int, day: int, hour: int = 0, minutes: int = 0, seconds: float = 0, tzinfo: dt.tzinfo | None = None, /
) -> _datetime: ...
def TimestampFromPy(datetime: dt.datetime, /) -> _datetime: ...
def TimestampFromTicks(ticks: float, /) -> _datetime: ...
def _connect(*args, **kwargs): ...
def adapt(obj: object, protocol=..., alternate=..., /) -> Any: ...
def encrypt_password(
    password: str | bytes, user: str | bytes, scope: connection | cursor | None = None, algorithm: str | None = None
) -> str: ...
def get_wait_callback() -> Incomplete | None: ...
def libpq_version() -> int: ...
def new_array_type(values: tuple[int, ...], name: str, baseobj: _type) -> _type: ...
def new_type(
    values: tuple[int, ...],
    name: str,
    castobj: Callable[[str | bytes | None, cursor], Any] | None = None,
    baseobj: Incomplete | None = None,
) -> _type: ...
def parse_dsn(dsn: str | bytes) -> dict[str, Any]: ...
def quote_ident(ident: str | bytes, scope) -> str: ...
def register_type(obj: _type, conn_or_curs: connection | cursor | None = None, /) -> None: ...
def set_wait_callback(none: Callable[..., Incomplete] | None, /) -> None: ...
