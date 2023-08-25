from _typeshed import Incomplete

from ..core import IslamicCalendar

class Turkey(IslamicCalendar):
    shift_new_years_day: bool
    WEEKEND_DAYS: Incomplete
    include_eid_al_fitr: bool
    length_eid_al_fitr: int
    include_eid_al_adha: bool
    length_eid_al_adha: int
    include_labour_day: bool
    labour_day_label: str
    FIXED_HOLIDAYS: Incomplete
    def get_delta_islamic_holidays(self, year): ...
