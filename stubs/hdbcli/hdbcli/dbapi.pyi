import decimal
from _typeshed import Incomplete, ReadableBuffer
from collections.abc import Sequence
from datetime import date, datetime, time
from types import TracebackType
from typing import Any, Literal, overload
from typing_extensions import Self, TypeAlias

from .resultrow import ResultRow

apilevel: str
threadsafety: int
paramstyle: tuple[str, ...]  # hdbcli defines it as a tuple which does not follow PEP 249
connect = Connection

class Connection:
    def __init__(
        self,
        address: str,
        port: int,
        user: str,
        password: str,
        autocommit: bool = ...,
        packetsize: int | None = ...,
        userkey: str | None = ...,
        *,
        sessionvariables: dict[str, str] | None = ...,
        forcebulkfetch: bool | None = ...,
    ) -> None: ...
    def cancel(self) -> bool: ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def cursor(self) -> Cursor: ...
    def getaddress(self) -> str: ...
    def getautocommit(self) -> bool: ...
    def getclientinfo(self, key: str = ...) -> str | dict[str, str]: ...
    def getproperty(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def isconnected(self) -> bool: ...
    def rollback(self) -> None: ...
    def setautocommit(self, auto: bool = ...) -> None: ...
    def setclientinfo(self, key: str, value: str | None = ...) -> None: ...

class LOB:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def close(self) -> bool: ...
    def find(self, object: str, length: int, position: int = ...) -> int: ...
    def read(self, size: int = ..., position: int = ...) -> str | bytes: ...
    def write(self, object: str | bytes) -> int: ...

_Parameters: TypeAlias = Sequence[tuple[Any, ...]] | None

class Cursor:
    description: tuple[tuple[Any, ...], ...]
    rowcount: int
    statementhash: str | None
    connection: Connection
    arraysize: int
    refreshts: int | None
    maxage: int
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, typ: type[BaseException] | None, val: BaseException | None, tb: TracebackType | None) -> None: ...
    def callproc(self, procname: str, parameters: tuple[Any, ...] = ..., overview: bool = ...) -> tuple[Any, ...]: ...
    def close(self) -> None: ...
    def description_ext(self) -> Sequence[tuple[Any, ...]]: ...
    def execute(self, operation: str, parameters: tuple[Any, ...] | None = ...) -> bool: ...
    def executemany(self, operation: str, parameters: _Parameters = ...) -> Any: ...
    def executemanyprepared(self, parameters: _Parameters = ...) -> Any: ...
    def executeprepared(self, parameters: _Parameters = ...) -> Any: ...
    def fetchone(self, uselob: bool = ...) -> ResultRow | None: ...
    def fetchall(self) -> list[ResultRow]: ...
    def fetchmany(self, size: int | None = ...) -> list[ResultRow]: ...
    def getrowsaffectedcounts(self) -> tuple[Any, ...]: ...
    def getpacketsize(self) -> int: ...
    def get_resultset_holdability(self) -> int: ...
    def getwarning(self) -> Warning | None: ...
    def haswarning(self) -> bool: ...
    def clearwarning(self) -> None: ...
    def has_result_set(self) -> bool: ...
    def nextset(self) -> None: ...
    def parameter_description(self) -> tuple[str, ...]: ...
    @overload
    def prepare(self, operation: str, newcursor: Literal[True]) -> Cursor: ...
    @overload
    def prepare(self, operation: str, newcursor: Literal[False]) -> Any: ...
    def print_message(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def parsenamedquery(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def scroll(self, value: int, mode: Literal["absolute", "relative"] = ...) -> None: ...
    def server_cpu_time(self) -> int: ...
    def server_memory_usage(self) -> int: ...
    def server_processing_time(self) -> int: ...
    def setinputsizes(self, *args: Any, **kwargs: Any) -> None: ...
    def setfetchsize(self, value: int) -> None: ...
    def setquerytimeout(self, value: int) -> None: ...
    def setpacketsize(self, value: int) -> None: ...
    def set_resultset_holdability(self, holdability: int) -> None: ...
    def setoutputsize(self, *args: Any, **kwargs: Any) -> None: ...
    def setcommandinfo(self, command_info: str, line_number: int) -> None: ...

class Warning(Exception):
    errorcode: int
    errortext: str

class Error(Exception):
    errorcode: int
    errortext: str

class DatabaseError(Error): ...
class OperationalError(DatabaseError): ...
class ProgrammingError(DatabaseError): ...
class IntegrityError(DatabaseError): ...
class InterfaceError(Error): ...
class InternalError(DatabaseError): ...
class DataError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...

class ExecuteManyError(Error):
    errors: Incomplete

class ExecuteManyErrorEntry(Error):
    rownumber: int

def Date(year: int, month: int, day: int) -> date: ...
def Time(hour: int, minute: int, second: int, millisecond: int = 0) -> time: ...
def Timestamp(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int = 0) -> datetime: ...
def DateFromTicks(ticks: float) -> date: ...
def TimeFromTicks(ticks: float) -> time: ...
def TimestampFromTicks(ticks: float) -> datetime: ...
def Binary(data: ReadableBuffer) -> memoryview: ...

Decimal = decimal.Decimal

NUMBER: type[int | float | complex]
DATETIME: type[date | time | datetime]
STRING = str
BINARY = memoryview
ROWID = int
