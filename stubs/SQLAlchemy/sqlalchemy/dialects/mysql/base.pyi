from _typeshed import Incomplete, Unused
from abc import ABCMeta
from typing import Any

from ...engine import default
from ...sql import compiler
from ...types import BINARY as BINARY, BLOB as BLOB, BOOLEAN as BOOLEAN, DATE as DATE, VARBINARY as VARBINARY
from .enumerated import ENUM as ENUM, SET as SET
from .json import JSON as JSON
from .types import (
    BIGINT as BIGINT,
    BIT as BIT,
    CHAR as CHAR,
    DATETIME as DATETIME,
    DECIMAL as DECIMAL,
    DOUBLE as DOUBLE,
    FLOAT as FLOAT,
    INTEGER as INTEGER,
    LONGBLOB as LONGBLOB,
    LONGTEXT as LONGTEXT,
    MEDIUMBLOB as MEDIUMBLOB,
    MEDIUMINT as MEDIUMINT,
    MEDIUMTEXT as MEDIUMTEXT,
    NCHAR as NCHAR,
    NUMERIC as NUMERIC,
    NVARCHAR as NVARCHAR,
    REAL as REAL,
    SMALLINT as SMALLINT,
    TEXT as TEXT,
    TIME as TIME,
    TIMESTAMP as TIMESTAMP,
    TINYBLOB as TINYBLOB,
    TINYINT as TINYINT,
    TINYTEXT as TINYTEXT,
    VARCHAR as VARCHAR,
    YEAR as YEAR,
)

AUTOCOMMIT_RE: Any
SET_RE: Any
MSTime = TIME
MSSet = SET
MSEnum = ENUM
MSLongBlob = LONGBLOB
MSMediumBlob = MEDIUMBLOB
MSTinyBlob = TINYBLOB
MSBlob = BLOB
MSBinary = BINARY
MSVarBinary = VARBINARY
MSNChar = NCHAR
MSNVarChar = NVARCHAR
MSChar = CHAR
MSString = VARCHAR
MSLongText = LONGTEXT
MSMediumText = MEDIUMTEXT
MSTinyText = TINYTEXT
MSText = TEXT
MSYear = YEAR
MSTimeStamp = TIMESTAMP
MSBit = BIT
MSSmallInteger = SMALLINT
MSTinyInteger = TINYINT
MSMediumInteger = MEDIUMINT
MSBigInteger = BIGINT
MSNumeric = NUMERIC
MSDecimal = DECIMAL
MSDouble = DOUBLE
MSReal = REAL
MSFloat = FLOAT
MSInteger = INTEGER
colspecs: Any
ischema_names: Any

class MySQLExecutionContext(default.DefaultExecutionContext):
    def should_autocommit_text(self, statement): ...
    def create_server_side_cursor(self): ...
    def fire_sequence(self, seq, type_): ...

class MySQLCompiler(compiler.SQLCompiler, metaclass=ABCMeta):
    render_table_with_column_in_update_from: bool
    extract_map: Any
    def default_from(self): ...
    def visit_random_func(self, fn, **kw): ...
    def visit_sequence(self, seq, **kw): ...
    def visit_sysdate_func(self, fn, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_on_duplicate_key_update(self, on_duplicate, **kw): ...
    def visit_concat_op_binary(self, binary, operator, **kw): ...
    def visit_mysql_match(self, element, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def get_from_hint_text(self, table, text): ...
    def visit_typeclause(self, typeclause, type_: Incomplete | None = None, **kw): ...
    def visit_cast(self, cast, **kw): ...
    def render_literal_value(self, value, type_): ...
    def visit_true(self, element, **kw): ...
    def visit_false(self, element, **kw): ...
    def get_select_precolumns(self, select, **kw): ...
    def visit_join(self, join, asfrom: bool = False, from_linter: Incomplete | None = None, **kwargs): ...
    def for_update_clause(self, select, **kw): ...
    def limit_clause(self, select, **kw): ...
    def update_limit_clause(self, update_stmt): ...
    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw): ...
    def update_from_clause(
        self, update_stmt: Unused, from_table: Unused, extra_froms: Unused, from_hints: Unused, **kw: Unused
    ) -> str | None: ...
    def delete_table_clause(self, delete_stmt, from_table, extra_froms): ...
    def delete_extra_from_clause(self, delete_stmt, from_table, extra_froms, from_hints, **kw): ...
    def visit_empty_set_expr(self, element_types): ...
    def visit_is_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_is_not_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw): ...

class MySQLDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kw): ...
    def post_create_table(self, table): ...
    def visit_create_index(self, create, **kw): ...
    def visit_primary_key_constraint(self, constraint): ...
    def visit_drop_index(self, drop): ...
    def visit_drop_constraint(self, drop): ...
    def define_constraint_match(self, constraint): ...
    def visit_set_table_comment(self, create): ...
    def visit_drop_table_comment(self, create): ...
    def visit_set_column_comment(self, create): ...

class MySQLTypeCompiler(compiler.GenericTypeCompiler):
    def visit_NUMERIC(self, type_, **kw): ...
    def visit_DECIMAL(self, type_, **kw): ...
    def visit_DOUBLE(self, type_, **kw): ...
    def visit_REAL(self, type_, **kw): ...
    def visit_FLOAT(self, type_, **kw): ...
    def visit_INTEGER(self, type_, **kw): ...
    def visit_BIGINT(self, type_, **kw): ...
    def visit_MEDIUMINT(self, type_, **kw): ...
    def visit_TINYINT(self, type_, **kw): ...
    def visit_SMALLINT(self, type_, **kw): ...
    def visit_BIT(self, type_, **kw): ...
    def visit_DATETIME(self, type_, **kw): ...
    def visit_DATE(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_YEAR(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_TINYTEXT(self, type_, **kw): ...
    def visit_MEDIUMTEXT(self, type_, **kw): ...
    def visit_LONGTEXT(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_NVARCHAR(self, type_, **kw): ...
    def visit_NCHAR(self, type_, **kw): ...
    def visit_VARBINARY(self, type_, **kw): ...
    def visit_JSON(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_enum(self, type_, **kw): ...
    def visit_BLOB(self, type_, **kw): ...
    def visit_TINYBLOB(self, type_, **kw): ...
    def visit_MEDIUMBLOB(self, type_, **kw): ...
    def visit_LONGBLOB(self, type_, **kw): ...
    def visit_ENUM(self, type_, **kw): ...
    def visit_SET(self, type_, **kw): ...
    def visit_BOOLEAN(self, type_, **kw): ...

class MySQLIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any
    def __init__(self, dialect, server_ansiquotes: bool = False, **kw) -> None: ...

class MariaDBIdentifierPreparer(MySQLIdentifierPreparer):
    reserved_words: Any

class MySQLDialect(default.DefaultDialect):
    logger: Any
    name: str
    supports_statement_cache: bool
    supports_alter: bool
    supports_native_boolean: bool
    max_identifier_length: int
    max_index_name_length: int
    max_constraint_name_length: int
    supports_native_enum: bool
    supports_sequences: bool
    sequences_optional: bool
    supports_for_update_of: bool
    supports_default_values: bool
    supports_default_metavalue: bool
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_multivalues_insert: bool
    supports_comments: bool
    inline_comments: bool
    default_paramstyle: str
    colspecs: Any
    cte_follows_insert: bool
    statement_compiler: Any
    ddl_compiler: Any
    type_compiler: Any
    ischema_names: Any
    preparer: Any
    is_mariadb: bool
    construct_arguments: Any
    isolation_level: Any
    def __init__(
        self,
        isolation_level: Incomplete | None = None,
        json_serializer: Incomplete | None = None,
        json_deserializer: Incomplete | None = None,
        is_mariadb: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def on_connect(self): ...
    def set_isolation_level(self, connection, level) -> None: ...
    def get_isolation_level(self, connection): ...
    def do_begin_twophase(self, connection, xid) -> None: ...
    def do_prepare_twophase(self, connection, xid) -> None: ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = True, recover: bool = False) -> None: ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = True, recover: bool = False) -> None: ...
    def do_recover_twophase(self, connection): ...
    def is_disconnect(self, e, connection, cursor) -> bool: ...
    def has_table(self, connection, table_name, schema: Incomplete | None = None) -> bool: ...  # type: ignore[override]
    def has_sequence(self, connection, sequence_name, schema: Incomplete | None = None) -> bool: ...  # type: ignore[override]
    def get_sequence_names(self, connection, schema: Incomplete | None = None, **kw): ...
    identifier_preparer: Any
    def initialize(self, connection) -> None: ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, schema: Incomplete | None = None, **kw): ...
    def get_view_names(self, connection, schema: Incomplete | None = None, **kw): ...
    def get_table_options(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_columns(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_pk_constraint(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_foreign_keys(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_check_constraints(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_table_comment(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_indexes(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_unique_constraints(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_view_definition(self, connection, view_name, schema: Incomplete | None = None, **kw): ...

class _DecodingRow:
    rowproxy: Any
    charset: Any
    def __init__(self, rowproxy, charset) -> None: ...
    def __getitem__(self, index): ...
    def __getattr__(self, attr: str): ...
