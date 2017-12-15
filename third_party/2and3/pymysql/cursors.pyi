from typing import Union, Tuple, Any, Dict, Optional, Text
from .connections import Connection

Gen = Union[Tuple[Any, ...], Dict[str, Any]]

class Cursor:
    connection = ...  # type: Connection
    description = ...  # type: Tuple[Text, ...]
    rownumber = ...  # type: int
    rowcount = ...  # type: int
    arraysize = ...  # type: int
    messages = ...  # type: Any
    errorhandler = ...  # type: Any
    lastrowid = ...  # type: int
    def __init__(self, connection: Connection) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def setinputsizes(self, *args): ...
    def setoutputsizes(self, *args): ...
    def nextset(self): ...
    def execute(self, query: str, args=None) -> int: ...
    def executemany(self, query: str, args) -> int: ...
    def callproc(self, procname, args=...): ...
    def fetchone(self) -> Optional[Gen]: ...
    def fetchmany(self, size: Optional[int] = ...) -> Optional[Gen]: ...
    def fetchall(self) -> Optional[Tuple[Gen, ...]]: ...
    def scroll(self, value, mode=''): ...
    def __iter__(self): ...

class DictCursor(Cursor):
    def fetchone(self) -> Optional[Dict[str, Any]]: ...
    def fetchmany(self, size=None) -> Optional[Tuple[Dict[str, Any], ...]]: ...
    def fetchall(self) -> Optional[Tuple[Dict[str, Any], ...]]: ...
