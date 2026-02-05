from _typeshed import Incomplete
from abc import abstractmethod

from dateparser.conf import Settings
from dateparser.parser import _parser

class CalendarBase:
    parser: Incomplete
    source: Incomplete
    def __init__(self, source) -> None: ...
    def get_date(self): ...

class non_gregorian_parser(_parser):
    calendar_converter: Incomplete
    default_year: Incomplete
    default_month: Incomplete
    default_day: Incomplete
    non_gregorian_date_cls: Incomplete
    @classmethod
    def to_latin(cls, source): ...
    @abstractmethod
    def handle_two_digit_year(self, year: int) -> int: ...
    @classmethod
    def parse(cls, datestring: str, settings: Settings) -> tuple[Incomplete, Incomplete]: ...  # type: ignore[override]
