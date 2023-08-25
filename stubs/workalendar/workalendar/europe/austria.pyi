from _typeshed import Incomplete

from ..core import WesternCalendar

class Austria(WesternCalendar):
    FIXED_HOLIDAYS: Incomplete
    include_labour_day: bool
    labour_day_label: ClassVar[str]
    include_epiphany: bool
    include_easter_monday: bool
    include_ascension: bool
    include_whit_monday: bool
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_immaculate_conception: bool
    include_christmas: bool
    include_boxing_day: bool
    boxing_day_label: ClassVar[str]
