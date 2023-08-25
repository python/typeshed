from _typeshed import Incomplete

from .core import UnitedStates

class Vermont(UnitedStates):
    FIXED_HOLIDAYS: Incomplete
    include_columbus_day: ClassVar[bool]
    def get_variable_days(self, year): ...
