from abc import abstractmethod
from datetime import datetime, tzinfo
from typing import ClassVar, Literal, Protocol, type_check_only

from dateparser.conf import Settings
from dateparser.date import DateData
from dateparser.parser import _parser

# Examples: `hijri_parser.hijri` class or `convertdate.persian` module
@type_check_only
class _CalendarConverter(Protocol):
    @classmethod
    def to_gregorian(cls, year: int, month: int, day: int) -> tuple[int, int, int]: ...
    @classmethod
    def from_gregorian(cls, year: int, month: int, day: int) -> tuple[int, int, int]: ...
    @classmethod
    def month_length(cls, year: int, month: int) -> int: ...

# Examples: `hijri_parser.HijriDate`, `jalali_parser.PersianDate` or `datetime.date`
@type_check_only
class _NonGregorianDate(Protocol):
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    def __init__(self, year: int, month: int, day: int) -> None: ...

class CalendarBase:
    parser: type[_parser]
    source: str
    def __init__(self, source: str) -> None: ...
    def get_date(self) -> DateData | None: ...

class non_gregorian_parser(_parser):
    calendar_converter: ClassVar[type[_CalendarConverter]]
    default_year: ClassVar[int]
    default_month: ClassVar[int]
    default_day: ClassVar[int]
    non_gregorian_date_cls: ClassVar[type[_NonGregorianDate]]
    @classmethod
    def to_latin(cls, source: str) -> str: ...
    @abstractmethod
    def handle_two_digit_year(self, year: int) -> int: ...
    @classmethod
    def parse(
        cls,
        datestring: str,
        settings: Settings,
        tz: tzinfo | None = None,
        date_order: Literal["DMY", "DYM", "MDY", "MYD", "YDM", "YMD"] | None = None,
    ) -> tuple[datetime, str | None]: ...
