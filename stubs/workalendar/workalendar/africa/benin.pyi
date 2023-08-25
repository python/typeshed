from _typeshed import Incomplete

from ..core import IslamoWesternCalendar

class Benin(IslamoWesternCalendar):
    include_labour_day: bool
    include_easter_monday: bool
    include_ascension: bool
    include_whit_monday: bool
    include_assumption: bool
    include_all_saints: bool
    include_prophet_birthday: bool
    include_eid_al_fitr: bool
    include_day_of_sacrifice: bool
    include_day_of_sacrifice_label: ClassVar[str]
    FIXED_HOLIDAYS: Incomplete
    WEEKEND_DAYS: Incomplete
