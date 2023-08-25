from _typeshed import Incomplete

from ..core import ChineseNewYearCalendar, IslamicMixin

class Malaysia(IslamicMixin, ChineseNewYearCalendar):
    include_labour_day: bool
    labour_day_label: str
    include_nuzul_al_quran: bool
    include_eid_al_fitr: bool
    length_eid_al_fitr: int
    eid_al_fitr_label: str
    include_day_of_sacrifice: bool
    day_of_sacrifice_label: str
    include_islamic_new_year: bool
    include_prophet_birthday: bool
    WEEKEND_DAYS: Incomplete
    FIXED_HOLIDAYS: Incomplete
    MSIA_DEEPAVALI: Incomplete
    MSIA_THAIPUSAM: Incomplete
    chinese_new_year_label: str
    include_chinese_second_day: bool
    chinese_second_day_label: str
    shift_sunday_holidays: bool
    def get_variable_days(self, year): ...
