from .core import UnitedStates

class Nebraska(UnitedStates):
    include_thanksgiving_friday: bool
    def get_variable_days(self, year): ...
