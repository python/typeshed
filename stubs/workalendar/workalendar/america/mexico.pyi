from _typeshed import Incomplete

from ..core import WesternCalendar

class Mexico(WesternCalendar):
    FIXED_HOLIDAYS: Incomplete
    include_labour_day: bool
    def get_variable_days(self, year): ...
    def get_calendar_holidays(self, year): ...
