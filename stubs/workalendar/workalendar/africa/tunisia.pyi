from _typeshed import Incomplete

from ..core import IslamicCalendar

class Tunisia(IslamicCalendar):
    include_labour_day: bool
    include_prophet_birthday: bool
    include_eid_al_fitr: bool
    length_eid_al_fitr: int
    include_day_of_sacrifice: bool
    length_eid_al_adha: int
    include_islamic_new_year: bool
    FIXED_HOLIDAYS: Incomplete
    WEEKEND_DAYS: Incomplete
    def get_fixed_holidays(self, year): ...
