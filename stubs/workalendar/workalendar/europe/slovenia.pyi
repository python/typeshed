from _typeshed import Incomplete

from ..core import WesternCalendar

class Slovenia(WesternCalendar):
    include_easter_sunday: bool
    include_easter_monday: bool
    include_whit_sunday: bool
    include_assumption: bool
    include_christmas: bool
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    def get_variable_days(self, year): ...
