from .core import UnitedStates

class Michigan(UnitedStates):
    include_christmas_eve: bool
    include_thanksgiving_friday: bool
    include_election_day_even: bool
    include_columbus_day: bool
    def get_fixed_holidays(self, year): ...
