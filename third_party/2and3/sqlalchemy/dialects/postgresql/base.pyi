# Stubs for sqlalchemy.dialects.postgresql.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from sqlalchemy.sql import compiler
from sqlalchemy import schema
from ...engine import default as default, reflection as reflection
from ...sql import compiler as compiler, expression as expression
from ... import types as sqltypes
from uuid import UUID as _python_UUID

from sqlalchemy.types import INTEGER as INTEGER, BIGINT as BIGINT, SMALLINT as SMALLINT, VARCHAR as VARCHAR, \
    CHAR as CHAR, TEXT as TEXT, FLOAT as FLOAT, NUMERIC as NUMERIC, \
    DATE as DATE, BOOLEAN as BOOLEAN, REAL as REAL

AUTOCOMMIT_REGEXP = ...  # type: Any
RESERVED_WORDS = ...  # type: Any

class BYTEA(sqltypes.LargeBinary):
    __visit_name__ = ...  # type: str

class DOUBLE_PRECISION(sqltypes.Float):
    __visit_name__ = ...  # type: str

class INET(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

PGInet = ...  # type: Any

class CIDR(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

PGCidr = ...  # type: Any

class MACADDR(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

PGMacAddr = ...  # type: Any

class OID(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

class TIMESTAMP(sqltypes.TIMESTAMP):
    precision = ...  # type: Any
    def __init__(self, timezone: bool = ..., precision: Optional[Any] = ...) -> None: ...

class TIME(sqltypes.TIME):
    precision = ...  # type: Any
    def __init__(self, timezone: bool = ..., precision: Optional[Any] = ...) -> None: ...

class INTERVAL(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str
    precision = ...  # type: Any
    def __init__(self, precision: Optional[Any] = ...) -> None: ...
    @property
    def python_type(self): ...

PGInterval = ...  # type: Any

class BIT(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str
    length = ...  # type: Any
    varying = ...  # type: Any
    def __init__(self, length: Optional[Any] = ..., varying: bool = ...) -> None: ...

PGBit = ...  # type: Any

class UUID(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str
    as_uuid = ...  # type: Any
    def __init__(self, as_uuid: bool = ...) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

PGUuid = ...  # type: Any

class TSVECTOR(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

class ENUM(sqltypes.Enum):
    create_type = ...  # type: Any
    def __init__(self, *enums, **kw) -> None: ...
    def create(self, bind: Optional[Any] = ..., checkfirst: bool = ...): ...
    def drop(self, bind: Optional[Any] = ..., checkfirst: bool = ...): ...

colspecs = ...  # type: Any
ischema_names = ...  # type: Any

class PGCompiler(compiler.SQLCompiler):
    def visit_array(self, element, **kw): ...
    def visit_slice(self, element, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_getitem_binary(self, binary, operator, **kw): ...
    def visit_aggregate_order_by(self, element, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def visit_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_notilike_op_binary(self, binary, operator, **kw): ...
    def render_literal_value(self, value, type_): ...
    def visit_sequence(self, seq): ...
    def limit_clause(self, select, **kw): ...
    def format_from_hint_text(self, sqltext, table, hint, iscrud): ...
    def get_select_precolumns(self, select, **kw): ...
    def for_update_clause(self, select, **kw): ...
    def returning_clause(self, stmt, returning_cols): ...
    def visit_substring_func(self, func, **kw): ...
    def visit_on_conflict_do_nothing(self, on_conflict, **kw): ...
    def visit_on_conflict_do_update(self, on_conflict, **kw): ...

class PGDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kwargs): ...
    def visit_create_enum_type(self, create): ...
    def visit_drop_enum_type(self, drop): ...
    def visit_create_index(self, create): ...
    def visit_drop_index(self, drop): ...
    def visit_exclude_constraint(self, constraint, **kw): ...
    def post_create_table(self, table): ...

class PGTypeCompiler(compiler.GenericTypeCompiler):
    def visit_TSVECTOR(self, type, **kw): ...
    def visit_INET(self, type_, **kw): ...
    def visit_CIDR(self, type_, **kw): ...
    def visit_MACADDR(self, type_, **kw): ...
    def visit_OID(self, type_, **kw): ...
    def visit_FLOAT(self, type_, **kw): ...
    def visit_DOUBLE_PRECISION(self, type_, **kw): ...
    def visit_BIGINT(self, type_, **kw): ...
    def visit_HSTORE(self, type_, **kw): ...
    def visit_JSON(self, type_, **kw): ...
    def visit_JSONB(self, type_, **kw): ...
    def visit_INT4RANGE(self, type_, **kw): ...
    def visit_INT8RANGE(self, type_, **kw): ...
    def visit_NUMRANGE(self, type_, **kw): ...
    def visit_DATERANGE(self, type_, **kw): ...
    def visit_TSRANGE(self, type_, **kw): ...
    def visit_TSTZRANGE(self, type_, **kw): ...
    def visit_datetime(self, type_, **kw): ...
    def visit_enum(self, type_, **kw): ...
    def visit_ENUM(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_INTERVAL(self, type_, **kw): ...
    def visit_BIT(self, type_, **kw): ...
    def visit_UUID(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_BYTEA(self, type_, **kw): ...
    def visit_ARRAY(self, type_, **kw): ...

class PGIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = ...  # type: Any
    def format_type(self, type_, use_schema: bool = ...): ...

class PGInspector(reflection.Inspector):
    def __init__(self, conn) -> None: ...
    def get_table_oid(self, table_name, schema: Optional[Any] = ...): ...
    def get_enums(self, schema: Optional[Any] = ...): ...
    def get_foreign_table_names(self, schema: Optional[Any] = ...): ...
    def get_view_names(self, schema: Optional[Any] = ..., include: Any = ...): ...

class CreateEnumType(schema._CreateDropBase):
    __visit_name__ = ...  # type: str

class DropEnumType(schema._CreateDropBase):
    __visit_name__ = ...  # type: str

class PGExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq, type_): ...
    def get_insert_default(self, column): ...
    def should_autocommit_text(self, statement): ...

class PGDialect(default.DefaultDialect):
    name = ...  # type: str
    supports_alter = ...  # type: bool
    max_identifier_length = ...  # type: int
    supports_sane_rowcount = ...  # type: bool
    supports_native_enum = ...  # type: bool
    supports_native_boolean = ...  # type: bool
    supports_smallserial = ...  # type: bool
    supports_sequences = ...  # type: bool
    sequences_optional = ...  # type: bool
    preexecute_autoincrement_sequences = ...  # type: bool
    postfetch_lastrowid = ...  # type: bool
    supports_default_values = ...  # type: bool
    supports_empty_insert = ...  # type: bool
    supports_multivalues_insert = ...  # type: bool
    default_paramstyle = ...  # type: str
    ischema_names = ...  # type: Any
    colspecs = ...  # type: Any
    statement_compiler = ...  # type: Any
    ddl_compiler = ...  # type: Any
    type_compiler = ...  # type: Any
    preparer = ...  # type: Any
    execution_ctx_cls = ...  # type: Any
    inspector = ...  # type: Any
    isolation_level = ...  # type: Any
    construct_arguments = ...  # type: Any
    reflection_options = ...  # type: Any
    def __init__(self, isolation_level: Optional[Any] = ..., json_serializer: Optional[Any] = ..., json_deserializer: Optional[Any] = ..., **kwargs) -> None: ...
    implicit_returning = ...  # type: Any
    def initialize(self, connection): ...
    def on_connect(self): ...
    def set_isolation_level(self, connection, level): ...
    def get_isolation_level(self, connection): ...
    def do_begin_twophase(self, connection, xid): ...
    def do_prepare_twophase(self, connection, xid): ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...): ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...): ...
    def do_recover_twophase(self, connection): ...
    def has_schema(self, connection, schema): ...
    def has_table(self, connection, table_name, schema: Optional[Any] = ...): ...
    def has_sequence(self, connection, sequence_name, schema: Optional[Any] = ...): ...
    def has_type(self, connection, type_name, schema: Optional[Any] = ...): ...
    def get_table_oid(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, schema: Optional[Any] = ..., **kw): ...
    def get_view_names(self, connection, schema: Optional[Any] = ..., include: Any = ..., **kw): ...
    def get_view_definition(self, connection, view_name, schema: Optional[Any] = ..., **kw): ...
    def get_columns(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_pk_constraint(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_foreign_keys(self, connection, table_name, schema: Optional[Any] = ..., postgresql_ignore_search_path: bool = ..., **kw): ...
    def get_indexes(self, connection, table_name, schema, **kw): ...
    def get_unique_constraints(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_check_constraints(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
