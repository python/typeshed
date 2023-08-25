from .core import UnitedStates

class Nevada(UnitedStates):
    include_thanksgiving_friday: bool
    thanksgiving_friday_label: ClassVar[str]
    include_columbus_day: bool
    def get_variable_days(self, year): ...
