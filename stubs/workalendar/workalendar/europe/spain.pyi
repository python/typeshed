from _typeshed import Incomplete

from ..core import WesternCalendar

class Spain(WesternCalendar):
    include_epiphany: bool
    include_good_friday: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool
    include_labour_day: bool
    labour_day_label: str
    FIXED_HOLIDAYS: Incomplete

class Andalusia(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class Aragon(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class CastileAndLeon(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class CastillaLaMancha(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class CanaryIslands(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class Catalonia(Spain):
    include_easter_monday: bool
    include_boxing_day: bool
    boxing_day_label: str
    FIXED_HOLIDAYS: Incomplete

class Extremadura(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class Galicia(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class BalearicIslands(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool
    include_easter_monday: bool

class LaRioja(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class CommunityofMadrid(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class Murcia(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class Navarre(Spain):
    include_holy_thursday: bool
    include_easter_monday: bool

class Asturias(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class BasqueCountry(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool
    include_easter_monday: bool

class Cantabria(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_holy_thursday: bool

class ValencianCommunity(Spain):
    FIXED_HOLIDAYS: Incomplete
    include_easter_monday: bool
