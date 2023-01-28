from abc import ABCMeta
from typing import Any

from .base import MySQLCompiler, MySQLDialect, MySQLExecutionContext

mariadb_cpy_minimum_version: Any

class MySQLExecutionContext_mariadbconnector(MySQLExecutionContext):
    def create_server_side_cursor(self): ...
    def create_default_cursor(self): ...

class MySQLCompiler_mariadbconnector(MySQLCompiler, metaclass=ABCMeta): ...

class MySQLDialect_mariadbconnector(MySQLDialect):
    driver: str
    supports_statement_cache: bool
    supports_unicode_statements: bool
    encoding: str
    convert_unicode: bool
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_native_decimal: bool
    default_paramstyle: str
    statement_compiler: Any
    supports_server_side_cursors: bool
    paramstyle: str
    def __init__(self, **kwargs) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def is_disconnect(self, e, connection, cursor) -> bool: ...
    def create_connect_args(self, url): ...
    def do_begin_twophase(self, connection, xid) -> None: ...
    def do_prepare_twophase(self, connection, xid) -> None: ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...

dialect = MySQLDialect_mariadbconnector
