from .core import UnitedStates

class Illinois(UnitedStates):
    include_thanksgiving_friday: ClassVar[bool]
    include_lincoln_birthday: ClassVar[bool]
    include_election_day_even: ClassVar[bool]

from typing import ClassVar

class ChicagoIllinois(Illinois):
    include_thanksgiving_friday: ClassVar[bool]
    def get_pulaski_day(self, year): ...
    def get_variable_days(self, year): ...
