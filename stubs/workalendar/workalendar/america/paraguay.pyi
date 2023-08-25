from _typeshed import Incomplete

from ..core import WesternCalendar

class Paraguay(WesternCalendar):
    FIXED_HOLIDAYS: Incomplete
    include_labour_day: bool
    include_holy_thursday: bool
    include_good_friday: bool
    include_easter_saturday: bool
    include_immaculate_conception: bool
    immaculate_conception_label: str
    def get_heroes_day(self, year): ...
    def get_founding_of_asuncion(self, year): ...
    def get_boqueron_battle_victory_day(self, year): ...
    def get_fixed_holidays(self, year): ...
