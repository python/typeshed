from .core import UnitedStates

class NorthCarolina(UnitedStates):
    include_good_friday: bool
    include_christmas_eve: bool
    include_thanksgiving_friday: bool
    include_boxing_day: bool
    include_federal_presidents_day: bool
    include_columbus_day: bool
    def get_christmas_shifts(self, year): ...
    def get_variable_days(self, year): ...
