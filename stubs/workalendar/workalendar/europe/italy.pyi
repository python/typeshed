from _typeshed import Incomplete

from ..core import WesternCalendar

class Italy(WesternCalendar):
    include_labour_day: bool
    labour_day_label: ClassVar[str]
    FIXED_HOLIDAYS: Incomplete
    include_immaculate_conception: bool
    include_epiphany: bool
    include_easter_monday: bool
    include_assumption: bool
    include_all_saints: bool
    include_boxing_day: bool
    boxing_day_label: ClassVar[str]
