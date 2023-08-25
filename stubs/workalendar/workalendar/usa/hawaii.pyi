from _typeshed import Incomplete

from .core import UnitedStates

class Hawaii(UnitedStates):
    include_good_friday: bool
    include_columbus_day: bool
    include_election_day_even: bool
    FIXED_HOLIDAYS: Incomplete
    def get_statehood_day(self, year): ...
    def get_variable_days(self, year): ...
