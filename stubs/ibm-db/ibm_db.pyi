from _typeshed import Self
from typing_extensions import final

ATTR_CASE: int
CASE_LOWER: int
CASE_NATURAL: int
CASE_UPPER: int
PARAM_FILE: int
QUOTED_LITERAL_REPLACEMENT_OFF: int
QUOTED_LITERAL_REPLACEMENT_ON: int
SQL_API_SQLROWCOUNT: int
SQL_ATTR_AUTOCOMMIT: int
SQL_ATTR_CURRENT_SCHEMA: int
SQL_ATTR_CURSOR_TYPE: int
SQL_ATTR_INFO_ACCTSTR: int
SQL_ATTR_INFO_APPLNAME: int
SQL_ATTR_INFO_PROGRAMNAME: int
SQL_ATTR_INFO_USERID: int
SQL_ATTR_INFO_WRKSTNNAME: int
SQL_ATTR_PARAMSET_SIZE: int
SQL_ATTR_PARAM_BIND_TYPE: int
SQL_ATTR_QUERY_TIMEOUT: int
SQL_ATTR_ROWCOUNT_PREFETCH: int
SQL_ATTR_TRUSTED_CONTEXT_PASSWORD: int
SQL_ATTR_TRUSTED_CONTEXT_USERID: int
SQL_ATTR_USE_TRUSTED_CONTEXT: int
SQL_ATTR_XML_DECLARATION: int
SQL_AUTOCOMMIT_OFF: int
SQL_AUTOCOMMIT_ON: int
SQL_BIGINT: int
SQL_BINARY: int
SQL_BIT: int
SQL_BLOB: int
SQL_BLOB_LOCATOR: int
SQL_BOOLEAN: int
SQL_CHAR: int
SQL_CLOB: int
SQL_CLOB_LOCATOR: int
SQL_CURSOR_DYNAMIC: int
SQL_CURSOR_FORWARD_ONLY: int
SQL_CURSOR_KEYSET_DRIVEN: int
SQL_CURSOR_STATIC: int
SQL_DBCLOB: int
SQL_DBCLOB_LOCATOR: int
SQL_DBMS_NAME: int
SQL_DBMS_VER: int
SQL_DECFLOAT: int
SQL_DECIMAL: int
SQL_DOUBLE: int
SQL_FALSE: int
SQL_FLOAT: int
SQL_GRAPHIC: int
SQL_INDEX_CLUSTERED: int
SQL_INDEX_OTHER: int
SQL_INTEGER: int
SQL_LONGVARBINARY: int
SQL_LONGVARCHAR: int
SQL_LONGVARGRAPHIC: int
SQL_NUMERIC: int
SQL_PARAM_BIND_BY_COLUMN: int
SQL_PARAM_INPUT: int
SQL_PARAM_INPUT_OUTPUT: int
SQL_PARAM_OUTPUT: int
SQL_REAL: int
SQL_ROWCOUNT_PREFETCH_OFF: int
SQL_ROWCOUNT_PREFETCH_ON: int
SQL_SMALLINT: int
SQL_TABLE_STAT: int
SQL_TINYINT: int
SQL_TRUE: int
SQL_TYPE_DATE: int
SQL_TYPE_TIME: int
SQL_TYPE_TIMESTAMP: int
SQL_VARBINARY: int
SQL_VARCHAR: int
SQL_VARGRAPHIC: int
SQL_WCHAR: int
SQL_WLONGVARCHAR: int
SQL_WVARCHAR: int
SQL_XML: int
USE_WCHAR: int
WCHAR_NO: int
WCHAR_YES: int

@final
class IBM_DBClientInfo:
    def __new__(cls: type[Self], *args: object, **kwargs: object) -> Self: ...
    APPL_CODEPAGE: str
    CONN_CODEPAGE: str
    DATA_SOURCE_NAME: str
    DRIVER_NAME: str
    DRIVER_ODBC_VER: str
    DRIVER_VER: str
    ODBC_SQL_CONFORMANCE: str
    ODBC_VER: str

@final
class IBM_DBConnection:
    def __new__(cls: type[Self], *args: object, **kwargs: object) -> Self: ...

@final
class IBM_DBServerInfo:
    def __new__(cls: type[Self], *args: object, **kwargs: object) -> Self: ...
    DBMS_NAME: str
    DBMS_VER: str
    DB_CODEPAGE: str
    DB_NAME: str
    DFT_ISOLATION: str
    IDENTIFIER_QUOTE_CHAR: str
    INST_NAME: str
    ISOLATION_OPTION: str
    KEYWORDS: str
    LIKE_ESCAPE_CLAUSE: bool
    MAX_COL_NAME_LEN: bytes
    MAX_IDENTIFIER_LEN: str
    MAX_INDEX_SIZE: bytes
    MAX_PROC_NAME_LEN: bytes
    MAX_ROW_SIZE: bytes
    MAX_SCHEMA_NAME_LEN: bytes
    MAX_STATEMENT_LEN: bytes
    MAX_TABLE_NAME_LEN: bytes
    NON_NULLABLE_COLUMNS: str
    PROCEDURES: bool
    SPECIAL_CHARS: str
    SQL_CONFORMANCE: str

@final
class IBM_DBStatement:
    def __new__(cls: type[Self], *args: object, **kwargs: object) -> Self: ...

def active(connection: IBM_DBConnection) -> bool: ...
def autocommit(connection: IBM_DBConnection, value: int | None = ...) -> int | bool: ...
def bind_param(
    stmt: IBM_DBStatement,
    parameter_number: int,
    variable: str,
    parameter_type: int | None = ...,
    data_type: int | None = ...,
    precision: int | None = ...,
    scale: int | None = ...,
    size: int | None = ...,
) -> bool: ...
def callproc(
    connection: IBM_DBConnection, procname: str, parameters: tuple[object, ...]
) -> IBM_DBStatement | tuple[object, ...] | None: ...
def check_function_support() -> bool: ...
def client_info(connection: IBM_DBConnection) -> IBM_DBClientInfo | bool: ...
def close(connection: IBM_DBConnection) -> bool: ...
def column_privileges(
    connection: IBM_DBConnection,
    qualifier: str | None = ...,
    schema: str | None = ...,
    table_name: str | None = ...,
    column_name: str | None = ...,
) -> IBM_DBStatement: ...
def columns(
    connection: IBM_DBConnection,
    qualifier: str | None = ...,
    schema: str | None = ...,
    table_name: str | None = ...,
    column_name: str | None = ...,
) -> IBM_DBStatement: ...
def commit(connection: IBM_DBConnection) -> bool: ...
def conn_error(connection: IBM_DBConnection | None = ...) -> str: ...
def conn_errormsg(connection: IBM_DBConnection | None = ...) -> str: ...
def conn_warn(connection: IBM_DBConnection | None = ...) -> str: ...
def connect(
    database: str, user: str, password: str, options: dict[int, int | str] | None = ..., replace_quoted_literal: int = ...
) -> IBM_DBConnection | None: ...
def createdb(connection: IBM_DBConnection, dbName: str, codeSet: str | None = ..., mode: str | None = ...) -> bool: ...
def createdbNX(connection: IBM_DBConnection, dbName: str, codeSet: str | None = ..., mode: str | None = ...) -> bool: ...
def cursor_type(stmt: IBM_DBStatement) -> int: ...
def dropdb(connection: IBM_DBConnection, dbName: str) -> bool: ...
def exec_immediate(connection: IBM_DBConnection, statement: str, options: dict[int, int]) -> IBM_DBStatement | bool: ...
def execute(stmt: IBM_DBStatement, parameters: tuple[object, ...] | None = ...) -> bool: ...
def execute_many(stmt: IBM_DBStatement, seq_of_parameters: tuple[object, ...]) -> int | None: ...
def fetch_assoc(stmt: IBM_DBStatement, row_number: int | None = ...) -> dict[str, object] | bool: ...
def fetch_both(stmt: IBM_DBStatement, row_number: int | None = ...) -> dict[int | str, object] | bool: ...
def fetch_row(stmt: IBM_DBStatement, row_number: int | None = ...) -> bool: ...
def fetch_tuple(stmt: IBM_DBStatement, row_number: int | None = ...) -> tuple[object, ...]: ...
def field_display_size(stmt: IBM_DBStatement, column: int | str) -> int | bool: ...
def field_name(stmt: IBM_DBStatement, column: int | str) -> str | bool: ...
def field_nullable(stmt: IBM_DBStatement, column: int | str) -> bool: ...
def field_num(stmt: IBM_DBStatement, column: int | str) -> str | bool: ...
def field_precision(stmt: IBM_DBStatement, column: int | str) -> int | bool: ...
def field_scale(stmt: IBM_DBStatement, column: int | str) -> int | bool: ...
def field_type(stmt: IBM_DBStatement, column: int | str) -> str | bool: ...
def field_width(stmt: IBM_DBStatement, column: int | str) -> int | bool: ...
def foreign_keys(
    connection: IBM_DBConnection,
    pk_qualifier: str,
    pk_schema: str,
    pk_table_name: str,
    fk_qualifier: str,
    fk_schema: str,
    fk_table_name: str,
) -> IBM_DBStatement: ...
def free_result(stmt: IBM_DBStatement) -> bool: ...
def free_stmt(stmt: IBM_DBStatement) -> bool: ...
def get_db_info(connection: IBM_DBConnection, option: int) -> str | bool: ...
def get_last_serial_value(stmt: IBM_DBStatement) -> str | bool: ...
def get_num_result(stmt: IBM_DBStatement) -> int | bool: ...
def get_option(resc: IBM_DBConnection | IBM_DBStatement, options: int, type: int) -> object: ...
def next_result(stmt: IBM_DBStatement) -> IBM_DBStatement | bool: ...
def num_fields(stmt: IBM_DBStatement) -> int | bool: ...
def num_rows(stmt: IBM_DBStatement) -> int: ...
def pconnect(
    database: str, username: str, password: str, options: dict[int, int | str] | None = ...
) -> IBM_DBConnection | None: ...
def prepare(connection: IBM_DBConnection, statement: str, options: dict[int, int | str] | None) -> IBM_DBStatement | bool: ...
def primary_keys(connection: IBM_DBConnection, qualifier: str | None, schema: str | None, table_name: str) -> IBM_DBStatement: ...
def procedure_columns(
    connection: IBM_DBConnection, qualifier: str | None, schema: str, procedure: str, parameter: str | None
) -> IBM_DBStatement: ...
def procedures(connection: IBM_DBConnection, qualifier: str | None, schema: str, procedure: str) -> IBM_DBStatement: ...
def recreatedb(connection: IBM_DBConnection, dbName: str, codeSet: str | None = ..., mode: str | None = ...) -> bool | None: ...
def result(stmt: IBM_DBStatement, column: int | str) -> object | None: ...
def rollback(connection: IBM_DBConnection) -> bool: ...
def server_info(connection: IBM_DBConnection) -> IBM_DBServerInfo | bool: ...
def set_option(resc: IBM_DBConnection | IBM_DBStatement, options: dict[int, int | str], type: int) -> bool: ...
def special_columns(
    connection: IBM_DBConnection, qualifier: str | None, schema: str, table_name: str, scope: int
) -> IBM_DBStatement: ...
def statistics(
    connection: IBM_DBConnection, qualifier: str | None, schema: str | None, table_name: str, unique: bool
) -> IBM_DBStatement: ...
def stmt_error(stmt: IBM_DBStatement | None = ...) -> str: ...
def stmt_errormsg(stmt: IBM_DBStatement | None = ...) -> str: ...
def stmt_warn(connection: IBM_DBConnection, qualifier: str | None, schema: str, table_name: str) -> IBM_DBStatement: ...
def table_privileges(connection: IBM_DBConnection, qualifier: str | None, schema: str, table_name: str) -> IBM_DBStatement: ...
def tables(
    connection: IBM_DBConnection, qualifier: str | None, schema: str, table_name: str, table_type: str | None
) -> IBM_DBStatement: ...
