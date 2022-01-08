from typing import Any, Callable, TypeVar, overload

import psycopg2
import psycopg2.extensions

BINARY: Any
BINARYARRAY: Any
BOOLEAN: Any
BOOLEANARRAY: Any
BYTES: Any
BYTESARRAY: Any
CIDRARRAY: Any
DATE: Any
DATEARRAY: Any
DATETIME: Any
DATETIMEARRAY: Any
DATETIMETZ: Any
DATETIMETZARRAY: Any
DECIMAL: Any
DECIMALARRAY: Any
FLOAT: Any
FLOATARRAY: Any
INETARRAY: Any
INTEGER: Any
INTEGERARRAY: Any
INTERVAL: Any
INTERVALARRAY: Any
LONGINTEGER: Any
LONGINTEGERARRAY: Any
MACADDRARRAY: Any
NUMBER: Any
PYDATE: Any
PYDATEARRAY: Any
PYDATETIME: Any
PYDATETIMEARRAY: Any
PYDATETIMETZ: Any
PYDATETIMETZARRAY: Any
PYINTERVAL: Any
PYINTERVALARRAY: Any
PYTIME: Any
PYTIMEARRAY: Any
REPLICATION_LOGICAL: int
REPLICATION_PHYSICAL: int
ROWID: Any
ROWIDARRAY: Any
STRING: Any
STRINGARRAY: Any
TIME: Any
TIMEARRAY: Any
UNICODE: Any
UNICODEARRAY: Any
UNKNOWN: Any
adapters: dict[Any, Any]
apilevel: str
binary_types: dict[Any, Any]
encodings: dict[Any, Any]
paramstyle: str
sqlstate_errors: dict[Any, Any]
string_types: dict[Any, Any]
threadsafety: int

__libpq_version__: int

class AsIs:
    adapted: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getquoted(self, *args, **kwargs): ...
    def __conform__(self, *args, **kwargs): ...

class Binary:
    adapted: Any
    buffer: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getquoted(self, *args, **kwargs): ...
    def prepare(self, conn): ...
    def __conform__(self, *args, **kwargs): ...

class Boolean:
    adapted: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getquoted(self, *args, **kwargs): ...
    def __conform__(self, *args, **kwargs): ...

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
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __getstate__(self): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __len__(self): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...
    def __setstate__(self, state): ...

class ConnectionInfo:
    backend_pid: Any
    dbname: Any
    dsn_parameters: Any
    error_message: Any
    host: Any
    needs_password: Any
    options: Any
    password: Any
    port: Any
    protocol_version: Any
    server_version: Any
    socket: Any
    ssl_attribute_names: Any
    ssl_in_use: Any
    status: Any
    transaction_status: Any
    used_password: Any
    user: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def parameter_status(self, *args, **kwargs): ...
    def ssl_attribute(self, *args, **kwargs): ...

class DataError(psycopg2.DatabaseError): ...
class DatabaseError(psycopg2.Error): ...

class Decimal:
    adapted: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getquoted(self, *args, **kwargs): ...
    def __conform__(self, *args, **kwargs): ...

class Diagnostics:
    column_name: Any
    constraint_name: Any
    context: Any
    datatype_name: Any
    internal_position: Any
    internal_query: Any
    message_detail: Any
    message_hint: Any
    message_primary: Any
    schema_name: Any
    severity: Any
    severity_nonlocalized: Any
    source_file: Any
    source_function: Any
    source_line: Any
    sqlstate: Any
    statement_position: Any
    table_name: Any
    def __init__(self, *args, **kwargs) -> None: ...

class Error(Exception):
    cursor: Any
    diag: Any
    pgcode: Any
    pgerror: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __setstate__(self, state): ...

class Float:
    adapted: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getquoted(self, *args, **kwargs): ...
    def __conform__(self, *args, **kwargs): ...

class ISQLQuote:
    _wrapped: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getbinary(self, *args, **kwargs): ...
    def getbuffer(self, *args, **kwargs): ...
    def getquoted(self, *args, **kwargs): ...

class Int:
    adapted: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getquoted(self, *args, **kwargs): ...
    def __conform__(self, *args, **kwargs): ...

class IntegrityError(psycopg2.DatabaseError): ...
class InterfaceError(psycopg2.Error): ...
class InternalError(psycopg2.DatabaseError): ...

class List:
    adapted: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getquoted(self, *args, **kwargs): ...
    def prepare(self, *args, **kwargs): ...
    def __conform__(self, *args, **kwargs): ...

class NotSupportedError(psycopg2.DatabaseError): ...

class Notify:
    channel: Any
    payload: Any
    pid: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __le__(self, other): ...
    def __len__(self): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...

class OperationalError(psycopg2.DatabaseError): ...
class ProgrammingError(psycopg2.DatabaseError): ...
class QueryCanceledError(psycopg2.OperationalError): ...

class QuotedString:
    adapted: Any
    buffer: Any
    encoding: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def getquoted(self, *args, **kwargs): ...
    def prepare(self, *args, **kwargs): ...
    def __conform__(self, *args, **kwargs): ...

class ReplicationConnection(psycopg2.extensions.connection):
    autocommit: Any
    isolation_level: Any
    replication_type: Any
    reset: Any
    set_isolation_level: Any
    set_session: Any
    def __init__(self, *args, **kwargs) -> None: ...

class ReplicationCursor(psycopg2.extensions.cursor):
    feedback_timestamp: Any
    io_timestamp: Any
    wal_end: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def consume_stream(self, consumer, keepalive_interval=...): ...
    def read_message(self, *args, **kwargs): ...
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

class TransactionRollbackError(psycopg2.OperationalError): ...
class Warning(Exception): ...

class Xid:
    bqual: Any
    database: Any
    format_id: Any
    gtrid: Any
    owner: Any
    prepared: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def from_string(self, *args, **kwargs): ...
    def __getitem__(self, index): ...
    def __len__(self): ...

_cursor = cursor
_T_cur = TypeVar("_T_cur", bound=_cursor)

class connection:
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
    async_: Any
    autocommit: Any
    binary_types: Any
    closed: Any
    cursor_factory: Callable[..., _cursor]
    deferrable: Any
    dsn: Any
    encoding: Any
    info: Any
    isolation_level: Any
    notices: Any
    notifies: Any
    pgconn_ptr: Any
    protocol_version: Any
    readonly: Any
    server_version: Any
    status: Any
    string_types: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def cancel(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def commit(self, *args, **kwargs): ...
    @overload
    def cursor(self, name=..., *, scrollable=..., withhold=...) -> _cursor: ...
    @overload
    def cursor(self, name=..., cursor_factory: Callable[..., _T_cur] = ..., scrollable=..., withhold=...) -> _T_cur: ...
    def fileno(self, *args, **kwargs): ...
    def get_backend_pid(self, *args, **kwargs): ...
    def get_dsn_parameters(self, *args, **kwargs): ...
    def get_native_connection(self, *args, **kwargs): ...
    def get_parameter_status(self, parameter): ...
    def get_transaction_status(self): ...
    def isexecuting(self, *args, **kwargs): ...
    def lobject(self, oid=..., mode=..., new_oid=..., new_file=..., lobject_factory=...): ...
    def poll(self, *args, **kwargs): ...
    def reset(self): ...
    def rollback(self): ...
    def set_client_encoding(self, encoding): ...
    def set_isolation_level(self, level): ...
    def set_session(self, *args, **kwargs): ...
    def tpc_begin(self, xid): ...
    def tpc_commit(self, *args, **kwargs): ...
    def tpc_prepare(self): ...
    def tpc_recover(self): ...
    def tpc_rollback(self, *args, **kwargs): ...
    def xid(self, format_id, gtrid, bqual): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...

class cursor:
    arraysize: int
    binary_types: Any
    closed: Any
    connection: Any
    description: Any
    itersize: Any
    lastrowid: Any
    name: Any
    pgresult_ptr: Any
    query: Any
    row_factory: Any
    rowcount: int
    rownumber: int
    scrollable: Any
    statusmessage: Any
    string_types: Any
    typecaster: Any
    tzinfo_factory: Any
    withhold: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def callproc(self, procname, parameters=...): ...
    def cast(self, oid, s): ...
    def close(self): ...
    def copy_expert(self, sql, file, size=...): ...
    def copy_from(self, file, table, sep=..., null=..., size=..., columns=...): ...
    def copy_to(self, file, table, sep=..., null=..., columns=...): ...
    def execute(self, query, vars=...): ...
    def executemany(self, query, vars_list): ...
    def fetchall(self) -> list[tuple[Any, ...]]: ...
    def fetchmany(self, size=...) -> list[tuple[Any, ...]]: ...
    def fetchone(self) -> tuple[Any, ...] | Any: ...
    def mogrify(self, *args, **kwargs): ...
    def nextset(self): ...
    def scroll(self, value, mode=...): ...
    def setinputsizes(self, sizes): ...
    def setoutputsize(self, size, column=...): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...
    def __iter__(self): ...
    def __next__(self): ...

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

def Date(year, month, day): ...
def DateFromPy(*args, **kwargs): ...
def DateFromTicks(ticks): ...
def IntervalFromPy(*args, **kwargs): ...
def Time(hour, minutes, seconds, tzinfo=...): ...
def TimeFromPy(*args, **kwargs): ...
def TimeFromTicks(ticks): ...
def Timestamp(year, month, day, hour, minutes, seconds, tzinfo=...): ...
def TimestampFromPy(*args, **kwargs): ...
def TimestampFromTicks(ticks): ...
def _connect(*args, **kwargs): ...
def adapt(*args, **kwargs): ...
def encrypt_password(*args, **kwargs): ...
def get_wait_callback(*args, **kwargs): ...
def libpq_version(*args, **kwargs): ...
def new_array_type(oids, name, baseobj): ...
def new_type(oids, name, castobj): ...
def parse_dsn(*args, **kwargs): ...
def quote_ident(*args, **kwargs): ...
def register_type(*args, **kwargs): ...
def set_wait_callback(_none): ...
