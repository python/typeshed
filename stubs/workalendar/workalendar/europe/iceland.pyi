from _typeshed import Incomplete

from ..core import WesternCalendar

class Iceland(WesternCalendar):
    include_holy_thursday: bool
    include_good_friday: bool
    include_easter_monday: bool
    include_ascension: bool
    include_whit_monday: bool
    include_christmas_eve: bool
    include_boxing_day: bool
    boxing_day_label: ClassVar[str]
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    def get_first_day_of_summer(self, year): ...
    def get_commerce_day(self, year): ...
    def get_variable_days(self, year): ...
