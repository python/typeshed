from _typeshed import Incomplete

from ..core import WesternCalendar

class Chile(WesternCalendar):
    FIXED_HOLIDAYS: Incomplete
    include_labour_day: bool
    include_good_friday: bool
    include_easter_saturday: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool
    def get_variable_days(self, year): ...
