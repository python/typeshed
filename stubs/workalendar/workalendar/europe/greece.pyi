from _typeshed import Incomplete

from ..core import OrthodoxCalendar

class Greece(OrthodoxCalendar):
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_epiphany: bool
    include_clean_monday: bool
    include_annunciation: bool
    include_good_friday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_whit_sunday: bool
    whit_sunday_label: str
    include_whit_monday: bool
    include_assumption: bool
    include_boxing_day: bool
    boxing_day_label: str
    include_orthodox_christmas: bool
