from _typeshed import Incomplete
from typing import ClassVar

from ..core import OrthodoxCalendar

class Romania(OrthodoxCalendar):
    include_labour_day: ClassVar[bool]
    FIXED_HOLIDAYS: Incomplete
    include_good_friday: ClassVar[bool]
    include_easter_sunday: ClassVar[bool]
    include_easter_monday: ClassVar[bool]
    include_whit_sunday: ClassVar[bool]
    whit_sunday_label: ClassVar[str]
    include_whit_monday: ClassVar[bool]
    include_christmas: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    boxing_day_label: ClassVar[str]
    include_orthodox_christmas: ClassVar[bool]
    def get_childrens_day(self, year): ...
    def get_liberation_day(self, year): ...
    def get_variable_days(self, year): ...
