import decimal
from _typeshed import ReadableBuffer
from datetime import date, datetime, time
from typing import Any, Sequence, Type, overload
from typing_extensions import Literal

from .resultrow import ResultRow

apilevel: str
threadsafety: int
paramstyle: tuple[str, ...]
connect: Type[Connection]

class Connection:
    def __init__(
        self,
        address: str,
        port: int,
        username: str,
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
    def isconnected(self) -> bool: ...
    def rollback(self) -> None: ...
    def setautocommit(self, auto: bool = ...) -> None: ...
    def setclientinfo(self, key: str, value: str | None = ...) -> None: ...

class LOB:
    def close(self) -> bool: ...
    def find(self, object: str, length: int, position: int = ...) -> int: ...
    def read(self, size: int = ..., position: int = ...) -> str | bytes: ...
    def write(self, object: str | bytes) -> int: ...

_Parameters = Sequence[tuple[Any, ...]]

class Cursor:
    description: tuple[tuple[Any, ...], ...]
    rowcount: int
    statementhash: str | None
    connection: Connection
    arraysize: int
    def callproc(self, procname: str, parameters: tuple[Any, ...] = ..., overview: bool = ...) -> tuple[Any, ...]: ...
    def close(self) -> None: ...
    def description_ext(self) -> Sequence[tuple[Any, ...]]: ...
    def execute(self, operation: str, parameters: tuple[Any, ...]) -> bool: ...
    def executemany(self, operation: str, parameters: _Parameters) -> Any: ...
    def executemanyprepared(self, parameters: _Parameters) -> Any: ...
    def executeprepared(self, parameters: _Parameters = ...) -> Any: ...
    def fetchone(self, uselob: bool = ...) -> ResultRow | None: ...
    def fetchall(self) -> list[ResultRow]: ...
    def fetchmany(self, size: int | None = ...) -> list[ResultRow]: ...
    def get_resultset_holdability(self) -> int: ...
    def getwarning(self) -> Warning | None: ...
    def haswarning(self) -> bool: ...
    def nextset(self) -> None: ...
    def parameter_description(self) -> tuple[str, ...]: ...
    @overload
    def prepare(self, operation: str, newcursor: Literal[True]) -> Cursor: ...
    @overload
    def prepare(self, operation: str, newcursor: Literal[False]) -> Any: ...
    def prepare(self, operation: str, newcursor: bool = ...) -> Cursor | Any: ...
    def scroll(self, value: int, mode: Literal["absolute"] | Literal["relative"] = ...) -> None: ...
    def server_cpu_time(self) -> int: ...
    def server_memory_usage(self) -> int: ...
    def server_processing_time(self) -> int: ...
    def setinputsizes(self, *args: Any, **kwwargs: Any) -> None: ...
    def setfetchsize(self, value: int) -> None: ...
    def set_resultset_holdability(self, holdability: int) -> None: ...
    def setoutputsize(self, *args: Any, **kwwargs: Any) -> None: ...

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

def Date(year: int, month: int, day: int) -> date: ...
def Time(hour: int, minute: int, second: int, millisecond: int = ...) -> time: ...
def Timestamp(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int = ...) -> datetime: ...
def DateFromTicks(ticks: float) -> date: ...
def TimeFromTicks(ticks: float) -> time: ...
def TimestampFromTicks(ticks: float) -> datetime: ...
def Binary(data: ReadableBuffer) -> memoryview: ...

Decimal: Type[decimal.Decimal]

NUMBER: Type[int] | Type[float] | Type[complex]
DATETIME: Type[date] | Type[time] | Type[datetime]
STRING: Type[str]
BINARY: Type[memoryview]
ROWID: Type[int]
