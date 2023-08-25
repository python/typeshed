from _typeshed import Incomplete

from ..core import WesternCalendar

class CzechRepublic(WesternCalendar):
    include_labour_day: bool
    include_easter_monday: bool
    include_good_friday: bool
    FIXED_HOLIDAYS: Incomplete
    def get_variable_days(self, year): ...
