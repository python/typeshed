# Stubs for sqlalchemy.dialects.sqlite.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import sqltypes
import compiler
import default
from ... import types as sqltypes, schema as sa_schema
from ...engine import default as default, reflection as reflection
from ...sql import compiler as compiler
from ...types import BLOB as BLOB, BOOLEAN as BOOLEAN, CHAR as CHAR, DECIMAL as DECIMAL, FLOAT as FLOAT, INTEGER as INTEGER, REAL as REAL, NUMERIC as NUMERIC, SMALLINT as SMALLINT, TEXT as TEXT, TIMESTAMP as TIMESTAMP, VARCHAR as VARCHAR

class _DateTimeMixin:
    def __init__(self, storage_format: Optional[Any] = ..., regexp: Optional[Any] = ..., **kw) -> None: ...
    @property
    def format_is_text_affinity(self): ...
    def adapt(self, cls, **kw): ...
    def literal_processor(self, dialect): ...

class DATETIME(_DateTimeMixin, sqltypes.DateTime):
    def __init__(self, *args, **kwargs) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class DATE(_DateTimeMixin, sqltypes.Date):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class TIME(_DateTimeMixin, sqltypes.Time):
    def __init__(self, *args, **kwargs) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

colspecs = ...  # type: Any
ischema_names = ...  # type: Any

class SQLiteCompiler(compiler.SQLCompiler):
    extract_map = ...  # type: Any
    def visit_now_func(self, fn, **kw): ...
    def visit_localtimestamp_func(self, func, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def visit_char_length_func(self, fn, **kw): ...
    def visit_cast(self, cast, **kwargs): ...
    def visit_extract(self, extract, **kw): ...
    def limit_clause(self, select, **kw): ...
    def for_update_clause(self, select, **kw): ...
    def visit_is_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_isnot_distinct_from_binary(self, binary, operator, **kw): ...

class SQLiteDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kwargs): ...
    def visit_primary_key_constraint(self, constraint): ...
    def visit_foreign_key_constraint(self, constraint): ...
    def define_constraint_remote_table(self, constraint, table, preparer): ...
    def visit_create_index(self, create, include_schema: bool = ..., include_table_schema: bool = ...): ...

class SQLiteTypeCompiler(compiler.GenericTypeCompiler):
    def visit_large_binary(self, type_, **kw): ...
    def visit_DATETIME(self, type_, **kw): ...
    def visit_DATE(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...

class SQLiteIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = ...  # type: Any
    def format_index(self, index, use_schema: bool = ..., name: Optional[Any] = ...): ...

class SQLiteExecutionContext(default.DefaultExecutionContext): ...

class SQLiteDialect(default.DefaultDialect):
    name = ...  # type: str
    supports_alter = ...  # type: bool
    supports_unicode_statements = ...  # type: bool
    supports_unicode_binds = ...  # type: bool
    supports_default_values = ...  # type: bool
    supports_empty_insert = ...  # type: bool
    supports_cast = ...  # type: bool
    supports_multivalues_insert = ...  # type: bool
    default_paramstyle = ...  # type: str
    execution_ctx_cls = ...  # type: Any
    statement_compiler = ...  # type: Any
    ddl_compiler = ...  # type: Any
    type_compiler = ...  # type: Any
    preparer = ...  # type: Any
    ischema_names = ...  # type: Any
    colspecs = ...  # type: Any
    isolation_level = ...  # type: Any
    construct_arguments = ...  # type: Any
    native_datetime = ...  # type: Any
    supports_right_nested_joins = ...  # type: Any
    def __init__(self, isolation_level: Optional[Any] = ..., native_datetime: bool = ..., **kwargs) -> None: ...
    def set_isolation_level(self, connection, level): ...
    def get_isolation_level(self, connection): ...
    def on_connect(self): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, schema: Optional[Any] = ..., **kw): ...
    def get_temp_table_names(self, connection, **kw): ...
    def get_temp_view_names(self, connection, **kw): ...
    def has_table(self, connection, table_name, schema: Optional[Any] = ...): ...
    def get_view_names(self, connection, schema: Optional[Any] = ..., **kw): ...
    def get_view_definition(self, connection, view_name, schema: Optional[Any] = ..., **kw): ...
    def get_columns(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_pk_constraint(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_foreign_keys(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_unique_constraints(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_check_constraints(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_indexes(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
