from typing import Any

from dateparser.calendars import CalendarBase as CalendarBase
from dateparser.calendars.hijri_parser import hijri_parser as hijri_parser

class HijriCalendar(CalendarBase):
    parser: Any = ...
