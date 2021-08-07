import datetime
from typing import List, Mapping, Optional, Set, Union

class BaseTzInfo(datetime.tzinfo):
    zone: str = ...
    def localize(self, dt: datetime.datetime, is_dst: bool | None = ...) -> datetime.datetime: ...
    def normalize(self, dt: datetime.datetime) -> datetime.datetime: ...

class _UTCclass(BaseTzInfo):
    def tzname(self, dt: datetime.datetime | None) -> str: ...
    def utcoffset(self, dt: datetime.datetime | None) -> datetime.timedelta: ...
    def dst(self, dt: datetime.datetime | None) -> datetime.timedelta: ...

class _StaticTzInfo(BaseTzInfo):
    def tzname(self, dt: datetime.datetime | None, is_dst: bool | None = ...) -> str: ...
    def utcoffset(self, dt: datetime.datetime | None, is_dst: bool | None = ...) -> datetime.timedelta: ...
    def dst(self, dt: datetime.datetime | None, is_dst: bool | None = ...) -> datetime.timedelta: ...

class _DstTzInfo(BaseTzInfo):
    def tzname(self, dt: datetime.datetime | None, is_dst: bool | None = ...) -> str: ...
    def utcoffset(self, dt: datetime.datetime | None, is_dst: bool | None = ...) -> datetime.timedelta | None: ...
    def dst(self, dt: datetime.datetime | None, is_dst: bool | None = ...) -> datetime.timedelta | None: ...

class UnknownTimeZoneError(KeyError): ...
class InvalidTimeError(Exception): ...
class AmbiguousTimeError(InvalidTimeError): ...
class NonExistentTimeError(InvalidTimeError): ...

utc: _UTCclass
UTC: _UTCclass

def timezone(zone: str) -> _UTCclass | _StaticTzInfo | _DstTzInfo: ...
def FixedOffset(offset: int) -> _UTCclass | datetime.tzinfo: ...

all_timezones: List[str]
all_timezones_set: Set[str]
common_timezones: List[str]
common_timezones_set: Set[str]
country_timezones: Mapping[str, List[str]]
country_names: Mapping[str, str]
ZERO: datetime.timedelta
HOUR: datetime.timedelta
VERSION: str
