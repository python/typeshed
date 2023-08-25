from _typeshed import Incomplete

from ..core import ChineseNewYearCalendar, IslamicMixin, WesternMixin

class Philippines(WesternMixin, IslamicMixin, ChineseNewYearCalendar):
    include_labour_day: bool
    include_new_years_eve: bool
    include_holy_thursday: bool
    holy_thursday_label: str
    include_good_friday: bool
    include_easter_saturday: bool
    include_easter_sunday: bool
    easter_saturday_label: str
    include_all_saints: bool
    include_all_souls: bool
    include_immaculate_conception: bool
    include_christmas_eve: bool
    include_eid_al_fitr: bool
    eid_al_fitr_label: str
    include_eid_al_adha: bool
    day_of_sacrifice_label: str
    WEEKEND_DAYS: Incomplete
    FIXED_HOLIDAYS: Incomplete
