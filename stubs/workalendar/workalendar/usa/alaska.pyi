from _typeshed import Incomplete

from .core import UnitedStates

class Alaska(UnitedStates):
    FIXED_HOLIDAYS: Incomplete
    include_columbus_day: bool
    def get_variable_days(self, year): ...
