import sys
from _typeshed import Self
from time import struct_time
from typing import ClassVar, NamedTuple, SupportsAbs, Type, TypeVar, overload
from typing_extensions import SupportsIndex, final

_S = TypeVar("_S")

MINYEAR: int
MAXYEAR: int

class tzinfo:
    def tzname(self, dt: datetime | None) -> str | None: ...
    def utcoffset(self, dt: datetime | None) -> timedelta | None: ...
    def dst(self, dt: datetime | None) -> timedelta | None: ...
    def fromutc(self, dt: datetime) -> datetime: ...
    def __reduce__(self: Self) -> tuple[Type[Self], tuple[Self]]: ...

# Alias required to avoid name conflicts with date(time).tzinfo.
_tzinfo = tzinfo

@final
class timezone(tzinfo):
    utc: ClassVar[timezone]
    min: ClassVar[timezone]
    max: ClassVar[timezone]
    def __init__(self, offset: timedelta, name: str = ...) -> None: ...
    def __hash__(self) -> int: ...

if sys.version_info >= (3, 9):
    class _IsoCalendarDate(NamedTuple):
        year: int
        week: int
        weekday: int

class date:
    min: ClassVar[date]
    max: ClassVar[date]
    resolution: ClassVar[timedelta]
    def __new__(cls: Type[_S], year: int, month: int, day: int) -> _S: ...
    @classmethod
    def fromtimestamp(cls: Type[_S], __timestamp: float) -> _S: ...
    @classmethod
    def today(cls: Type[_S]) -> _S: ...
    @classmethod
    def fromordinal(cls: Type[_S], n: int) -> _S: ...
    if sys.version_info >= (3, 7):
        @classmethod
        def fromisoformat(cls: Type[_S], date_string: str) -> _S: ...
    if sys.version_info >= (3, 8):
        @classmethod
        def fromisocalendar(cls: Type[_S], year: int, week: int, day: int) -> _S: ...
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    def ctime(self) -> str: ...
    def strftime(self, fmt: str) -> str: ...
    def __format__(self, fmt: str) -> str: ...
    def isoformat(self) -> str: ...
    def timetuple(self) -> struct_time: ...
    def toordinal(self) -> int: ...
    def replace(self, year: int = ..., month: int = ..., day: int = ...) -> date: ...
    def __le__(self, other: date) -> bool: ...
    def __lt__(self, other: date) -> bool: ...
    def __ge__(self, other: date) -> bool: ...
    def __gt__(self, other: date) -> bool: ...
    if sys.version_info >= (3, 8):
        def __add__(self: _S, other: timedelta) -> _S: ...
        def __radd__(self: _S, other: timedelta) -> _S: ...
    else:
        def __add__(self, other: timedelta) -> date: ...
        def __radd__(self, other: timedelta) -> date: ...
    @overload
    def __sub__(self, other: timedelta) -> date: ...
    @overload
    def __sub__(self, other: date) -> timedelta: ...
    def __reduce__(self: Self) -> tuple[Type[Self], tuple[bytes]]: ...
    if sys.version_info >= (3, 8):
        def __reduce_ex__(self: Self, __protocol: SupportsIndex) -> tuple[Type[Self], tuple[bytes]]: ...
    else:
        def __reduce_ex__(self: Self, __protocol: int) -> tuple[Type[Self], tuple[bytes]]: ...
    def __hash__(self) -> int: ...
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
        cls: Type[_S],
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
        *,
        fold: int = ...,
    ) -> _S: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> _tzinfo | None: ...
    @property
    def fold(self) -> int: ...
    def __le__(self, other: time) -> bool: ...
    def __lt__(self, other: time) -> bool: ...
    def __ge__(self, other: time) -> bool: ...
    def __gt__(self, other: time) -> bool: ...
    def __hash__(self) -> int: ...
    def __reduce__(self: Self) -> tuple[Type[Self], tuple[bytes]]: ...
    if sys.version_info >= (3, 8):
        def __reduce_ex__(self: Self, __protocol: SupportsIndex) -> tuple[Type[Self], tuple[bytes]]: ...
    else:
        def __reduce_ex__(self: Self, __protocol: int) -> tuple[Type[Self], tuple[bytes]]: ...
    def isoformat(self, timespec: str = ...) -> str: ...
    if sys.version_info >= (3, 7):
        @classmethod
        def fromisoformat(cls: Type[_S], time_string: str) -> _S: ...
    def strftime(self, fmt: str) -> str: ...
    def __format__(self, fmt: str) -> str: ...
    def utcoffset(self) -> timedelta | None: ...
    def tzname(self) -> str | None: ...
    def dst(self) -> timedelta | None: ...
    def replace(
        self,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
        *,
        fold: int = ...,
    ) -> time: ...

_date = date
_time = time

class timedelta(SupportsAbs[timedelta]):
    min: ClassVar[timedelta]
    max: ClassVar[timedelta]
    resolution: ClassVar[timedelta]
    def __new__(
        cls: Type[_S],
        days: float = ...,
        seconds: float = ...,
        microseconds: float = ...,
        milliseconds: float = ...,
        minutes: float = ...,
        hours: float = ...,
        weeks: float = ...,
    ) -> _S: ...
    @property
    def days(self) -> int: ...
    @property
    def seconds(self) -> int: ...
    @property
    def microseconds(self) -> int: ...
    def total_seconds(self) -> float: ...
    def __add__(self, other: timedelta) -> timedelta: ...
    def __radd__(self, other: timedelta) -> timedelta: ...
    def __sub__(self, other: timedelta) -> timedelta: ...
    def __rsub__(self, other: timedelta) -> timedelta: ...
    def __neg__(self) -> timedelta: ...
    def __pos__(self) -> timedelta: ...
    def __abs__(self) -> timedelta: ...
    def __mul__(self, other: float) -> timedelta: ...
    def __rmul__(self, other: float) -> timedelta: ...
    @overload
    def __floordiv__(self, other: timedelta) -> int: ...
    @overload
    def __floordiv__(self, other: int) -> timedelta: ...
    @overload
    def __truediv__(self, other: timedelta) -> float: ...
    @overload
    def __truediv__(self, other: float) -> timedelta: ...
    def __mod__(self, other: timedelta) -> timedelta: ...
    def __divmod__(self, other: timedelta) -> tuple[int, timedelta]: ...
    def __le__(self, other: timedelta) -> bool: ...
    def __lt__(self, other: timedelta) -> bool: ...
    def __ge__(self, other: timedelta) -> bool: ...
    def __gt__(self, other: timedelta) -> bool: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __reduce__(self: Self) -> tuple[type[Self], tuple[int, int, int]]: ...

class datetime(date):
    min: ClassVar[datetime]
    max: ClassVar[datetime]
    resolution: ClassVar[timedelta]
    def __new__(
        cls: Type[_S],
        year: int,
        month: int,
        day: int,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
        *,
        fold: int = ...,
    ) -> _S: ...
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> _tzinfo | None: ...
    @property
    def fold(self) -> int: ...
    @classmethod
    def fromtimestamp(cls: Type[_S], t: float, tz: _tzinfo | None = ...) -> _S: ...
    @classmethod
    def utcfromtimestamp(cls: Type[_S], t: float) -> _S: ...
    @classmethod
    def today(cls: Type[_S]) -> _S: ...
    @classmethod
    def fromordinal(cls: Type[_S], n: int) -> _S: ...
    if sys.version_info >= (3, 8):
        @classmethod
        def now(cls: Type[_S], tz: _tzinfo | None = ...) -> _S: ...
    else:
        @overload
        @classmethod
        def now(cls: Type[_S], tz: None = ...) -> _S: ...
        @overload
        @classmethod
        def now(cls, tz: _tzinfo) -> datetime: ...
    @classmethod
    def utcnow(cls: Type[_S]) -> _S: ...
    @classmethod
    def combine(cls, date: _date, time: _time, tzinfo: _tzinfo | None = ...) -> datetime: ...
    if sys.version_info >= (3, 7):
        @classmethod
        def fromisoformat(cls: Type[_S], date_string: str) -> _S: ...
    def strftime(self, fmt: str) -> str: ...
    def __format__(self, fmt: str) -> str: ...
    def toordinal(self) -> int: ...
    def timetuple(self) -> struct_time: ...
    def timestamp(self) -> float: ...
    def utctimetuple(self) -> struct_time: ...
    def date(self) -> _date: ...
    def time(self) -> _time: ...
    def timetz(self) -> _time: ...
    def replace(
        self,
        year: int = ...,
        month: int = ...,
        day: int = ...,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
        *,
        fold: int = ...,
    ) -> datetime: ...
    if sys.version_info >= (3, 8):
        def astimezone(self: _S, tz: _tzinfo | None = ...) -> _S: ...
    else:
        def astimezone(self, tz: _tzinfo | None = ...) -> datetime: ...
    def ctime(self) -> str: ...
    def isoformat(self, sep: str = ..., timespec: str = ...) -> str: ...
    @classmethod
    def strptime(cls, date_string: str, format: str) -> datetime: ...
    def utcoffset(self) -> timedelta | None: ...
    def tzname(self) -> str | None: ...
    def dst(self) -> timedelta | None: ...
    def __le__(self, other: datetime) -> bool: ...  # type: ignore
    def __lt__(self, other: datetime) -> bool: ...  # type: ignore
    def __ge__(self, other: datetime) -> bool: ...  # type: ignore
    def __gt__(self, other: datetime) -> bool: ...  # type: ignore
    if sys.version_info >= (3, 8):
        def __add__(self: _S, other: timedelta) -> _S: ...
        def __radd__(self: _S, other: timedelta) -> _S: ...
    else:
        def __add__(self, other: timedelta) -> datetime: ...
        def __radd__(self, other: timedelta) -> datetime: ...
    @overload  # type: ignore
    def __sub__(self, other: datetime) -> timedelta: ...
    @overload
    def __sub__(self, other: timedelta) -> datetime: ...
    def __hash__(self) -> int: ...
    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    if sys.version_info >= (3, 9):
        def isocalendar(self) -> _IsoCalendarDate: ...
    else:
        def isocalendar(self) -> tuple[int, int, int]: ...
