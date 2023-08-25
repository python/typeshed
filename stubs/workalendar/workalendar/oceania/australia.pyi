from _typeshed import Incomplete

from ..core import WesternCalendar

class Australia(WesternCalendar):
    include_good_friday: ClassVar[bool]
    include_easter_monday: ClassVar[bool]
    include_queens_birthday: ClassVar[bool]
    include_labour_day_october: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    shift_anzac_day: ClassVar[bool]
    ANZAC_SHIFT_DAYS: Incomplete
    FIXED_HOLIDAYS: Incomplete
    def get_canberra_day(self, year): ...
    def get_queens_birthday(self, year): ...
    def get_labour_day_october(self, year): ...
    def get_anzac_day(self, year): ...
    def get_variable_days(self, year): ...

class AustralianCapitalTerritory(Australia):
    include_easter_saturday: ClassVar[bool]
    include_queens_birthday: ClassVar[bool]
    include_labour_day_october: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    def get_family_community_day(self, year): ...
    def get_reconciliation_day(self, year): ...
    def get_variable_days(self, year): ...

class NewSouthWales(Australia):
    include_queens_birthday: ClassVar[bool]
    include_easter_saturday: ClassVar[bool]
    include_easter_sunday: ClassVar[bool]
    include_labour_day_october: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    ANZAC_SHIFT_DAYS: Incomplete

class NorthernTerritory(Australia):
    include_easter_saturday: ClassVar[bool]
    include_queens_birthday: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    ANZAC_SHIFT_DAYS: Incomplete
    def get_may_day(self, year): ...
    def get_picnic_day(self, year): ...
    def get_variable_days(self, year): ...

class Queensland(Australia):
    include_easter_saturday: ClassVar[bool]
    include_queens_birthday: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    ANZAC_SHIFT_DAYS: Incomplete
    def get_labour_day_may(self, year): ...
    def get_variable_days(self, year): ...

class SouthAustralia(Australia):
    include_easter_saturday: ClassVar[bool]
    include_queens_birthday: ClassVar[bool]
    include_labour_day_october: ClassVar[bool]
    ANZAC_SHIFT_DAYS: Incomplete
    def get_adelaides_cup(self, year): ...
    def get_proclamation_day(self, year): ...
    def get_variable_days(self, year): ...

class Tasmania(Australia):
    include_queens_birthday: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    shift_anzac_day: ClassVar[bool]
    @property
    def has_recreation_day(self): ...
    def get_eight_hours_day(self, year): ...
    def get_recreation_day(self, year): ...
    def get_variable_days(self, year): ...

class Hobart(Tasmania):
    @property
    def has_recreation_day(self): ...
    def get_hobart(self, year): ...
    def get_variable_days(self, year): ...

class Victoria(Australia):
    include_easter_saturday: ClassVar[bool]
    include_queens_birthday: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    shift_anzac_day: ClassVar[bool]
    def get_labours_day_in_march(self, year): ...
    def get_melbourne_cup(self, year): ...
    def get_variable_days(self, year): ...

from typing import ClassVar

class WesternAustralia(Australia):
    include_boxing_day: ClassVar[bool]
    def get_labours_day_in_march(self, year): ...
    def get_western_australia_day(self, year): ...
    def get_variable_days(self, year): ...
