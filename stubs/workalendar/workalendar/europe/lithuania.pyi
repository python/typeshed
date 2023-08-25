from _typeshed import Incomplete

from ..core import WesternCalendar

class Lithuania(WesternCalendar):
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_easter_sunday: bool
    include_easter_monday: bool
    include_assumption: bool
    include_all_saints: bool
    include_christmas_eve: bool
    include_christmas: bool
    include_boxing_day: bool
    boxing_day_label: str
    def get_mothers_day(self, year): ...
    def get_fathers_day(self, year): ...
    include_all_souls: Incomplete
    def get_variable_days(self, year): ...
