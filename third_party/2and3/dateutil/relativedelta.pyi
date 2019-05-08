from typing import overload, Any, List, Optional, SupportsFloat, TypeVar, Union
from datetime import date, datetime, timedelta

from ._common import weekday

_S = TypeVar('_S', bound=relativedelta)
_D = TypeVar('_D', date, datetime)
# Work around attribute and type having the same name.
_weekday = weekday

MO: weekday
TU: weekday
WE: weekday
TH: weekday
FR: weekday
SA: weekday
SU: weekday


class relativedelta(object):
    years: int
    months: int
    days: int
    leapdays: int
    hours: int
    minutes: int
    seconds: int
    microseconds: int
    year: Optional[int]
    month: Optional[int]
    weekday: Optional[_weekday]
    day: Optional[int]
    hour: Optional[int]
    minute: Optional[int]
    second: Optional[int]
    microsecond: Optional[int]
    def __init__(self,
                 dt1: Optional[date] = ...,
                 dt2: Optional[date] = ...,
                 years: Optional[int] = ..., months: Optional[int] = ...,
                 days: Optional[int] = ..., leapdays: Optional[int] = ...,
                 weeks: Optional[int] = ...,
                 hours: Optional[int] = ..., minutes: Optional[int] = ...,
                 seconds: Optional[int] = ..., microseconds: Optional[int] = ...,
                 year: Optional[int] = ..., month: Optional[int] = ...,
                 day: Optional[int] = ...,
                 weekday: Optional[Union[int, _weekday]] = ...,
                 yearday: Optional[int] = ...,
                 nlyearday: Optional[int] = ...,
                 hour: Optional[int] = ..., minute: Optional[int] = ...,
                 second: Optional[int] = ...,
                 microsecond: Optional[int] = ...) -> None: ...
    @property
    def weeks(self) -> int: ...
    @weeks.setter
    def weeks(self, value: int) -> None: ...
    def normalized(self: _S) -> _S: ...
    # TODO: use Union when mypy will handle it properly in overloaded operator
    # methods (#2129, #1442, #1264 in mypy)
    @overload
    def __add__(self: _S, other: relativedelta) -> _S: ...
    @overload
    def __add__(self: _S, other: timedelta) -> _S: ...
    @overload
    def __add__(self, other: _D) -> _D: ...
    @overload
    def __radd__(self: _S, other: relativedelta) -> _S: ...
    @overload
    def __radd__(self: _S, other: timedelta) -> _S: ...
    @overload
    def __radd__(self, other: _D) -> _D: ...
    @overload
    def __rsub__(self: _S, other: relativedelta) -> _S: ...
    @overload
    def __rsub__(self: _S, other: timedelta) -> _S: ...
    @overload
    def __rsub__(self, other: _D) -> _D: ...
    def __sub__(self: _S, other: relativedelta) -> _S: ...
    def __neg__(self: _S) -> _S: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __mul__(self: _S, other: SupportsFloat) -> _S: ...
    def __rmul__(self: _S, other: SupportsFloat) -> _S: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __div__(self: _S, other: SupportsFloat) -> _S: ...
    def __truediv__(self: _S, other: SupportsFloat) -> _S: ...
    def __repr__(self) -> str: ...
