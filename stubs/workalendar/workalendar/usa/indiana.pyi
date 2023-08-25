from .core import UnitedStates

class Indiana(UnitedStates):
    include_good_friday: bool
    include_thanksgiving_friday: bool
    thanksgiving_friday_label: str
    include_federal_presidents_day: bool
    label_washington_birthday_december: str
    include_election_day_even: bool
    election_day_label: str
    def get_washington_birthday_december(self, year): ...
    def get_primary_election_day(self, year): ...
    def get_variable_days(self, year): ...
