from _typeshed import Incomplete

from .core import UnitedStates

class WestVirginia(UnitedStates):
    include_thanksgiving_friday: bool
    include_election_day_even: bool
    election_day_label: str
    west_virginia_include_christmas_eve: bool
    west_virginia_include_nye: bool
    FIXED_HOLIDAYS: Incomplete
    shift_exceptions: Incomplete
    def get_fixed_holidays(self, year): ...
