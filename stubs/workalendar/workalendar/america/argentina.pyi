from _typeshed import Incomplete

from ..core import WesternCalendar

class Argentina(WesternCalendar):
    include_labour_day: bool
    labour_day_label: ClassVar[str]
    include_fat_tuesday: bool
    fat_tuesday_label: ClassVar[str]
    include_good_friday: bool
    include_easter_saturday: bool
    include_easter_sunday: bool
    include_christmas: bool
    include_immaculate_conception: bool
    immaculate_conception_label: ClassVar[str]
    FIXED_HOLIDAYS: Incomplete
    def get_general_guemes_day(self, year): ...
    def get_general_martin_day(self, year): ...
    def get_soberania_day(self, year): ...
    def get_diversidad_day(self, year): ...
    def get_malvinas_day(self, year): ...
    def get_variable_days(self, year): ...
