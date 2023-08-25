from _typeshed import Incomplete

from ..core import OrthodoxCalendar

class Romania(OrthodoxCalendar):
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_good_friday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_whit_sunday: bool
    whit_sunday_label: ClassVar[str]
    include_whit_monday: bool
    include_christmas: bool
    include_boxing_day: bool
    boxing_day_label: ClassVar[str]
    include_orthodox_christmas: bool
    def get_childrens_day(self, year): ...
    def get_liberation_day(self, year): ...
    def get_variable_days(self, year): ...
