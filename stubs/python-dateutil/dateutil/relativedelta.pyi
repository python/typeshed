from datetime import date, datetime, timedelta
from typing import SupportsFloat, SupportsIndex, TypeAlias, TypeVar, overload
from typing_extensions import Self

# See #9817 for why we reexport this here
from ._common import _Weekday, weekday as weekday

_DateTimeT = TypeVar("_DateTimeT", bound=datetime)

_FloatInput: TypeAlias = SupportsFloat | SupportsIndex | str | bytes | bytearray

MO: weekday
TU: weekday
WE: weekday
TH: weekday
FR: weekday
SA: weekday
SU: weekday

__all__ = ["relativedelta", "MO", "TU", "WE", "TH", "FR", "SA", "SU"]

class relativedelta:
    years: int
    months: int
    days: float
    leapdays: float
    hours: float
    minutes: float
    seconds: float
    microseconds: float
    year: int | None
    month: int | None
    weekday: _Weekday | None
    day: int | None
    hour: int | None
    minute: int | None
    second: int | None
    microsecond: int | None
    def __init__(
        self,
        dt1: date | None = None,
        dt2: date | None = None,
        years: float = 0,
        months: float = 0,
        days: float = 0,
        leapdays: float = 0,
        weeks: float = 0,
        hours: float = 0,
        minutes: float = 0,
        seconds: float = 0,
        microseconds: float = 0,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None,
        weekday: int | _Weekday | None = None,
        yearday: int | None = None,
        nlyearday: int | None = None,
        hour: int | None = None,
        minute: int | None = None,
        second: int | None = None,
        microsecond: int | None = None,
    ) -> None: ...

    @property
    def weeks(self) -> int: ...
    @weeks.setter
    def weeks(self, value: float) -> None: ...

    def normalized(self) -> Self: ...

    @overload
    def __add__(self, other: timedelta | relativedelta) -> Self: ...
    @overload
    def __add__(self, other: _DateTimeT) -> _DateTimeT: ...
    @overload
    def __add__(self, other: date) -> date: ...

    @overload
    def __radd__(self, other: timedelta | relativedelta) -> Self: ...
    @overload
    def __radd__(self, other: _DateTimeT) -> _DateTimeT: ...
    @overload
    def __radd__(self, other: date) -> date: ...

    @overload
    def __rsub__(self, other: timedelta | relativedelta) -> Self: ...
    @overload
    def __rsub__(self, other: _DateTimeT) -> _DateTimeT: ...
    @overload
    def __rsub__(self, other: date) -> date: ...

    def __sub__(self, other: relativedelta) -> Self: ...
    def __neg__(self) -> Self: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __mul__(self, other: _FloatInput) -> Self: ...
    def __rmul__(self, other: _FloatInput) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def __div__(self, other: _FloatInput) -> Self: ...
    def __truediv__(self, other: _FloatInput) -> Self: ...
    def __abs__(self) -> Self: ...
    def __hash__(self) -> int: ...
