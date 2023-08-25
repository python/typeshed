from _typeshed import Incomplete
from collections.abc import Generator

from ..core import IslamoWesternCalendar

class Kenya(IslamoWesternCalendar):
    include_labour_day: bool
    include_good_friday: bool
    include_easter_monday: bool
    include_eid_al_fitr: bool
    include_day_of_sacrifice: bool
    shift_sunday_holidays: bool
    WEEKEND_DAYS: Incomplete
    FIXED_HOLIDAYS: Incomplete
    def get_fixed_holidays(self, year): ...
    def get_shifted_holidays(self, dates) -> Generator[Incomplete, None, None]: ...
    def get_calendar_holidays(self, year): ...
