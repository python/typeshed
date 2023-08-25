from .core import UnitedStates

class NewMexico(UnitedStates):
    include_thanksgiving_friday: bool
    thanksgiving_friday_label: ClassVar[str]
    include_federal_presidents_day: bool
