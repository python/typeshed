import sys
from typing import Callable, FrozenSet, Tuple, Union

from .connections import Connection as _Connection
from .constants import FIELD_TYPE as FIELD_TYPE
from .converters import escape_dict as escape_dict
from .converters import escape_sequence as escape_sequence
from .converters import escape_string as escape_string
from .err import DatabaseError as DatabaseError
from .err import DataError as DataError
from .err import Error as Error
from .err import IntegrityError as IntegrityError
from .err import InterfaceError as InterfaceError
from .err import InternalError as InternalError
from .err import MySQLError as MySQLError
from .err import NotSupportedError as NotSupportedError
from .err import OperationalError as OperationalError
from .err import ProgrammingError as ProgrammingError
from .err import Warning as Warning
from .times import Date as Date
from .times import DateFromTicks as DateFromTicks
from .times import Time as Time
from .times import TimeFromTicks as TimeFromTicks
from .times import Timestamp as Timestamp
from .times import TimestampFromTicks as TimestampFromTicks

threadsafety: int
apilevel: str
paramstyle: str

class DBAPISet(FrozenSet[int]):
    def __ne__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

STRING: DBAPISet
BINARY: DBAPISet
NUMBER: DBAPISet
DATE: DBAPISet
TIME: DBAPISet
TIMESTAMP: DBAPISet
DATETIME: DBAPISet
ROWID: DBAPISet

if sys.version_info >= (3, 0):
    def Binary(x) -> bytes: ...
else:
    def Binary(x) -> bytearray: ...
def Connect(*args, **kwargs) -> _Connection: ...
def get_client_info() -> str: ...

connect: Callable[..., _Connection]
Connection: Callable[..., _Connection]
__version__: str
version_info: Tuple[int, int, int, str, int]
NULL: str

def thread_safe() -> bool: ...
def install_as_MySQLdb() -> None: ...
