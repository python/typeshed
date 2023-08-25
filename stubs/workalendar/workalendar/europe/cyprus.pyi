from _typeshed import Incomplete

from ..core import WesternCalendar

class Cyprus(WesternCalendar):
    include_labour_day: bool
    include_epiphany: bool
    include_clean_monday: bool
    include_good_friday: bool
    include_easter_saturday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_whit_monday: bool
    whit_monday_label: ClassVar[str]
    include_christmas_eve: bool
    include_christmas_day: bool
    include_boxing_day: bool
    FIXED_HOLIDAYS: Incomplete
    def get_variable_days(self, year): ...
