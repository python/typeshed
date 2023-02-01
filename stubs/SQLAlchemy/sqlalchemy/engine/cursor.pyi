from _typeshed import Incomplete
from abc import ABCMeta
from typing import Any

from ..sql.compiler import RM_NAME as RM_NAME, RM_OBJECTS as RM_OBJECTS, RM_RENDERED_NAME as RM_RENDERED_NAME, RM_TYPE as RM_TYPE
from ..util.langhelpers import memoized_property
from .result import Result, ResultMetaData
from .row import LegacyRow

MD_INDEX: int
MD_RESULT_MAP_INDEX: int
MD_OBJECTS: int
MD_LOOKUP_KEY: int
MD_RENDERED_NAME: int
MD_PROCESSOR: int
MD_UNTRANSLATED: int

class CursorResultMetaData(ResultMetaData):
    returns_rows: bool
    case_sensitive: Any
    def __init__(self, parent, cursor_description) -> None: ...

class LegacyCursorResultMetaData(CursorResultMetaData): ...

class ResultFetchStrategy:
    alternate_cursor_description: Any
    def soft_close(self, result, dbapi_cursor) -> None: ...
    def hard_close(self, result, dbapi_cursor) -> None: ...
    def yield_per(self, result, dbapi_cursor, num) -> None: ...
    def fetchone(self, result, dbapi_cursor, hard_close: bool = ...) -> None: ...
    def fetchmany(self, result, dbapi_cursor, size: Incomplete | None = ...) -> None: ...
    def fetchall(self, result) -> None: ...
    def handle_exception(self, result, dbapi_cursor, err) -> None: ...

class NoCursorFetchStrategy(ResultFetchStrategy):
    def soft_close(self, result, dbapi_cursor) -> None: ...
    def hard_close(self, result, dbapi_cursor) -> None: ...
    def fetchone(self, result, dbapi_cursor, hard_close: bool = ...): ...
    def fetchmany(self, result, dbapi_cursor, size: Incomplete | None = ...): ...
    def fetchall(self, result, dbapi_cursor): ...

class NoCursorDQLFetchStrategy(NoCursorFetchStrategy): ...
class NoCursorDMLFetchStrategy(NoCursorFetchStrategy): ...

class CursorFetchStrategy(ResultFetchStrategy):
    def soft_close(self, result, dbapi_cursor) -> None: ...
    def hard_close(self, result, dbapi_cursor) -> None: ...
    def handle_exception(self, result, dbapi_cursor, err) -> None: ...
    def yield_per(self, result, dbapi_cursor, num) -> None: ...
    def fetchone(self, result, dbapi_cursor, hard_close: bool = ...): ...
    def fetchmany(self, result, dbapi_cursor, size: Incomplete | None = ...): ...
    def fetchall(self, result, dbapi_cursor): ...

class BufferedRowCursorFetchStrategy(CursorFetchStrategy):
    def __init__(
        self, dbapi_cursor, execution_options, growth_factor: int = ..., initial_buffer: Incomplete | None = ...
    ) -> None: ...
    @classmethod
    def create(cls, result): ...
    def yield_per(self, result, dbapi_cursor, num) -> None: ...
    def soft_close(self, result, dbapi_cursor) -> None: ...
    def hard_close(self, result, dbapi_cursor) -> None: ...
    def fetchone(self, result, dbapi_cursor, hard_close: bool = ...): ...
    def fetchmany(self, result, dbapi_cursor, size: Incomplete | None = ...): ...
    def fetchall(self, result, dbapi_cursor): ...

class FullyBufferedCursorFetchStrategy(CursorFetchStrategy):
    alternate_cursor_description: Any
    def __init__(
        self, dbapi_cursor, alternate_description: Incomplete | None = ..., initial_buffer: Incomplete | None = ...
    ) -> None: ...
    def yield_per(self, result, dbapi_cursor, num) -> None: ...
    def soft_close(self, result, dbapi_cursor) -> None: ...
    def hard_close(self, result, dbapi_cursor) -> None: ...
    def fetchone(self, result, dbapi_cursor, hard_close: bool = ...): ...
    def fetchmany(self, result, dbapi_cursor, size: Incomplete | None = ...): ...
    def fetchall(self, result, dbapi_cursor): ...

class _NoResultMetaData(ResultMetaData):
    returns_rows: bool
    @property
    def keys(self) -> None: ...

class _LegacyNoResultMetaData(_NoResultMetaData):
    @property
    def keys(self): ...

class BaseCursorResult:
    out_parameters: Any
    closed: bool
    context: Any
    dialect: Any
    cursor: Any
    cursor_strategy: Any
    connection: Any
    def __init__(self, context, cursor_strategy, cursor_description): ...
    @property
    def inserted_primary_key_rows(self): ...
    @property
    def inserted_primary_key(self): ...
    def last_updated_params(self): ...
    def last_inserted_params(self): ...
    @property
    def returned_defaults_rows(self): ...
    @property
    def returned_defaults(self): ...
    def lastrow_has_defaults(self): ...
    def postfetch_cols(self): ...
    def prefetch_cols(self): ...
    def supports_sane_rowcount(self): ...
    def supports_sane_multi_rowcount(self): ...
    @memoized_property
    def rowcount(self): ...
    @property
    def lastrowid(self): ...
    @property
    def returns_rows(self): ...
    @property
    def is_insert(self): ...

class CursorResult(BaseCursorResult, Result):
    def merge(self, *others): ...
    def close(self) -> None: ...

class LegacyCursorResult(CursorResult):
    def close(self) -> None: ...

ResultProxy = LegacyCursorResult

class BufferedRowResultProxy(ResultProxy): ...
class FullyBufferedResultProxy(ResultProxy): ...
class BufferedColumnRow(LegacyRow, metaclass=ABCMeta): ...
class BufferedColumnResultProxy(ResultProxy): ...
