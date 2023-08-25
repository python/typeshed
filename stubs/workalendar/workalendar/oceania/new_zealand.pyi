from _typeshed import Incomplete

from ..core import WesternCalendar

class NewZealand(WesternCalendar):
    include_good_friday: bool
    include_easter_monday: bool
    include_boxing_day: bool
    FIXED_HOLIDAYS: Incomplete
    def get_queens_birthday(self, year): ...
    def get_labour_day(self, year): ...
    def get_variable_days(self, year): ...
