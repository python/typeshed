from _typeshed import Incomplete

from dateparser.calendars import non_gregorian_parser

class PersianDate:
    year: Incomplete
    month: Incomplete
    day: Incomplete
    def __init__(self, year, month, day) -> None: ...
    def weekday(self): ...

class jalali_parser(non_gregorian_parser):
    calendar_converter: Incomplete
    default_year: int
    default_month: int
    default_day: int
    non_gregorian_date_cls: type[PersianDate]
    def handle_two_digit_year(self, year: int) -> int: ...
