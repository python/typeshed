from . import CalendarBase as CalendarBase
from dateparser.calendars.jalali_parser import jalali_parser as jalali_parser
from typing import Any

class JalaliCalendar(CalendarBase):
    parser: Any = ...
