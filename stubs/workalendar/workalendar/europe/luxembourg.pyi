from _typeshed import Incomplete

from ..core import WesternCalendar

class Luxembourg(WesternCalendar):
    include_easter_monday: bool
    include_ascension: bool
    include_whit_monday: bool
    include_all_saints: bool
    include_assumption: bool
    include_boxing_day: bool
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    def get_fixed_holidays(self, year): ...
