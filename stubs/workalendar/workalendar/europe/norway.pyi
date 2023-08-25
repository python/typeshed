from _typeshed import Incomplete

from ..core import WesternCalendar

class Norway(WesternCalendar):
    include_holy_thursday: bool
    include_good_friday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_ascension: bool
    include_whit_monday: bool
    include_whit_sunday: bool
    include_boxing_day: bool
    boxing_day_label: str
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
