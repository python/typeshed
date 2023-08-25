from .core import UnitedStates

class RhodeIsland(UnitedStates):
    include_federal_presidents_day: bool
    include_election_day_even: bool
    def get_variable_days(self, year): ...
