from _typeshed import Incomplete

from ..core import WesternCalendar

class Panama(WesternCalendar):
    include_labour_day: bool
    include_good_friday: bool
    include_easter_saturday: bool
    include_easter_sunday: bool
    FIXED_HOLIDAYS: Incomplete
    def get_variable_days(self, year): ...
