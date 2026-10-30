from typing import ClassVar, Final

import _win32typing

def odbc(connectionString: str, /) -> _win32typing.odbcconn: ...
def SQLDataSources(direction: int, /) -> tuple[str, str] | None: ...

STRING: Final = "STRING"
RAW: Final = "RAW"
NUMBER: Final = "NUMBER"
DATE: Final = "DATE"
TYPES: Final = ("STRING", "RAW", "NUMBER", "DATE")
SQL_FETCH_NEXT: Final[int]
SQL_FETCH_FIRST: Final[int]
SQL_FETCH_LAST: Final[int]
SQL_FETCH_PRIOR: Final[int]
SQL_FETCH_ABSOLUTE: Final[int]
SQL_FETCH_RELATIVE: Final[int]
SQL_FETCH_FIRST_USER: Final[int]
SQL_FETCH_FIRST_SYSTEM: Final[int]

class error(Exception):
    __name__: ClassVar[str] = "odbcError"

# These all pretend to come from a module called "dbi", but that module doesn't exist
class noError(Exception): ...
class opError(Exception): ...
class progError(Exception): ...
class integrityError(Exception): ...
class dataError(Exception): ...
class internalError(Exception): ...
