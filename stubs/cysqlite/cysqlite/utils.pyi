from typing import Literal

from ._cysqlite import Connection

def slow_query_log(conn: Connection, threshold_ms: int = 50, logger=None, level=30, expand_sql: bool = True) -> Literal[True]: ...
