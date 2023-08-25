from _typeshed import Incomplete

from ..core import WesternCalendar

class Estonia(WesternCalendar):
    include_good_friday: bool
    include_easter_sunday: bool
    include_whit_sunday: bool
    whit_sunday_label: ClassVar[str]
    include_christmas_eve: bool
    include_christmas: bool
    include_boxing_day: bool
    boxing_day_label: ClassVar[str]
    FIXED_HOLIDAYS: Incomplete
