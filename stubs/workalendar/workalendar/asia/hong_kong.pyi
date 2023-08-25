from _typeshed import Incomplete

from ..core import ChineseNewYearCalendar, WesternMixin

class HongKong(WesternMixin, ChineseNewYearCalendar):
    include_labour_day: bool
    include_good_friday: bool
    include_easter_saturday: bool
    include_easter_monday: bool
    include_boxing_day: bool
    WEEKEND_DAYS: Incomplete
    FIXED_HOLIDAYS: Incomplete
    chinese_new_year_label: str
    include_chinese_second_day: bool
    chinese_second_day_label: str
    include_chinese_third_day: bool
    chinese_third_day_label: str
    shift_sunday_holidays: bool
    shift_start_cny_sunday: bool
    def get_variable_days(self, year): ...

class HongKongBank(HongKong):
    WEEKEND_DAYS: Incomplete
