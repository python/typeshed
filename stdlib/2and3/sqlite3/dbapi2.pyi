# Filip Hron <filip.hron@gmail.com>
# based heavily on Andrey Vlasovskikh's python-skeletons https://github.com/JetBrains/python-skeletons/blob/master/sqlite3.py

import sys
from typing import Any, Callable, Iterable, Iterator, List, Optional, Text, Tuple, Type, TypeVar, Union
from datetime import date, time, datetime

_T = TypeVar('_T')

paramstyle: str
threadsafety: int
apilevel: str
Date = date
Time = time
Timestamp = datetime

def DateFromTicks(ticks): ...
def TimeFromTicks(ticks): ...
def TimestampFromTicks(ticks): ...

version_info: str
sqlite_version_info: Tuple[int, int, int]
if sys.version_info >= (3,):
    Binary = memoryview
else:
    Binary = buffer

def register_adapters_and_converters(): ...

# The remaining definitions are imported from _sqlite3.

PARSE_COLNAMES = ...  # type: int
PARSE_DECLTYPES = ...  # type: int
SQLITE_ALTER_TABLE = ...  # type: int
SQLITE_ANALYZE = ...  # type: int
SQLITE_ATTACH = ...  # type: int
SQLITE_CREATE_INDEX = ...  # type: int
SQLITE_CREATE_TABLE = ...  # type: int
SQLITE_CREATE_TEMP_INDEX = ...  # type: int
SQLITE_CREATE_TEMP_TABLE = ...  # type: int
SQLITE_CREATE_TEMP_TRIGGER = ...  # type: int
SQLITE_CREATE_TEMP_VIEW = ...  # type: int
SQLITE_CREATE_TRIGGER = ...  # type: int
SQLITE_CREATE_VIEW = ...  # type: int
SQLITE_DELETE = ...  # type: int
SQLITE_DENY = ...  # type: int
SQLITE_DETACH = ...  # type: int
SQLITE_DROP_INDEX = ...  # type: int
SQLITE_DROP_TABLE = ...  # type: int
SQLITE_DROP_TEMP_INDEX = ...  # type: int
SQLITE_DROP_TEMP_TABLE = ...  # type: int
SQLITE_DROP_TEMP_TRIGGER = ...  # type: int
SQLITE_DROP_TEMP_VIEW = ...  # type: int
SQLITE_DROP_TRIGGER = ...  # type: int
SQLITE_DROP_VIEW = ...  # type: int
SQLITE_IGNORE = ...  # type: int
SQLITE_INSERT = ...  # type: int
SQLITE_OK = ...  # type: int
SQLITE_PRAGMA = ...  # type: int
SQLITE_READ = ...  # type: int
SQLITE_REINDEX = ...  # type: int
SQLITE_SELECT = ...  # type: int
SQLITE_TRANSACTION = ...  # type: int
SQLITE_UPDATE = ...  # type: int
adapters = ...  # type: Any
converters = ...  # type: Any
sqlite_version = ...  # type: str
version = ...  # type: str

# TODO: adapt needs to get probed
def adapt(obj, protocol, alternate): ...
def complete_statement(sql: str) -> bool: ...
if sys.version_info >= (3, 4):
    def connect(database: Union[bytes, Text],
                timeout: float = ...,
                detect_types: int = ...,
                isolation_level: Optional[str] = ...,
                check_same_thread: bool = ...,
                factory: Optional[Type[Connection]] = ...,
                cached_statements: int = ...,
                uri: bool = ...) -> Connection: ...
else:
    def connect(database: Union[bytes, Text],
                timeout: float = ...,
                detect_types: int = ...,
                isolation_level: Optional[str] = ...,
                check_same_thread: bool = ...,
                factory: Optional[Type[Connection]] = ...,
                cached_statements: int = ...) -> Connection: ...
def enable_callback_tracebacks(flag: bool) -> None: ...
def enable_shared_cache(do_enable: int) -> None: ...
def register_adapter(type: Type[_T], callable: Callable[[_T], Union[int, float, str, bytes]]) -> None: ...
def register_converter(typename: str, callable: Callable[[bytes], Any]) -> None: ...

class Cache(object):
    def __init__(self, *args, **kwargs) -> None: ...
    def display(self, *args, **kwargs) -> None: ...
    def get(self, *args, **kwargs) -> None: ...

class Connection(object):
    DataError = ...  # type: Any
    DatabaseError = ...  # type: Any
    Error = ...  # type: Any
    IntegrityError = ...  # type: Any
    InterfaceError = ...  # type: Any
    InternalError = ...  # type: Any
    NotSupportedError = ...  # type: Any
    OperationalError = ...  # type: Any
    ProgrammingError = ...  # type: Any
    Warning = ...  # type: Any
    in_transaction = ...  # type: Any
    isolation_level = ...  # type: Any
    row_factory = ...  # type: Any
    text_factory = ...  # type: Any
    total_changes = ...  # type: Any
    def __init__(self, *args, **kwargs): ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def create_aggregate(self, name: str, num_params: int, aggregate_class: type) -> None: ...
    def create_collation(self, name: str, callable: Any) -> None: ...
    def create_function(self, name: str, num_params: int, func: Any) -> None: ...
    def cursor(self, cursorClass: Optional[type] = ...) -> Cursor: ...
    def execute(self, sql: str, parameters: Iterable = ...) -> Cursor: ...
    # TODO: please check in executemany() if seq_of_parameters type is possible like this
    def executemany(self, sql: str, seq_of_parameters: Iterable[Iterable]) -> Cursor: ...
    def executescript(self, sql_script: Union[bytes, Text]) -> Cursor: ...
    def interrupt(self, *args, **kwargs) -> None: ...
    def iterdump(self, *args, **kwargs) -> None: ...
    def rollback(self, *args, **kwargs) -> None: ...
    # TODO: set_authorizer(authorzer_callback)
    # see https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.set_authorizer
    # returns [SQLITE_OK, SQLITE_DENY, SQLITE_IGNORE] so perhaps int
    def set_authorizer(self, *args, **kwargs) -> None: ...
    # set_progress_handler(handler, n) -> see https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.set_progress_handler
    def set_progress_handler(self, *args, **kwargs) -> None: ...
    def set_trace_callback(self, *args, **kwargs): ...
    if sys.version_info >= (3, 7):
        def backup(self, target: Connection, *, pages: int = ...,
                   progress: Optional[Callable[[int, int, int], object]] = ..., name: str = ...,
                   sleep: float = ...) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __enter__(self, *args, **kwargs): ...
    def __exit__(self, *args, **kwargs): ...

class Cursor(Iterator[Any]):
    arraysize = ...  # type: Any
    connection = ...  # type: Any
    description = ...  # type: Any
    lastrowid = ...  # type: Any
    row_factory = ...  # type: Any
    rowcount = ...  # type: Any
    # TODO: Cursor class accepts exactly 1 argument
    # required type is sqlite3.Connection (which is imported as _Connection)
    # however, the name of the __init__ variable is unknown
    def __init__(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def execute(self, sql: str, parameters: Iterable = ...) -> Cursor: ...
    def executemany(self, sql: str, seq_of_parameters: Iterable[Iterable]): ...
    def executescript(self, sql_script: Union[bytes, Text]) -> Cursor: ...
    def fetchall(self) -> List[Any]: ...
    def fetchmany(self, size: Optional[int] = ...) -> List[Any]: ...
    def fetchone(self) -> Any: ...
    def setinputsizes(self, *args, **kwargs): ...
    def setoutputsize(self, *args, **kwargs): ...
    def __iter__(self) -> Cursor: ...
    if sys.version_info >= (3, 0):
        def __next__(self) -> Any: ...
    else:
        def next(self) -> Any: ...


class DataError(DatabaseError): ...

class DatabaseError(Error): ...

class Error(Exception): ...

class IntegrityError(DatabaseError): ...

class InterfaceError(Error): ...

class InternalError(DatabaseError): ...

class NotSupportedError(DatabaseError): ...

class OperationalError(DatabaseError): ...

class OptimizedUnicode(object):
    maketrans = ...  # type: Any
    def __init__(self, *args, **kwargs): ...
    def capitalize(self, *args, **kwargs): ...
    def casefold(self, *args, **kwargs): ...
    def center(self, *args, **kwargs): ...
    def count(self, *args, **kwargs): ...
    def encode(self, *args, **kwargs): ...
    def endswith(self, *args, **kwargs): ...
    def expandtabs(self, *args, **kwargs): ...
    def find(self, *args, **kwargs): ...
    def format(self, *args, **kwargs): ...
    def format_map(self, *args, **kwargs): ...
    def index(self, *args, **kwargs): ...
    def isalnum(self, *args, **kwargs): ...
    def isalpha(self, *args, **kwargs): ...
    def isdecimal(self, *args, **kwargs): ...
    def isdigit(self, *args, **kwargs): ...
    def isidentifier(self, *args, **kwargs): ...
    def islower(self, *args, **kwargs): ...
    def isnumeric(self, *args, **kwargs): ...
    def isprintable(self, *args, **kwargs): ...
    def isspace(self, *args, **kwargs): ...
    def istitle(self, *args, **kwargs): ...
    def isupper(self, *args, **kwargs): ...
    def join(self, *args, **kwargs): ...
    def ljust(self, *args, **kwargs): ...
    def lower(self, *args, **kwargs): ...
    def lstrip(self, *args, **kwargs): ...
    def partition(self, *args, **kwargs): ...
    def replace(self, *args, **kwargs): ...
    def rfind(self, *args, **kwargs): ...
    def rindex(self, *args, **kwargs): ...
    def rjust(self, *args, **kwargs): ...
    def rpartition(self, *args, **kwargs): ...
    def rsplit(self, *args, **kwargs): ...
    def rstrip(self, *args, **kwargs): ...
    def split(self, *args, **kwargs): ...
    def splitlines(self, *args, **kwargs): ...
    def startswith(self, *args, **kwargs): ...
    def strip(self, *args, **kwargs): ...
    def swapcase(self, *args, **kwargs): ...
    def title(self, *args, **kwargs): ...
    def translate(self, *args, **kwargs): ...
    def upper(self, *args, **kwargs): ...
    def zfill(self, *args, **kwargs): ...
    def __add__(self, other): ...
    def __contains__(self, *args, **kwargs): ...
    def __eq__(self, other): ...
    def __format__(self, *args, **kwargs): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __getnewargs__(self, *args, **kwargs): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __iter__(self): ...
    def __le__(self, other): ...
    def __len__(self, *args, **kwargs): ...
    def __lt__(self, other): ...
    def __mod__(self, other): ...
    def __mul__(self, other): ...
    def __ne__(self, other): ...
    def __rmod__(self, other): ...
    def __rmul__(self, other): ...

class PrepareProtocol(object):
    def __init__(self, *args, **kwargs): ...

class ProgrammingError(DatabaseError): ...

class Row(object):
    def __init__(self, *args, **kwargs): ...
    def keys(self, *args, **kwargs): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __iter__(self): ...
    def __le__(self, other): ...
    def __len__(self, *args, **kwargs): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...

class Statement(object):
    def __init__(self, *args, **kwargs): ...

class Warning(Exception): ...
