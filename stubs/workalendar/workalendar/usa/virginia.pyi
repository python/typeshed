from .core import UnitedStates

class Virginia(UnitedStates):
    include_christmas_eve: bool
    include_thanksgiving_friday: bool
    include_boxing_day: bool
    presidents_day_label: ClassVar[str]
    include_thanksgiving_wednesday: bool
    def get_variable_days(self, year): ...
