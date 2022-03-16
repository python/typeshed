from _typeshed import Self
from time import struct_time
from typing import AnyStr, ClassVar, SupportsAbs, overload

_Text = str | unicode

MINYEAR: int
MAXYEAR: int

class tzinfo:
    def tzname(self, dt: datetime | None) -> str | None: ...
    def utcoffset(self, dt: datetime | None) -> timedelta | None: ...
    def dst(self, dt: datetime | None) -> timedelta | None: ...
    def fromutc(self, dt: datetime) -> datetime: ...

_tzinfo = tzinfo

class date:
    min: ClassVar[date]
    max: ClassVar[date]
    resolution: ClassVar[timedelta]
    def __new__(cls: type[Self], year: int, month: int, day: int) -> Self: ...
    @classmethod
    def fromtimestamp(cls: type[Self], __timestamp: float) -> Self: ...
    @classmethod
    def today(cls: type[Self]) -> Self: ...
    @classmethod
    def fromordinal(cls: type[Self], n: int) -> Self: ...
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    def ctime(self) -> str: ...
    def strftime(self, fmt: _Text) -> str: ...
    def __format__(self, fmt: AnyStr) -> AnyStr: ...
    def isoformat(self) -> str: ...
    def timetuple(self) -> struct_time: ...
    def toordinal(self) -> int: ...
    def replace(self, year: int = ..., month: int = ..., day: int = ...) -> date: ...
    def __le__(self, other: date) -> bool: ...
    def __lt__(self, other: date) -> bool: ...
    def __ge__(self, other: date) -> bool: ...
    def __gt__(self, other: date) -> bool: ...
    def __add__(self, other: timedelta) -> date: ...
    def __radd__(self, other: timedelta) -> date: ...
    @overload
    def __sub__(self, other: timedelta) -> date: ...
    @overload
    def __sub__(self, other: date) -> timedelta: ...
    def __hash__(self) -> int: ...
    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    def isocalendar(self) -> tuple[int, int, int]: ...

class time:
    min: ClassVar[time]
    max: ClassVar[time]
    resolution: ClassVar[timedelta]
    def __new__(
        cls: type[Self],
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
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
    def tzinfo(self) -> _tzinfo | None: ...
    def __le__(self, other: time) -> bool: ...
    def __lt__(self, other: time) -> bool: ...
    def __ge__(self, other: time) -> bool: ...
    def __gt__(self, other: time) -> bool: ...
    def __hash__(self) -> int: ...
    def isoformat(self) -> str: ...
    def strftime(self, fmt: _Text) -> str: ...
    def __format__(self, fmt: AnyStr) -> AnyStr: ...
    def utcoffset(self) -> timedelta | None: ...
    def tzname(self) -> str | None: ...
    def dst(self) -> timedelta | None: ...
    def replace(
        self, hour: int = ..., minute: int = ..., second: int = ..., microsecond: int = ..., tzinfo: _tzinfo | None = ...
    ) -> time: ...

_date = date
_time = time

class timedelta(SupportsAbs[timedelta]):
    min: ClassVar[timedelta]
    max: ClassVar[timedelta]
    resolution: ClassVar[timedelta]
    def __new__(
        cls: type[Self],
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
    def __div__(self, other: timedelta) -> float: ...
    @overload
    def __div__(self, other: float) -> timedelta: ...
    def __le__(self, other: timedelta) -> bool: ...
    def __lt__(self, other: timedelta) -> bool: ...
    def __ge__(self, other: timedelta) -> bool: ...
    def __gt__(self, other: timedelta) -> bool: ...
    def __hash__(self) -> int: ...

class datetime(date):
    min: ClassVar[datetime]
    max: ClassVar[datetime]
    resolution: ClassVar[timedelta]
    def __new__(
        cls: type[Self],
        year: int,
        month: int,
        day: int,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
    ) -> Self: ...
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
    @classmethod
    def fromtimestamp(cls: type[Self], t: float, tz: _tzinfo | None = ...) -> Self: ...
    @classmethod
    def utcfromtimestamp(cls: type[Self], t: float) -> Self: ...
    @classmethod
    def today(cls: type[Self]) -> Self: ...
    @classmethod
    def fromordinal(cls: type[Self], n: int) -> Self: ...
    @overload
    @classmethod
    def now(cls: type[Self], tz: None = ...) -> Self: ...
    @overload
    @classmethod
    def now(cls, tz: _tzinfo) -> datetime: ...
    @classmethod
    def utcnow(cls: type[Self]) -> Self: ...
    @classmethod
    def combine(cls, date: _date, time: _time) -> datetime: ...
    def strftime(self, fmt: _Text) -> str: ...
    def __format__(self, fmt: AnyStr) -> AnyStr: ...
    def toordinal(self) -> int: ...
    def timetuple(self) -> struct_time: ...
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
    ) -> datetime: ...
    def astimezone(self, tz: _tzinfo) -> datetime: ...
    def ctime(self) -> str: ...
    def isoformat(self, sep: str = ...) -> str: ...
    @classmethod
    def strptime(cls, date_string: _Text, format: _Text) -> datetime: ...
    def utcoffset(self) -> timedelta | None: ...
    def tzname(self) -> str | None: ...
    def dst(self) -> timedelta | None: ...
    def __le__(self, other: datetime) -> bool: ...
    def __lt__(self, other: datetime) -> bool: ...
    def __ge__(self, other: datetime) -> bool: ...
    def __gt__(self, other: datetime) -> bool: ...
    def __add__(self, other: timedelta) -> datetime: ...
    def __radd__(self, other: timedelta) -> datetime: ...
    @overload
    def __sub__(self, other: datetime) -> timedelta: ...
    @overload
    def __sub__(self, other: timedelta) -> datetime: ...
    def __hash__(self) -> int: ...
    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    def isocalendar(self) -> tuple[int, int, int]: ...
