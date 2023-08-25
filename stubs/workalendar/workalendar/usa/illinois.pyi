from .core import UnitedStates

class Illinois(UnitedStates):
    include_thanksgiving_friday: bool
    include_lincoln_birthday: bool
    include_election_day_even: bool

class ChicagoIllinois(Illinois):
    include_thanksgiving_friday: bool
    def get_pulaski_day(self, year): ...
    def get_variable_days(self, year): ...
