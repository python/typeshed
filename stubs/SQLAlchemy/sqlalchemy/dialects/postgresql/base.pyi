from _typeshed import Incomplete
from datetime import timedelta
from re import Pattern
from typing import Any, NoReturn

from ...engine import characteristics, default, reflection
from ...schema import _CreateDropBase
from ...sql import compiler, elements, sqltypes
from ...sql.ddl import DDLBase
from ...sql.type_api import TypeEngine
from ...types import (
    BIGINT as BIGINT,
    BOOLEAN as BOOLEAN,
    CHAR as CHAR,
    DATE as DATE,
    FLOAT as FLOAT,
    INTEGER as INTEGER,
    NUMERIC as NUMERIC,
    REAL as REAL,
    SMALLINT as SMALLINT,
    TEXT as TEXT,
    VARCHAR as VARCHAR,
)
from ...util.langhelpers import memoized_property

IDX_USING: Pattern[str]
AUTOCOMMIT_REGEXP: Pattern[str]
RESERVED_WORDS: set[str]

class BYTEA(sqltypes.LargeBinary):
    __visit_name__: str

class DOUBLE_PRECISION(sqltypes.Float):
    __visit_name__: str

class INET(sqltypes.TypeEngine):
    __visit_name__: str

PGInet = INET

class CIDR(sqltypes.TypeEngine):
    __visit_name__: str

PGCidr = CIDR

class MACADDR(sqltypes.TypeEngine):
    __visit_name__: str

PGMacAddr = MACADDR

class MACADDR8(sqltypes.TypeEngine):
    __visit_name__: str

PGMacAddr8 = MACADDR8

class MONEY(sqltypes.TypeEngine):
    __visit_name__: str

class OID(sqltypes.TypeEngine):
    __visit_name__: str

class REGCLASS(sqltypes.TypeEngine):
    __visit_name__: str

class TIMESTAMP(sqltypes.TIMESTAMP):
    precision: int | None
    def __init__(self, timezone: bool = ..., precision: int | None = ...) -> None: ...

class TIME(sqltypes.TIME):
    precision: int | None
    def __init__(self, timezone: bool = ..., precision: int | None = ...) -> None: ...

class INTERVAL(sqltypes.NativeForEmulated, sqltypes._AbstractInterval):
    __visit_name__: str
    native: bool
    precision: int | None
    fields: str | None
    def __init__(self, precision: int | None = ..., fields: str | None = ...) -> None: ...
    @classmethod
    def adapt_emulated_to_native(cls, interval, **kw) -> INTERVAL: ...  # type: ignore[override]  # Return type incompatible with supertype
    def as_generic(self, allow_nulltype: bool = ...): ...
    @property
    def python_type(self) -> type[timedelta]: ...
    def coerce_compared_value(self, op, value): ...

PGInterval = INTERVAL

class BIT(sqltypes.TypeEngine):
    __visit_name__: str
    length: int | None
    varying: bool
    def __init__(self, length: int | None = ..., varying: bool = ...) -> None: ...

PGBit = BIT

class UUID(sqltypes.TypeEngine):
    __visit_name__: str
    as_uuid: bool
    def __init__(self, as_uuid: bool = ...) -> None: ...
    def coerce_compared_value(self, op, value): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

PGUuid = UUID

class TSVECTOR(sqltypes.TypeEngine):
    __visit_name__: str

class ENUM(sqltypes.NativeForEmulated, sqltypes.Enum):  # type: ignore[misc]  # base classes incompatible
    native_enum: bool
    create_type: Any
    def __init__(self, *enums, **kw) -> None: ...
    @classmethod
    def adapt_emulated_to_native(cls, impl, **kw): ...
    def create(self, bind: Incomplete | None = ..., checkfirst: bool = ...) -> None: ...
    def drop(self, bind: Incomplete | None = ..., checkfirst: bool = ...) -> None: ...

    class EnumGenerator(DDLBase):
        checkfirst: Any
        def __init__(self, dialect, connection, checkfirst: bool = ..., **kwargs) -> None: ...
        def visit_enum(self, enum) -> None: ...

    class EnumDropper(DDLBase):
        checkfirst: Any
        def __init__(self, dialect, connection, checkfirst: bool = ..., **kwargs) -> None: ...
        def visit_enum(self, enum) -> None: ...

class _ColonCast(elements.Cast):
    __visit_name__: str
    @memoized_property
    def type(self) -> Incomplete: ...
    clause: Any
    typeclause: Any
    def __init__(self, expression, type_) -> None: ...

colspecs: dict[TypeEngine, TypeEngine]
ischema_names: dict[str, TypeEngine]

class PGCompiler(compiler.SQLCompiler):
    def visit_colon_cast(self, element, **kw): ...
    def visit_array(self, element, **kw): ...
    def visit_slice(self, element, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, _cast_applied: bool = ..., **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, _cast_applied: bool = ..., **kw): ...
    def visit_getitem_binary(self, binary, operator, **kw): ...
    def visit_aggregate_order_by(self, element, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def visit_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_not_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw): ...
    def visit_empty_set_expr(self, element_types): ...
    def render_literal_value(self, value, type_): ...
    def visit_sequence(self, seq, **kw) -> str: ...  # type: ignore[override]  # Different params
    def limit_clause(self, select, **kw): ...
    def format_from_hint_text(self, sqltext, table, hint, iscrud): ...
    def get_select_precolumns(self, select, **kw): ...
    def for_update_clause(self, select, **kw): ...
    def returning_clause(self, stmt, returning_cols): ...
    def visit_substring_func(self, func, **kw): ...
    def visit_on_conflict_do_nothing(self, on_conflict, **kw): ...
    def visit_on_conflict_do_update(self, on_conflict, **kw): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def delete_extra_from_clause(self, delete_stmt, from_table, extra_froms, from_hints, **kw) -> str: ...  # type: ignore[override]  # Different params
    def fetch_clause(self, select, **kw): ...

class PGDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kwargs): ...
    def visit_check_constraint(self, constraint): ...
    def visit_foreign_key_constraint(self, constraint) -> str: ...  # type: ignore[override]  # Different params
    def visit_drop_table_comment(self, drop): ...
    def visit_create_enum_type(self, create): ...
    def visit_drop_enum_type(self, drop): ...
    def visit_create_index(self, create) -> str: ...  # type: ignore[override]  # Different params
    def visit_drop_index(self, drop): ...
    def visit_exclude_constraint(self, constraint, **kw): ...
    def post_create_table(self, table): ...
    def visit_computed_column(self, generated): ...
    def visit_create_sequence(self, create, **kw): ...

class PGTypeCompiler(compiler.GenericTypeCompiler):
    def visit_TSVECTOR(self, type_, **kw): ...
    def visit_INET(self, type_, **kw): ...
    def visit_CIDR(self, type_, **kw): ...
    def visit_MACADDR(self, type_, **kw): ...
    def visit_MONEY(self, type_, **kw): ...
    def visit_OID(self, type_, **kw): ...
    def visit_REGCLASS(self, type_, **kw): ...
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
    def visit_ENUM(self, type_, identifier_preparer: Incomplete | None = ..., **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_INTERVAL(self, type_, **kw): ...
    def visit_BIT(self, type_, **kw): ...
    def visit_UUID(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_BYTEA(self, type_, **kw): ...
    def visit_ARRAY(self, type_, **kw): ...

class PGIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any
    def format_type(self, type_, use_schema: bool = ...): ...

class PGInspector(reflection.Inspector):
    def get_table_oid(self, table_name, schema: Incomplete | None = ...): ...
    def get_enums(self, schema: Incomplete | None = ...): ...
    def get_foreign_table_names(self, schema: Incomplete | None = ...): ...
    def get_view_names(self, schema: Incomplete | None = ..., include=...): ...

class CreateEnumType(_CreateDropBase):
    __visit_name__: str

class DropEnumType(_CreateDropBase):
    __visit_name__: str

class PGExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq, type_): ...
    def get_insert_default(self, column): ...
    def should_autocommit_text(self, statement): ...

class PGReadOnlyConnectionCharacteristic(characteristics.ConnectionCharacteristic):
    transactional: bool
    def reset_characteristic(self, dialect, dbapi_conn) -> None: ...
    def set_characteristic(self, dialect, dbapi_conn, value) -> None: ...
    def get_characteristic(self, dialect, dbapi_conn): ...

class PGDeferrableConnectionCharacteristic(characteristics.ConnectionCharacteristic):
    transactional: bool
    def reset_characteristic(self, dialect, dbapi_conn) -> None: ...
    def set_characteristic(self, dialect, dbapi_conn, value) -> None: ...
    def get_characteristic(self, dialect, dbapi_conn): ...

class PGDialect(default.DefaultDialect):
    name: str
    supports_statement_cache: bool
    supports_alter: bool
    max_identifier_length: int
    supports_sane_rowcount: bool
    supports_native_enum: bool
    supports_native_boolean: bool
    supports_smallserial: bool
    supports_sequences: bool
    sequences_optional: bool
    preexecute_autoincrement_sequences: bool
    postfetch_lastrowid: bool
    supports_comments: bool
    supports_default_values: bool
    supports_default_metavalue: bool
    supports_empty_insert: bool
    supports_multivalues_insert: bool
    supports_identity_columns: bool
    default_paramstyle: str
    ischema_names: Any
    colspecs: Any
    statement_compiler: Any
    ddl_compiler: Any
    type_compiler: Any
    preparer: Any
    inspector: Any
    isolation_level: Any
    implicit_returning: bool
    full_returning: bool
    connection_characteristics: Any
    construct_arguments: Any
    reflection_options: Any
    def __init__(
        self,
        isolation_level: Incomplete | None = ...,
        json_serializer: Incomplete | None = ...,
        json_deserializer: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...
    def initialize(self, connection) -> None: ...
    def on_connect(self): ...
    def set_isolation_level(self, connection, level) -> None: ...
    def get_isolation_level(self, connection): ...
    # These 4 methods are meant to be overriden. But not all instanciated subclasses override them
    def set_readonly(self, connection, value) -> NoReturn | None: ...
    def get_readonly(self, connection) -> NoReturn | bool: ...
    def set_deferrable(self, connection, value) -> NoReturn | None: ...
    def get_deferrable(self, connection) -> NoReturn | bool: ...
    def do_begin_twophase(self, connection, xid) -> None: ...
    def do_prepare_twophase(self, connection, xid) -> None: ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_recover_twophase(self, connection): ...
    def has_schema(self, connection, schema) -> bool: ...
    def has_table(self, connection, table_name, schema: Incomplete | None = ...) -> bool: ...  # type: ignore[override]
    def has_sequence(self, connection, sequence_name, schema: Incomplete | None = ...) -> bool: ...  # type: ignore[override]
    def has_type(self, connection, type_name, schema: Incomplete | None = ...) -> bool: ...
    def get_table_oid(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, schema: Incomplete | None = ..., **kw): ...
    def get_view_names(self, connection, schema: Incomplete | None = ..., include=..., **kw): ...
    def get_sequence_names(self, connection, schema: Incomplete | None = ..., **kw): ...
    def get_view_definition(self, connection, view_name, schema: Incomplete | None = ..., **kw): ...
    def get_columns(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_pk_constraint(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_foreign_keys(
        self, connection, table_name, schema: Incomplete | None = ..., postgresql_ignore_search_path: bool = ..., **kw
    ): ...
    def get_indexes(self, connection, table_name, schema, **kw): ...
    def get_unique_constraints(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_table_comment(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_check_constraints(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
