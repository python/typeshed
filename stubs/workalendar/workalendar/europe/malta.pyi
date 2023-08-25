from _typeshed import Incomplete

from ..core import WesternCalendar

class Malta(WesternCalendar):
    include_good_friday: bool
    include_assumption: bool
    include_immaculate_conception: bool
    include_christmas: bool
    include_labour_day: bool
    labour_day_label: str
    FIXED_HOLIDAYS: Incomplete
