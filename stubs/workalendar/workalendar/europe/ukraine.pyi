from _typeshed import Incomplete

from ..core import OrthodoxCalendar

class Ukraine(OrthodoxCalendar):
    shift_sunday_holidays: bool
    shift_new_years_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_labour_day: bool
    labour_day_label: str
    include_christmas: bool
    include_good_friday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_whit_monday: bool
    def get_variable_days(self, year): ...
