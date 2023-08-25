from _typeshed import Incomplete

from ..core import WesternCalendar

class ElSalvador(WesternCalendar):
    include_labour_day: bool
    include_holy_thursday: bool
    include_good_friday: bool
    include_easter_saturday: bool
    FIXED_HOLIDAYS: Incomplete
