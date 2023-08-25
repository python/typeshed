from _typeshed import Incomplete

from ..core import WesternCalendar

class Slovakia(WesternCalendar):
    include_epiphany: bool
    include_easter_monday: bool
    include_good_friday: bool
    include_all_saints: bool
    include_christmas_eve: bool
    include_boxing_day: bool
    boxing_day_label: str
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
