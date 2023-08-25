from _typeshed import Incomplete
from collections.abc import Generator

MON: Incomplete
TUE: Incomplete
WED: Incomplete
THU: Incomplete
FRI: Incomplete
SAT: Incomplete
SUN: Incomplete
ISO_MON: Incomplete
ISO_TUE: Incomplete
ISO_WED: Incomplete
ISO_THU: Incomplete
ISO_FRI: Incomplete
ISO_SAT: Incomplete
ISO_SUN: Incomplete

class classproperty:
    getter: Incomplete
    __doc__: Incomplete
    def __init__(self, getter) -> None: ...
    def __get__(self, instance, owner): ...

def cleaned_date(day, keep_datetime: bool = False): ...
def daterange(start, end) -> Generator[Incomplete, None, None]: ...

class ChristianMixin:
    EASTER_METHOD: Incomplete
    include_epiphany: bool
    include_clean_monday: bool
    include_annunciation: bool
    include_fat_tuesday: bool
    fat_tuesday_label: Incomplete
    include_ash_wednesday: bool
    ash_wednesday_label: str
    include_palm_sunday: bool
    include_holy_thursday: bool
    holy_thursday_label: str
    include_good_friday: bool
    good_friday_label: str
    include_easter_monday: bool
    include_easter_saturday: bool
    easter_saturday_label: str
    include_easter_sunday: bool
    include_all_saints: bool
    include_immaculate_conception: bool
    immaculate_conception_label: str
    include_christmas: bool
    christmas_day_label: str
    include_christmas_eve: bool
    include_ascension: bool
    include_assumption: bool
    include_whit_sunday: bool
    whit_sunday_label: str
    include_whit_monday: bool
    whit_monday_label: str
    include_corpus_christi: bool
    include_boxing_day: bool
    boxing_day_label: str
    include_all_souls: bool
    def get_fat_tuesday(self, year): ...
    def get_ash_wednesday(self, year): ...
    def get_palm_sunday(self, year): ...
    def get_holy_thursday(self, year): ...
    def get_good_friday(self, year): ...
    def get_clean_monday(self, year): ...
    def get_easter_saturday(self, year): ...
    def get_easter_sunday(self, year): ...
    def get_easter_monday(self, year): ...
    def get_ascension_thursday(self, year): ...
    def get_whit_monday(self, year): ...
    def get_whit_sunday(self, year): ...
    def get_corpus_christi(self, year): ...
    def shift_christmas_boxing_days(self, year): ...
    def get_variable_days(self, year): ...

class WesternMixin(ChristianMixin):
    EASTER_METHOD: Incomplete
    WEEKEND_DAYS: Incomplete

class OrthodoxMixin(ChristianMixin):
    EASTER_METHOD: Incomplete
    WEEKEND_DAYS: Incomplete
    include_orthodox_christmas: bool
    orthodox_christmas_day_label: str
    def get_fixed_holidays(self, year): ...

class LunarMixin:
    @staticmethod
    def lunar(year, month, day): ...

class ChineseNewYearMixin(LunarMixin):
    include_chinese_new_year_eve: bool
    chinese_new_year_eve_label: str
    include_chinese_new_year: bool
    chinese_new_year_label: str
    include_chinese_second_day: bool
    chinese_second_day_label: str
    include_chinese_third_day: bool
    chinese_third_day_label: str
    shift_sunday_holidays: bool
    shift_start_cny_sunday: bool
    def get_chinese_new_year(self, year): ...
    def get_variable_days(self, year): ...
    def get_shifted_holidays(self, dates) -> Generator[Incomplete, None, None]: ...
    def get_calendar_holidays(self, year): ...

class CalverterMixin:
    conversion_method: Incomplete
    ISLAMIC_HOLIDAYS: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def converted(self, year): ...
    def calverted_years(self, year): ...
    def get_islamic_holidays(self): ...
    def get_delta_islamic_holidays(self, year) -> None: ...
    def get_variable_days(self, year): ...

class IslamicMixin(CalverterMixin):
    WEEKEND_DAYS: Incomplete
    conversion_method: Incomplete
    include_prophet_birthday: bool
    include_day_after_prophet_birthday: bool
    include_start_ramadan: bool
    include_eid_al_fitr: bool
    length_eid_al_fitr: int
    eid_al_fitr_label: str
    include_eid_al_adha: bool
    eid_al_adha_label: str
    length_eid_al_adha: int
    include_day_of_sacrifice: bool
    day_of_sacrifice_label: str
    include_islamic_new_year: bool
    include_laylat_al_qadr: bool
    include_nuzul_al_quran: bool
    def get_islamic_holidays(self): ...

class CoreCalendar:
    FIXED_HOLIDAYS: Incomplete
    WEEKEND_DAYS: Incomplete
    def __init__(self) -> None: ...
    def name(cls): ...
    def get_fixed_holidays(self, year): ...
    def get_variable_days(self, year): ...
    def get_calendar_holidays(self, year): ...
    def holidays(self, year: Incomplete | None = None): ...
    def get_holiday_label(self, day): ...
    def holidays_set(self, year: Incomplete | None = None): ...
    def get_weekend_days(self): ...
    def is_working_day(self, day, extra_working_days: Incomplete | None = None, extra_holidays: Incomplete | None = None): ...
    def is_holiday(self, day, extra_holidays: Incomplete | None = None): ...
    def add_working_days(
        self,
        day,
        delta,
        extra_working_days: Incomplete | None = None,
        extra_holidays: Incomplete | None = None,
        keep_datetime: bool = False,
    ): ...
    def sub_working_days(
        self,
        day,
        delta,
        extra_working_days: Incomplete | None = None,
        extra_holidays: Incomplete | None = None,
        keep_datetime: bool = False,
    ): ...
    def find_following_working_day(self, day): ...
    @staticmethod
    def get_nth_weekday_in_month(year, month, weekday, n: int = 1, start: Incomplete | None = None): ...
    @staticmethod
    def get_last_weekday_in_month(year, month, weekday): ...
    @staticmethod
    def get_iso_week_date(year, week_nb, weekday=1): ...
    @staticmethod
    def get_first_weekday_after(day, weekday): ...
    def get_working_days_delta(
        self,
        start,
        end,
        include_start: bool = False,
        extra_working_days: Incomplete | None = None,
        extra_holidays: Incomplete | None = None,
    ): ...
    def export_to_ical(self, period=[2000, 2030], target_path: Incomplete | None = None): ...

class Calendar(CoreCalendar):
    include_new_years_day: bool
    include_new_years_eve: bool
    shift_new_years_day: bool
    include_labour_day: bool
    labour_day_label: str
    def __init__(self, **kwargs) -> None: ...
    def get_fixed_holidays(self, year): ...
    def get_variable_days(self, year): ...

class WesternCalendar(WesternMixin, Calendar): ...
class OrthodoxCalendar(OrthodoxMixin, Calendar): ...

class ChineseNewYearCalendar(ChineseNewYearMixin, Calendar):
    WEEKEND_DAYS: Incomplete

class IslamicCalendar(IslamicMixin, Calendar): ...

class IslamoWesternCalendar(IslamicMixin, WesternMixin, Calendar):
    FIXED_HOLIDAYS: Incomplete
