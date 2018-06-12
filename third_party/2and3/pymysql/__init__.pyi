from typing import Union, Tuple, Callable
from .connections import Connection
from .constants import FIELD_TYPE as FIELD_TYPE
from .converters import escape_dict as escape_dict, escape_sequence as escape_sequence, escape_string as escape_string
from .err import (
    Warning as Warning,
    Error as Error,
    InterfaceError as InterfaceError,
    DataError as DataError,
    DatabaseError as DatabaseError,
    OperationalError as OperationalError,
    IntegrityError as IntegrityError,
    InternalError as InternalError,
    NotSupportedError as NotSupportedError,
    ProgrammingError as ProgrammingError,
    MySQLError as MySQLError,
)
from .times import (
    Date as Date,
    Time as Time,
    Timestamp as Timestamp,
    DateFromTicks as DateFromTicks,
    TimeFromTicks as TimeFromTicks,
    TimestampFromTicks as TimestampFromTicks,
)

threadsafety: int
apilevel: str
paramstyle: str

class DBAPISet(frozenset):
    def __ne__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

STRING: DBAPISet
BINARY: DBAPISet
NUMBER: DBAPISet
DATE: DBAPISet
TIME: DBAPISet
TIMESTAMP: DBAPISet
ROWID: DBAPISet
def Binary(x) -> Union[bytearray, bytes]: ...
def Connect(*args, **kwargs) -> Connection: ...
def get_client_info() -> str: ...

connect: Callable[..., Connection]

version_info: Tuple[int, int, int, str, int]
NULL: str
def install_as_MySQLdb() -> None: ...
