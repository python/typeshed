from .core import UnitedStates

class TexasBase(UnitedStates):
    include_columbus_day: bool
    texas_include_confederate_heroes: bool
    texas_include_independance_day: bool
    texas_san_jacinto_day: bool
    texas_emancipation_day: bool
    texas_lyndon_johnson_day: bool
    include_thanksgiving_friday: bool
    include_christmas_eve: bool
    include_boxing_day: bool
    def get_fixed_holidays(self, year): ...

class Texas(TexasBase):
    texas_include_confederate_heroes: bool
    texas_include_independance_day: bool
    texas_san_jacinto_day: bool
    texas_emancipation_day: bool
    texas_lyndon_johnson_day: bool
    include_thanksgiving_friday: bool
    include_christmas_eve: bool
    include_boxing_day: bool
