# Stubs for sqlalchemy.dialects.mysql.pymysql (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .mysqldb import MySQLDialect_mysqldb as MySQLDialect_mysqldb
from ...util import langhelpers as langhelpers, py3k as py3k

class MySQLDialect_pymysql(MySQLDialect_mysqldb):
    driver = ...  # type: str
    description_encoding = ...  # type: Any
    supports_unicode_statements = ...  # type: bool
    supports_unicode_binds = ...  # type: bool
    server_side_cursors = ...  # type: Any
    def __init__(self, server_side_cursors: bool = ..., **kwargs) -> None: ...
    def supports_server_side_cursors(self): ...
    @classmethod
    def dbapi(cls): ...

dialect = ...  # type: Any
