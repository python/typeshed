from _typeshed import Incomplete, Unused
from re import Pattern
from typing import ClassVar, overload
from typing_extensions import Literal, TypeGuard

from openpyxl.descriptors import Strict, String
from openpyxl.descriptors.base import Integer, _ConvertibleToInt
from openpyxl.descriptors.serialisable import Serialisable

BUILTIN_FORMATS: dict[int, str]
BUILTIN_FORMATS_MAX_SIZE: int
BUILTIN_FORMATS_REVERSE: dict[str, int]
FORMAT_GENERAL: str
FORMAT_TEXT: str
FORMAT_NUMBER: str
FORMAT_NUMBER_00: str
FORMAT_NUMBER_COMMA_SEPARATED1: str
FORMAT_NUMBER_COMMA_SEPARATED2: str
FORMAT_PERCENTAGE: str
FORMAT_PERCENTAGE_00: str
FORMAT_DATE_YYYYMMDD2: str
FORMAT_DATE_YYMMDD: str
FORMAT_DATE_DDMMYY: str
FORMAT_DATE_DMYSLASH: str
FORMAT_DATE_DMYMINUS: str
FORMAT_DATE_DMMINUS: str
FORMAT_DATE_MYMINUS: str
FORMAT_DATE_XLSX14: str
FORMAT_DATE_XLSX15: str
FORMAT_DATE_XLSX16: str
FORMAT_DATE_XLSX17: str
FORMAT_DATE_XLSX22: str
FORMAT_DATE_DATETIME: str
FORMAT_DATE_TIME1: str
FORMAT_DATE_TIME2: str
FORMAT_DATE_TIME3: str
FORMAT_DATE_TIME4: str
FORMAT_DATE_TIME5: str
FORMAT_DATE_TIME6: str
FORMAT_DATE_TIME7: str
FORMAT_DATE_TIME8: str
FORMAT_DATE_TIMEDELTA: str
FORMAT_DATE_YYMMDDSLASH: str
FORMAT_CURRENCY_USD_SIMPLE: str
FORMAT_CURRENCY_USD: str
FORMAT_CURRENCY_EUR_SIMPLE: str
COLORS: str
LITERAL_GROUP: str
LOCALE_GROUP: str
STRIP_RE: Pattern[str]
TIMEDELTA_RE: Pattern[str]

def is_date_format(fmt: str | None) -> TypeGuard[str]: ...
def is_timedelta_format(fmt): ...
@overload
def is_datetime(fmt: None) -> None: ...
@overload
def is_datetime(fmt: str) -> Literal["datetime", "date", "time", None]: ...
def is_builtin(fmt: str) -> bool: ...
def builtin_format_code(index: int) -> str | None: ...
def builtin_format_id(fmt): ...

class NumberFormatDescriptor(String[Incomplete]):
    def __set__(self, instance: Serialisable | Strict, value) -> None: ...

class NumberFormat(Serialisable):
    numFmtId: Integer[Literal[False]]
    formatCode: String[Literal[False]]
    def __init__(self, numFmtId: _ConvertibleToInt, formatCode: str) -> None: ...

class NumberFormatList(Serialisable):
    # Overwritten by property below
    # count: Integer
    numFmt: Incomplete
    __elements__: ClassVar[tuple[str, ...]]
    __attrs__: ClassVar[tuple[str, ...]]
    def __init__(self, count: Unused = None, numFmt=()) -> None: ...
    @property
    def count(self) -> int: ...
    def __getitem__(self, idx) -> NumberFormat: ...
