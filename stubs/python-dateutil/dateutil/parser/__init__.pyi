from collections.abc import Mapping
from datetime import datetime, tzinfo
from typing import IO, Any, Text, Union

from .isoparser import isoparse as isoparse, isoparser as isoparser

_FileOrStr = Union[bytes, Text, IO[str], IO[Any]]

class parserinfo(object):
    JUMP: list[str]
    WEEKDAYS: list[tuple[str, str]]
    MONTHS: list[tuple[str, str]]
    HMS: list[tuple[str, str, str]]
    AMPM: list[tuple[str, str]]
    UTCZONE: list[str]
    PERTAIN: list[str]
    TZOFFSET: dict[str, int]
    def __init__(self, dayfirst: bool = ..., yearfirst: bool = ...) -> None: ...
    def jump(self, name: Text) -> bool: ...
    def weekday(self, name: Text) -> int | None: ...
    def month(self, name: Text) -> int | None: ...
    def hms(self, name: Text) -> int | None: ...
    def ampm(self, name: Text) -> int | None: ...
    def pertain(self, name: Text) -> bool: ...
    def utczone(self, name: Text) -> bool: ...
    def tzoffset(self, name: Text) -> int | None: ...
    def convertyear(self, year: int) -> int: ...
    def validate(self, res: datetime) -> bool: ...

class parser(object):
    def __init__(self, info: parserinfo | None = ...) -> None: ...
    def parse(
        self,
        timestr: _FileOrStr,
        default: datetime | None = ...,
        ignoretz: bool = ...,
        tzinfos: Mapping[Text, tzinfo] | None = ...,
        **kwargs: Any,
    ) -> datetime: ...

DEFAULTPARSER: parser

def parse(timestr: _FileOrStr, parserinfo: parserinfo | None = ..., **kwargs: Any) -> datetime: ...

class _tzparser: ...

DEFAULTTZPARSER: _tzparser

class ParserError(ValueError): ...
