from typing import ClassVar
from _typeshed import Incomplete

from ..core import WesternCalendar


class Netherlands(WesternCalendar):
    include_good_friday: ClassVar[bool]
    include_easter_sunday: ClassVar[bool]
    include_easter_monday: ClassVar[bool]
    include_ascension: ClassVar[bool]
    include_whit_sunday: ClassVar[bool]
    include_whit_monday: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    FIXED_HOLIDAYS: Incomplete
    include_carnival: Incomplete
    def __init__(self, include_carnival: bool = False) -> None: ...
    def get_king_queen_day(self, year): ...
    def get_carnival_days(self, year): ...
    def get_variable_days(self, year): ...


FALL_HOLIDAYS_EARLY_REGIONS: Incomplete
SPRING_HOLIDAYS_EARLY_REGIONS: Incomplete
SUMMER_HOLIDAYS_EARLY_REGIONS: Incomplete
SUMMER_HOLIDAYS_LATE_REGIONS: Incomplete


class NetherlandsWithSchoolHolidays(Netherlands):
    region: Incomplete
    carnival_instead_of_spring: Incomplete

    def __init__(
        self,
        region,
        carnival_instead_of_spring: bool = False,
        **kwargs) -> None: ...

    def get_fall_holidays(self, year): ...
    def get_christmas_holidays(self, year): ...
    def get_spring_holidays(self, year): ...
    def get_carnival_holidays(self, year): ...
    def get_may_holidays(self, year): ...
    def get_summer_holidays(self, year): ...
    def get_variable_days(self, year): ...
