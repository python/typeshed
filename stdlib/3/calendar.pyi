import datetime

from time import struct_time
from typing import Any, Iterable, List, Optional, Sequence, Tuple, Union


LocaleType = Tuple[Optional[str], Optional[str]]

class IllegalMonthError(ValueError):
    def __init__(self, month: int) -> None: ...
    def __str__(self) -> str: ...

class IllegalWeekdayError(ValueError):
    def __init__(self, weekday: int) -> None: ...
    def __str__(self) -> str: ...

def isleap(year: int) -> bool: ...
def leapdays(y1: int, y2: int) -> int: ...
def weekday(year: int, month: int, day: int) -> int: ...
def monthrange(year: int, month: int) -> Tuple[int, int]: ...

class Calendar:
    def __init__(self, firstweekday: int = ...) -> None: ...
    def getfirstweekday(self) -> int: ...
    def setfirstweekday(self, firstweekday: int) -> None: ...
    def iterweekdays(self) -> Iterable[int]: ...
    def itermonthdates(self, year: int, month: int) -> Iterable[datetime.date]: ...
    def itermonthdays2(self, year: int, month: int) -> Iterable[Tuple[int, int]]: ...
    def itermonthdays(self, year: int, month: int) -> Iterable[int]: ...
    def monthdatescalendar(self, year: int, month: int) -> List[List[datetime.date]]: ...
    def monthdays2calendar(self, year: int, month: int) -> List[List[Tuple[int, int]]]: ...
    def monthdayscalendar(self, year: int, month: int) -> List[List[int]]: ...
    def yeardatescalendar(self, year: int, width: int = ...) -> List[List[int]]: ...
    def yeardays2calendar(self, year: int, width: int = ...) -> List[List[Tuple[int, int]]]: ...
    def yeardayscalendar(self, year: int, width: int = ...) -> List[List[int]]: ...

class TextCalendar(Calendar):
    def prweek(self, theweek: int, width: int) -> None: ...
    def formatday(self, day: int, weekday: int, width: int) -> str: ...
    def formatweek(self, theweek: int, width: int) -> str: ...
    def formatweekday(self, day: int, width: int) -> str: ...
    def formatweekheader(self, width: int) -> str: ...
    def formatmonthname(self, theyear: int, themonth: int, width: int, withyear: bool = ...) -> str: ...
    def prmonth(self, theyear: int, themonth: int, w: Any=0, l: Any = 0) -> None: ...
    def formatmonth(self, theyear: int, themonth: int, w: int = ..., l: int = ...) -> str: ...
    def formatyear(self, theyear: int, w: int = ..., l: int = ..., c: int = ..., m: int = ...) -> str: ...
    def pryear(self, theyear: int, w: Any = 0, l: Any = 0, c: Any = 6, m: Any = 3) -> None: ...

class HTMLCalendar(Calendar):
    def formatday(self, day: int, weekday: int) -> str: ...
    def formatweek(self, theweek: int) -> str: ...
    def formatweekday(self, day: int) -> str: ...
    def formatweekheader(self) -> str: ...
    def formatmonthname(self, theyear: int, themonth: int, withyear: bool = ...) -> str: ...
    def formatmonth(self, theyear: int, themonth: int, withyear: bool = ...) -> str: ...
    def formatyear(self, theyear: int, width: int = ...) -> str: ...
    def formatyearpage(self, theyear: int, width: int = ..., css: Optional[str] = ..., encoding: Optional[str] = ...) -> str: ...

class different_locale:
    def __init__(self, locale: LocaleType) -> None: ...
    def __enter__(self) -> LocaleType: ...
    def __exit__(self, *args) -> None: ...

class LocaleTextCalendar(TextCalendar):
    def __init__(self, firstweekday: int = ..., locale: Optional[LocaleType] = ...) -> None: ...
    def formatweekday(self, day: int, width: int) -> str: ...
    def formatmonthname(self, theyear: int, themonth: int, width: int, withyear: bool = ...) -> str: ...

class LocaleHTMLCalendar(HTMLCalendar):
    def __init__(self, firstweekday: int = ..., locale: Optional[LocaleType] = ...) -> None: ...
    def formatweekday(self, day: int) -> str: ...
    def formatmonthname(self, theyear: int, themonth: int, withyear: bool = ...) -> str: ...

c = ...  # type: TextCalendar
def setfirstweekday(firstweekday: int) -> None: ...
def format(cols: int, colwidth: int = ..., spacing: int = ...) -> str: ...
def formatstring(cols: int, colwidth: int = ..., spacing: int = ...) -> str: ...
def timegm(tuple: Union[Tuple[int, ...], struct_time]) -> int: ...

# Data attributes
day_name = ...  # type: Sequence[str]
day_abbr = ...  # type: Sequence[str]
month_name = ...  # type: Sequence[str]
month_abbr = ...  # type: Sequence[str]

# Below constants are not in docs or __all__, but enough people have used them
# they are now effectively public.

MONDAY = ...  # type: int
TUESDAY = ...  # type: int
WEDNESDAY = ...  # type: int
THURSDAY = ...  # type: int
FRIDAY = ...  # type: int
SATURDAY = ...  # type: int
SUNDAY = ...  # type: int
