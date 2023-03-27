from collections.abc import Iterable
from datetime import date, datetime, time, timedelta, tzinfo
from typing import SupportsInt, overload
from typing_extensions import Literal, TypeAlias

from babel.core import Locale
from babel.localedata import LocaleDataDict
from babel.util import LOCALTZ as LOCALTZ, UTC as UTC
from pytz import BaseTzInfo

# The module contents here are organized the same way they are in the API documentation at
# http://babel.pocoo.org/en/latest/api/dates.html

# Date and Time Formatting
_Instant: TypeAlias = date | time | float | None
_PredefinedTimeFormat: TypeAlias = Literal["full", "long", "medium", "short"]
_Context: TypeAlias = Literal["format", "stand-alone"]

def format_datetime(
    datetime: _Instant = None,
    format: _PredefinedTimeFormat | str = "medium",
    tzinfo: tzinfo | None = None,
    locale: Locale | str | None = None,
) -> str: ...
def format_date(
    date: date | None = None, format: _PredefinedTimeFormat | str = "medium", locale: Locale | str | None = None
) -> str: ...
def format_time(
    time: time | datetime | float | None = None,
    format: _PredefinedTimeFormat | str = "medium",
    tzinfo: tzinfo | None = None,
    locale: Locale | str | None = None,
) -> str: ...
def format_timedelta(
    delta: timedelta | int,
    granularity: Literal["year", "month", "week", "day", "hour", "minute", "second"] = "second",
    threshold: float = 0.85,
    add_direction: bool = False,
    format: Literal["narrow", "short", "medium", "long"] = "long",
    locale: Locale | str | None = None,
) -> str: ...
def format_skeleton(
    skeleton: str, datetime: _Instant = None, tzinfo: tzinfo | None = None, fuzzy: bool = True, locale: Locale | str | None = None
) -> str: ...
def format_interval(
    start: _Instant,
    end: _Instant,
    skeleton: str | None = None,
    tzinfo: tzinfo | None = None,
    fuzzy: bool = True,
    locale: Locale | str | None = None,
) -> str: ...

# Timezone Functionality
@overload
def get_timezone(zone: str | BaseTzInfo | None = None) -> BaseTzInfo: ...
@overload
def get_timezone(zone: tzinfo) -> tzinfo: ...
def get_timezone_gmt(
    datetime: _Instant = None,
    width: Literal["long", "short", "iso8601", "iso8601_short"] = "long",
    locale: Locale | str | None = None,
    return_z: bool = False,
) -> str: ...

_DtOrTzinfo: TypeAlias = datetime | tzinfo | str | int | time | None

def get_timezone_location(
    dt_or_tzinfo: _DtOrTzinfo = None, locale: Locale | str | None = None, return_city: bool = False
) -> str: ...
def get_timezone_name(
    dt_or_tzinfo: _DtOrTzinfo = None,
    width: Literal["long", "short"] = "long",
    uncommon: bool = False,
    locale: Locale | str | None = None,
    zone_variant: Literal["generic", "daylight", "standard"] | None = None,
    return_zone: bool = False,
) -> str: ...

# Note: While Babel accepts any tzinfo for the most part, the get_next_timeout_transition()
# function requires a tzinfo that is produced by get_timezone()/pytz AND has DST info.
# The typing here will help you with the first requirement, but will not protect against
# pytz tzinfo's without DST info, like what you get from get_timezone("UTC") for instance.
def get_next_timezone_transition(zone: BaseTzInfo | None = None, dt: _Instant = None) -> TimezoneTransition: ...

class TimezoneTransition:
    # This class itself is not included in the documentation, yet it is mentioned by name.
    # See https://github.com/python-babel/babel/issues/823
    activates: datetime
    from_tzinfo: tzinfo
    to_tzinfo: tzinfo
    reference_date: datetime | None
    def __init__(
        self, activates: datetime, from_tzinfo: tzinfo, to_tzinfo: tzinfo, reference_date: datetime | None = None
    ) -> None: ...
    @property
    def from_tz(self) -> str: ...
    @property
    def to_tz(self) -> str: ...
    @property
    def from_offset(self) -> int: ...
    @property
    def to_offset(self) -> int: ...

# Data Access
def get_period_names(
    width: Literal["abbreviated", "narrow", "wide"] = "wide",
    context: _Context = "stand-alone",
    locale: Locale | str | None = None,
) -> LocaleDataDict: ...
def get_day_names(
    width: Literal["abbreviated", "narrow", "short", "wide"] = "wide",
    context: _Context = "format",
    locale: Locale | str | None = None,
) -> LocaleDataDict: ...
def get_month_names(
    width: Literal["abbreviated", "narrow", "wide"] = "wide", context: _Context = "format", locale: Locale | str | None = None
) -> LocaleDataDict: ...
def get_quarter_names(
    width: Literal["abbreviated", "narrow", "wide"] = "wide", context: _Context = "format", locale: Locale | str | None = None
) -> LocaleDataDict: ...
def get_era_names(
    width: Literal["abbreviated", "narrow", "wide"] = "wide", locale: Locale | str | None = None
) -> LocaleDataDict: ...
def get_date_format(format: _PredefinedTimeFormat = "medium", locale: Locale | str | None = None) -> DateTimePattern: ...
def get_datetime_format(format: _PredefinedTimeFormat = "medium", locale: Locale | str | None = None) -> DateTimePattern: ...
def get_time_format(format: _PredefinedTimeFormat = "medium", locale: Locale | str | None = None) -> DateTimePattern: ...

class ParseError(ValueError): ...

# Basic Parsing
def parse_date(string: str, locale: Locale | str | None = None, format: _PredefinedTimeFormat = "medium") -> date: ...
def parse_time(string: str, locale: Locale | str | None = None, format: _PredefinedTimeFormat = "medium") -> time: ...
def parse_pattern(pattern: str) -> DateTimePattern: ...

# Undocumented
NO_INHERITANCE_MARKER: str
LC_TIME: str | None
date_ = date
datetime_ = datetime
time_ = time

TIMEDELTA_UNITS: tuple[tuple[str, int], ...]

def get_period_id(
    time: _Instant, tzinfo: BaseTzInfo | None = None, type: Literal["selection"] | None = None, locale: Locale | str | None = None
): ...

class DateTimePattern:
    pattern: str
    format: DateTimeFormat
    def __init__(self, pattern: str, format: DateTimeFormat) -> None: ...
    def __mod__(self, other: DateTimeFormat) -> str: ...
    def apply(self, datetime: _Instant, locale: Locale | str | None) -> str: ...

class DateTimeFormat:
    value: date | time
    locale: Locale
    def __init__(self, value: date | time, locale: Locale | str) -> None: ...
    def __getitem__(self, name: str) -> str: ...
    def extract(self, char: str) -> int: ...
    def format_era(self, char: str, num: int) -> str: ...
    def format_year(self, char: str, num: int) -> str: ...
    def format_quarter(self, char: str, num: int) -> str: ...
    def format_month(self, char: str, num: int) -> str: ...
    def format_week(self, char: str, num: int) -> str: ...
    def format_weekday(self, char: str = "E", num: int = 4) -> str: ...
    def format_day_of_year(self, num: int) -> str: ...
    def format_day_of_week_in_month(self) -> str: ...
    def format_period(self, char: str, num: int) -> str: ...
    def format_frac_seconds(self, num: int) -> str: ...
    def format_milliseconds_in_day(self, num: int) -> str: ...
    def format_timezone(self, char: str, num: int) -> str: ...
    def format(self, value: SupportsInt, length: int) -> str: ...
    def get_day_of_year(self, date: date | None = None) -> int: ...
    def get_week_number(self, day_of_period: int, day_of_week: int | None = None) -> int: ...

PATTERN_CHARS: dict[str, list[int] | None]
PATTERN_CHAR_ORDER: str

def tokenize_pattern(pattern: str) -> list[tuple[str, str | tuple[str, int]]]: ...
def untokenize_pattern(tokens: Iterable[tuple[str, str | tuple[str, int]]]) -> str: ...
def split_interval_pattern(pattern: str) -> list[str]: ...
def match_skeleton(skeleton: str, options: Iterable[str], allow_different_fields: bool = False) -> str | None: ...
