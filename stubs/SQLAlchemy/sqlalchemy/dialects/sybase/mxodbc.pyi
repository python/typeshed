from typing import Any

from sqlalchemy.connectors.mxodbc import MxODBCConnector
from sqlalchemy.dialects.sybase.base import SybaseDialect, SybaseExecutionContext

class SybaseExecutionContext_mxodbc(SybaseExecutionContext): ...

class SybaseDialect_mxodbc(MxODBCConnector, SybaseDialect):
    execution_ctx_cls: Any
    supports_statement_cache: bool

dialect = SybaseDialect_mxodbc
