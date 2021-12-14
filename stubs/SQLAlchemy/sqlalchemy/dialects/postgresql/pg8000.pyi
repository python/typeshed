from typing import Any

from ... import types as sqltypes
from .array import ARRAY as PGARRAY
from .base import ENUM, INTERVAL, UUID, PGCompiler, PGDialect, PGExecutionContext, PGIdentifierPreparer
from .json import JSON, JSONB, JSONPathType

class _PGNumeric(sqltypes.Numeric):
    def result_processor(self, dialect, coltype): ...

class _PGNumericNoBind(_PGNumeric):
    def bind_processor(self, dialect) -> None: ...

class _PGJSON(JSON):
    def result_processor(self, dialect, coltype) -> None: ...
    def get_dbapi_type(self, dbapi): ...

class _PGJSONB(JSONB):
    def result_processor(self, dialect, coltype) -> None: ...
    def get_dbapi_type(self, dbapi): ...

class _PGJSONIndexType(sqltypes.JSON.JSONIndexType):
    def get_dbapi_type(self, dbapi) -> None: ...

class _PGJSONIntIndexType(sqltypes.JSON.JSONIntIndexType):
    def get_dbapi_type(self, dbapi): ...

class _PGJSONStrIndexType(sqltypes.JSON.JSONStrIndexType):
    def get_dbapi_type(self, dbapi): ...

class _PGJSONPathType(JSONPathType):
    def get_dbapi_type(self, dbapi): ...

class _PGUUID(UUID):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _PGEnum(ENUM):
    def get_dbapi_type(self, dbapi): ...

class _PGInterval(INTERVAL):
    def get_dbapi_type(self, dbapi): ...
    @classmethod
    def adapt_emulated_to_native(cls, interval, **kw): ...

class _PGTimeStamp(sqltypes.DateTime):
    def get_dbapi_type(self, dbapi): ...

class _PGTime(sqltypes.Time):
    def get_dbapi_type(self, dbapi): ...

class _PGInteger(sqltypes.Integer):
    def get_dbapi_type(self, dbapi): ...

class _PGSmallInteger(sqltypes.SmallInteger):
    def get_dbapi_type(self, dbapi): ...

class _PGNullType(sqltypes.NullType):
    def get_dbapi_type(self, dbapi): ...

class _PGBigInteger(sqltypes.BigInteger):
    def get_dbapi_type(self, dbapi): ...

class _PGBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi): ...

class _PGARRAY(PGARRAY):
    def bind_expression(self, bindvalue): ...

class PGExecutionContext_pg8000(PGExecutionContext):
    def create_server_side_cursor(self): ...
    def pre_exec(self) -> None: ...

class ServerSideCursor:
    server_side: bool
    ident: Any
    cursor: Any
    def __init__(self, cursor, ident) -> None: ...
    @property
    def connection(self): ...
    @property
    def rowcount(self): ...
    @property
    def description(self): ...
    def execute(self, operation, args=..., stream: Any | None = ...): ...
    def executemany(self, operation, param_sets): ...
    def fetchone(self): ...
    def fetchmany(self, num: Any | None = ...): ...
    def fetchall(self): ...
    def close(self) -> None: ...
    def setinputsizes(self, *sizes) -> None: ...
    def setoutputsize(self, size, column: Any | None = ...) -> None: ...

class PGCompiler_pg8000(PGCompiler):
    def visit_mod_binary(self, binary, operator, **kw): ...

class PGIdentifierPreparer_pg8000(PGIdentifierPreparer):
    def __init__(self, *args, **kwargs) -> None: ...

class PGDialect_pg8000(PGDialect):
    driver: str
    supports_statement_cache: bool
    supports_unicode_statements: bool
    supports_unicode_binds: bool
    default_paramstyle: str
    supports_sane_multi_rowcount: bool
    execution_ctx_cls: Any
    statement_compiler: Any
    preparer: Any
    supports_server_side_cursors: bool
    use_setinputsizes: bool
    description_encoding: Any
    colspecs: Any
    client_encoding: Any
    def __init__(self, client_encoding: Any | None = ..., **kwargs) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...
    def set_isolation_level(self, connection, level) -> None: ...
    def set_readonly(self, connection, value) -> None: ...
    def get_readonly(self, connection): ...
    def set_deferrable(self, connection, value) -> None: ...
    def get_deferrable(self, connection): ...
    def set_client_encoding(self, connection, client_encoding) -> None: ...
    def do_set_input_sizes(self, cursor, list_of_tuples, context) -> None: ...
    def do_begin_twophase(self, connection, xid) -> None: ...
    def do_prepare_twophase(self, connection, xid) -> None: ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_recover_twophase(self, connection): ...
    def on_connect(self): ...

dialect = PGDialect_pg8000
