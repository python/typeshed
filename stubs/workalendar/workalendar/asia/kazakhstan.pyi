from _typeshed import Incomplete

from ..core import IslamicCalendar, OrthodoxCalendar

class Kazakhstan(OrthodoxCalendar, IslamicCalendar):
    include_christmas: bool
    include_christmas_eve: bool
    include_new_years_day: bool
    include_orthodox_christmas: bool
    include_epiphany: bool
    include_good_friday: bool
    include_easter_saturday: bool
    include_easter_sunday: bool
    include_easter_monday: bool
    include_prophet_birthday: bool
    include_day_after_prophet_birthday: bool
    include_start_ramadan: bool
    include_eid_al_fitr: bool
    length_eid_al_fitr: int
    include_eid_al_adha: bool
    length_eid_al_adha: int
    include_day_of_sacrifice: bool
    day_of_sacrifice_label: ClassVar[str]
    include_islamic_new_year: bool
    include_laylat_al_qadr: bool
    include_nuzul_al_quran: bool
    FIXED_HOLIDAYS: Incomplete
    def get_fixed_holidays(self, year): ...
    def get_variable_days(self, year): ...
