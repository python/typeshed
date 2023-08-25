from _typeshed import Incomplete

from .core import UnitedStates

class California(UnitedStates):
    include_thanksgiving_friday: bool
    include_cesar_chavez_day: bool
    include_columbus_day: bool
    shift_exceptions: Incomplete
    def get_cesar_chavez_days(self, year): ...

class CaliforniaEducation(California):
    def get_variable_days(self, year): ...

class CaliforniaBerkeley(California):
    FIXED_HOLIDAYS: Incomplete
    include_cesar_chavez_day: bool
    include_lincoln_birthday: bool
    include_columbus_day: bool
    columbus_day_label: ClassVar[str]

class CaliforniaSanFrancisco(California):
    include_cesar_chavez_day: bool
    include_columbus_day: bool

class CaliforniaWestHollywood(California):
    FIXED_HOLIDAYS: Incomplete
    include_cesar_chavez_day: bool
    include_thanksgiving_friday: bool
