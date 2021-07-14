from typing import Any

from dateparser.calendars.jalali_parser import jalali_parser as jalali_parser

from . import CalendarBase as CalendarBase

class JalaliCalendar(CalendarBase):
    parser: Any = ...
