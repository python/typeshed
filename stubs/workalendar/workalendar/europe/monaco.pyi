from _typeshed import Incomplete

from ..core import WesternCalendar

class Monaco(WesternCalendar):
    include_easter_monday: bool
    include_ascension: bool
    include_whit_monday: bool
    include_all_saints: bool
    include_assumption: bool
    include_corpus_christi: bool
    include_immaculate_conception: bool
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
