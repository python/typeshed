from _typeshed import Incomplete

from ..core import WesternCalendar

class Portugal(WesternCalendar):
    include_good_friday: bool
    include_easter_sunday: bool
    include_christmas: bool
    include_immaculate_conception: bool
    immaculate_conception_label: str
    include_labour_day: bool
    labour_day_label: str
    FIXED_HOLIDAYS: Incomplete
    def get_fixed_holidays(self, year): ...
    def get_variable_days(self, year): ...
