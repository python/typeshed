import datetime
from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from typing import Final, Literal, TypeAlias, overload
from typing_extensions import Self

from dateutil.parser._parser import _TzInfos

from ._common import _Gettable, _Weekday, weekday as weekdaybase

__all__ = [
    "rrule",
    "rruleset",
    "rrulestr",
    "YEARLY",
    "MONTHLY",
    "WEEKLY",
    "DAILY",
    "HOURLY",
    "MINUTELY",
    "SECONDLY",
    "MO",
    "TU",
    "WE",
    "TH",
    "FR",
    "SA",
    "SU",
]

M366MASK: Final[tuple[int, ...]]
MDAY366MASK: Final[tuple[int, ...]]
MDAY365MASK: Final[tuple[int, ...]]
NMDAY366MASK: Final[tuple[int, ...]]
NMDAY365MASK: Final[list[int]]
M366RANGE: Final[tuple[int, ...]]
M365RANGE: Final[tuple[int, ...]]
WDAYMASK: Final[list[int]]
M365MASK: Final[tuple[int, ...]]
FREQNAMES: Final[list[str]]
YEARLY: Final = 0
MONTHLY: Final = 1
WEEKLY: Final = 2
DAILY: Final = 3
HOURLY: Final = 4
MINUTELY: Final = 5
SECONDLY: Final = 6

class weekday(weekdaybase): ...

weekdays: tuple[weekday, weekday, weekday, weekday, weekday, weekday, weekday]
MO: weekday
TU: weekday
WE: weekday
TH: weekday
FR: weekday
SA: weekday
SU: weekday

class rrulebase:
    def __init__(self, cache: bool | None = False) -> None: ...
    def __iter__(self) -> Iterator[datetime.datetime]: ...

    @overload
    def __getitem__(self, item: int) -> datetime.datetime: ...
    @overload
    def __getitem__(self, item: slice) -> Sequence[datetime.datetime]: ...

    def __contains__(self, item: datetime.datetime) -> bool: ...
    def count(self) -> int: ...
    def before(self, dt: datetime.datetime, inc: bool = False) -> datetime.datetime | None: ...
    def after(self, dt: datetime.datetime, inc: bool = False) -> datetime.datetime | None: ...
    def xafter(self, dt: datetime.datetime, count: int | None = None, inc: bool = False) -> Generator[datetime.datetime]: ...
    def between(
        self, after: datetime.datetime, before: datetime.datetime, inc: bool = False, count: int = 1
    ) -> list[datetime.datetime]: ...

class rrule(rrulebase):
    def __init__(
        self,
        freq: int,
        dtstart: datetime.date | None = None,
        interval: int = 1,
        wkst: _Weekday | int | None = None,
        count: int | None = None,
        until: datetime.date | None = None,
        bysetpos: int | Iterable[int] | None = None,
        bymonth: int | Iterable[int] | None = None,
        bymonthday: int | Iterable[int] | None = None,
        byyearday: int | Iterable[int] | None = None,
        byeaster: int | Iterable[int] | None = None,
        byweekno: int | Iterable[int] | None = None,
        byweekday: int | _Weekday | Iterable[int | _Weekday] | None = None,
        byhour: int | Iterable[int] | None = None,
        byminute: int | Iterable[int] | None = None,
        bysecond: int | Iterable[int] | None = None,
        cache: bool | None = False,
    ) -> None: ...
    def replace(
        self,
        *,
        freq: int = ...,
        dtstart: datetime.date | None = ...,
        interval: int = ...,
        wkst: _Weekday | int | None = ...,
        count: int | None = ...,
        until: datetime.date | None = ...,
        bysetpos: int | Iterable[int] | None = None,
        bymonth: int | Iterable[int] | None = None,
        bymonthday: int | Iterable[int] | None = None,
        byyearday: int | Iterable[int] | None = None,
        byeaster: int | Iterable[int] | None = None,
        byweekno: int | Iterable[int] | None = None,
        byweekday: int | _Weekday | Iterable[int | _Weekday] | None = None,
        byhour: int | Iterable[int] | None = None,
        byminute: int | Iterable[int] | None = None,
        bysecond: int | Iterable[int] | None = None,
        cache: bool | None = ...,
    ) -> rrule: ...

_RRule: TypeAlias = rrule

class _iterinfo:
    __slots__ = [
        "rrule",
        "lastyear",
        "lastmonth",
        "yearlen",
        "nextyearlen",
        "yearordinal",
        "yearweekday",
        "mmask",
        "mrange",
        "mdaymask",
        "nmdaymask",
        "wdaymask",
        "wnomask",
        "nwdaymask",
        "eastermask",
    ]
    rrule: _RRule
    def __init__(self, rrule: _RRule) -> None: ...
    yearlen: int | None
    nextyearlen: int | None
    yearordinal: int | None
    yearweekday: int | None
    mmask: Sequence[int] | None
    mdaymask: Sequence[int] | None
    nmdaymask: Sequence[int] | None
    wdaymask: Sequence[int] | None
    mrange: Sequence[int] | None
    wnomask: Sequence[int] | None
    nwdaymask: Sequence[int] | None
    eastermask: Sequence[int] | None
    lastyear: int | None
    lastmonth: int | None
    def rebuild(self, year: int, month: int) -> None: ...
    def ydayset(self, year: int, month: int, day: int) -> tuple[Iterable[int | None], int, int]: ...
    def mdayset(self, year: int, month: int, day: int) -> tuple[Iterable[int | None], int, int]: ...
    def wdayset(self, year: int, month: int, day: int) -> tuple[Iterable[int | None], int, int]: ...
    def ddayset(self, year: int, month: int, day: int) -> tuple[Iterable[int | None], int, int]: ...
    def htimeset(self, hour: int, minute: int, second: int) -> list[datetime.time]: ...
    def mtimeset(self, hour: int, minute: int, second: int) -> list[datetime.time]: ...
    def stimeset(self, hour: int, minute: int, second: int) -> tuple[datetime.time, ...]: ...

class rruleset(rrulebase):
    class _genitem:
        dt: datetime.datetime
        genlist: list[Self]
        gen: Iterator[datetime.datetime]
        def __init__(self, genlist: list[Self], gen: Iterator[datetime.datetime]) -> None: ...
        def __next__(self) -> None: ...
        next = __next__
        def __lt__(self, other: Self) -> bool: ...
        def __gt__(self, other: Self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...

    def __init__(self, cache: bool | None = False) -> None: ...
    def rrule(self, rrule: Iterable[datetime.datetime]) -> None: ...
    def rdate(self, rdate: datetime.datetime) -> None: ...
    def exrule(self, exrule: Iterable[datetime.datetime]) -> None: ...
    def exdate(self, exdate: datetime.datetime) -> None: ...

class _rrulestr:
    @overload
    def __call__(
        self,
        s: str,
        *,
        forceset: Literal[True],
        dtstart: datetime.date | None = None,
        cache: bool | None = None,
        unfold: bool = False,
        compatible: bool = False,
        ignoretz: bool = False,
        tzids: Callable[[str], datetime.tzinfo | None] | _Gettable[str, datetime.tzinfo] | None = None,
        tzinfos: _TzInfos | None = None,
    ) -> rruleset: ...
    @overload
    def __call__(
        self,
        s: str,
        *,
        compatible: Literal[True],
        dtstart: datetime.date | None = None,
        cache: bool | None = None,
        unfold: bool = False,
        forceset: bool = False,
        ignoretz: bool = False,
        tzids: Callable[[str], datetime.tzinfo | None] | _Gettable[str, datetime.tzinfo] | None = None,
        tzinfos: _TzInfos | None = None,
    ) -> rruleset: ...
    @overload
    def __call__(
        self,
        s: str,
        *,
        dtstart: datetime.date | None = None,
        cache: bool | None = False,
        unfold: bool = False,
        forceset: bool = False,
        compatible: bool = False,
        ignoretz: bool = False,
        tzids: Callable[[str], datetime.tzinfo | None] | _Gettable[str, datetime.tzinfo] | None = None,
        tzinfos: _TzInfos | None = None,
    ) -> rrule | rruleset: ...

rrulestr: _rrulestr
