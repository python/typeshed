from dateparser.calendars import CalendarBase as CalendarBase
from dateparser.calendars.hijri_parser import hijri_parser as hijri_parser
from typing import Any

class HijriCalendar(CalendarBase):
    parser: Any = ...
