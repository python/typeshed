from _typeshed import Incomplete
from collections.abc import Generator
from datetime import tzinfo

def total_seconds(td): ...
def dt_to_timestamp(dt): ...
def isoparse(iso_str): ...
def parse_timedelta(text): ...

parse_td = parse_timedelta

def decimal_relative_time(d, other: Incomplete | None = ..., ndigits: int = ..., cardinalize: bool = ...): ...
def relative_time(d, other: Incomplete | None = ..., ndigits: int = ...): ...
def strpdate(string, format): ...
def daterange(start, stop, step: int = ..., inclusive: bool = ...) -> Generator[Incomplete, None, Incomplete]: ...

ZERO: Incomplete
HOUR: Incomplete

class ConstantTZInfo(tzinfo):
    name: Incomplete
    offset: Incomplete
    def __init__(self, name: str = ..., offset=...) -> None: ...
    @property
    def utcoffset_hours(self): ...
    def utcoffset(self, dt): ...
    def tzname(self, dt): ...
    def dst(self, dt): ...

UTC: Incomplete
EPOCH_AWARE: Incomplete
EPOCH_NAIVE: Incomplete

class LocalTZInfo(tzinfo):
    def is_dst(self, dt): ...
    def utcoffset(self, dt): ...
    def dst(self, dt): ...
    def tzname(self, dt): ...

LocalTZ: Incomplete

class USTimeZone(tzinfo):
    stdoffset: Incomplete
    reprname: Incomplete
    stdname: Incomplete
    dstname: Incomplete
    def __init__(self, hours, reprname, stdname, dstname) -> None: ...
    def tzname(self, dt): ...
    def utcoffset(self, dt): ...
    def dst(self, dt): ...

Eastern: Incomplete
Central: Incomplete
Mountain: Incomplete
Pacific: Incomplete
