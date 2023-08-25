from _typeshed import Incomplete

from .core import UnitedStates

class HebrewHolidays:
    hebrew_calendars: Incomplete
    @classmethod
    def get_hebrew_calendar(cls, gregorian_year): ...
    @classmethod
    def search_hebrew_calendar(cls, gregorian_year, hebrew_month, hebrew_day): ...
    @classmethod
    def get_rosh_hashanah(cls, year): ...
    @classmethod
    def get_yom_kippur(cls, year): ...

class Florida(UnitedStates):
    include_thanksgiving_friday: bool
    thanksgiving_friday_label: str
    include_columbus_day: bool
    include_federal_presidents_day: bool

class FloridaLegal(Florida):
    FIXED_HOLIDAYS: Incomplete
    include_fat_tuesday: bool
    include_lincoln_birthday: bool
    include_federal_presidents_day: bool
    include_good_friday: bool
    include_confederation_day: bool
    include_jefferson_davis_birthday: bool
    include_columbus_day: bool
    columbus_day_label: str
    include_election_day_every_year: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def get_confederate_day(self, year): ...
    def get_jefferson_davis_birthday(self, year): ...

class FloridaCircuitCourts(HebrewHolidays, Florida):
    include_federal_presidents_day: bool
    include_good_friday: bool
    def get_variable_days(self, year): ...

class FloridaMiamiDade(Florida):
    include_federal_presidents_day: bool
    include_columbus_day: bool
