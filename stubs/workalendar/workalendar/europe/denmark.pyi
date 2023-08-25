from ..core import WesternCalendar

class Denmark(WesternCalendar):
    include_holy_thursday: bool
    include_good_friday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_ascension: bool
    include_whit_sunday: bool
    whit_sunday_label: str
    include_whit_monday: bool
    whit_monday_label: str
    include_boxing_day: bool
    boxing_day_label: str
    include_christmas_eve: bool
    def get_store_bededag(self, year): ...
    def get_variable_days(self, year): ...
