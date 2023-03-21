import sys
from _typeshed import SupportsIndex
from abc import abstractmethod
from time import struct_time
from typing import ClassVar, NamedTuple, NoReturn, TypeVar, overload
from typing_extensions import Literal, Self, TypeAlias, final

if sys.version_info >= (3, 11):
    __all__ = ("date", "datetime", "time", "timedelta", "timezone", "tzinfo", "MINYEAR", "MAXYEAR", "UTC")
elif sys.version_info >= (3, 9):
    __all__ = ("date", "datetime", "time", "timedelta", "timezone", "tzinfo", "MINYEAR", "MAXYEAR")

_D = TypeVar("_D", bound=date)
_IntLike: TypeAlias = int | SupportsIndex

MINYEAR: Literal[1]
MAXYEAR: Literal[9999]

class tzinfo:
    @abstractmethod
    def tzname(self, __dt: datetime | None) -> str | None: ...
    @abstractmethod
    def utcoffset(self, __dt: datetime | None) -> timedelta | None: ...
    @abstractmethod
    def dst(self, __dt: datetime | None) -> timedelta | None: ...
    def fromutc(self, __dt: datetime) -> datetime: ...

# Alias required to avoid name conflicts with date(time).tzinfo.
_TzInfo: TypeAlias = tzinfo

@final
class timezone(tzinfo):
    utc: ClassVar[timezone]
    min: ClassVar[timezone]
    max: ClassVar[timezone]
    def __init__(self, offset: timedelta, name: str = ...) -> None: ...
    def tzname(self, __dt: datetime | None) -> str: ...
    def utcoffset(self, __dt: datetime | None) -> timedelta: ...
    def dst(self, __dt: datetime | None) -> None: ...

if sys.version_info >= (3, 11):
    UTC: timezone

if sys.version_info >= (3, 9):
    class _IsoCalendarDate(NamedTuple):
        year: int
        week: int
        weekday: int

class date:
    min: ClassVar[date]
    max: ClassVar[date]
    resolution: ClassVar[timedelta]
    def __new__(cls, year: _IntLike, month: _IntLike, day: _IntLike) -> Self: ...
    @classmethod
    def fromtimestamp(cls, __timestamp: float) -> Self: ...
    @classmethod
    def today(cls) -> Self: ...
    @classmethod
    def fromordinal(cls, __n: int) -> Self: ...
    @classmethod
    def fromisoformat(cls, __date_string: str) -> Self: ...
    if sys.version_info >= (3, 8):
        @classmethod
        def fromisocalendar(cls, year: int, week: int, day: int) -> Self: ...

    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    def ctime(self) -> str: ...
    # On <3.12, the name of the parameter in the pure-Python implementation
    # didn't match the name in the C implementation,
    # meaning it is only *safe* to pass it as a keyword argument on 3.12+
    if sys.version_info >= (3, 12):
        def strftime(self, format: str) -> str: ...
    else:
        def strftime(self, __format: str) -> str: ...

    def __format__(self, __fmt: str) -> str: ...
    def isoformat(self) -> str: ...
    def timetuple(self) -> struct_time: ...
    def toordinal(self) -> int: ...
    def replace(self, year: _IntLike = ..., month: _IntLike = ..., day: _IntLike = ...) -> Self: ...
    def __le__(self, __value: date) -> bool: ...
    def __lt__(self, __value: date) -> bool: ...
    def __ge__(self, __value: date) -> bool: ...
    def __gt__(self, __value: date) -> bool: ...
    if sys.version_info >= (3, 8):
        def __add__(self, __value: timedelta) -> Self: ...
        def __radd__(self, __value: timedelta) -> Self: ...
        @overload
        def __sub__(self, __value: timedelta) -> Self: ...
        @overload
        def __sub__(self, __value: datetime) -> NoReturn: ...
        @overload
        def __sub__(self: _D, __value: _D) -> timedelta: ...
    else:
        # Prior to Python 3.8, arithmetic operations always returned `date`, even in subclasses
        def __add__(self, __value: timedelta) -> date: ...
        def __radd__(self, __value: timedelta) -> date: ...
        @overload
        def __sub__(self, __value: timedelta) -> date: ...
        @overload
        def __sub__(self, __value: datetime) -> NoReturn: ...
        @overload
        def __sub__(self, __value: date) -> timedelta: ...

    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    if sys.version_info >= (3, 9):
        def isocalendar(self) -> _IsoCalendarDate: ...
    else:
        def isocalendar(self) -> tuple[int, int, int]: ...

class time:
    min: ClassVar[time]
    max: ClassVar[time]
    resolution: ClassVar[timedelta]
    def __new__(
        cls,
        hour: _IntLike = ...,
        minute: _IntLike = ...,
        second: _IntLike = ...,
        microsecond: _IntLike = ...,
        tzinfo: _TzInfo | None = ...,
        *,
        fold: int = ...,
    ) -> Self: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> _TzInfo | None: ...
    @property
    def fold(self) -> int: ...
    def __le__(self, __value: time) -> bool: ...
    def __lt__(self, __value: time) -> bool: ...
    def __ge__(self, __value: time) -> bool: ...
    def __gt__(self, __value: time) -> bool: ...
    def isoformat(self, timespec: str = ...) -> str: ...
    @classmethod
    def fromisoformat(cls, __time_string: str) -> Self: ...
    # On <3.12, the name of the parameter in the pure-Python implementation
    # didn't match the name in the C implementation,
    # meaning it is only *safe* to pass it as a keyword argument on 3.12+
    if sys.version_info >= (3, 12):
        def strftime(self, format: str) -> str: ...
    else:
        def strftime(self, __format: str) -> str: ...

    def __format__(self, __fmt: str) -> str: ...
    def utcoffset(self) -> timedelta | None: ...
    def tzname(self) -> str | None: ...
    def dst(self) -> timedelta | None: ...
    def replace(
        self,
        hour: _IntLike = ...,
        minute: _IntLike = ...,
        second: _IntLike = ...,
        microsecond: _IntLike = ...,
        tzinfo: _TzInfo | None = ...,
        *,
        fold: int = ...,
    ) -> Self: ...

_Date: TypeAlias = date
_Time: TypeAlias = time

class timedelta:
    min: ClassVar[timedelta]
    max: ClassVar[timedelta]
    resolution: ClassVar[timedelta]
    def __new__(
        cls,
        days: float = ...,
        seconds: float = ...,
        microseconds: float = ...,
        milliseconds: float = ...,
        minutes: float = ...,
        hours: float = ...,
        weeks: float = ...,
    ) -> Self: ...
    @property
    def days(self) -> int: ...
    @property
    def seconds(self) -> int: ...
    @property
    def microseconds(self) -> int: ...
    def total_seconds(self) -> float: ...
    def __add__(self, __value: timedelta) -> timedelta: ...
    def __radd__(self, __value: timedelta) -> timedelta: ...
    def __sub__(self, __value: timedelta) -> timedelta: ...
    def __rsub__(self, __value: timedelta) -> timedelta: ...
    def __neg__(self) -> timedelta: ...
    def __pos__(self) -> timedelta: ...
    def __abs__(self) -> timedelta: ...
    def __mul__(self, __value: float) -> timedelta: ...
    def __rmul__(self, __value: float) -> timedelta: ...
    @overload
    def __floordiv__(self, __value: timedelta) -> int: ...
    @overload
    def __floordiv__(self, __value: int) -> timedelta: ...
    @overload
    def __truediv__(self, __value: timedelta) -> float: ...
    @overload
    def __truediv__(self, __value: float) -> timedelta: ...
    def __mod__(self, __value: timedelta) -> timedelta: ...
    def __divmod__(self, __value: timedelta) -> tuple[int, timedelta]: ...
    def __le__(self, __value: timedelta) -> bool: ...
    def __lt__(self, __value: timedelta) -> bool: ...
    def __ge__(self, __value: timedelta) -> bool: ...
    def __gt__(self, __value: timedelta) -> bool: ...
    def __bool__(self) -> bool: ...

class datetime(date):
    min: ClassVar[datetime]
    max: ClassVar[datetime]
    def __new__(
        cls,
        year: _IntLike,
        month: _IntLike,
        day: _IntLike,
        hour: _IntLike = ...,
        minute: _IntLike = ...,
        second: _IntLike = ...,
        microsecond: _IntLike = ...,
        tzinfo: _TzInfo | None = ...,
        *,
        fold: int = ...,
    ) -> Self: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> _TzInfo | None: ...
    @property
    def fold(self) -> int: ...
    # On <3.12, the name of the first parameter in the pure-Python implementation
    # didn't match the name in the C implementation,
    # meaning it is only *safe* to pass it as a keyword argument on 3.12+
    if sys.version_info >= (3, 12):
        @classmethod
        def fromtimestamp(cls, timestamp: float, tz: _TzInfo | None = ...) -> Self: ...
    else:
        @classmethod
        def fromtimestamp(cls, __timestamp: float, tz: _TzInfo | None = ...) -> Self: ...

    @classmethod
    def utcfromtimestamp(cls, __t: float) -> Self: ...
    if sys.version_info >= (3, 8):
        @classmethod
        def now(cls, tz: _TzInfo | None = None) -> Self: ...
    else:
        @overload
        @classmethod
        def now(cls, tz: None = None) -> Self: ...
        @overload
        @classmethod
        def now(cls, tz: _TzInfo) -> datetime: ...

    @classmethod
    def utcnow(cls) -> Self: ...
    @classmethod
    def combine(cls, date: _Date, time: _Time, tzinfo: _TzInfo | None = ...) -> Self: ...
    def timestamp(self) -> float: ...
    def utctimetuple(self) -> struct_time: ...
    def date(self) -> _Date: ...
    def time(self) -> _Time: ...
    def timetz(self) -> _Time: ...
    def replace(
        self,
        year: _IntLike = ...,
        month: _IntLike = ...,
        day: _IntLike = ...,
        hour: _IntLike = ...,
        minute: _IntLike = ...,
        second: _IntLike = ...,
        microsecond: _IntLike = ...,
        tzinfo: _TzInfo | None = ...,
        *,
        fold: int = ...,
    ) -> Self: ...
    if sys.version_info >= (3, 8):
        def astimezone(self, tz: _TzInfo | None = ...) -> Self: ...
    else:
        def astimezone(self, tz: _TzInfo | None = ...) -> datetime: ...

    def isoformat(self, sep: str = ..., timespec: str = ...) -> str: ...
    @classmethod
    def strptime(cls, __date_string: str, __format: str) -> Self: ...
    def utcoffset(self) -> timedelta | None: ...
    def tzname(self) -> str | None: ...
    def dst(self) -> timedelta | None: ...
    def __le__(self, __value: datetime) -> bool: ...  # type: ignore[override]
    def __lt__(self, __value: datetime) -> bool: ...  # type: ignore[override]
    def __ge__(self, __value: datetime) -> bool: ...  # type: ignore[override]
    def __gt__(self, __value: datetime) -> bool: ...  # type: ignore[override]
    if sys.version_info >= (3, 8):
        @overload  # type: ignore[override]
        def __sub__(self, __value: timedelta) -> Self: ...
        @overload
        def __sub__(self: _D, __value: _D) -> timedelta: ...
    else:
        # Prior to Python 3.8, arithmetic operations always returned `datetime`, even in subclasses
        def __add__(self, __value: timedelta) -> datetime: ...
        def __radd__(self, __value: timedelta) -> datetime: ...
        @overload  # type: ignore[override]
        def __sub__(self, __value: datetime) -> timedelta: ...
        @overload
        def __sub__(self, __value: timedelta) -> datetime: ...
