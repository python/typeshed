from datetime import date
from typing import ClassVar

from . import CalendarBase, non_gregorian_parser

class _minguo:
    @classmethod
    def to_gregorian(cls, year: int, month: int, day: int) -> tuple[int, int, int]: ...
    @classmethod
    def from_gregorian(cls, year: int, month: int, day: int) -> tuple[int, int, int]: ...
    @classmethod
    def month_length(cls, year: int, month: int) -> int: ...

class _minguo_parser(non_gregorian_parser):
    calendar_converter: ClassVar[type[_minguo]]
    non_gregorian_date_cls: ClassVar[type[date]]
    def handle_two_digit_year(self, year: int) -> int: ...

class MinguoCalendar(CalendarBase):
    parser: type[_minguo_parser]
