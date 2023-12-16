import sys
from _typeshed import ReadableBuffer, StrOrBytesPath
from collections.abc import Callable
from sqlite3 import (
    Connection as Connection,
    Cursor as Cursor,
    DatabaseError as DatabaseError,
    DataError as DataError,
    Error as Error,
    IntegrityError as IntegrityError,
    InterfaceError as InterfaceError,
    InternalError as InternalError,
    NotSupportedError as NotSupportedError,
    OperationalError as OperationalError,
    PrepareProtocol as PrepareProtocol,
    ProgrammingError as ProgrammingError,
    Row as Row,
    Warning as Warning,
)
from typing import Any, TypeVar, overload
from typing_extensions import TypeAlias

if sys.version_info >= (3, 11):
    from sqlite3 import Blob as Blob

if sys.version_info < (3, 8):
    from sqlite3 import Cache as Cache, Statement as Statement

_T = TypeVar("_T")
_SqliteData: TypeAlias = str | ReadableBuffer | int | float | None
_Adapter: TypeAlias = Callable[[_T], _SqliteData]
_Converter: TypeAlias = Callable[[bytes], Any]

PARSE_COLNAMES: int
PARSE_DECLTYPES: int
SQLITE_ALTER_TABLE: int
SQLITE_ANALYZE: int
SQLITE_ATTACH: int
SQLITE_CREATE_INDEX: int
SQLITE_CREATE_TABLE: int
SQLITE_CREATE_TEMP_INDEX: int
SQLITE_CREATE_TEMP_TABLE: int
SQLITE_CREATE_TEMP_TRIGGER: int
SQLITE_CREATE_TEMP_VIEW: int
SQLITE_CREATE_TRIGGER: int
SQLITE_CREATE_VIEW: int
SQLITE_CREATE_VTABLE: int
SQLITE_DELETE: int
SQLITE_DENY: int
SQLITE_DETACH: int
SQLITE_DONE: int
SQLITE_DROP_INDEX: int
SQLITE_DROP_TABLE: int
SQLITE_DROP_TEMP_INDEX: int
SQLITE_DROP_TEMP_TABLE: int
SQLITE_DROP_TEMP_TRIGGER: int
SQLITE_DROP_TEMP_VIEW: int
SQLITE_DROP_TRIGGER: int
SQLITE_DROP_VIEW: int
SQLITE_DROP_VTABLE: int
SQLITE_FUNCTION: int
SQLITE_IGNORE: int
SQLITE_INSERT: int
SQLITE_OK: int
SQLITE_PRAGMA: int
SQLITE_READ: int
SQLITE_RECURSIVE: int
SQLITE_REINDEX: int
SQLITE_SAVEPOINT: int
SQLITE_SELECT: int
SQLITE_TRANSACTION: int
SQLITE_UPDATE: int
adapters: dict[tuple[type[Any], type[Any]], _Adapter[Any]]
converters: dict[str, _Converter]
sqlite_version: str
if sys.version_info < (3, 12):
    version: str

if sys.version_info >= (3, 12):
    LEGACY_TRANSACTION_CONTROL: int
    SQLITE_DBCONFIG_DEFENSIVE: int
    SQLITE_DBCONFIG_DQS_DDL: int
    SQLITE_DBCONFIG_DQS_DML: int
    SQLITE_DBCONFIG_ENABLE_FKEY: int
    SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER: int
    SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION: int
    SQLITE_DBCONFIG_ENABLE_QPSG: int
    SQLITE_DBCONFIG_ENABLE_TRIGGER: int
    SQLITE_DBCONFIG_ENABLE_VIEW: int
    SQLITE_DBCONFIG_LEGACY_ALTER_TABLE: int
    SQLITE_DBCONFIG_LEGACY_FILE_FORMAT: int
    SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE: int
    SQLITE_DBCONFIG_RESET_DATABASE: int
    SQLITE_DBCONFIG_TRIGGER_EQP: int
    SQLITE_DBCONFIG_TRUSTED_SCHEMA: int
    SQLITE_DBCONFIG_WRITABLE_SCHEMA: int

if sys.version_info >= (3, 11):
    SQLITE_ABORT: int
    SQLITE_ABORT_ROLLBACK: int
    SQLITE_AUTH: int
    SQLITE_AUTH_USER: int
    SQLITE_BUSY: int
    SQLITE_BUSY_RECOVERY: int
    SQLITE_BUSY_SNAPSHOT: int
    SQLITE_BUSY_TIMEOUT: int
    SQLITE_CANTOPEN: int
    SQLITE_CANTOPEN_CONVPATH: int
    SQLITE_CANTOPEN_DIRTYWAL: int
    SQLITE_CANTOPEN_FULLPATH: int
    SQLITE_CANTOPEN_ISDIR: int
    SQLITE_CANTOPEN_NOTEMPDIR: int
    SQLITE_CANTOPEN_SYMLINK: int
    SQLITE_CONSTRAINT: int
    SQLITE_CONSTRAINT_CHECK: int
    SQLITE_CONSTRAINT_COMMITHOOK: int
    SQLITE_CONSTRAINT_FOREIGNKEY: int
    SQLITE_CONSTRAINT_FUNCTION: int
    SQLITE_CONSTRAINT_NOTNULL: int
    SQLITE_CONSTRAINT_PINNED: int
    SQLITE_CONSTRAINT_PRIMARYKEY: int
    SQLITE_CONSTRAINT_ROWID: int
    SQLITE_CONSTRAINT_TRIGGER: int
    SQLITE_CONSTRAINT_UNIQUE: int
    SQLITE_CONSTRAINT_VTAB: int
    SQLITE_CORRUPT: int
    SQLITE_CORRUPT_INDEX: int
    SQLITE_CORRUPT_SEQUENCE: int
    SQLITE_CORRUPT_VTAB: int
    SQLITE_EMPTY: int
    SQLITE_ERROR: int
    SQLITE_ERROR_MISSING_COLLSEQ: int
    SQLITE_ERROR_RETRY: int
    SQLITE_ERROR_SNAPSHOT: int
    SQLITE_FORMAT: int
    SQLITE_FULL: int
    SQLITE_INTERNAL: int
    SQLITE_INTERRUPT: int
    SQLITE_IOERR: int
    SQLITE_IOERR_ACCESS: int
    SQLITE_IOERR_AUTH: int
    SQLITE_IOERR_BEGIN_ATOMIC: int
    SQLITE_IOERR_BLOCKED: int
    SQLITE_IOERR_CHECKRESERVEDLOCK: int
    SQLITE_IOERR_CLOSE: int
    SQLITE_IOERR_COMMIT_ATOMIC: int
    SQLITE_IOERR_CONVPATH: int
    SQLITE_IOERR_CORRUPTFS: int
    SQLITE_IOERR_DATA: int
    SQLITE_IOERR_DELETE: int
    SQLITE_IOERR_DELETE_NOENT: int
    SQLITE_IOERR_DIR_CLOSE: int
    SQLITE_IOERR_DIR_FSYNC: int
    SQLITE_IOERR_FSTAT: int
    SQLITE_IOERR_FSYNC: int
    SQLITE_IOERR_GETTEMPPATH: int
    SQLITE_IOERR_LOCK: int
    SQLITE_IOERR_MMAP: int
    SQLITE_IOERR_NOMEM: int
    SQLITE_IOERR_RDLOCK: int
    SQLITE_IOERR_READ: int
    SQLITE_IOERR_ROLLBACK_ATOMIC: int
    SQLITE_IOERR_SEEK: int
    SQLITE_IOERR_SHMLOCK: int
    SQLITE_IOERR_SHMMAP: int
    SQLITE_IOERR_SHMOPEN: int
    SQLITE_IOERR_SHMSIZE: int
    SQLITE_IOERR_SHORT_READ: int
    SQLITE_IOERR_TRUNCATE: int
    SQLITE_IOERR_UNLOCK: int
    SQLITE_IOERR_VNODE: int
    SQLITE_IOERR_WRITE: int
    SQLITE_LIMIT_ATTACHED: int
    SQLITE_LIMIT_COLUMN: int
    SQLITE_LIMIT_COMPOUND_SELECT: int
    SQLITE_LIMIT_EXPR_DEPTH: int
    SQLITE_LIMIT_FUNCTION_ARG: int
    SQLITE_LIMIT_LENGTH: int
    SQLITE_LIMIT_LIKE_PATTERN_LENGTH: int
    SQLITE_LIMIT_SQL_LENGTH: int
    SQLITE_LIMIT_TRIGGER_DEPTH: int
    SQLITE_LIMIT_VARIABLE_NUMBER: int
    SQLITE_LIMIT_VDBE_OP: int
    SQLITE_LIMIT_WORKER_THREADS: int
    SQLITE_LOCKED: int
    SQLITE_LOCKED_SHAREDCACHE: int
    SQLITE_LOCKED_VTAB: int
    SQLITE_MISMATCH: int
    SQLITE_MISUSE: int
    SQLITE_NOLFS: int
    SQLITE_NOMEM: int
    SQLITE_NOTADB: int
    SQLITE_NOTFOUND: int
    SQLITE_NOTICE: int
    SQLITE_NOTICE_RECOVER_ROLLBACK: int
    SQLITE_NOTICE_RECOVER_WAL: int
    SQLITE_OK_LOAD_PERMANENTLY: int
    SQLITE_OK_SYMLINK: int
    SQLITE_PERM: int
    SQLITE_PROTOCOL: int
    SQLITE_RANGE: int
    SQLITE_READONLY: int
    SQLITE_READONLY_CANTINIT: int
    SQLITE_READONLY_CANTLOCK: int
    SQLITE_READONLY_DBMOVED: int
    SQLITE_READONLY_DIRECTORY: int
    SQLITE_READONLY_RECOVERY: int
    SQLITE_READONLY_ROLLBACK: int
    SQLITE_ROW: int
    SQLITE_SCHEMA: int
    SQLITE_TOOBIG: int
    SQLITE_WARNING: int
    SQLITE_WARNING_AUTOINDEX: int
    threadsafety: int

@overload
def adapt(__obj: Any, __proto: Any) -> Any: ...
@overload
def adapt(__obj: Any, __proto: Any, __alt: _T) -> Any | _T: ...
def complete_statement(statement: str) -> bool: ...
def connect(
    database: StrOrBytesPath,
    timeout: float = ...,
    detect_types: int = ...,
    isolation_level: str | None = ...,
    check_same_thread: bool = ...,
    factory: type[Connection] | None = ...,
    cached_statements: int = ...,
    uri: bool = ...,
) -> Connection: ...
def enable_callback_tracebacks(__enable: bool) -> None: ...

if sys.version_info < (3, 12):
    # takes a pos-or-keyword argument because there is a C wrapper
    def enable_shared_cache(do_enable: int) -> None: ...

if sys.version_info >= (3, 10):
    def register_adapter(__type: type[_T], __adapter: _Adapter[_T]) -> None: ...
    def register_converter(__typename: str, __converter: _Converter) -> None: ...

else:
    def register_adapter(__type: type[_T], __caster: _Adapter[_T]) -> None: ...
    def register_converter(__name: str, __converter: _Converter) -> None: ...

if sys.version_info < (3, 10):
    OptimizedUnicode = str
