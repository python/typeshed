from _typeshed import Incomplete

from ..core import WesternCalendar

class Ireland(WesternCalendar):
    include_easter_monday: bool
    include_boxing_day: bool
    boxing_day_label: str
    shift_new_years_day: bool
    def get_june_holiday(self, year): ...
    def get_august_holiday(self, year): ...
    include_whit_monday: Incomplete
    def get_variable_days(self, year): ...
