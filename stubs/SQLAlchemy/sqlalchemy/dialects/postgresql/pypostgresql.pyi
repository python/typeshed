from typing import Any

from ... import types as sqltypes
from .base import PGDialect, PGExecutionContext

class PGNumeric(sqltypes.Numeric):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class PGExecutionContext_pypostgresql(PGExecutionContext): ...

class PGDialect_pypostgresql(PGDialect):
    driver: str
    supports_statement_cache: bool
    supports_unicode_statements: bool
    supports_unicode_binds: bool
    description_encoding: Any
    default_paramstyle: str
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    execution_ctx_cls: Any
    colspecs: Any
    @classmethod
    def dbapi(cls): ...
    def dbapi_exception_translation_map(self): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect = PGDialect_pypostgresql
