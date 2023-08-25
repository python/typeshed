from _typeshed import Incomplete
from collections.abc import Generator

from ..core import OrthodoxCalendar

class Bulgaria(OrthodoxCalendar):
    FIXED_HOLIDAYS: Incomplete
    include_labour_day: bool
    labour_day_label: str
    include_good_friday: bool
    include_easter_saturday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_christmas_eve: bool
    include_christmas: bool
    include_boxing_day: bool
    include_orthodox_christmas: bool
    boxing_day_label: str
    def get_shifted_holidays(self, days) -> Generator[Incomplete, None, None]: ...
    def get_fixed_holidays(self, year): ...
    def shift_christmas_boxing_days(self, year): ...
    def get_variable_days(self, year): ...
