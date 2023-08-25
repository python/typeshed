from _typeshed import Incomplete

from ..core import IslamoWesternCalendar

class Nigeria(IslamoWesternCalendar):
    include_labour_day: bool
    labour_day_label: ClassVar[str]
    include_good_friday: bool
    include_easter_monday: bool
    include_boxing_day: bool
    include_eid_al_fitr: bool
    include_day_of_sacrifice: bool
    shift_sunday_holidays: bool
    shift_new_years_day: bool
    WEEKEND_DAYS: Incomplete
    FIXED_HOLIDAYS: Incomplete
    def get_fixed_holidays(self, year): ...
