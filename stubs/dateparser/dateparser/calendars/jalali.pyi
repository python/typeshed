from typing import Any

from dateparser.calendars.jalali_parser import jalali_parser

from . import CalendarBase

class JalaliCalendar(CalendarBase):
    parser: Any = ...
