from _typeshed import Incomplete

from ..core import WesternCalendar

class EuropeanCentralBank(WesternCalendar):
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_good_friday: bool
    include_easter_monday: bool
