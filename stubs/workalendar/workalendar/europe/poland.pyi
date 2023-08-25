from _typeshed import Incomplete

from ..core import WesternCalendar

class Poland(WesternCalendar):
    include_labour_day: bool
    FIXED_HOLIDAYS: Incomplete
    include_easter_sunday: bool
    include_easter_monday: bool
    include_whit_sunday: bool
    whit_sunday_label: str
    include_corpus_christi: bool
    include_assumption: bool
    include_all_saints: bool
    include_boxing_day: bool
