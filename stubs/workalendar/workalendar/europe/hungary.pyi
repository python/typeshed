from _typeshed import Incomplete

from ..core import WesternCalendar

class Hungary(WesternCalendar):
    include_easter_sunday: bool
    include_easter_monday: bool
    include_whit_sunday: bool
    whit_sunday_label: str
    include_whit_monday: bool
    whit_monday_label: str
    include_boxing_day: bool
    boxing_day_label: str
    include_all_saints: bool
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_good_friday: Incomplete
    def get_variable_days(self, year): ...
