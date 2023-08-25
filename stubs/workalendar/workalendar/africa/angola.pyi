from _typeshed import Incomplete

from ..core import WesternCalendar

class Angola(WesternCalendar):
    include_labour_day: bool
    labour_day_label: ClassVar[str]
    include_fat_tuesday: bool
    fat_tuesday_label: ClassVar[str]
    include_good_friday: bool
    include_easter_sunday: bool
    include_christmas: bool
    include_all_souls: bool
    FIXED_HOLIDAYS: Incomplete
