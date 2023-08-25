from .core import UnitedStates

class Mississippi(UnitedStates):
    include_thanksgiving_friday: bool
    include_confederation_day: bool
    include_columbus_day: bool
    martin_luther_king_label: ClassVar[str]
    veterans_day_label: ClassVar[str]
    national_memorial_day_label: ClassVar[str]
