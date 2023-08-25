from _typeshed import Incomplete

from ..core import ChineseNewYearCalendar, IslamicMixin, WesternMixin

class Singapore(WesternMixin, IslamicMixin, ChineseNewYearCalendar):
    include_labour_day: bool
    include_good_friday: bool
    include_eid_al_fitr: bool
    eid_al_fitr_label: ClassVar[str]
    include_day_of_sacrifice: bool
    day_of_sacrifice_label: ClassVar[str]
    FIXED_HOLIDAYS: Incomplete
    WEEKEND_DAYS: Incomplete
    DEEPAVALI: Incomplete
    chinese_new_year_label: ClassVar[str]
    include_chinese_second_day: bool
    chinese_second_day_label: ClassVar[str]
    shift_sunday_holidays: bool
    def get_variable_days(self, year): ...
