from _typeshed import Incomplete

from ..core import WesternCalendar

class Latvia(WesternCalendar):
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_good_friday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_christmas_eve: bool
    include_christmas: bool
    include_boxing_day: bool
    def get_independence_days(self, year): ...
    def get_republic_days(self, year): ...
    def get_variable_days(self, year): ...
