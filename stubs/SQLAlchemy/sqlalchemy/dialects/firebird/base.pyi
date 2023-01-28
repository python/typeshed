from _typeshed import Incomplete
from typing import Any

from ...engine import default
from ...sql import compiler, sqltypes
from ...types import (
    BIGINT as BIGINT,
    BLOB as BLOB,
    DATE as DATE,
    FLOAT as FLOAT,
    INTEGER as INTEGER,
    NUMERIC as NUMERIC,
    SMALLINT as SMALLINT,
    TEXT as TEXT,
    TIME as TIME,
    TIMESTAMP as TIMESTAMP,
    Integer as Integer,
)

RESERVED_WORDS: Any

class _StringType(sqltypes.String):
    charset: Any
    def __init__(self, charset: Incomplete | None = ..., **kw) -> None: ...

class VARCHAR(_StringType, sqltypes.VARCHAR):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = ..., **kwargs) -> None: ...

class CHAR(_StringType, sqltypes.CHAR):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = ..., **kwargs) -> None: ...

class _FBDateTime(sqltypes.DateTime):
    def bind_processor(self, dialect): ...

colspecs: Any
ischema_names: Any

class FBTypeCompiler(compiler.GenericTypeCompiler):
    def visit_boolean(self, type_, **kw): ...
    def visit_datetime(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_BLOB(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...

class FBCompiler(compiler.SQLCompiler):
    ansi_bind_rules: bool
    def visit_now_func(self, fn, **kw): ...
    def visit_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_mod_binary(self, binary, operator, **kw): ...
    def visit_alias(self, alias, asfrom: bool = ..., **kwargs): ...  # type: ignore[override]
    def visit_substring_func(self, func, **kw): ...
    def visit_length_func(self, function, **kw): ...
    visit_char_length_func: Any
    def function_argspec(self, func, **kw): ...
    def default_from(self): ...
    def visit_sequence(self, seq, **kw): ...
    def get_select_precolumns(self, select, **kw): ...
    def limit_clause(self, select, **kw): ...
    def returning_clause(self, stmt, returning_cols): ...

class FBDDLCompiler(compiler.DDLCompiler):
    def visit_create_sequence(self, create): ...
    def visit_drop_sequence(self, drop): ...
    def visit_computed_column(self, generated): ...

class FBIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any
    illegal_initial_characters: Any
    def __init__(self, dialect) -> None: ...

class FBExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq, type_): ...

class FBDialect(default.DefaultDialect):
    name: str
    supports_statement_cache: bool
    max_identifier_length: int
    supports_sequences: bool
    sequences_optional: bool
    supports_default_values: bool
    postfetch_lastrowid: bool
    supports_native_boolean: bool
    requires_name_normalize: bool
    supports_empty_insert: bool
    statement_compiler: Any
    ddl_compiler: Any
    preparer: Any
    type_compiler: Any
    colspecs: Any
    ischema_names: Any
    construct_arguments: Any
    def __init__(self, *args, **kwargs) -> None: ...
    implicit_returning: Any
    def initialize(self, connection) -> None: ...
    def has_table(self, connection, table_name, schema: Incomplete | None = ...) -> bool: ...  # type: ignore[override]
    def has_sequence(self, connection, sequence_name, schema: Incomplete | None = ...) -> bool: ...  # type: ignore[override]
    def get_table_names(self, connection, schema: Incomplete | None = ..., **kw): ...
    def get_view_names(self, connection, schema: Incomplete | None = ..., **kw): ...
    def get_view_definition(self, connection, view_name, schema: Incomplete | None = ..., **kw): ...
    def get_pk_constraint(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_column_sequence(self, connection, table_name, column_name, schema: Incomplete | None = ..., **kw): ...
    def get_columns(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_foreign_keys(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_indexes(self, connection, table_name, schema: Incomplete | None = ..., **kw): ...
