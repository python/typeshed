import re
from collections.abc import Callable, Sequence
from datetime import _TzInfo, datetime
from io import StringIO
from typing import Literal, Protocol, TypeAlias, overload, type_check_only
from typing_extensions import Self

from .._common import _ContainsGet, _SizedReader

_FileOrStr: TypeAlias = bytes | bytearray | str | _SizedReader[str]
_TzData: TypeAlias = _TzInfo | int | str | None
_TzInfos: TypeAlias = _ContainsGet[str, _TzData] | Callable[[str | None, int | None], _TzData]

__all__ = ["parse", "parserinfo", "ParserError"]

class _timelex:
    _split_decimal: re.Pattern[str]
    instream: StringIO | _SizedReader[str]
    charstack: list[str]
    tokenstack: list[str]
    eof: bool
    def __init__(self, instream: str | bytes | bytearray | _SizedReader[str]) -> None: ...
    def get_token(self) -> str | None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> str: ...
    def next(self) -> str: ...
    @classmethod
    def split(cls, s: str) -> list[str]: ...
    @classmethod
    def isword(cls, nextchar: str) -> bool: ...
    @classmethod
    def isnum(cls, nextchar: str) -> bool: ...
    @classmethod
    def isspace(cls, nextchar: str) -> bool: ...

class _resultbase:
    def __init__(self) -> None: ...
    def _repr(self, classname: str) -> str: ...
    def __len__(self) -> int: ...

@type_check_only
class _ParserInfo(Protocol):
    @property
    def dayfirst(self) -> bool: ...
    @property
    def yearfirst(self) -> bool: ...
    @property
    def UTCZONE(self) -> Sequence[str]: ...
    def convertyear(self, year: int, century_specified: bool = False) -> int: ...
    def validate(self, res: parser._result) -> bool: ...
    def jump(self, name: str) -> bool: ...
    def pertain(self, name: str) -> bool: ...
    def utczone(self, name: str) -> bool: ...
    def weekday(self, name: str) -> int | None: ...
    def month(self, name: str) -> int | None: ...
    def hms(self, name: str) -> int | None: ...
    def ampm(self, name: str) -> int | None: ...
    def tzoffset(self, name: str) -> int | None: ...

class parserinfo:
    dayfirst: bool
    yearfirst: bool
    JUMP: list[str]
    WEEKDAYS: list[tuple[str, str]]
    MONTHS: list[tuple[str, str] | tuple[str, str, str]]
    HMS: list[tuple[str, str, str]]
    AMPM: list[tuple[str, str]]
    UTCZONE: list[str]
    PERTAIN: list[str]
    TZOFFSET: dict[str, int]
    def __init__(self, dayfirst: bool = False, yearfirst: bool = False) -> None: ...
    def jump(self, name: str) -> bool: ...
    def weekday(self, name: str) -> int | None: ...
    def month(self, name: str) -> int | None: ...
    def hms(self, name: str) -> int | None: ...
    def ampm(self, name: str) -> int | None: ...
    def pertain(self, name: str) -> bool: ...
    def utczone(self, name: str) -> bool: ...
    def tzoffset(self, name: str) -> int | None: ...
    def convertyear(self, year: int, century_specified: bool = False) -> int: ...
    def validate(self, res: parser._result) -> bool: ...

class _ymd(list[int]):
    century_specified: bool
    dstridx: int | None
    mstridx: int | None
    ystridx: int | None
    @property
    def has_year(self) -> bool: ...
    @property
    def has_month(self) -> bool: ...
    @property
    def has_day(self) -> bool: ...
    def could_be_day(self, value: int) -> bool: ...
    def append(self, val: str | int, label: str | None = None) -> None: ...
    def _resolve_from_stridxs(self, strids: dict[str, int]) -> tuple[int, int, int]: ...
    def resolve_ymd(self, yearfirst: bool | None, dayfirst: bool | None) -> tuple[int, int, int]: ...

class parser:
    class _result(_resultbase):
        year: int | None
        month: int | None
        day: int | None
        weekday: int | None
        hour: int | None
        minute: int | None
        second: int | None
        microsecond: int | None
        tzname: str | None
        tzoffset: int | None
        ampm: int | None
        any_unused_tokens: bool | None

    info: _ParserInfo
    def __init__(self, info: _ParserInfo | None = None) -> None: ...

    @overload
    def parse(
        self,
        timestr: _FileOrStr,
        default: datetime | None = None,
        ignoretz: bool | None = False,
        tzinfos: _TzInfos | None = None,
        *,
        dayfirst: bool | None = ...,
        yearfirst: bool | None = ...,
        fuzzy: bool = ...,
        fuzzy_with_tokens: Literal[False] = False,
    ) -> datetime: ...
    @overload
    def parse(
        self,
        timestr: _FileOrStr,
        default: datetime | None = None,
        ignoretz: bool | None = False,
        tzinfos: _TzInfos | None = None,
        *,
        dayfirst: bool | None = ...,
        yearfirst: bool | None = ...,
        fuzzy: bool = ...,
        fuzzy_with_tokens: Literal[True],
    ) -> tuple[datetime, tuple[str, ...]]: ...
    @overload
    def parse(
        self,
        timestr: _FileOrStr,
        default: datetime | None = None,
        ignoretz: bool | None = False,
        tzinfos: _TzInfos | None = None,
        *,
        dayfirst: bool | None = ...,
        yearfirst: bool | None = ...,
        fuzzy: bool = ...,
        fuzzy_with_tokens: bool,
    ) -> datetime | tuple[datetime, tuple[str, ...]]: ...

DEFAULTPARSER: parser

@overload
def parse(
    timestr: _FileOrStr,
    parserinfo: _ParserInfo | None = None,
    *,
    dayfirst: bool | None = ...,
    yearfirst: bool | None = ...,
    ignoretz: bool | None = ...,
    fuzzy: bool = ...,
    fuzzy_with_tokens: Literal[False] = False,
    default: datetime | None = ...,
    tzinfos: _TzInfos | None = ...,
) -> datetime: ...
@overload
def parse(
    timestr: _FileOrStr,
    parserinfo: _ParserInfo | None = None,
    *,
    dayfirst: bool | None = ...,
    yearfirst: bool | None = ...,
    ignoretz: bool | None = ...,
    fuzzy: bool = ...,
    fuzzy_with_tokens: Literal[True],
    default: datetime | None = ...,
    tzinfos: _TzInfos | None = ...,
) -> tuple[datetime, tuple[str, ...]]: ...
@overload
def parse(
    timestr: _FileOrStr,
    parserinfo: _ParserInfo | None = None,
    *,
    dayfirst: bool | None = ...,
    yearfirst: bool | None = ...,
    ignoretz: bool | None = ...,
    fuzzy: bool = ...,
    fuzzy_with_tokens: bool,
    default: datetime | None = ...,
    tzinfos: _TzInfos | None = ...,
) -> datetime | tuple[datetime, tuple[str, ...]]: ...

class _tzparser:
    class _result(_resultbase):
        __slots__ = ["stdabbr", "stdoffset", "dstabbr", "dstoffset", "start", "end"]
        stdabbr: str | None
        stdoffset: int | None
        dstabbr: str | None
        dstoffset: int | None
        start: _attr  # pyrefly: ignore [unknown-name]
        end: _attr  # pyrefly: ignore [unknown-name]

        class _attr(_resultbase):
            __slots__ = ["month", "week", "weekday", "yday", "jyday", "day", "time"]
            month: int | None
            week: int | None
            weekday: int | None
            yday: int | None
            jyday: int | None
            day: int | None
            time: int | None

        def __init__(self) -> None: ...

    def parse(self, tzstr: str | re.Pattern[str]) -> _result | None: ...

DEFAULTTZPARSER: _tzparser

class ParserError(ValueError): ...
class UnknownTimezoneWarning(RuntimeWarning): ...
