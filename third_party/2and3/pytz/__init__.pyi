# Stubs for pytz (Python 3.5)

import datetime as dt
from pytz.lazy import LazyList, LazyDict  # NOQA

all_timezones = ...  # type: LazyList
all_timezones_set = ...  # type: LazySet
common_timezones = ...  # type: LazyList
common_timezones_set = ...  # type: LazySet
country_timezones = ...  # type: LazyDict
country_names = ...  # type: LazyDict


class UTC(dt.tzinfo):
    zone = ...  # type: str
    def fromutc(self, dt: dt.datetime) -> dt.datetime: ...
    def utcoffset(self, dt: dt.datetime) -> dt.timedelta: ...
    def tzname(self, dt: dt.datetime) -> str: ...
    def dst(self, dt: dt.datetime) -> dt.timedelta: ...
    def localize(self, dt: dt.datetime, is_dst: bool=...) -> dt.datetime: ...
    def normalize(self, dt: dt.datetime, is_dst: bool=...) -> dt.datetime: ...

utc = ...  # type: UTC

def timezone(zone: str) -> UTC: ...
