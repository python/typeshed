from _typeshed import Incomplete
from typing import Any

from ...engine import AdaptedConnection
from ...sql import sqltypes
from . import json
from .base import ENUM, INTERVAL, OID, REGCLASS, UUID, PGCompiler, PGDialect, PGExecutionContext, PGIdentifierPreparer

class AsyncpgTime(sqltypes.Time):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgDate(sqltypes.Date):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgDateTime(sqltypes.DateTime):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi): ...

class AsyncPgInterval(INTERVAL):
    def get_dbapi_type(self, dbapi): ...
    @classmethod
    def adapt_emulated_to_native(cls, interval, **kw): ...

class AsyncPgEnum(ENUM):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgInteger(sqltypes.Integer):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgBigInteger(sqltypes.BigInteger):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgJSON(json.JSON):
    def get_dbapi_type(self, dbapi): ...
    def result_processor(self, dialect, coltype) -> None: ...

class AsyncpgJSONB(json.JSONB):
    def get_dbapi_type(self, dbapi): ...
    def result_processor(self, dialect, coltype) -> None: ...

class AsyncpgJSONIndexType(sqltypes.JSON.JSONIndexType):
    def get_dbapi_type(self, dbapi) -> None: ...

class AsyncpgJSONIntIndexType(sqltypes.JSON.JSONIntIndexType):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgJSONStrIndexType(sqltypes.JSON.JSONStrIndexType):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgJSONPathType(json.JSONPathType):
    def bind_processor(self, dialect): ...

class AsyncpgUUID(UUID):
    def get_dbapi_type(self, dbapi): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class AsyncpgNumeric(sqltypes.Numeric):
    def get_dbapi_type(self, dbapi): ...
    def bind_processor(self, dialect) -> None: ...
    def result_processor(self, dialect, coltype): ...

class AsyncpgFloat(AsyncpgNumeric):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgREGCLASS(REGCLASS):
    def get_dbapi_type(self, dbapi): ...

class AsyncpgOID(OID):
    def get_dbapi_type(self, dbapi): ...

class PGExecutionContext_asyncpg(PGExecutionContext):
    def handle_dbapi_exception(self, e) -> None: ...
    exclude_set_input_sizes: Any
    def pre_exec(self) -> None: ...
    def create_server_side_cursor(self): ...

class PGCompiler_asyncpg(PGCompiler): ...
class PGIdentifierPreparer_asyncpg(PGIdentifierPreparer): ...

class AsyncAdapt_asyncpg_cursor:
    server_side: bool
    description: Any
    arraysize: int
    rowcount: int
    def __init__(self, adapt_connection) -> None: ...
    def close(self) -> None: ...
    def execute(self, operation, parameters: Incomplete | None = None) -> None: ...
    def executemany(self, operation, seq_of_parameters): ...
    def setinputsizes(self, *inputsizes) -> None: ...
    def __iter__(self): ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = None): ...
    def fetchall(self): ...

class AsyncAdapt_asyncpg_ss_cursor(AsyncAdapt_asyncpg_cursor):
    server_side: bool
    def __init__(self, adapt_connection) -> None: ...
    def close(self) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self) -> None: ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = None): ...
    def fetchall(self): ...
    def executemany(self, operation, seq_of_parameters) -> None: ...

class AsyncAdapt_asyncpg_connection(AdaptedConnection):
    await_: Any
    dbapi: Any
    isolation_level: str
    readonly: bool
    deferrable: bool
    def __init__(self, dbapi, connection, prepared_statement_cache_size: int = 100) -> None: ...
    @property
    def autocommit(self): ...
    @autocommit.setter
    def autocommit(self, value) -> None: ...
    def set_isolation_level(self, level) -> None: ...
    def cursor(self, server_side: bool = False): ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...

class AsyncAdaptFallback_asyncpg_connection(AsyncAdapt_asyncpg_connection):
    await_: Any

class AsyncAdapt_asyncpg_dbapi:
    asyncpg: Any
    paramstyle: str
    def __init__(self, asyncpg) -> None: ...
    def connect(self, *arg, **kw): ...

    class Error(Exception): ...
    class Warning(Exception): ...
    class InterfaceError(Error): ...
    class DatabaseError(Error): ...
    class InternalError(DatabaseError): ...
    class OperationalError(DatabaseError): ...
    class ProgrammingError(DatabaseError): ...
    class IntegrityError(DatabaseError): ...
    class DataError(DatabaseError): ...
    class NotSupportedError(DatabaseError): ...
    class InternalServerError(InternalError): ...

    class InvalidCachedStatementError(NotSupportedError):
        def __init__(self, message) -> None: ...

    def Binary(self, value): ...
    STRING: Any
    TIMESTAMP: Any
    TIMESTAMP_W_TZ: Any
    TIME: Any
    TIME_W_TZ: Incomplete
    DATE: Any
    INTERVAL: Any
    NUMBER: Any
    FLOAT: Any
    BOOLEAN: Any
    INTEGER: Any
    BIGINTEGER: Any
    BYTES: Any
    DECIMAL: Any
    JSON: Any
    JSONB: Any
    ENUM: Any
    UUID: Any
    BYTEA: Any
    DATETIME: Any
    BINARY: Any

class PGDialect_asyncpg(PGDialect):
    driver: str
    supports_statement_cache: bool
    supports_unicode_statements: bool
    supports_server_side_cursors: bool
    supports_unicode_binds: bool
    has_terminate: bool
    default_paramstyle: str
    supports_sane_multi_rowcount: bool
    statement_compiler: Any
    preparer: Any
    use_setinputsizes: bool
    use_native_uuid: bool
    colspecs: Any
    is_async: bool
    @classmethod
    def dbapi(cls): ...
    def set_isolation_level(self, connection, level) -> None: ...
    def set_readonly(self, connection, value) -> None: ...
    def get_readonly(self, connection): ...
    def set_deferrable(self, connection, value) -> None: ...
    def get_deferrable(self, connection): ...
    def create_connect_args(self, url): ...
    @classmethod
    def get_pool_class(cls, url): ...
    def is_disconnect(self, e, connection, cursor) -> bool: ...
    def do_set_input_sizes(self, cursor, list_of_tuples, context) -> None: ...
    async def setup_asyncpg_json_codec(self, conn): ...
    async def setup_asyncpg_jsonb_codec(self, conn): ...
    def on_connect(self): ...
    def get_driver_connection(self, connection): ...

dialect = PGDialect_asyncpg
