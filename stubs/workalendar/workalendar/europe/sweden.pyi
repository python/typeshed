from _typeshed import Incomplete

from ..core import WesternCalendar

class Sweden(WesternCalendar):
    include_epiphany: bool
    include_good_friday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_ascension: bool
    include_whit_sunday: bool
    whit_sunday_label: str
    include_christmas_eve: bool
    include_boxing_day: bool
    boxing_day_label: str
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    def get_midsummer_eve(self, year): ...
    def get_midsummer_day(self, year): ...
    def get_variable_all_saints(self, year): ...
    def get_variable_days(self, year): ...
